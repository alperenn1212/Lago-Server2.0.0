import socket, ipaddress, requests, time
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

print("                                                                -------------------------------------------            ")
print("                                             --------------------------------------------------------------------------")
print("                                     ---------------------------------------------------------------------------------------")
print("                                      LAGO SERVER     LAGO SERVER     LAGO SERVER    LAGO SERVER LAGO SERVER LAGO SERVER LAGO SERVER LAGO SERVER LAGO SERVER ")
print("                              -------------------------------------------------------------------------------------------------------------------------------------")
print("                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("       ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("Welcome to my termux channel!")
print("Let's Go Start it.")
time.sleep(5)
print("figlet download...")
print("%30")
time.sleep(5)
print("requests download...")
print("%50")
time.sleep(10)
print("figo download...")
print("%70")
time.sleep(3)
print("lolcat download...")
print("%80")
time.sleep(3)
print("papo download...")
print("%90")
time.sleep(4)
print("slid download...")
print("%100...")
print("Download Complete! Pls wait 5 seconds.")
time.sleep(5)


Type = carrier.PhoneNumberType()

phonenumber = input("Please Enter Your Phone Number And Country Code: ")
print("Login Completed!")

pN = phonenumbers.parse(phonenumber)

for phonenumber in pN:
 if pN == phonenumber:
    service = carrier.name_for_number(pN,'en')
    print("Service provider:"+service)
    Region = geocoder.country_name_for_number(pN,'en')
    print("Country Name:"+Region)
    codecountry = phonenumbers.country_code_for_region(pN,'en')
    print("Country:"+codecountry)
    Region2 = geocoder.region_code_for_country_code(pN,'en')
    print("Country Code:"+Region2)
    Code = geocoder.is_number_type_geographical(pN,'en')
    print("Typing geographical:"+Code)
    TimeZone = timezone.time_zones_for_number(pN)
    print(TimeZone)
    TimeZone2 = timezone.time_zones_for_geographical_number(pN)
    print(TimeZone2)
    GEO = geocoder.description_for_number(pN,'en')
    print("Location:"+GEO)


    
