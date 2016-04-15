# Spark4Python_Twitter_API.py
# AN - version 20150426
#
# 1-Access Twitter API with OAuth Credentials
# 2-Search Twitter for query = "ApacheSpark" (JSON - Tweets)
# 3-Parse Tweets (TweetId, CreatedAt, UserId, UserName, TweetText, TweetURL)
#
#
import twitter
import urlparse
from pprint import pprint as pp

class TwitterAPI(object):
    """
    TwitterAPI class allows the Connection to Twitter via OAuth
    once you have registered with Twitter and receive the 
    necessary credentiials 
    """


    def __init__(self):
        consumer_key = '52spraJ39wfXFGmW0OZFAgu2a'
        consumer_secret = 'cGxitcn7POmDOxbDvkGZuo4raRqCbmR8rL4ULEN3QdNdXMw9IM'
        access_token = '2893875282-GXhr9Xrd1fhkztnYitE5keBKWhQh7ti8jewWkz5'
        access_secret = '8BkSzzEMx8sQkPbaphXXl8pJCldNkZbmVphf8vUGH54vy'
     
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)
        self.api = twitter.Twitter(auth=self.auth)

    def searchTwitter(self, q, max_res=10,**kwargs):
        search_results = self.api.search.tweets(q=q, count=10, **kwargs)
        statuses = search_results['statuses']
        max_results = min(1000, max_res)

        for _ in range(10): 
            try:
                next_results = search_results['search_metadata']['next_results']
            except KeyError as e: 
                break

            next_results = urlparse.parse_qsl(next_results[1:])
            kwargs = dict(next_results)
            search_results = self.api.search.tweets(**kwargs)
            statuses += search_results['statuses']

            if len(statuses) > max_results: 
                break
        return statuses

    def parseTweets(self, statuses):
        return [ (status['id'], 
                  status['created_at'], 
                  status['user']['id'],
                  status['user']['name'], 
                  status['text'], 
                  url['expanded_url']) 
                        for status in statuses 
                            for url in status['entities']['urls'] ]