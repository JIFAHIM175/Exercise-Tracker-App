import requests
import datetime
APP_ID = "162a6d55"
API_KEY = "deb37af0bf904166728b5f465339f179"

GENDER = "male"
WEIGHT = 50
HEIGHT = 175
AGE = 22

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Type in what exercises you did today:")

params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=API_ENDPOINT, json=params, headers=HEADERS)
result = response.json()

date_today = datetime.datetime.now().strftime("%d/%m/%Y")
time_now = datetime.datetime.now().strftime("%X")


SHEETY_API = "https://api.sheety.co/5367751af3a468d2da8eca82347b232d/myWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_header = {
    "Authorization":f"Bearer ajnksdbhsndnoisaiuhdoidsiisnidasu"
}

sheet_response = requests.post(url=SHEETY_API, json=sheet_inputs)


print(sheet_response.text)