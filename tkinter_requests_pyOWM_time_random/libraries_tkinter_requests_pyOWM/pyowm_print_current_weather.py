# https://pypi.org/project/pyowm/
# https://github.com/csparpa/pyowm

import pyowm


city = input("What city you are interested:")

def print_current_weather(city):
    owm = pyowm.OWM('1250f5d30b063ec8a638c3e8ac131b17')    # provide a valid API key
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather  #print(w)  #<Weather - reference time=2013-12-18 09:20, status=Clouds>
    temperature = w.temperature('celsius') # print(temperature)

    print(f"Min temperature {w.temperature('celsius')['temp_min']}")
    print(f"Max temperature {temperature['temp_max']}")
    print(f"Temperature {temperature['temp']}")

    # print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
    print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature['temp']) + " for the Celsius")
    print("In this city "+ w.detailed_status)
    # print(w.detailed_status)

print_current_weather(city)