import tweepy
from getTextBeta import *



api_key = " "
api_secret = " "
bearer_token = " "
acess_token =  " "
acess_token_secret = " "

client = tweepy.Client(bearer_token, api_key, api_secret, acess_token, acess_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, acess_token, acess_token_secret)
api = tweepy.API(auth)

testt = imprimir_cardapio_bandejao()
client.create_tweet(text=testt)


  