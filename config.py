import json, os

from dotenv import load_dotenv

load_dotenv()

with open("./config.json", "r") as f:
	config = json.load(f)
	print("Config loaded.")

with open("./application_config.json") as f:
	app_config = json.load(f)
	print("Application config loaded.")

# Bot Config

PREFIX = config["prefix"]
TOKEN = os.getenv("TOKEN")

# Application Config

title = app_config["app_title"]
button_name = app_config["button_name"]

questions = app_config["questions"]
styles = app_config["styles"]
required = app_config["required"]
placeholders = app_config["placeholders"]
custom_ids = app_config["custom_ids"]

embed_name = app_config["embed_name"]
embed_description = app_config["embed_description"]

submit_message = app_config["submit_message"]
submit_channel_id = app_config["submit_channel_id"]