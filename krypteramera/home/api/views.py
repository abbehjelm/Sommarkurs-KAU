from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import authentication, permissions
import hashlib
import sys
import os 
from .serializers import *
from home.aes_methods import *
from home.forms import *

class Encrypt(APIView):    
    def get(self, request, format=None):        
        return Response("This endpoint only accepts post requests")
    
    parser_classes = [JSONParser]

    def post(self, request, format=None):        
        serializer = EncryptionSerializerAccept(data = request.data)
        if serializer.is_valid():
            key = serializer.validated_data['key']
            plainText = serializer.validated_data['plainText']
            
            iv = os.urandom(16)
       
        
            hash = hashlib.sha3_256()
            hash.update(str.encode(key))     
                    
            
            cipher = encrypt(hash.hexdigest(),plainText, iv)
            iv = base64.b64encode(iv).decode()
            
            jsonData = {
                'iv': iv,
                'cipher' : cipher,
            }
            
            return Response(jsonData)     
        
        return Response({'error': "The data submitted was not in the correct format. Format should be { 'key' : 'Your chosen key', 'plainText' : 'The text you want to encrypt' } "})        
    
    
class Decrypt(APIView):    
    def get(self, request, format=None):        
        return Response("This endpoint only accepts post requests")
    
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        postData = request.data
        serializer = DecryptionSerializerAccept(data=request.data)
        
        if serializer.is_valid():
            key = serializer.validated_data['key']
            iv = serializer.validated_data['iv']
            cipher = serializer.validated_data['cipher']
        
            hash = hashlib.sha3_256()
            hash.update(str.encode(key))                    
            
            try:
                plainText = decrypt(hash.hexdigest(),cipher,iv)
            except:
                plainText = cipher
                
                
            jsonData = {
                'plainText' : plainText
            }
            
            
            return Response(jsonData)
        else :
            return Response({'error': "The data submitted was not in the correct format. Format should be  { 'key' : 'Your key',  'cipher' : 'The cipher you want to decrypt', 'iv' : 'The initialization vector generated upon encryption' }"})        
