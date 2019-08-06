# Google Vision API

This repository contains for a RESTful API based on Flask and Flask-RESTPlus to perform object detection using Google Vision API

## Requirements
Python 3

## Installation and Usage

```
$ sudo apt-get install python3 python3-venv python3-pip
$ cd /path/to/my/workspace/
$ git clone https://github.com/daviwu/google-vision-api
$ cd google-vision-api
$ export GOOGLE_APPLICATION_CREDENTIALS="./google_vision/credentials/mltest-9b3e9fa1939d.json"
$ pyvenv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt
$ (venv) export PYTHONPATH=.:$PYTHONPATH
$ (venv) python3 google_vision/app.py &
$ (venv) curl -X GET localhost:5000/detect_objects -d '{"uri": "https://www.hlaw.ca/wp-content/uploads/2009/01/15.09.24-67201591.jpg"}' -H 'Content-Type: application/json'
$ (venv) python3 google_vision/test/unit_tests.py
$ (venv) fg
$ (venv) <Ctrl-C>
$ (venv) deactivate
$
```

## Documentation
swagger doc is at `localhost:5000/swagger_doc`

## Discussions and Limitations

* The server only accept sync requests. This is a problem for a production environment since Google Api responces are slow (>3s). To allow async requests with multiple workers, use gunicorn such as
```
gunicorn -b 0.0.0.0:8080 app:app -w 5 -k eventlet --timeout 60 --keep-alive 30
```
or alternatively, create service in kubernetes and increase allocation of pods.

* This implementation assumes the Google Vision API `label_detection` texts of labels of `car`, `traffic light`, etc does not change.

* According to the specification, GET requests usually does not go with -d option but is allowed. Therefore a POST request of identical parameters is also implemented

* Assume that picture for object detection is not adversarial (e.g., https://www.researchgate.net/figure/Left-Adversarial-examples-in-physical-domain-remain-adversarial-at-multiple-angles-Top_fig14_320582292)

* Some corner cases for pictures are tested (see unit tests). For example, batmobiles are correctly identified as cars by Google Vision (confidence > .9), and Lego batmobiles are correctly identified as NOT a car (confidence < .9). A parade not on streets is correctly identified as not a pedestrian.