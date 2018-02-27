import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "5rlMttD4zmG6NF8MH59PmtxVD",
    "consumer_secret"     : "bSgVTIYPBZzdGffvGNg9DBxgnLd9AjIWD5k2zRUJM067Vpq3Ua",
    "access_token"        : "968401692957073408-0cQQ0oJkpZF2xHlm9pHcOcfYKkQzFFX",
    "access_token_secret" : "8XN6H7h0XyMPyR5o6FursmjukOl2Y0YEvtl70bAhcO7HT" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
