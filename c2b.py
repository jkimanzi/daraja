import requests
from requests.auth import HTTPBasicAuth

from utils import generate_token
import keys

def register_url():
    access_token = generate_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = { "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://micronics.co.ke/lipa/confirmation",
        "ValidationURL": "https://micronics.co.ke/lipa/validation"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
#register_url() - url already registered; function is run once hence # comment

def simulate_c2b():
    access_token = generate_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": keys.shortcode,
    "CommandID": "CustomerPayBillOnline",
    "Amount": "4",
    "Msisdn": keys.test_msisdn,
    "BillRefNumber": "Inv-0004" }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
simulate_c2b()