import pytest
import requests
import  json

a=101

#Decorator
#Skip execution of any specific testcase
@pytest.mark.skip("Skipping as this functionality is not working devloper fixed it new build")
def test_tc_001_login_logout_Testing():
    print("This is login & logout test case...")
    print("This is end of test case...")

#Conditionaly skip execution of any specific testcase
@pytest.mark.skipif(a>100,reason="a is smaller than 100")
def test_tc_002_login_logout_Invalid_Credential_Testing():
    print("This is my invalid testcase test case...")
    print("This is end of test case...")


def test_tc_003_login_logout_Invalid_Credential_Testing():
        print("This is my invalid testcase test case...")
        print("This is end of test case...")