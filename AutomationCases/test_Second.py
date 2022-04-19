import pytest
@pytest.mark.Smoke
def test_tc_001_login_logout_Testing():
    print("This is smoke test case...")
    print("This is end of test case...")

@pytest.mark.Sanity
def test_tc_002_login_logout_Invalid_Credential_Testing():
    print("This is my sanity test case...")
    print("This is end of test case...")

##Note:
#Print staement output display on console or terminal '-s'
#Verbose mode-display test cases name with status     '-v'
