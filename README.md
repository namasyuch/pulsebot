# PulseBot
PulseBot is a simple Slack bot I built with **Python** and **Slack Bolt**.

It has a few useful slash commands that you can use directly in Slack.

## Features
* `/pulse-help` — Shows all available commands
* `/pulse-motivate` — Sends a random motivational message
* `/pulse-time` — Shows the current time

## Built With
* Python
* Slack Bolt
* Slack Socket Mode
* Railway
* GitHub

## How It Works
PulseBot uses Slack's **Socket Mode** to receive commands from Slack.
When someone uses one of the commands, the bot receives it, runs the matching Python function, and sends a response back to Slack.

## Run It Yourself
### 1. Clone the repository
git clone https://github.com/namasyuch/pulsebot.git
cd pulsebot

### 2. Install the requirements
pip install -r requirements.txt

### 3. Set your Slack tokens
You need a Slack Bot Token and Slack App Token.
Set them as environment variables:
SLACK_BOT_TOKEN=your_bot_token
SLACK_APP_TOKEN=your_app_token
Don't put your real tokens inside the code or upload them to GitHub.

### 4. Run the bot
python app.py

You should see:
PulseBot is running!
Then install the slash commands in your Slack app and try them in Slack.

## Deployment
I deployed PulseBot using **Railway**, so the bot can keep running without my laptop being turned on.

## What I Learned
While making PulseBot, I learned about:
* Creating Slack apps
* Slash commands
* Slack Socket Mode
* Python with Slack Bolt
* Environment variables
* Git and GitHub
* Cloud deployment

## Project
GitHub: https://github.com/namasyuch/pulsebot
PulseBot started as a small project to learn how Slack bots work, and I enjoyed taking it from a local Python program to a working cloud deployment.
