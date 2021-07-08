import pywhatkit

country_code = input("Country Code : ")
if country_code[0] != "+":
    country_code = "+" + country_code

mobile_number = input("Mobile Number : ")
message = input("Message : ")
hour = int(input("Hour(24 hrs) : "))
min = int(input("Minutes : "))

pywhatkit.sendwhatmsg(country_code + " " + mobile_number, message, hour, min, tab_close = 5)
