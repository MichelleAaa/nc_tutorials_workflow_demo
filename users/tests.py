from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.

# Fixture for creating a test user object in the database.
# The django_user_model fixture is a built-in fixture. It acts as a shortcut to accessing the User model for this project.
# creates a new user with the Django create_user() method and sets a username and password.
# Then it returns the username and password as a tuple.  
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple


# Test that logging into the app works, using the test_user fixture as a parameter to first add a user.
# The client passed in as a parameter is a built-in "dummy web client" provided by Django as part of its testing tools.
def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True
# login() method helps us test that we can log into the app, and the test_user fixture makes sure that we have a valid user to test with.