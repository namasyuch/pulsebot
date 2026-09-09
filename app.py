import os
import random
from datetime import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# Create the Slack app using the Bot User OAuth Token
app = App(
    token=os.environ["SLACK_BOT_TOKEN"]
)


# /pulse-help
@app.command("/pulse-help")
def help_command(ack, respond):
    ack()

    respond(
        "⚡ *PulseBot Commands*\n"
        "• `/pulse-help` — Show all commands\n"
        "• `/pulse-motivate` — Get a motivational message\n"
        "• `/pulse-time` — Show the current time"
    )


# /pulse-motivate
@app.command("/pulse-motivate")
def motivate_command(ack, respond):
    ack()

    messages = [
        "🚀 Keep building. Small progress adds up!",
        "🔥 You've got this. Keep shipping!",
        "💡 Every project starts with one line of code.",
        "⚡ Stay curious. Keep creating!"
    ]

    respond(random.choice(messages))


# /pulse-time
@app.command("/pulse-time")
def time_command(ack, respond):
    ack()

    current_time = datetime.now().strftime("%I:%M:%S %p")

    respond(f"🕐 Current time: `{current_time}`")


# Start the bot using Slack Socket Mode
if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]

    handler = SocketModeHandler(app, app_token)

    print("⚡ PulseBot is running!")
    handler.start()