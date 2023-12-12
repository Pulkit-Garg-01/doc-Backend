from django.shortcuts import render

from .. import models
from django.shortcuts import redirect
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from DOCS import settings
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.conf import settings
from rest_framework import status
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your views here.
class OAuthAuthorizeView(APIView):
    def get(self, request):
       
        state = 'success'
        print(settings.OAUTH2_CLIENT_ID)


        # Build the authorization URL
        authorization_url = f'https://channeli.in/oauth/authorise/?client_id={settings.OAUTH2_CLIENT_ID}&redirect_uri={settings.OAUTH2_REDIRECT_URI}&state={state}'
        
        print(authorization_url)
       
       
        return redirect(authorization_url)
    
    
class oauth2_callback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        token_url = 'https://channeli.in/open_auth/token/'
        payload = {
            'code': code,
            'client_id': settings.OAUTH2_CLIENT_ID,
            'client_secret': settings.OAUTH2_CLIENT_SECRET,
            'redirect_uri': settings.OAUTH2_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }
        response = requests.post(token_url, data=payload)
        token_data = response.json()
        print(token_data)
        access_token = token_data.get('access_token')
        refresh_token = token_data.get('refresh_token')
        # print(access_token)
        if(access_token):
           new_url = f'http://127.0.0.1:8000/get_user_data/?access_token={access_token}'
        #    print("hhhhhhhhhiiiiiiiiiiiiiiiiiiii")
           return redirect(new_url)
        else:
             return Response({'error': 'Access token not found'})


        
        


class GetUserDataView(APIView):
    def get(self, request):
        access_token = request.GET.get('access_token')  
        # print(access_token)
        if not access_token:
            return Response({'error': 'Access token is missing'}, status=400)

       
        user_data_url = 'https://channeli.in/open_auth/get_user_data/'
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get(user_data_url, headers=headers)

        if response.status_code == 200:

            user_data = response.json()
            # return HttpResponse(response)
            print(user_data)
            role=user_data['person']['roles'][1]['role']
            username=user_data['username']
                                
            name=user_data['person']['fullName']
            words = name.split()
            email=user_data['contactInformation']['emailAddress']
            year=user_data['student']['currentYear']
            profile_pic=user_data['person']['displayPicture']
            # auth_token=user_data
            if(role=='Maintainer'):
           
                
                existing_users = models.User.objects.filter(username=username)
                
                # if(not existing_users):
                #     new_user=models.User.objects.create(
                #         name=words
                #     )
                
                if(not existing_users):
                    new_user=models.User.objects.create(
                        
                        name=words,
                        username=username,
                        email=email,
                        year=year,
                        profile_pic=profile_pic,
                        enrollmentNo=username,
                        access_token=access_token,
                        image='https://channeli.in' +
                    user_data['person']['displayPicture'],
                        # refresh_token=refresh_token,
                        



                    )
                    new_user.save()
                    
                else: 
                    print('user already exist')
                    
                existing_users1 = models.User.objects.get(username=username)
                token,created=Token.objects.get_or_create(user=existing_users1)
                print(token.key)
                authToken=token.key
                userId=existing_users1.id
                userName=existing_users1.username
                
                response = HttpResponseRedirect('http://localhost:5173/test/?auth_token=' + authToken + '&userid=' + str(userId) + '&username=' + userName)

                # response = HttpResponseRedirect('http://localhost:5173/?auth_token=' + authToken + '&username=' + userName)

               
                return response
               
                
            else:
                return HttpResponseRedirect('http://localhost:5173/')
        else:
            
            return HttpResponseRedirect('http://localhost:5173',status==451)
            
            