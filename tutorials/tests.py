from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"
# Test to make sure that when we reverse the view named home, we get the expected path for the homepage on the website, which is "/". 

#pytest -k create	The decorator @pytest.mark.django_db is used to allow this test access to the connected database, which is required by this particular view. 
# @pytest.mark.django_db 
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a Django application',
#         published=True
#     )
#     assert tutorial.title == "Pytest"
# •	This test verifies that we are able to successfully create a Tutorial object in the database.


@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# •	This new_tutorials() fixture function will create a new tutorial object with the attributes described (a title of 'Pytest', etc) any time it is used as a parameter in a test function.
# •	Then, in that test function, that tutorial object will be available to use under the same name as the function name, new_tutorial. 


# •	These test functions use new_tutorial as a parameter. 
# •	This causes the new_tutorial() fixture function to be run first when either of these tests is run.
# First test: checks that the object created by the fixture exists, by searching for an object with the same title.
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()
# Second Test: updates the title of the new_tutorial object, saves the update, and asserts that a tutorial with the updated name exists in the database. 
# o	Inside this test function's body, new_tutorial refers not to the new_tutorial fixture function, but to the object returned from that fixture function.
def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

# Fixture function that creates a different Tutorials object
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# Adds a test that uses both fixtures as parameters
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk
# The test asserts that the .pk attributes are not equal to the other.
# The .pk attribute in the Django ORM refers to the primary key of a database object, which is automatically generated when it is created.
