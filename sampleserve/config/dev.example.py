
DEBUG = True
SERVER_NAME = 'sampleserve.dev'
FRONTEND_SERVER_NAME = 'sampleserve.dev'
CORS_SERVER_NAME = [
    "http://test.sampleserve-app.dev",
    "http://csi-labs-inc.sampleserve-app.dev",
    "http://test-b.sampleserve-app.dev",
    "http://sos-analytical.sampleserve-app.dev",
    "http://southern-petroleum-laboratory-spl.sampleserve-app.dev",
    "http://fibertec-environmental-services.sampleserve-app.dev",
    "http://bio-chem.sampleserve-app.dev",
    "http://mdnre-lab-lansing.sampleserve-app.dev",
    "http://pace-analytical-services.sampleserve-app.dev",
    "http://pace-analytical.sampleserve-app.dev",
    "http://rti-laboratories-inc.sampleserve-app.dev",
    "http://brighton-analytical.sampleserve-app.dev",
    "http://grand-traverse-analytical.sampleserve-app.dev",
    "http://testamerica-labs.sampleserve-app.dev",
    "http://als-laboratory-group-colorado.sampleserve-app.dev",
    "http://trace-analytical.sampleserve-app.dev",
    "http://merit-laboratories.sampleserve-app.dev",
    "http://lancaster-labs.sampleserve-app.dev",
    "http://ppb-labs.sampleserve-app.dev",
    "http://test-all-analytical-inc.sampleserve-app.dev",
    "http://trimatrix.sampleserve-app.dev",
    "http://analytical-environmental-services-inc.sampleserve-app.dev",
    "http://esc-lab-sciences.sampleserve-app.dev",
    "http://microbial-insights.sampleserve-app.dev",
    "http://xenco-laboratories.sampleserve-app.dev",
    "http://testamerica-lab-1.sampleserve-app.dev",
    "http://testamerica-lab-2.sampleserve-app.dev",
    "http://als-laboratory-group-holland.sampleserve-app.dev",
    "http://brighton-analytical-2.sampleserve-app.dev",
    "http://accutest-laboratories.sampleserve-app.dev",
    "http://test.sampleserve-webapp.dev",
    "http://csi-labs-inc.sampleserve-webapp.dev",
    "http://test-b.sampleserve-webapp.dev",
    "http://sos-analytical.sampleserve-webapp.dev",
    "http://southern-petroleum-laboratory-spl.sampleserve-webapp.dev",
    "http://fibertec-environmental-services.sampleserve-webapp.dev",
    "http://bio-chem.sampleserve-webapp.dev",
    "http://mdnre-lab-lansing.sampleserve-webapp.dev",
    "http://pace-analytical-services.sampleserve-webapp.dev",
    "http://pace-analytical.sampleserve-webapp.dev",
    "http://rti-laboratories-inc.sampleserve-webapp.dev",
    "http://brighton-analytical.sampleserve-webapp.dev",
    "http://grand-traverse-analytical.sampleserve-webapp.dev",
    "http://testamerica-labs.sampleserve-webapp.dev",
    "http://als-laboratory-group-colorado.sampleserve-webapp.dev",
    "http://trace-analytical.sampleserve-webapp.dev",
    "http://merit-laboratories.sampleserve-webapp.dev",
    "http://lancaster-labs.sampleserve-webapp.dev",
    "http://ppb-labs.sampleserve-webapp.dev",
    "http://test-all-analytical-inc.sampleserve-webapp.dev",
    "http://trimatrix.sampleserve-webapp.dev",
    "http://analytical-environmental-services-inc.sampleserve-webapp.dev",
    "http://esc-lab-sciences.sampleserve-webapp.dev",
    "http://microbial-insights.sampleserve-webapp.dev",
    "http://xenco-laboratories.sampleserve-webapp.dev",
    "http://testamerica-lab-1.sampleserve-webapp.dev",
    "http://testamerica-lab-2.sampleserve-webapp.dev",
    "http://als-laboratory-group-holland.sampleserve-webapp.dev",
    "http://brighton-analytical-2.sampleserve-webapp.dev",
    "http://accutest-laboratories.sampleserve-webapp.dev",
]
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'postgres://sampleserve:sampleserve@db/sampleserve'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dev'

MAIL_DEFAULT_SENDER = 'contact@sampleserve.com'
MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'postmaster@sampleserve.com'
MAIL_PASSWORD = ''
WTF_CSRF_ENABLED = False
