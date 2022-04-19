

import pytest
import requests
import  json

a=101

@pytest.fixture(scope="module")
def fixture_code():
    print("This is fixture")
    print(".................")
    yield                          ####Note:code above the yield execute before starting test case and code below the yield will ececute after executing the testcase.
    print("Close the db connection")
    print(".................")




@pytest.mark.Smoke
def test_tc_001_login_logout_Testing(fixture_code):
    print("This is smoke test case...")
    print("This is end of test case...")

@pytest.mark.Sanity
def test_tc_002_login_logout_Invalid_Credential_Testing(fixture_code):
    print("This is my sanity test case...")
    print("This is end of test case...")


def test_tc_003_login_logout_Invalid_Credential_Testingfixture_code():
        print("This is my invalid testcase test case...")
        print("This is end of test case...")




##Scope:if you provide the scope=module so task which you want perform to before testcase it will execute first of all testcases  and task which you want to perform end of the testcases it will execute only 1 time at the end of the testcases.
#like:this is fixture is execute before starting the testcases execution  and close the db connection is execute only 1 time after execution of all testcases is completed.
