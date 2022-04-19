
#Test case Code must be written inside a method
#Method name must be written with test_ or nd with _test

actual_result="Testing"

def test_tc_001_login_logout_Testing():
    print("This is login & logout test case...")
    print("This is end of test case...")
    #assert actual_result=="Hello"      #Assertion    #compare data to be same
    assert actual_result !="Hello"      #Compare data not to be same
    assert actual_result == "Hello" ,"This 2 values must be same"          #Compare data and display CUstomized message in terms of failurre

def test_tc_002_login_logout_Invalid_Credential_Testing():
    print("This is my invalid testcase test case...")
    print("This is end of test case...")

##Note:
#Print staement output display on console or terminal '-s'
#Verbose mode-display test cases name with status     '-v'
