from app import app
import unittest

class testing(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_main_page(self):
        for rule in app.url_map.iter_rules():
            print(f"{', '.join(rule.methods)} - {rule.rule} - {rule.endpoint}")
        print()
        print('Starting tests')
        routes = [
            ['GET','/']
        ]
        for route in routes:
            print('Testing "'+route[0]+' - '+route[1]+'"')
            if route[0] == 'GET':
                response = self.app.get(route[1], follow_redirects=True)
            else:
                response = self.app.post(route[1], follow_redirects=True)
            self.assertEqual(response.status_code, 401)