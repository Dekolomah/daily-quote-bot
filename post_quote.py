import tweepy
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API credentials from .env (with strip to avoid whitespace issues)
bearer_token = os.getenv("TWITTER_BEARER_TOKEN").strip()
api_key = os.getenv("TWITTER_API_KEY").strip()
api_secret_key = os.getenv("TWITTER_API_SECRET").strip()
access_token = os.getenv("TWITTER_ACCESS_TOKEN").strip()
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET").strip()

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret_key,
    access_token=access_token,
    access_token_secret=access_token_secret
)

quotes = [
    "If your dreams don't scare you, they're not big enough.",
    "Love yourself first, because you'll be with you forever.",
    "In a world where you can be anything, be kind.",
    "Every day may not be good, but there's good in every day.",
    "In silence, we hear our loudest thoughts.",
    "We're all stardust, so aim for the stars.",
    "Are you brave enough to see beauty in chaos, divinity in the abyss?",
    "Words have power. Use them wisely or they'll control you.",
    "The opposite of love is not hate, it's indifference.",
    "If you could time travel, which moment would you revisit?",
    "The best camera is your memory.",
    "Everything is connected.",
    "Only for today, I will smile...",
    "Who am I? A question I often ask myself.",
    "The most beautiful things are felt, not seen or touched.",
    "True friends are those who find common ground.",
    "All you need sometimes is tea and a good book.",
    "To get the universe, think vibes, not just facts.",
    "Strengths and weaknesses, two sides of the same coin.",
    "Nothing beats seeing your ideas become reality.",
    "Your character speaks louder than your wealth or status.",
    "True faith is wishing others well as you do yourself.",
    "Speak positivity or silence is golden.",
    "Patience is key in pain and desire alike.",
    "Real wealth is being content with what you have.",
    "Treat others how you want to be treated.",
    "Who/What you imagine also imagines you.",
    "3 Questions to ask myself every morning: 1. Am I breathing?  2. Am I smiling?  3. Who Am I? ",
    "Breath is not just air",
]

# Remove any leading or trailing whitespace and quotes from each quote
quotes = [quote.strip('"\n ') for quote in quotes]

index = 0  # Start from the first quote

while True:
    if index >= len(quotes):
        index = 0  # Reset index to start over
    try:
        tweet = client.create_tweet(text=quotes[index])
        print(f"Tweet '{quotes[index]}' posted successfully. ID: {tweet.data['id']}")

        # Countdown timer for the next post (6 hours = 21600 seconds)
        for remaining_time in range(21600, 0, -60):
            if remaining_time % 3600 == 0:  # Fixed: % 3600 for hourly prints (was % 360)
                hours, remainder = divmod(remaining_time, 3600)
                minutes, _ = divmod(remainder, 60)
                print(f"Time until next post: {hours} hours, {minutes} minutes.")
            time.sleep(60)

        index += 1  # Move to the next quote
    except Exception as e:
        print(f"Error posting tweet: {e}")