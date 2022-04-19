import  pytest
import  requests
import  json
import  jsonpath


def test_add_student_data():
    App_url = "http://thetestingworldapi.com/api/studentsDetails"
    # f=open('C:\\Users\\Rushikesh.Patil\\Desktop\\json file\\createNewUser2.json','r')
    # request_json=json.loads(f.read())

    data = {
        "first_name": "Rushikesh",
        "middle_name": "v.",
        "last_name": "patil",
        "date_of_birth": "2/6/1653"

    }
    headers = {"content-type": "application/json"}

    response = requests.post(App_url, json=data, headers=headers)
    print(response.url)
    print(response.headers)
    print(response.status_code)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])
    print("...........................")
    return str (id[0])




def test_get_student_data():

    id=json.loads(test_add_student_data())
    print("id come from add studenet mehtod",id)

    url=f"http://thetestingworldapi.com/api/studentsDetails/{id}"

    response=requests.get(url)
    print(response.url)
    print(response.text)
    json_response=json.loads(response.text)
    id1=jsonpath.jsonpath(json_response,"data.id")
    assert  id1[0]==id
    print("...........................")




def test_update_student_data():
    id = json.loads(test_add_student_data())
    print("we update the data of id:",id)
    App_url = f"http://thetestingworldapi.com/api/studentsDetails/{id}"
    # f=open('C:\\Users\\Rushikesh.Patil\\Desktop\\json file\\createNewUser2.json','r')
    # request_json=json.loads(f.read())

    data = {
        "id":f"{id}",
        "first_name": "Rushi",
        "middle_name": "vijay ",
        "last_name": "patil",
        "date_of_birth": "2/8/1653"

    }
    headers = {"content-type": "application/json"}

    response = requests.post(App_url, json=data, headers=headers)
    print(response.url)
    print(response.headers)
    print(response.status_code)
    print(response.text)
    id2= jsonpath.jsonpath(response.json(), 'id')
    print(id2[0])
    print("...........................")




def test_delete_student():
    id = json.loads(test_add_student_data())
    url=f"http://thetestingworldapi.com/api/studentsDetails/{id}"
    response=requests.delete(url)
    print(response.url)
    print(response.text)


    print("...........................")




#After deleting the student i try to fetch the student
def test_check_delete_student_data():

    id=json.loads(test_add_student_data())

    url=f"http://thetestingworldapi.com/api/studentsDetails/{id}"

    response=requests.get(url)
    print(response.url)
    print(response.text)
    json_response=json.loads(response.text)
    id1=jsonpath.jsonpath(json_response,"data.id")

    print("...........................")








