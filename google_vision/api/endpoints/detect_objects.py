import logging

from flask_restplus import Resource, fields
from google_vision.api.restplus import api
from google.cloud import vision
from flask_restplus import reqparse

log = logging.getLogger(__name__)

ns = api.namespace('detect_objects', description='Detect objects using google vision api')
resource_fields = api.model('Resource', {
     'uri': fields.String,
})

model = api.model('Model', {
    'car': fields.Boolean,
    'pedestrian': fields.Boolean,
    'traffic_light': fields.Boolean
})

OBJECT_CLASSES = ["car", "pedestrian", "traffic light"]
CONFIDENCE_THRESHOLD = 0.9

parser = reqparse.RequestParser()
parser.add_argument('uri', required=True, help='uri of the image file')

@ns.route('')
@api.response(200, 'OK', model)
class DetectObjects(Resource):

    @api.expect(parser)
    def get(self):
        return self.post()

    @api.expect(parser)
    def post(self):

        args = parser.parse_args()
        if not args['uri']:
            return "Missing required parameter: uri", 400

        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        image = vision.types.Image()
        image.source.image_uri = args['uri']

        response = client.label_detection(image=image)
        if response.error.code != 0:
            return response.error.message, 400
        labels = response.label_annotations

        api_response = {}
        for obj_class in OBJECT_CLASSES:
            api_response[self.underscore(obj_class)] = 'false'

        for label in labels:
            if label.description and isinstance(label.description, str) \
                    and label.description.lower() in OBJECT_CLASSES \
                    and label.score and label.score >= CONFIDENCE_THRESHOLD:
                api_response[self.underscore(label.description.lower())] = 'true'
        return api_response, 200

    def underscore(self, string):
        return "_".join( string.split() )
