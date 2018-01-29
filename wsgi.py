
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from sampleserve.app import create_app
from sampleserve.admin.app import create_admin_app
from sampleserve.config import settings


application = DispatcherMiddleware(create_app(), {
    '/admin': create_admin_app()
})

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True, threaded=True)
