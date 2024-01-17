import os
import tweepy
from getTextBeta import *

from google.cloud import secretmanager

project_id = os.environ["GCP_PROJECT"] 
client = secretmanager.SecretManagerServiceClient() 
Z
def get_secrets(secret_request): 
    name = f"projects/{project_id}/secrets/{secret_request}/versions/latest"
    response = client.access_secret_version(name=name) 
    return response.payload.data.decode("UTF-8")

def twetarCardapio(event, context):
    api_key = get_secrets("twitter_consumer_key")
    api_secret = get_secrets("twitter_consumer_secret")
    bearer_token = get_secrets("btoken")
    acess_token =  get_secrets("twitter_acess_token")
    acess_token_secret = get_secrets("twitter_acess_secret")

    clientt = tweepy.Client(bearer_token, api_key, api_secret, acess_token, acess_token_secret)

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, acess_token, acess_token_secret)
    api = tweepy.API(auth)

    testt = imprimir_cardapio_bandejao()
    clientt.create_tweet(text=testt)
    return 'OK'
