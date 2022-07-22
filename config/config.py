import json, os

from dotenv import load_dotenv

load_dotenv()

with open("./config/config.json", "r") as f:
	config = json.load(f)
	print("Config loaded.")

with open("./config/application_config.json") as f:
	app_config = json.load(f)
	print("Application config loaded.")

with open("./config/messages.json") as f:
	messages = json.load(f)
	print("Messages config loaded.")

# Bot Config

PREFIX = config["prefix"]
TOKEN = os.getenv("TOKEN")

admin_role_id = config["admin_role_id"]

GUILD_IDS = config["guild_ids"]

questions_timeout = config["questions_timeout"]
confirmation_timeout = config["confirmation_timeout"]

# Application Config

title = app_config["app_title"]
app_custom_id = app_config["app_custom_id"]
button_name = app_config["button_name"]

questions = app_config["questions"]

embed_name = app_config["embed_name"]
embed_description = app_config["embed_description"]

submit_channel_id = app_config["submit_channel_id"]

# Messages Config

question_not_answered_message = messages["question_not_answered_message"]


configuration_started_message = messages["configuration_started_message"]
configuration_timed_out_message = messages["configuration_timed_out_message"]

submit_message = messages["submit_message"]

sent_button_to_channel_message = messages["sent_button_to_channel_message"]
send_button_to_channel_description = messages["send_button_to_channel_description"]

configuration_cancel_message = messages["configuration_cancel_message"]
configuration_not_cancelled_message = messages["configuration_not_cancelled_message"]
configuration_cancel_confirmation_message = messages["configuration_cancel_confirmation_message"]
configuration_timeout_confirmation_message = messages["configuration_timeout_confirmation_message"]

error_message = messages["error_message"]

start_config_message = messages["start_config_message"]
configuration_channel_message = messages["configuration_channel_message"]

app_title_message = messages["app_title_message"]
configuration_title_message = messages["configuration_title_message"]

app_custom_id_message = messages["app_custom_id_message"]
configuration_custom_id_message = messages["configuration_custom_id_message"]

app_button_name_message = messages["app_button_name_message"]
configuration_button_name_message = messages["configuration_button_name_message"]

app_embed_name_message = messages["app_embed_name_message"]
configuration_embed_name_message = messages["configuration_embed_name_message"]

app_embed_description_message = messages["app_embed_description_message"]
configuration_embed_description_message = messages["configuration_embed_description_message"]

question_message = messages["question_message"]
configuration_question_message = messages["configuration_question_message"]