# from django.shortcuts import render
import boto3
import os
from rest_framework.response import Response
from f2api.models import Profile
from f2api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from fileuploadapi.settings import MEDIA_ROOT
from django.core.files.storage import default_storage


class profile(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Your file uploaded sucessfully..!'})
        return Response(serializer.errors)

    def get(self, request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        profile_data = Profile.objects.get(pk)
        serializer = ProfileSerializer(profile_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

        # return Response(serializer.errors)

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = 'AKIAUWTSHFLYBQ3HZWQZ'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME= 'eriktest12'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_REGION_NAME = 'ap-south-1'
# AWS_MEDIA_LOCATION = 'album'

# Create your views here.

# class ProfileView(APIView):
#     def post(self, request, format=None):
#         def upload(request):
#             folder = request.path.replace("/", "_")
#             uploaded_filename = request.FILES['file'].name

#             # create the folder if it doesn't exist.
#             try:
#                 os.mkdir(os.path.join(MEDIA_ROOT, folder))
#             except:
#                 pass

#             # save the uploaded file inside that folder.
#             full_filename = os.path.join(MEDIA_ROOT, folder, uploaded_filename)
#             fout = open(full_filename, 'wb+')
#             # Iterate through the chunks.
#             for chunk in fout.chunks():
#                 fout.write(chunk)
#             fout.close()
            
            
#         serializer= ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'File Uploaded Successfully',
#                              'status':'success', 'candidate':serializer.data}, 
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def get(self, request, format=None):
#         data = Profile.objects.all()
#         serializer = ProfileSerializer(data, many=True)
#         return Response({'status':'success', 'data':serializer.data}, 
#                         status=status.HTTP_200_OK)
    
    
    

    

        
    
            