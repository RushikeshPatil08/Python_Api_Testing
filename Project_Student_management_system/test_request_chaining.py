import  requests
import  json
import jsonpath


def test_add_new_student():
    global id
    url="http://thetestingworldapi.com/api/studentsDetails"
    data={
        "first_name": "Rushikesh",
        "middle_name": "v.",
        "last_name": "patil",
        "date_of_birth": "2/6/1653"

    }
    response=requests.post(url,json=data)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])



def test_get_details():
    url="http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response=requests.get(url)
    print(response.text)


