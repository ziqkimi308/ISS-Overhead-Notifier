# Import
import requests
import datetime as dt
import smtplib
import time

# --------------------------------- CONSTANT ------------------------------------------- #
# CHANGE YOUR LATITUDE AND LONGITUDE HERE
MY_LATITUDE = 3.139003
MY_LONGITUDE = 101.686852

# CHANGE YOUR EMAIL AND PASSWORD HERE
MY_EMAIL = "sweetsugarpastry@gmail.com"
MY_PASSWORD = "rqaarmydmibkgzdl" # Get your specific app password from your respective email provider
TO_EMAIL = "sweetsugarpastry22@yahoo.com"

# ---------------------------------- ISS SETUP --------------------------------------- #
def is_iss_overhead():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()

	data = response.json()

	iss_longitude = float(data["iss_position"]["longitude"])
	iss_latitude = float(data["iss_position"]["latitude"])


	if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE <= iss_longitude <= MY_LONGITUDE:
		return True

# -------------------------------- SUNRISE SUNSET SETUP ----------------------------------------- #
def is_night():
	# Parameters
	parameters = {
		"lat": MY_LATITUDE,
		"lng": MY_LONGITUDE,
		"formatted": 0
	}

	response = requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400", params=parameters)
	response.raise_for_status()
	data_response = response.json()

	# Sunrise and sunset times (hour only)
	sunrise = int(data_response["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data_response["results"]["sunset"].split("T")[1].split(":")[0])

	# Current time (hour only)
	time_now = dt.datetime.now().hour

	if time_now <= sunrise or time_now >= sunset:
		return True

# ------------------------------ EMAIL SETUP -------------------------------- #
if is_iss_overhead() and is_night():
	connection = smtplib.SMTP("smtp.gmail.com", 587)
	connection.starttls()
	connection.login(MY_EMAIL, MY_PASSWORD)
	connection.sendmail(
		from_addr=MY_EMAIL,
		to_addrs=TO_EMAIL,
		msg="Subject:Look up to the sky!\n\nThe ISS is above you in the sky!"
	)

# You can make this code always running by:
# while True:
# 	# Use sleep function from time module. sleep() delays execution by 60 seconds in this case
# 	time.sleep(60)
# 	connection = smtplib.SMTP("smtp.gmail.com", 587)
# 	connection.starttls()
# 	connection.login(MY_EMAIL, MY_PASSWORD)
# 	connection.sendmail(
# 		from_addr=MY_EMAIL,
# 		to_addrs=TO_EMAIL,
# 		msg="Subject:Look up to the sky!\n\nThe ISS is above you in the sky!"
# 	)