import logging.config
import os

from flask import Flask, Blueprint
from google_vision import settings
from google_vision.api.endpoints.detect_objects import ns as detect_objects_namespace
from google_vision.api.restplus import api

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if GOOGLE_APPLICATION_CREDENTIALS:
        print ("GOOGLE_APPLICATION_CREDENTIALS: {}".format(GOOGLE_APPLICATION_CREDENTIALS))
    else:
        print ("GOOGLE_APPLICATION_CREDENTIALS not set in environment, using credentials in google_vision/credentials")
        GOOGLE_APPLICATION_CREDENTIALS = 'google_vision/credentials/mltest-9b3e9fa1939d.json'
    flask_app.config['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(detect_objects_namespace)
    flask_app.register_blueprint(blueprint)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/<<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == "__main__":
    main()
