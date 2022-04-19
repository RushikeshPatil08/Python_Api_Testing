import requests
import json
import  jsonpath
import openpyxl
from Data_Driven_Testing import Library


def test_add_multiple_data():
    #API
    url="http://thetestingworldapi.com/api/studentsDetails"
    f=open('C:/Users/Rushikesh.Patil/Desktop/json file/AddStudentDetail.json','r')
    json_request = json.loads(f.read())

    obj=Library.Common('C:/Users/Rushikesh.Patil/Desktop/json file/TestData.xlsx','Sheet1')
    col=obj.fetch_column_count()
    row=obj.fetch_row_count()
    keyList=obj.fetch_key_names()



    for i in range(2,row+1):
        updated_json_request=obj.update_request_with_data(i,json_request,keyList)
        response=requests.post(url,updated_json_request)
        print(response.status_code)
        print(response.text)
        assert response.status_code==201


    # json_request=json.loads(f.read())
    # response=requests.post(url,json_request)
    # print(response.status_code)
    # assert response.status_code==201



