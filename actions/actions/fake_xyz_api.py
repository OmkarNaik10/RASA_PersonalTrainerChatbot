
# importing the requests library 

# import requests
# import json 

  
 

# URL = "http://universities.hipolabs.com/search?country=United+States"



# r = requests.get(url = URL) 

  


# data = r.json() 

# print(data[0]['country'])
# ui=input("enter:")
# print(len(data))
# for i in range(len(data)):
#     if(data[i]['country']=='United States'):
#         print(data[i]['name'])
# else:
#     print("does not exist")
#     break

# print(data[]['state-province'])
# print(data['data'][0]) 


#gymname
# def gymname(city):
#     URL = "http://localhost:3001/api/getGyms?city="+city
#     response = requests.request("GET", URL)
#     data=response.text
#     res = json.loads(data)
#     l='Planet Fitness, 24 hour fitness'
#     for i in res['data']['result']:
#         l=l+','+' '+i 

#     return l


# #import requests
# city=input("enter city")
# x=gymname(city)
# print(x)
# print(type(x))
# url = "http://localhost:3001/api/getGyms?city="+city




# response = requests.request("GET", url)

# print(response.text)