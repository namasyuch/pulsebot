import os
import random
from datetime import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.installation_store import FileInstallationStore


installation_store = FileInstallationStore(
    base_dir="./data/installations"
)

app = App(
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
    installation_store=installation_store,
    oauth_settings=OAuthSettings(
        client_id=os.environ["SLACK_CLIENT_ID"],
        client_secret=os.environ["SLACK_CLIENT_SECRET"],
        scopes=["commands"],
        user_scopes=[],
        installation_store=installation_store,
        redirect_uri=os.environ["SLACK_REDIRECT_URI"],
    )
)


@app.command("/pulse-help")
def help_command(ack, respond):
    ack()

    respond(
        "⚡ *PulseBot Commands*\n"
        "• `/pulse-help` — Show all commands\n"
        "• `/pulse-motivate` — Get a motivational message\n"
        "• `/pulse-time` — Show the current time"
    )


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


@app.command("/pulse-time")
def time_command(ack, respond):
    ack()

    current_time = datetime.now().strftime("%I:%M:%S %p")

    respond(f"🕐 Current time: `{current_time}`")


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]

    handler = SocketModeHandler(app, app_token)

    print("⚡ PulseBot is running!")
    handler.start()