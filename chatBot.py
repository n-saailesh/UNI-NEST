
import os
import requests
import panadas as pd
import warnings
from openai import OpenAI
import json

from dotenv import load_dotenv
import os
import openai

from flask import Flask, request, render_template
city = ""
state = ""
minimum = 0
maximum = 0         
structures = []
bathrooms = 0
bedrooms = 0

app = Flask(__name__)

load_dotenv()

# Retrieve OpenAI API key from environment variables
OPEN_AI_TOKEN = os.getenv('API_KEY')

# Set OpenAI API key
openai.api_key = OPEN_AI_TOKEN

#The retrieval user's infomation using flask and returns it in the parameters of the function: retrival_from_html
def retrival_from_html(city_retrived, state_retrived,minimum_retrived, maximum_retrived, strcutures,bathrooms_retrived, bedrooms_retrived):
    
    print("from script.py to chatBot.html" + city_retrived, state_retrived,minimum_retrived, maximum_retrived, strcutures,bathrooms_retrived, bedrooms_retrived)

    city = city_retrived
    state = state_retrived
    minimum = int(minimum_retrived) # Convert to integer
    maximum = int(maximum_retrived) # Convert to integer
    structures = strcutures  # This will be a list of structures
    bathrooms = int(bathrooms_retrived)
    bedrooms = int(bedrooms_retrived)

    return f"{city} {state} {minimum} {maximum} {structures} {bathrooms} {bedrooms}"


# load_dotenv()

# os.getenv("rentcast_API")

# headers = {
#     'X-Api-Key': os.getenv("rentcast_API"),
#     'Content-Type': 'application/json'
# }

city = "Orlando"
state = "FL"
params = {
    'city': city, 
    'state': state,
              }


# # response = requests.get("https://api.rentcast.io/v1/listings/rental/long-term",headers=headers, params = params)



# # print(response.status_code)
# # print(response.text)
 
# # data = response.json()

# # for j in data:
# #     print(j)

# #Sample
f = open("florida_realEstateEXAMPLE.txt")

text = f.read()

details = json.loads(text)

structure = ["Apartment"]
minimum = 1000
maximum = 1500

# city = city.lower()
# state = state.lower()   
# structures = structures[0].lower()


strong_match = []
good_match = []
weak_match = []
bad_match = []


for num in range(len(details)):

    if(city == details[num]["city"]):

        if(state == details[num]["state"]):
            if(minimum < details[num]["price"] < maximum):
                strong_match.append(details[num])

                if (structure[0] == "Apartment" and details[num]["propertyType"] == "Condo") or (structure[0] == "House" and details[num]["propertyType"] == "Single Family") or ((structure[0] == "Apartment" and details[num]["propertyType"] == "Condo") and (structure[1] == "House" and details[num]["propertyType"] == "Single Family")):
                    strong_match.append(details[num])
                
                    if bathrooms == details[num]["bathrooms"]:

                        if bedrooms == details[num]["bedrooms"]:
                            strong_match.append(details[num])

                    else:
                        good_match.append(details[num])

                else:
                    weak_match.append(details[num])
            else:
                weak_match.append(details[num])

        else:
            bad_match.append(details[num])
    else:
        bad_match.append(details[num])


# for i in strong_match:
#     print(i)

@app.route('/')
def chatBot():
    good_result = strong_match

    if len(strong_match) != 0:
        print("file ready to send to chatBot.html")

    return render_template("chatBot.html", good_result=good_result, city=city)


# @app.route('/test')
# def test():
#     test_data = [
#         {'propertyType': 'House', 'price': 250000, 'address': '123 Test St'}
#     ]
#     print("Test route called with:", test_data)
#     return render_template("chatBot.html", good_result=test_data, city="Test City")



if __name__ == '__main__':
    app.run(debug=True)

    

        
    
     








