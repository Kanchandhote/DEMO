import os 
import boto3
import requests
from botocore.exceptions import ClientError

access_key = 'AKIAUWTSHFLYBQ3HZWQZ'
access_secret = '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'
bucket_name = 'eriktest12'
# my_session = boto3.session.Session()

client_s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = access_secret,
    region_name= 'ap-south-1',
    object_name='album'  
)
# client_s3.put_object(
#     file,
#     bucket_name,
#     'album/test.jpg'
# );


    # # If S3 object_name was not specified, use file_name
    # if object_name is None:
    #     object_name = file_name

   

import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name='album'):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print('folder is')
        return False
    return True

# """
#  Uploading Files to S3 Bucket
# """
# data_file_folder = os.path.join(os.getcwd(), 'Data Files')
# for file in os.listdir(data_file_folder):
#     if not file.startswith('.'):
#         try:
#             print('Uploading file {0}...'.format(file))
#             client_s3.upload_file(
#                 os.path.join(data_file_folder, file),
#                 bucket_name,
#                 file    
#             )  
#         except ClientError as e:
#             print('Credential is Incorrect')
#             print(e)
#         except Exception as e:
#             print(e)
            
#  client_s3.download_file(bucket_name, '152526748.jpg', os.path.join('./Files Download/', 'test1.jpg'))

# URL = "https://eriktest12.s3.ap-south-1.amazonaws.com/test1.jpg"
# r = requests.get(URL)
# print(r.content)
            
            

# """
# Downloading  Files from S3 Bucket
# """
#     <h2>Download File</h2>
#     <button class="btn"><i class="fa fa-download"></i> Download</button> 
#     client_s3.download_file(bucket_name, '152526748.jpg', os.path.join('./Files Download/', 'test.jpg'))


            

            
            

            