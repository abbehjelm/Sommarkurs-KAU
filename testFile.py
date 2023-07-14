import json
import os
import requests
import base64

encryption_url = "http://localhost:8000/api/encrypt/"
decryption_url = "http://localhost:8000/api/decrypt/"


def encrypt(key, iv, plain_text):

    post_data = {
        'key': key,
        'iv': iv,
        'plainText': plain_text,
    }        

    headers = {
        "Content-Type": "application/json",
    }
    
    response = requests.post(encryption_url, json=post_data, headers=headers )

    response_json = json.loads(response.text)    

    return response_json


def decrypt(key, iv, cipher):
    post_data = {
        'key': key,
        'iv': iv,
        'cipher': cipher,
    }        

    headers = {
        "Content-Type": "application/json",
    }
    
    response = requests.post(decryption_url, json=post_data, headers=headers)

    response_json = json.loads(response.text)    

    return response_json


# Defining main function
def main():
    iv = os.urandom(16)
    iv = base64.b64encode(iv).decode()

    return_dict = encrypt("albin", iv, "Hejsan svejsan på  dejsan sa hejsanä")
    print(return_dict)
    return_dict_2 = decrypt("albin",return_dict['iv'],return_dict['cipher'])
    print(return_dict_2) 

# __name__
if __name__ == "__main__":
    main()
