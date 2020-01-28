from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_module as s

#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.


#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""

class Listener(StreamListener):
    def on_data(self , data):
        all_data = json.loads(data)
        tweet = all_data["text"]#text only
        sentiment_value , confidence = s.sentiment(tweet)
        print(tweet , sentiment_value , confidence)

        if confidence * 100 >= 80:
            output = open("output_from_twitter" , "a")# a
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True
    def on_error(self , status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["awesome"])
