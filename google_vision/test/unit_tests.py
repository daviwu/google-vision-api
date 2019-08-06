import unittest, requests, os
import urllib.parse

server_url = "http://localhost:5000"

class TestClass(unittest.TestCase):

    def test_00_server_is_up_and_running(self):
        # print ("test_00")
        url = server_url + "/swagger_doc/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)


    def test_01_example(self):
        url = server_url + "/detect_objects"
        image_uri = "https://www.hlaw.ca/wp-content/uploads/2009/01/15.09.24-67201591.jpg"
        response = requests.get(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'true')
        self.assertEqual(resp['pedestrian'], 'true')
        self.assertEqual(resp['traffic_light'], 'false')

    def test_02_no_data(self):
        url = server_url + "/detect_objects"
        response = requests.get(url)
        resp = response.json()
        self.assertEqual(response.status_code, 400)

    def test_03_invalid_url(self):
        url = server_url + "/detect_objects"
        image_uri = "https://www.some.ca/bogus/url/file.jpg"
        response = requests.get(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(response.status_code, 400)

    def test_04_post(self):
        url = server_url + "/detect_objects"
        image_uri = "https://www.hlaw.ca/wp-content/uploads/2009/01/15.09.24-67201591.jpg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'true')
        self.assertEqual(resp['pedestrian'], 'true')
        self.assertEqual(resp['traffic_light'], 'false')


if __name__ == '__main__':
    unittest.main()