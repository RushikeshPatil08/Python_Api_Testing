import pytest
import requests
import  json

a=101

#Decorator
@pytest.mark.Smoke
def test_tc_001_login_logout_Testing():
    print("This is my smoke test case...")
    print("This is end of test case...")

@pytest.mark.Sanity
def test_tc_002_login_logout_Invalid_Credential_Testing():
    print("This is my sanity test case...")
    print("This is end of test case...")


def test_tc_003_login_logout_Invalid_Credential_Testing():
        print("This is my invalid testcase test case...")
        print("This is end of test case...")