from flask_testing import TestCase
from flask import current_app, url_for #url_for Redirectioning to the function name URL 
from main import app #The True app
                #current_app: The app that is on or off when we make testing 

class MainTest(TestCase): #Heritating TestCase
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app
    
    def test_app_exists_web(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_testing_mode(self): #current_app: The app that is on or off when we make testing 
        self.assertTrue(current_app.config["TESTING"])
    
    def test_index_redirects(self): #url_for Redirectioning to the function name 
        response = self.client.get(url_for("index"))            #_external=True: generates an absolute URL
       # self.assertRedirects(response, url_for("show_information"))  #  If I need to assert the full URL
        self.assertEqual(response.location, url_for("show_information", _external=False)) #If I need to assert the relative URL

    def test_show_information_get(self):
        response = self.client.get(url_for("show_information"))
        self.assert200(response)

    def test_show_information_post(self):
        test_form_fake = {
            "username": "J",
            "password": "33"
        }
        response = self.client.post(url_for("show_information"), data=test_form_fake)
       # self.assertRedirects(response, url_for("index"))     #  If I need to assert the full URL        #_external=True: generates an absolute URL
        self.assertEqual(response.location, url_for("index", _external=False)) #If I need to assert the relative URL
