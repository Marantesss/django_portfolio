"""
Inside this module, we need to import the path object as well as our app’s views module.
Then we want to create a list of URL patterns that correspond to the various view functions.
At the moment, we have only created one view function, so we need only create one URL
"""
from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]