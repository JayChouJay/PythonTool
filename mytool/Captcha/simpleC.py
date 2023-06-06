import requests

def get_token(token_url,client_id,client_secret):
    payload='client_id=' + str(client_id) + \
            '&client_secret=' + str(client_secret) + '&grant_type=client_credentials'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", token_url, headers=headers, data=payload, verify=False)
    result = response.json()
    return result
get_token()