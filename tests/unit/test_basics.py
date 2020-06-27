import unittest
from flask import current_app
from app import db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = 