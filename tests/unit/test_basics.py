import unittest
import os 

from flask import current_app
from dotenv import load_dotenv, find_dotenv

from app import create_app
from app.db import db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        load_dotenv(find_dotenv())

        config_name = os.environ.get('FLASK_ENV')
        print(config_name)
        self.app = create_app(config_name)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_app_exists(self):
        self.assertFalse(current_app is None)
    
    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])