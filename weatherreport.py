import requests
#imports requests module
from datetime import datetime
#imports datetime 
import pytz
#imports pytz which was used to get time by country code

my_key = 'ff48c5c68c604ee606ba13abff5bb76c'
#key given by weather api

location = input("Enter the city name: ")
#It is field to take input

common_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+my_key
#It is the link to access the web
req_link = requests.get(common_link)
#requesting server to get link
api_format = req_link.json()

IST = pytz.timezone('Asia/Kolkata')
#timezone selection for time

#create variables to store and display data
loc_temp = ((api_format['main']['temp']) - 273.15)
#calling temperature to "loc_temp" variable
des_wthr = api_format['weather'][0]['description']
#calling description to "api_format" variable
hmdt = api_format['main']['humidity']
#calling %of humidity to "hmdt" variable
wind_spd = api_format['wind']['speed']
#calling wind speed to "wind_spd" variable
country = api_format['sys']['country']
#calling country code to "country" variable
sun_rise = api_format['sys']['sunrise']
sun_set = api_format['sys']['sunset']
#calling the sunrise and sunset
date_time = datetime.now(IST).strftime("%d :%m :%Y | %H:%M:%S %p")
#calling date and time in a format

#making variables for easy access
first_out = "Weather report for - {}  || {} . ".format(location.upper(), date_time)
second_out = "{} belongs to {} country.".format(location.upper(), country)
third_out = " The Sun rises at {} AM and sets at {} PM . ".format(sun_rise/246000000, sun_set/246000000)
fourth_out = "Current temperature is: {:.2f} °C .".format(loc_temp)
fifth_out = "Current weather looks  : {} .".format(des_wthr)
sixth_out = "Current Humidity  is : {} % .".format(hmdt)
seventh_out = "Current wind speed is nearly: {} kmph . ".format(wind_spd)

#printing all the results
print("---------------------------------------------------------------------")
print(first_out)
print(second_out)
print(third_out)
print("----‐------------------------------------------------------------------")
print(fourth_out)
print(fifth_out)
print(sixth_out)
print(seventh_out)
print("Thank you for using me")
#The saving of txt file starts from here
with open("weatherreport.txt" ,mode = 'w' ,encoding ='utf-8')as f :
	f.write("----------------------------------------------------------‐--")
	f.write(first_out)
	f.write(second_out)
	f.write(third_out)
	f.write("=====================================")
	f.write(fourth_out)
	f.write(fifth_out)
	f.write(sixth_out)
	f.write(seventh_out)
	f.write("--------------**********------‐------")
	
	f.close()
#stops saving values from here
