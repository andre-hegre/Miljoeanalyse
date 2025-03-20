import sys
import json
print("Python executable:", sys.executable)

import requests

url="https://api.met.no/weatherapi/airqualityforecast/0.1/?lat=60&lon=10&areaclass=grunnkrets"
headers={"User-Agent": "værdatainnsamling/1.0 (andrhegr@stud.ntnu.no)"}

response=requests.get(url,headers=headers)
if response.status_code == 200:
    data = response.json()
<<<<<<< HEAD
    with open("Miljoeanalyse/proj_environment-main/data/weather_data.json", "w") as json_file:
=======
    with open("proj_environment-main/weather_data.json", "w") as json_file:
>>>>>>> ec06f7a7d687f2f5f864b18b73a3398533e44ffb
        json.dump(data, json_file, indent=4)
else: 
    print("error")
   
