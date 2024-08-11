import requests

base = "https://petstore.swagger.io/v2"

def view_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response Body:: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print("The incoming content is not in JSON format.")
        print(f"Response Body: {response.text}")
    print("\n")
    
#-------------- CREATE -------
# CREATE - Positive Scenario
def create_positive():
    data = {
        "id": 123456,
        "name": "Gökhan",
        "status": "valid"
    }
    response = requests.post(f"{base}/pet", json=data)
    print("CREATE - Positive Scenario:")
    view_response(response)

# CREATE - Negative Scenario
def create_negative():
    data = {
        "id": "in_valid", #created with id that does not match the format
        "name": "Gökhan",
        "status": "valid"
    }
    response = requests.post(f"{base}/pet", json=data)
    print("CREATE - Negative Scenario:")
    view_response(response)
    
#-------------- READ -------
# READ - Positive Scenario
def get_positive():
    id = 123456
    response = requests.get(f"{base}/pet/{id}")
    print("READ - Positive Scenario:")
    view_response(response)

# READ - Negative Scenario
def get_negative():
    id = 999999  #is retrieved with a non-existent id
    response = requests.get(f"{base}/pet/{id}")
    print("READ - Negative Scenario:")
    view_response(response)

#-------------- UPDATE -------
# UPDATE - Positive Scenario
def update_positive():
    data = {
        "id": 123456,
        "name": "Gokhan",
        "status": "valid"
    }
    response = requests.put(f"{base}/pet", json=data)
    print("UPDATE - Positive Scenario:")
    view_response(response)

# UPDATE - Negative Scenario 
def update_negative():
    data = {
        "id": "invalid id", 
        "name": "Gokhan",
        "status": "invalid_status"  
    }
    response = requests.put(f"{BASE_URL}/pet", json=data)
    print("UPDATE - Negative Scenario:")
    view_response(response)
    
#-------------- DELETE -------
# DELETE - Positive Scenario
def delete_positive():
    id = 123456
    response = requests.delete(f"{BASE_URL}/pet/{id}")
    print("DELETE - Positive Scenario:")
    view_response(response)

# DELETE - Negative Scenario
def delete_negative():
    id = 999999 #deleted with non-existent id
    response = requests.delete(f"{BASE_URL}/pet/{id}")
    print("DELETE - Negative Scenario:")
    view_response(response)

if __name__ == "__main__":
    create_positive()
    create_negative()
    
    get_positive()
    get_negative()
    
    update_positive()
    update_negative()
    
    delete_positive()
    delete_negative()