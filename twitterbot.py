import json
from typing import Dict

from requests_oauthlib import OAuth1Session


def read_config() -> Dict:
    with open("env.json") as file:
        config = json.load(file)
    return config


config = read_config()

oauth = OAuth1Session(
    config['api_key'],
    client_secret=config['api_secret'],
    resource_owner_key=config['oauth_token'],
    resource_owner_secret=config['oauth_token_secret'],
)

first_message = """Want to learn how to create a #TwitterBot in 15 minutes?

Follow my guide:

1/7"""

first_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": first_message},
)

second_message = """Sign up for a @TwitterDev account, create a project with an app, and save the API key and secret.

https://developer.twitter.com/en/portal/petition/essential/basic-info

2/7"""

second_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": second_message,
          "reply": {"in_reply_to_tweet_id": first_tweet.json()["data"]["id"]}},
)

third_message = """Clone my @Twitter Bot #Tutorial:

https://github.com/jakubwaller/twitter-bot-tutorial

3/7"""

third_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": third_message,
          "reply": {"in_reply_to_tweet_id": second_tweet.json()["data"]["id"]}},
)

fourth_message = """Plug the API key and secret into the env.json file.

https://github.com/jakubwaller/twitter-bot-tutorial/blob/main/env.json

4/7"""

fourth_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": fourth_message,
          "reply": {"in_reply_to_tweet_id": third_tweet.json()["data"]["id"]}},
)

fifth_message = """Run the authenticate script and follow the instructions to enable your bot to tweet on your behalf.
Save the oauth_token and the oauth_token_secret into the env.json file.

https://github.com/jakubwaller/twitter-bot-tutorial/blob/main/authenticate.py

5/7"""

fifth_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": fifth_message,
          "reply": {"in_reply_to_tweet_id": fourth_tweet.json()["data"]["id"]}},
)

sixth_message = """Your bot is ready to tweet! Initialise a session:

oauth = OAuth1Session(
    config['api_key'],
    client_secret=config['api_secret'],
    resource_owner_key=config['oauth_token'],
    resource_owner_secret=config['oauth_token_secret'],
)

6/7"""

sixth_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": sixth_message,
          "reply": {"in_reply_to_tweet_id": fifth_tweet.json()["data"]["id"]}},
)

seventh_message = """And tweet:

oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": text_of_your_tweet},
)

For more examples see https://github.com/jakubwaller/twitter-bot-tutorial/blob/main/twitterbot.py

7/7"""

seventh_tweet = oauth.post(
    "https://api.twitter.com/2/tweets",
    json={"text": seventh_message,
          "reply": {"in_reply_to_tweet_id": sixth_tweet.json()["data"]["id"]}},
)
