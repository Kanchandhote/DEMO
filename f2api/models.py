from django.db import models
import boto3
import os

access_key = 'AKIAUWTSHFLYBQ3HZWQZ'
access_secret = '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'
bucket_name = 'eriktest12'
# my_session = boto3.session.Session()

client_s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = access_secret,
    region_name= 'ap-south-1'    
)

class Profile(models.Model):
    def fileName(instance, filename):
        s3 = boto3.client('s3')
        return '/'.join([str(instance.folder_name), filename])
    folder_name= models.CharField(max_length=300)
    file=models.FileField(upload_to=fileName, blank=True)