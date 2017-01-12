#!/usr/bin/env python

import requests

print requests.__version__


response = requests.get("https://raw.githubusercontent.com/saemorris/cmput404lab1/master/check_version.py")

print response.text
print response.status_code
