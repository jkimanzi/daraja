import requests
from requests.auth import HTTPBasicAuth

import base64
from datetime import datetime

import keys

def get_timestamp():

    time_now = datetime.now()
    time_stamp = time_now.strftime("%Y%m%d%H%M%S")
    return time_stamp

def generate_token():

    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = response.json()
    access_token = json_response['access_token']
    return access_token

def generate_passwd(time_stamp):
    time_now = datetime.now() 
    time_stamp = time_now.strftime("%Y%m%d%H%M%S")
    
    #Generate password by base64 encoding BusinessShortcode, Passkey and Timestamp.
    data_to_encode = keys.business_code + keys.passkey + time_stamp
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8') 
    
    return decoded_password