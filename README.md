# bizanime
*Business anime GIF tweets*

How to get this working?

1) download/clone repo

2) enter the project directory

` cd bizanime`

3) create a virtual environment 

`python3 -m venv`

4) enter virtual environment

`source venv/bin/activate`

5) install "requests" and "tweepy"

`pip install requests tweepy`

6) get Twitter/GIPHY API keys, create an apikeys.txt file in this format:

```
[apikeys]
giphy_apikey = THE_GIPHY_API_KEY
[twitter]
consumer_key = THE_TWITTER_API_KEY
consumer_secret = THE_TWITTER_API_KEY
access_token = THE_TWITTER_API_KEY
access_token_secret = THE_TWITTER_API_KEY
```

7) run python app:

`python3 app.py`

8) edit code (text files, GIPHY search term and parameters) to taste

At this point, you'll have a fully functional python app that can tweet weird text and GIFs. To continue on and move this code to AWS:

9) Make sure your AWS `configuration` file is in place.

10) install zappa:

`pip install zappa`

11) init zappa:

`zappa init`

12) push to production:

`zappa deploy production`
