import phonenumbers
from phonenumbers import geocoder

#Code to track/trace the country of a phone number

number = "+27182652456"
phonenumber = phonenumbers.parse(number)

print(geocoder.description_for_number(phonenumber, 'en'))