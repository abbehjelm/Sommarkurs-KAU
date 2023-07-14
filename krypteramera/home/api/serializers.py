from rest_framework import serializers


class EncryptionSerializerAccept(serializers.Serializer):
    key = serializers.CharField(max_length=32,min_length=3)
    plainText = serializers.CharField(max_length=1000, min_length=1)
    
    
class DecryptionSerializerAccept(serializers.Serializer):    
    cipher = serializers.CharField(max_length=1000)
    key = serializers.CharField(max_length=32)
    iv = serializers.CharField(max_length=32)

class EncryptionSerializerReturn(serializers.Serializer):
    iv = serializers.CharField(max_length=32)
    cipher = serializers.CharField(max_length=1000)
    
    
class DecryptionSerializerReturn(serializers.Serializer):    
    plainText = serializers.CharField(max_length=1000)
   