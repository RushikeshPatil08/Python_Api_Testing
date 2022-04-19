import  requests
import  json
import jsonpath




def test_Add_new_data() :
    App_url="http://thetestingworldapi.com/api/studentsDetails"
    # f=open('C:\\Users\\Rushikesh.Patil\\Desktop\\json file\\createNewUser2.json','r')
    # request_json=json.loads(f.read())


    data={
    "first_name": "Rushikesh",
    "middle_name": "v.",
    "last_name": "patil",
    "date_of_birth":"2/6/1653"

    }
    headers={"content-type":"application/json"}

    response=requests.post(App_url,json=data,headers=headers)
    print(response.headers)
    print(response.status_code)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    print("/////////////////////////////")

##Technical detail
    tech_Api_Url="http://thetestingworldapi.com/api/technicalskills"
    # f=open('C:\\Users\\Rushikesh.Patil\\Desktop\\json file\\TechDetails.json','r')
    # request_json=json.loads(f.read())
    # request_json['id']=int(id[0])
    # request_json['st_id'] = id[0]


    response = requests.post(tech_Api_Url, json={
   "id":1117497,
   "language":[
       "java",
       "python"
   ],
    "yearexp":"2",
    "lastused":"2022",
    "st_id":"1117497"
})
    print(response.json())
    print(response.content)
    print(response.status_code)
    print(response.text)
    print("///////////////////////////////")



  #Address Detail

    address_Api_Url = "http://thetestingworldapi.com/api/addresses"
    f = open('C:\\Users\\Rushikesh.Patil\\Desktop\\json file\\Student_Addresses.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId']=id[0]
    response = requests.post(address_Api_Url, request_json)
    print(response.status_code)
    print(response.text)

    final_details="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(final_details)
    print(response.text)

    print("/////////////////////////////////")



#Final Deatil
    final_detail_url="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(final_detail_url)
    print(response.text)


    print("////////////////////////////////////")





