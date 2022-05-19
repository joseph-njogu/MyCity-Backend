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
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    global booking_info
    booking_info = body
    paid_car = body['car']
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": body['amount'],
        "PartyA": body['phone'],
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": body['phone'],
        "CallBackURL": "https://cityparkapi1.herokuapp.com/citypark/callback/",
        "AccountReference": "Parkcity for %s" % body['car'],
        "TransactionDesc": "Parkcity for %s" % body['car']
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')

@csrf_exempt
def MpesaCallBack(request):
    data = request.body.decode('utf-8')
    mpesa_payment = json.loads(data)
    if mpesa_payment['Body']['stkCallback']['Resultcode'] is 0:
        SubmitToDB()
    return JsonResponse(mpesa_payment)

def SubmitToDB():
    print(booking_info)
