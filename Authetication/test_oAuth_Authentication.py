import requests
import  json
import jsonpath

def test_oAuth_api():

    token_url="https://thetestingworldapi.com/Token"
    data={
        "grant_type":"password",
        "username":"admin",
        "password":"adminpass"

    }
    response1=requests.post(token_url, data)
    token_value=jsonpath.jsonpath(response1,'access_token')

    auth={"Authorization":"Bearer "+token_value}


    url="http://thetestingworldapi.com/api/StDetails/1104"
    response2=requests.get(url,headers=auth)
    print(response2.text)