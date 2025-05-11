
import os
import openai
from openai import OpenAI
import requests
import flask
from flask import Flask, request, render_template, jsonify, redirect

from dotenv import load_dotenv
import os
import openai

app = Flask(__name__)

load_dotenv()

# Retrieve OpenAI API key from environment variables
OPEN_AI_TOKEN = os.getenv('API_KEY')

# Set OpenAI API key
openai.api_key = OPEN_AI_TOKEN

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/preferences")
def preferences():
    return render_template("preferences.html")

@app.route("/register", methods=["POST"])
def sub_register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    print(f"Registering user: Name={name}, Email={email}, Password={password}")

    # Redirect to preferences page
    return redirect("/preferences")



@app.route("/save_preferences", methods=["POST"])
def save_preferences():
    city = request.form.get("city")
    minimum = request.form.get("minimum")
    maximum = request.form.get("maximum")
    structure = request.form.getlist("structure[]")
    print(f"Saving preferences: City={city}, Minimum={minimum}, Maximum={maximum}, Structure={structure}")
    return redirect("/chat")


@app.route("/chat")
def chat():
    return render_template("chatBot.html")

# Function to handle OpenAI API calls
def response_to_pref(name, email, password, city, minimum, maximum, structure): 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are an intelligent real estate assistant that searches the internet to find the best estate options based on a user's preferences. 
                Given criteria such as location, budget, property type, number of bedrooms/bathrooms, square footage, amenities, and preferred neighborhood features, your job is to:

                1. "Search and analyze up-to-date listings from reliable real estate platforms and aggregator websites."
                2. "Filter and rank the options based on how well they match the user's criteria."
                3. "Return a clean, structured list of top property matches with detailed information (e.g., price, location, images, contact info, and key features)."
                4. "Ensure listings are current and avoid duplicates or outdated links."
            """},
            {"role": "user", "content": f"Your client needs {city, minimum, maximum, structure}. Provide all the suitable estate"}
        ]
    )
    return response['choices'][0]['message']['content']
