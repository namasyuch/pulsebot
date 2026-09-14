# PulseBot
PulseBot is a Slack bot I made for StarDance using Python and Slack Bolt.

## Commands
* `/pulse-help` — shows the commands
* `/pulse-motivate` — sends a random motivational message
* `/pulse-time` — shows the current time

## Running it

Clone the repo and install the requirements.


git clone https://github.com/namasyuch/pulsebot.git
cd pulsebot
pip install -r requirements.txt


You need a Slack Bot Token and Slack App Token as environment variables:

```
SLACK_BOT_TOKEN=your_bot_token
SLACK_APP_TOKEN=your_app_token
```

Keep the real tokens private.

Run the bot with:
```
python app.py
```

## Deployment
I tested the bot on my laptop first and then deployed it to Railway so it could keep running when my laptop is off.

## What I learned
I learned how Slack slash commands work, how to use Socket Mode, how to use environment variables, and how to deploy a Python bot.

## GitHub
https://github.com/namasyuch/pulsebot
