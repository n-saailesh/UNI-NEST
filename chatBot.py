
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


app = Flask(__name__)

load_dotenv()

# Retrieve OpenAI API key from environment variables
OPEN_AI_TOKEN = os.getenv('API_KEY')

# Set OpenAI API key
openai.api_key = OPEN_AI_TOKEN

#The retrieval user's infomation using flask and returns it in the parameters of the function: retrival_from_html
def retrival_from_html(city, minimum, maximum, structures):
    
    print(city, minimum, maximum, structures)

    return f"{city} {minimum} {maximum} {structures}"




load_dotenv()

os.getenv("rentcast_API")

headers = {
    'X-Api-Key': os.getenv("rentcast_API"),
    'Content-Type': 'application/json'
}

city = "Orlando"
state = "FL"
params = {
    'city': city, 
    'state': state
              }


# response = requests.get("https://api.rentcast.io/v1/listings/rental/long-term",headers=headers, params = params)



# print(response.status_code)
# print(response.text)
 
# data = response.json()

# for j in data:
#     print(j)

#Sample
f = open("florida_realEstateEXAMPLE.txt")

text = f.read()

details = json.loads(text)

structure = "Apartment"
minimum = 1000
maximum = 1500

strong_match = []
good_match = []
weak_match = []
bad_match = []


for num in range(len(details)):

    if(city == details[num]["city"]):

        if(minimum < details[num]["price"] < maximum):
            strong_match.append(details[num])

            if (structure[0] == "Apartment" and details[num]["propertyType"] == "Condo") or (structure[0] == "House" and details[num]["propertyType"] == "Single Family") or ((structure[0] == "Apartment" and details[num]["propertyType"] == "Condo") and (structure[1] == "House" and details[num]["propertyType"] == "Single Family")):
                strong_match.append(details[num])
    
        else:
            good_match.append(details[num])
    
    else:
        weak_match.append(details[num])

    for i in strong_match:
        print(i)

    # print(good_match)

    # print(weak_match)
        
    
     








