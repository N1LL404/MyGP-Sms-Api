# MyGP API OTP Login

A Python script to request an OTP (One-Time Password) login from the MyGP (Grameenphone) mobile application API.

## Overview

This script sends a GET request to the MyGP API endpoint to initiate the OTP login process for a Grameenphone mobile number.

## Requirements

```bash
pip install requests
```

## Code

```python
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

response = requests.get(
    'https://mygp.grameenphone.com/mygpapi/v2/otp-login', 
    params=params, 
    headers=headers
)

print(response.text)
```

## Parameters

### Headers
- **Cache-Control**: Prevents caching of the request
- **User-Agent**: Identifies as MyGP Android app version 475 on Android 34
- **Accept-Language**: Requests English language content
- **APP-MSISDN**: The mobile number making the request
- **ng**: Network generation parameter (set to '0')
- **Connection**: Maintains persistent connection

### Query Parameters
- **msisdn**: Mobile Station International Subscriber Directory Number (phone number in format 8801711111111)
- **lang**: Language preference (en for English)
- **ng**: Network generation parameter

## Usage

1. Replace `8801711111111` with your actual Grameenphone mobile number
2. Run the script:
   ```bash
   python script.py
   ```
3. The API response will be printed to the console

## API Endpoint

```
GET https://mygp.grameenphone.com/mygpapi/v2/otp-login
```

## Response

The response will contain the OTP request status and details. The exact format depends on the API implementation.

## Notes

- This script requires a valid Grameenphone mobile number
- The OTP will be sent to the specified mobile number via SMS
- Ensure you have proper authorization to use this API
- This is for educational and authorized use only

## Security Considerations

⚠️ **Important**: 
- Never hardcode real phone numbers in production code
- Store sensitive information in environment variables
- Use proper authentication mechanisms for production applications
- Comply with Grameenphone's API terms of service

## License

This documentation is provided for educational purposes.

## Disclaimer

This code is for demonstration purposes. Ensure you have proper authorization from Grameenphone and comply with their API usage policies before using this in any production environment.
