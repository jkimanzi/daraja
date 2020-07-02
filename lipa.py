import requests
from requests.auth import HTTPBasicAuth

from utils import generate_token
from utils import generate_passwd
from utils import get_timestamp
import keys

def lipa_na_mpesa():
    access_token = generate_token()
    time_stamp = get_timestamp()
    decoded_password = generate_passwd(time_stamp)

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.business_code,
        "Password": decoded_password,
        "Timestamp": time_stamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "2",
        "PartyA": keys.PhoneNumber,
        "PartyB": keys.business_code,
        "PhoneNumber": keys.PhoneNumber,
        "CallBackURL": "Your CallBackURL",
        "AccountReference": "Your AccountReference",
        "TransactionDesc": "Your TransactionDesc"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)
lipa_na_mpesa()
