import logging
import traceback

from flask_restplus import Api
from flask_query_api import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Google Vision API', doc='/swagger_doc/',
          description='An Object Detection App using Google Vision API')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

