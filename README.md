# PulseBot ⚡
PulseBot is a Slack bot I made using Python and Slack Bolt.
I wanted to make a small bot that could do a few useful things directly in Slack.

## What it does
* `/pulse-help` — shows the commands
* `/pulse-motivate` — sends a random motivational message
* `/pulse-time` — shows the current time

## How I made it
I used Python with Slack Bolt and Slack Socket Mode. The bot listens for the slash commands and sends a response when one is used.

## Run it yourself
Clone the repo:
```bash
git clone https://github.com/namasyuch/pulsebot.git
cd pulsebot
```

Install the packages:
```bash
pip install -r requirements.txt
```

You also need a Slack Bot Token and Slack App Token. Set them as:
```text
SLACK_BOT_TOKEN=your_bot_token
SLACK_APP_TOKEN=your_app_token
```

Keep these tokens private.
Then run:
```bash
python app.py
```

You should see:
```text
⚡ PulseBot is running!
```
After setting up the Slack commands, you can try them in your workspace.

## Deployment
I deployed the bot on Railway so it can keep running even when my laptop is off.

## What I learned
This project helped me learn more about Slack apps, slash commands, Socket Mode, environment variables, GitHub and deploying a Python project.

## GitHub
https://github.com/namasyuch/pulsebot
