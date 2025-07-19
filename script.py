

from flask import Flask, request, render_template

import os
import requests
# import pandas as pd
import warnings
from openai import OpenAI
import json

from dotenv import load_dotenv
import os
import openai

from flask import Flask, request, render_template

#Setting up the Flask framwork and tempalte folder for the pathway of all the HTML files
app = Flask(__name__, template_folder='docs')

#When the user goes to the preferences page, it will render the preference.html amd ask the user to fill the quick form (GET by default)
@app.route('/preferences.html')
def preferences():
    return render_template('preferences.html')

#When the user submits the form, it will retrieve the data from the form and send it to the sever (POST)
@app.route('/a', methods = ['POST'])
def submit():

    if request.method == "POST":
        city_retrived = request.form.get('city')
        print("City retrieved:", city_retrived)
        state_retrived = request.form.get('state')
        print("State retrieved:", state_retrived)
        minimum_retrived = int(request.form.get('minimum'))
        print("Minimum retrieved:", minimum_retrived)
        maximum_retrived = int(request.form.get('maximum'))
        print("Maximum retrieved:", maximum_retrived)
        structures_retrived = request.form.getlist('structure')
        print("Structures retrieved:", structures_retrived)
        bathrooms_retrived = int(request.form.get('bathroom'))
        print("Bathrooms retrieved:", bathrooms_retrived)
        bedrooms_retrived = int(request.form.get('bedroom'))
        print("Bedrooms retrieved:", bedrooms_retrived)


    try:
        details = user_rentalInfo(city_retrived,state_retrived)


        strong_match, good_match, weak_match, bad_match = rental_algorithm(details,city_retrived,state_retrived,minimum_retrived,maximum_retrived,structures_retrived,bathrooms_retrived,bedrooms_retrived)




        return render_template("chatBot.html", strong_result=strong_match,good_result = good_match,weak_result = weak_match, bad_result = bad_match , city=city_retrived)


    except Exception as e:
        print("An error occurred:", e)
        return render_template("preferences.html", error_message=str(e))
    
    return render_template("preferences.html")






city = ""
state = ""
minimum = 0
maximum = 0         
structures = []
bathrooms = 0
bedrooms = 0
num = 0

# app = Flask(__name__)

load_dotenv()

# Retrieve OpenAI API key from environment variables
OPEN_AI_TOKEN = os.getenv('API_KEY')


# load_dotenv()

# os.getenv("rentcast_API")

def user_rentalInfo(city,state):

    load_dotenv()

    os.getenv("rentcast_API")

    headers = {
        'X-Api-Key': os.getenv("rentcast_API"),
        'Content-Type': 'application/json'
    }

    # city = "Orlando"
    # state = "FL"
    params = {
        'city': city, 
        'state': state,
                }


    response = requests.get("https://api.rentcast.io/v1/listings/rental/long-term",headers=headers, params = params)

    response_string = str(response.content, 'utf-8')

    return json.loads(response_string)

# # print(response.status_code)
# # print(response.text)
 
# # data = response.json()

# # for j in data:
# #     print(j)

# #Sample
# f = open("florida_realEstateEXAMPLE.txt")

# text = f.read()


# structure = ["Apartment"]
# minimum = 1000
# maximum = 1500

# city = city.lower()
# state = state.lower()   
# structures = structures[0].lower()


def rental_algorithm(details,city,state,minimum,maximum,structures,bathrooms,bedrooms):
    # global strong_match, good_match, weak_match, bad_match

    strong_match = []
    good_match = []
    weak_match = []
    bad_match = []



    for num in range(len(details)):

        if(city == details[num]["city"]):

            if(state == details[num]["state"]):
                if(minimum < details[num]["price"] < maximum):
                    strong_match.append(details[num])

                    if (structures[0] == "Apartment" and details[num]["propertyType"] == "Condo") or (structures[0] == "House" and details[num]["propertyType"] == "Single Family") or ((structures[0] == "Apartment" and details[num]["propertyType"] == "Condo") and (structures[1] == "House" and details[num]["propertyType"] == "Single Family")):
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

    return strong_match, good_match, weak_match, bad_match


# for i in strong_match:
#     print(i)

# @app.route('/')
# def chatBot():
#     strong_result = strong_match
#     good_result = good_match
#     weak_result = weak_match
#     bad_result = bad_match

#     if len(strong_match) != 0:
#         print("file ready to send to chatBot.html")

#     return render_template("chatBot.html", strong_result=strong_result,good_result = good_result,weak_result = weak_result, bad_result = bad_result , city=city)


# @app.route('/test

# @app.route('/chatBot.html')
# def chatBot():
#     strong_result = strong_match
#     good_result = good_match
#     weak_result = weak_match
#     bad_result = bad_match

#     if len(strong_match) != 0:
#         print("file ready to send to chatBot.html")

#     return render_template("chatBot.html", strong_result=strong_result,good_result = good_result,weak_result = weak_result, bad_result = bad_result , city=city)


if __name__ == '__main__':
    app.run(debug=True)
