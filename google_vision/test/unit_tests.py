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

    def test_04_flower(self):
        url = server_url + "/detect_objects"
        image_uri = "http://www.dahliadivas.com/shop/images/th_colwoodcrush_13.jpg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'false')
        self.assertEqual(resp['pedestrian'], 'false')
        self.assertEqual(resp['traffic_light'], 'false')

    def test_05_light_bulbs(self):
        url = server_url + "/detect_objects"
        image_uri = "http://blissfullydomestic.com/wp-content/uploads/primary-colors-light-bulbs.jpeg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'false')
        self.assertEqual(resp['pedestrian'], 'false')
        self.assertEqual(resp['traffic_light'], 'false')

    def test_06_parade(self):
        url = server_url + "/detect_objects"
        image_uri = "https://joshuaproject.net/assets/media/profiles/photos/p10466.jpg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'false')
        self.assertEqual(resp['pedestrian'], 'false')
        self.assertEqual(resp['traffic_light'], 'false')

    def test_07_batmobile1(self):
        url = server_url + "/detect_objects"
        image_uri = "https://exoticlassic.files.wordpress.com/2012/07/tdk-20080820-batman-returns-batmobile-for-auction.jpg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'true')
        self.assertEqual(resp['pedestrian'], 'false')
        self.assertEqual(resp['traffic_light'], 'false')

    def test_08_batmobile2(self):
        url = server_url + "/detect_objects"
        image_uri = "http://wp-content.rpmware.com/wp-content/uploads/2008/05/batmobile-7.jpg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'true')
        self.assertEqual(resp['pedestrian'], 'false')
        self.assertEqual(resp['traffic_light'], 'false')

    def test_08_batmobile_lego(self):
        url = server_url + "/detect_objects"
        image_uri = "https://c4.staticflickr.com/1/460/31849076235_93101dfbc4.jpg"
        response = requests.post(url, data={"uri": image_uri})
        resp = response.json()
        self.assertEqual(resp['car'], 'false')
        self.assertEqual(resp['pedestrian'], 'false')
        self.assertEqual(resp['traffic_light'], 'false')



if __name__ == '__main__':
    unittest.main()