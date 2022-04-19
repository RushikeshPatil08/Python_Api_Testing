import requests
import json
import  pytest
import jsonpath
from requests.auth import HTTPBasicAuth


def test_basic_auth():
    url="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"
    response=requests.get(url,auth=HTTPBasicAuth('rushi.patil9051@gmail.com','(password of github)'))
    print(response.text)
