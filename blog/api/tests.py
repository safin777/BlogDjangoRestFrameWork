from django.test import TestCase
import requests # This is a third party library that allows us to make HTTP requests

# Create your tests here.

request = requests.get('http://127.0.0.1:8000') # This is the HTTP request
print(request.json()) # This is the HTTP response