# import json
# import requests 

# def demograph(state):
#     URL = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=2019"
#     r = requests.get(url = URL) 
#     data = r.json() 
#     ui=input("enter state:")
#     l=[]
#     flag=False
#     for i in data['data']:
#         if(i['State']==ui):
#             l.append(i)
#             print(i)
#             flag=True
#             break
#     if not flag:
#         print("does not exist")
#         return None
#     return l



# def bmi(payload):
#     URL ="http://localhost:3001/api/getBMI"
#     # h= float(input("enter:"))
#     # w= float(input("enter:"))
#     # n= input("enter:")
#     # payload = {

#     # "height": h,
#     # "weight": w,
#     # "Name": n

#     #     }
#     r = requests.request("GET", URL, json=payload)
#     #r = requests.get(url = URL) 
#     data = r.text
#     res = json.loads(data) 
#     #ui=input("enter state:")
#     # l=''
#     # flag=False
#     # for i in data:
#     #     l=l+i

#     return res['message']


#import requests

# h= float(input("enter:"))
# w= float(input("enter:"))
# n= input("enter:")
# m={

#     "height": 1.75,
#     "weight": 60,
#     "Name": 'omi'

#     }

# p= bmi(m)
# print(p)
# print(type(p))

# url = "http://localhost:3001/api/getBMI"


# h= float(input("enter:"))
# w= float(input("enter:"))
# n= input("enter:")
# payload = {

#   "height": h,
#   "weight": w,
#   "Name": n

# }



# response = requests.request("GET", url, json=payload)

# print(response.text)


#import requests

# url = "https://mega-fitness-calculator1.p.rapidapi.com/bmi"

# querystring = {"weight":"61","height":"175"}

# headers = {
# 	"X-RapidAPI-Host": "mega-fitness-calculator1.p.rapidapi.com",
# 	"X-RapidAPI-Key": "0e9ea9299cmsh7181dc2853b9830p132c6fjsnadeb96451fc7"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)



# def bmi(x,y):
#     querystring = {"weight":x,"height":y}
#     url ="https://mega-fitness-calculator1.p.rapidapi.com/bmi"
#     headers = {"X-RapidAPI-Host": "mega-fitness-calculator1.p.rapidapi.com",
# 	"X-RapidAPI-Key": "0e9ea9299cmsh7181dc2853b9830p132c6fjsnadeb96451fc7"}
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     # h= float(input("enter:"))
#     # w= float(input("enter:"))
#     # n= input("enter:")
#     # payload = {

#     # "height": h,
#     # "weight": w,
#     # "Name": n

#     #     }
#     #r = requests.request("GET", URL, json=payload)
#     #r = requests.get(url = URL) 
#     data = response.text
#     res = json.loads(data) 
#     #ui=input("enter state:")
#     # l=''
#     # flag=False
#     # for i in data:
#     #     l=l+i
    
#     l= str(res['info']['bmi'])+' '+res['info']['health']+' '+res['info']['healthy_bmi_range']
#     return l

# r=bmi('60','175')
# print(r)


# def calories(x):
#     url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"

#     querystring = {"ingr":x}
#     headers = {"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
#     "X-RapidAPI-Key": "0e9ea9299cmsh7181dc2853b9830p132c6fjsnadeb96451fc7"}
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     data=response.text
#     res = json.loads(data)

#     return res['calories'] 


# y=calories('2 large mango')
# print(y)

# import requests

# url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"

# querystring = {"ingr":"1 large mango"}

# headers = {
# 	"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
# 	"X-RapidAPI-Key": "0e9ea9299cmsh7181dc2853b9830p132c6fjsnadeb96451fc7"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)




# #import mysql.connector
# import sqlite3

# #mydb=mysql.connector.connect(host="localhost",user="root",passwd="latanaik",database="Rasa_feedback")
# def DataUpdate(exercise, details):
#     conn=sqlite3.connect('gym.db')
#     mycursor = conn.cursor()
#     mycursor.execute("""CREATE TABLE IF NOT EXISTS Physique (Height TEXT, Weight TEXT);""")
#     mycursor.execute("INSERT INTO Physique VALUES (?,?)",(exercise,details))
#     conn.commit()
#     print(mycursor.rowcount,"record inserted")
#     #conn.close()

# #DataUpdate("1.75","155")
# #DataUpdate("1.8","160")
# DataUpdate("1.75","65")
 

