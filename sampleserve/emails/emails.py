
from flask import current_app, g, Blueprint, jsonify, url_for, render_template
from sampleserve.emails.helpers import send_email
from sampleserve.core import db
from sampleserve.users.models import User, Lab, Company
from sampleserve.sites.imports.import_data import import_data
from sampleserve.emails.helpers import async
from sampleserve.models import Upload

from pprint import pprint

RESET_LINK = 'http://{}.{}/forgot?code={}'
ACCEPT_LINK = 'http://{}.{}/accept-invite?code={}'
DOWNLOAD_LINK = 'http://{}.{}/'


def get_clients(user, lab=None):
    if user.role_id == 1:
        return ["Sampleserve"]
    if user.role_id == 2 or user.role_id == 3:
        return [lab.title]
    if user.role_id == 4 or user.role_id == 5:
        return [c.title for c in user.companies]
    if user.role_id == 6 or user.role_id == 7:
        return [s.title for s in user.sites]


def invite_user(user):
    lab = Lab.query.get(user.lab_id)
    clients = get_clients(user, lab)
    accept_link = ACCEPT_LINK.format(lab.url, current_app.config.get('FRONTEND_SERVER_NAME'), user.invite_code)

    html_body = render_template(
        '/emails/invite-user.html',
        clients=clients,
        accept_link=accept_link,
    )
    send_email(
        subject="You've been invited to collaborate",
        recipients=[user.email],
        html_body=html_body
    )


def accepted_invite(user):
    # Email the invitee about acceptance
    lab = Lab.query.get(user.lab_id)
    clients = get_clients(user, lab)

    html_body = render_template(
        '/emails/invitation-acceptance-confirmation.html',
        user=user,
        clients=clients
    )

    if user.invitee:
        send_email(
            subject="Accepted invitation to collaborate",
            recipients=[user.invitee.email],
            html_body=html_body
        )


def reset_password(user):
    lab = Lab.query.get(user.lab_id)
    reset_link = RESET_LINK.format(lab.url, current_app.config.get('FRONTEND_SERVER_NAME'), user.reset_code)

    html_body = render_template(
        '/emails/reset-password.html',
        reset_link=reset_link,
    )

    send_email(
        subject='Password Reset Requested',
        recipients=[user.email],
        html_body=html_body,
    )


def send_lab_results(upload):
    # Start post-processing the CSV, save values to database
    print("running send_lab_results")
    company = Company.query.get(upload.company_id)
    users = company.users.all()
    pprint(users)
    lab = Lab.query.get(upload.lab_id)
    download_link = DOWNLOAD_LINK.format(lab.url, current_app.config.get('FRONTEND_SERVER_NAME'))

    # Import the data for real, without dry run
    csv = import_data(lab_id=upload.lab_id, upload_type=upload.upload_type, company_id=upload.company_id, url=upload.url)

    # Set the site_id so it displays properly
    rupload = Upload.query.get(upload.id)
    rupload.site_id = csv['site_id']
    print(rupload, rupload.site_id)
    db.session.commit()

    for user in users:
        if not user.active:
            # Swap out the download link for the accept invitation link if the user has not accepted invitation
            download_link = ACCEPT_LINK.format(lab.url, current_app.config.get('FRONTEND_SERVER_NAME'), user.invite_code)

        html_body = render_template(
            '/emails/send-lab-results.html',
            user=user,
            lab_name=lab.title,
            client_name=csv['client_name'],
            site_name=csv['site_name'],
            sample_dates=csv['sample_dates'],
            download_link=download_link
        )

        send_email(
            subject="%s - %s - (%s) Results Available" % (csv['client_name'], csv['site_name'], csv['sample_dates'][0]),
            recipients=[user.email],
            html_body=html_body
        )


@async
def send_lab_results_async(upload):
    print("running send_lab_results_async")
    from sampleserve.app import create_app
    with create_app().test_request_context():
        send_lab_results(upload)


def free_trial_inquiry(
    name,
    company_name,
    email,
    phone,
    number_of_employees,
):

    html_body = render_template(
        '/emails/free-trial-inquiry.html',
        name=name,
        company_name=company_name,
        email=email,
        phone=phone,
        number_of_employees=number_of_employees,
    )
    send_email(
        subject="Free Trial Inquiry from %s" % company_name,
        reply_to=email,
        recipients=["nick@sampleserve.com", "schindler@sampleserve.com"],
        # recipients=["nick@sampleserve.com", "schindler@sampleserve.com"],
        html_body=html_body
    )
