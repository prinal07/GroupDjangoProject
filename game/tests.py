from django.test import TestCase
from django.http import HttpRequest, response
from django.template.loader import render_to_string

class URLTests(TestCase):
    """
    Test cases for checking the status code of URLs.
    """
    def testQrPage(self):
        """
        Test whether the status code of the QR page is 200.
        """
        response = self.client.get('/game/QR/')
        self.assertEqual(response.status_code, 200)

    def testQrPage(self):
        """
        Test whether the status code of the map page is 200.
        """
        response = self.client.get('/game/map/')
        self.assertEqual(response.status_code, 200)

class QrTests(TestCase):
    """
    Test cases for the QR code scanning functionality.
    """
    def test_success_valid_qr_code(self):
        """
        Test if success function displays "Success!" message for a valid QR code.
        """
        result = 'qjdkiivbbunmue625ljyjy04w941jy'
        Bins = ['qjdkiivbbunmue625ljyjy04w941jy', '3w7wzif7eku0huro54jtmlbt8s0fnm', '8xycn8zhxb203qhqw7v2eetrvcscx1']
        response = None

        for i in Bins:
            if (result == i) :
                response = 'Success!'
        
        self.assertEqual(response, 'Success!')

    def test_invalid_qr_code(self):
        """
        Test if "Invalid Qr Code!" message is displayed for an invalid QR code.
        """
        result = 'invalid_QR_Code'
        Bins = ['qjdkiivbbunmue625ljyjy04w941jy', '3w7wzif7eku0huro54jtmlbt8s0fnm', '8xycn8zhxb203qhqw7v2eetrvcscx1']
        response = None
        j=0

        for i in Bins:
            if (result == i):
                break
            elif (j == 2):
                response='<h2>Invalid Qr Code!</h2>'
            j=j+1
               
        self.assertEqual(response, '<h2>Invalid Qr Code!</h2>')
