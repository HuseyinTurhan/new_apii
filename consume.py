import requests

response = requests.get("http://127.0.0.1:8000/students")

print("After GET request..")
print(response)
print(response.json())


response = requests.post("http://127.0.0.1:8000/students", json = {'name':"George Bush", 'age':45, 'course':'Goverment', 'college': "USA Academy"})

print("After POST request..")
print(response)
print(response.json())

response = requests.put("http://127.0.0.1:8000/students/5", data = {'name':"George Bush", 'age':55, 'course':'State admin', 'college': "USA Academy"})

print("After PUT request..")
print(response)
print(response.json())

response = requests.delete("http://127.0.0.1:8000/students/5")

print("After DELETE request..")
print(response)
