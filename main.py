import requests
from datetime import datetime
import os
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["API_ID"]  # raises exception if key does not exist

API_KEY = os.environ["API_KEY"]
sheets_endpoint = os.environ["sheets_endpoint"]
YOUR_USERNAME = "fabio777"
YOUR_PASSWORD = "fabiopass123"
token = os.environ["token"]
# API_KEY = "01f46814400ab28b220802941597b756"
# sheets_endpoint = "https://api.sheety.co/bbdf5e2cf39cb5f0ad921d023af513d5/myWorkouts/workouts"
# YOUR_USERNAME = "fabio777"
# YOUR_PASSWORD = "fabiopass123"
# token = {
#     "Authorization": f"Bearer sjunveoqrupvnqeo89"
# }

exercise_text = input("Tell me which exercises you did today: ")

GENDER = "Male"
WEIGHT_KG = 95
HEIGHT_CM = 185
AGE = 20


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

now = datetime.today()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

for exercise in result["exercises"]:
    parameters2 = {
      "workout": {
        "date": date,
        "time": time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
      }
}

sheets_response = requests.post(url=sheets_endpoint, json=parameters2,  auth=(YOUR_USERNAME, YOUR_PASSWORD))
print(sheets_response.text)