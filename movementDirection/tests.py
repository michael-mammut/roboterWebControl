from django.test import TestCase as djangoTestCase
import os
import unittest

# Create your tests here.
class TestExample(djangoTestCase):

    def setUp(self):
        print('setup')
        print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def test_abc(self):
        self.assertEqual(1,1)

    def test_def(self):
        self.assertEqual(1,1)

    def tearDown(self):
        print('tearDown')
