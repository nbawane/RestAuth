from django.test import TestCase
import requests
# Create your tests here.
class PhotoAPI(TestCase):
    def test_login_api_with_valid_creds(self):

        url = r'http://127.0.0.1:8000/api/V1/login/'
        data = {'username':'admin','password':'Rasengan'}
        r = requests.post(url,data=data)
        print(r.json())
        self.assertEqual(r.status_code,200) #test if response if ok


    def test_login_api_without_valid_creds(self):
        url = r'http://127.0.0.1:8000/api/V1/login/'
        data = {'username':'admin','password':'rasengan'}
        r = requests.post(url,data=data)
        #pri(r.json())
        self.assertEqual(r.status_code,400) #test if response if ok

    def test_logout(self):
        url = r'http://127.0.0.1:8000/api/V1/logout/'
        r= requests.post(url)
        #pri(r.json())

    def test_group_with_login(self):
        #login
        url = r'http://127.0.0.1:8000/api/V1/login/'
        data = {'username':'admin','password':'Rasengan'}
        r = requests.post(url,data=data)
        #pri(r.json())
        self.assertEqual(r.status_code,200) #test if response if ok
        token = r.json()['key']
        #pri(token)
        #print('preparing for group data')
        groupurl = 'http://127.0.0.1:8000/api/V1/groups/'
        token = 'Token {}'.format(token)
        print(token)
        r = requests.get(groupurl, headers={'Authorization': token})
        print('*'*50)
        print(r.json())
        self.assertEqual(r.status_code, 200)  # test if response if ok
        #pri(r.json())

    def test_group_without_login(self):
        #logging out
        self.test_logout()
        groupurl = 'http://127.0.0.1:8000/api/V1/groups/'
        r = requests.get(groupurl)
        print('*'*50)
        print(r.json())
        self.assertNotEqual(r.status_code, 200)

    def test_logout_without_login(self):
        self.test_logout()

