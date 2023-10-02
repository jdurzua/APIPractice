#rest apis
#application programming interface
import requests #request something from
# the internet
import json #json stands for javascript

response = requests.get("https://randomuser.me/api/")
# print(response.json())                        
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
name1 = response.json()['results'][0]['name']['first']
name2 = response.json()['results'][0]['name']['last']
print(name1)
print(name2)
email = response.json()['results'][0]['email']
print(email)
phone = response.json()['results'][0]['phone']
print(phone)
city = response.json()['results'][0]['location']['city']
print(city)
postal_code = response.json()['results'][0]['location']['postcode']
print(postal_code)
address = response.json()['results'][0]['location']['street']
print(address)
DOB = response.json()['results'][0]['dob']['date']
print(DOB)
id = response.json()['results'][0]['id']
print(id)

