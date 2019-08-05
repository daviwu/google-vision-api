# Google Vision API

This repository contains for a RESTful API based on Flask and Flask-RESTPlus to perform object detection using Google Vision API

## Requirements
Python 3

## Installation and Usage

```
$ sudo apt-get install python3 python3-venv python3-pip
$ cd /path/to/my/workspace/
$ git clone https://github.com/daviwu/google-vision-api
$ cd flask-query-api
$ pyvenv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt
$ (venv) export PYTHONPATH=.:$PYTHONPATH
$ (venv) python3 google_vision/app.py &
$ (venv) curl -X GET localhost:5000/detect_objects -d '{"uri": "https://www.hlaw.ca/wp-content/uploads/2009/01/15.09.24-67201591.jpg"}' -H 'Content-Type: application/json'
$ (venv) python3 flask_query_api/test/unit_tests.py
$ (venv) fg
$ (venv) <Ctrl-C>
$ (venv) deactivate
$
```

## Discussions and Limitations

* The server only accept sync requests. This is a problem for a production environment since Google Api responces are slow (>3s). To allow async requests with multiple workers, use gunicorn such as
```
gunicorn -b 0.0.0.0:8080 app:app -w 5 -k eventlet --timeout 60 --keep-alive 30
```
or alternatively, create service in kubernetes and increase allocation of pods.

* This implementation assumes the Google Vision API `label_detection` texts of labels of `car`, `traffic light`, etc does not change.


