from django.http import HttpResponse
from django.http import JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


def getAccessToken(request):
    consumer_key = 'pl1iuAP0UJTg7iHSGWsuTwKNBXcAbZCU'
    consumer_secret = 'BUzDTBeGOO0P8HMn'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)

@csrf_exempt
def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254701020901,
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254701020901,
        "CallBackURL": "https://cityparkapi1.herokuapp.com/citypark/callback/",
        "AccountReference": "Henry",
        "TransactionDesc": "Testing stk push"
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')

@csrf_exempt
def MpesaCallBack(request):
    # logging.info("{}".format("Callback from MPESA"))
    data = request.body.decode('utf-8')
    mpesa_payment = json.loads(data)
    # print("Mpesa Payment")
    # print(mpesa_payment)
    # -print(mpesa_payment['FirstName'])
    # return mpesa_payment
    return JsonResponse(mpesa_payment)