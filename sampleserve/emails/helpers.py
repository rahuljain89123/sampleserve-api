
from threading import Thread
from flask_mail import Mail
from flask_mail import Message as Msg
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
from sampleserve import mail


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async
def send_async_email(msg):
    from sampleserve.app import create_app
    with create_app().test_request_context():
        mail.send(msg)


def send_email(
        subject,
        recipients,
        sender='contact@sampleserve.com',
        html_body=None,
        plain_body=None,
        reply_to=None,
        bcc=['nick@sampleserve.com'],
        host=None,
        testmode=False):
        # Flask Mail Parameters
        # subject - email subject header
        # recipients - list of email addresses
        # body - plain text message
        # html - HTML message
        # sender - email sender address, or MAIL_DEFAULT_SENDER by default
        # cc - CC list
        # bcc - BCC list
        # attachments - list of Document instances
        # reply_to - reply-to address
        # date - send date
        # charset - message character set
        # extra_headers - A dictionary of additional headers for the message
    msg = Msg(
        subject=subject,
        recipients=recipients,
        body=dehtml(html_body) if not plain_body else plain_body,
        html=html_body,
        sender=sender,
        reply_to=reply_to,
        bcc=bcc)
    if testmode is True:
        msg.extra_headers = {"o:testmode": "yes"}
    else:
        send_async_email(msg)


def nl2br(value):
    return value.replace('\n', '<br>\n')


def firstname(full_name):
    try:
        return full_name.split(' ')[0]
    except:
        return full_name


class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


@async
def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text
