"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
from django.test import TestCase
from models import AWSServer

class AWSServerTest(TestCase):

    def setUp(self):
        # save aws keys in environment for testing (so as to not put them in public github)
        TEST_AWS_NAME = os.environ.get("TEST_AWS_NAME")
        TEST_AWS_ACCESS_KEY = os.environ.get("TEST_AWS_ACCESS_KEY")
        TEST_AWS_SECRET_KEY = os.environ.get("TEST_AWS_SECRET_KEY")
        TEST_AWS_REGION = os.environ.get("TEST_AWS_REGION")
        TEST_AWS_USER_NAME = os.environ.get("TEST_AWS_USER_NAME")

        # make sure env vars are set
        self.assertIsNotNone(TEST_AWS_ACCESS_KEY)
        self.assertIsNotNone(TEST_AWS_SECRET_KEY)
        self.assertIsNotNone(TEST_AWS_REGION)
        self.assertIsNotNone(TEST_AWS_USER_NAME)

        test_server = AWSServer(
            name = TEST_AWS_NAME,
            description = "Test AWS Server",
            aws_access_key = TEST_AWS_ACCESS_KEY,
            aws_secret_key = TEST_AWS_SECRET_KEY,
            aws_region = TEST_AWS_REGION,
            user_name = TEST_AWS_USER_NAME,
        )
        test_server.save()

    def test_server_state(self):
        """ connect to the server and get it's state """
        test_server = AWSServer.objects.get(pk=1)
        state = test_server.get_server_state()
        self.assertIn(state, ("running", "stopped", "shutting-down", "terminated", "stopping"))

    def test_server_name_incorrect(self):
        """ Test that an incorrect server name will give the appropriate error msg """
        test_server = AWSServer.objects.get(pk=1)
        test_server.name = "wrongname"
        try:
            test_server.get_server_state()
        except Exception as e:
            msg = str(e)

        self.assertEqual(msg, "AWS Instance not found, check settings.")

