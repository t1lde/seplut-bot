# Seplut Bot

An old practice project of mine, I don't run the bot anymore since twitter changed their rules on bot accounts (and the in-joke is stale)...

I appreciate how cute and simple the python code is, the separation of multiple python scripts is neat and unix-ey.

Seplut Bot is a Markov Chain Twitter Bot which generates tweets based on titles of Robin Seplut's videos (https://www.youtube.com/channel/UCTZUTvv_1Onm-f-533Hyurw for reference).
If you change the url in scrape_titles.py this can be used for an arbitrary channel.

## Setup

### Pip

To set up:

Install python prerequisites, see requirements.txt 

    pip install -r requirements.txt

### Selenium

Install the Firefox Selenium Webdriver:
see: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver#Setting_up_the_geckodriver_executable

### Training

In order to train the bot on a youtube user's video titles, run scrape_titles.py, this will open an automated instance of firefox. This step may take a while. 
The script may exit early if your connection is slow, if so increase the amount of time it waits for.

Once the titles have been scraped, run train_bot.py to generate the probabilities for the markov chain.

### Send Tweet

send_tweet.py can be run to send a tweet using your credentials, which it looks for as variables in keys.py. Use cron to run regularly.




