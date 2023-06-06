import requests

def get_token(token_url,client_id,client_secret):
    payload='client_id=' + str(client_id) + \
            '&client_secret=' + str(client_secret) + '&grant_type=client_credentials'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", token_url, headers=headers, data=payload, verify=False)
    result = response.json()
    access_token = result['token_type'] + ' ' + result['access_token']
    return access_token

def easy_vcode_detect(token_url,imgpath,request_url,client_id,client_secret):
    token = get_token(token_url,client_id,client_secret)
    print(token)
    request_files = {
        'image_file': open(imgpath, 'rb')
    }
    headers = {
        'Authorization': str(token)
    }
    r = requests.post(url=request_url,files=request_files,headers=headers, verify=False)
    result = r.json()
    return result

if __name__ == "__main__":
    token_url = "https://ai.kingsware.cn:8443/api/ai/vcode/v1/general_basic/oauth2/token"
    request_url = 'https://ai.kingsware.cn:8443/api/ai/vcode/v1/general_basic'
    imgpath = "0.jpg"
    api_key = '5F56P57854885535'
    secret_key = 'CFR656P411562147U8I511BE7P03007F'
    result = easy_vcode_detect(token_url,imgpath,request_url,api_key,secret_key)
    print(result)