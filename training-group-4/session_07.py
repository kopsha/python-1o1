import requests

api_root = "https://jsonplaceholder.typicode.com"


## Cleaner version
def call_get(api_resource, resource_id):
    api_url = f"{api_root}/{api_resource}/{resource_id}"
    response = requests.get(api_url)
    assert response.status_code == 200
    print("GET", api_url, "=>", response)
    data = response.json()
    return data


def call_post(api_resource, payload: dict):
    api_url = f"{api_root}/{api_resource}"
    response = requests.post(api_url, data=payload)
    assert response.status_code == 201
    print("POST", api_url, "=>", response)
    print(response.json())


def call_put(api_resource, resource_id, payload: dict):
    api_url = f"{api_root}/{api_resource}/{resource_id}"
    response = requests.put(api_url, data=payload)
    assert response.status_code == 200
    print("PUT", api_url, "=>", response)
    print(response.json())


print("Hello API world")
data = call_get("todos", 1)
print(f"Todo 1, contains {data}")
assert "id" in data
assert "title" in data
assert len(data["title"]) > 10

albums_data = call_get("albums", 38)
print(albums_data)

call_post(
    "posts",
    payload={
        "title": "Shiny new post",
        "test_info": "Fake API is tested",
        "address": {
            "streetname": "Calarasi",
            "number": 123,
        },
    },
)

call_put("albums", 38, payload={
    "title": "Manele, manele",
    "test_info": "Another API is tested",
    "address": "Cluj-Napoca",
})


for some_id in range(10, 100, 5):
    payload = dict(
        title = f"Manele #{some_id}",
        author = "Babasha",
    )
    call_post("albums", payload=payload)

