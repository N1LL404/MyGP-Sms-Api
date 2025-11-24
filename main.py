import requests

headers = {
    'Cache-Control': 'no-cache',
    'User-Agent': 'Android/34 MyGP/475 (en)',
    'Accept-Language': 'en',
    'Vary': 'Accept-Language',
    'APP-MSISDN': '8801711111111',
    'ng': '0',
    'Connection': 'Keep-Alive',
}

params = {
    'msisdn': '8801711111111',
    'lang': 'en',
    'ng': '0',
}

response = requests.get('https://mygp.grameenphone.com/mygpapi/v2/otp-login', params=params, headers=headers)



print(response.text)
