import nextcord, asyncio, json
from nextcord.ext import commands

from utils.config import *

class Question:

	# Question(configurator : int, alive : bool, ctx : commands.Context, bot : commands.Bot)
	def __init__(self, ctx : commands.Context, bot : commands.Bot):
		# Parameters
		self.ctx = ctx
		self.bot = bot

	# Parse Question Function (question : str)
	async def return_question_answer(self, question : str):
		answers = {
			start_config_message : "submit_channel_id",
			app_title_message : "app_title",
			app_custom_id_message : "app_custom_id",
			app_button_name_message : "button_name",
			app_embed_name_message : "embed_name",
			app_embed_description_message : "embed_description"
		}
		return answers[question]

	async def return_question_answer_(self, question : str):
		answers = {
			question_message : "question",
			placeholder_message : "placeholder",
			required_message : "required",
			style_message : "style",
			input_style_message : "input_style",
			question_custom_id_message : "custom_id"
		}
		return answers[question]

	# Parse Question Response (question : str)
	async def return_question_response(self, question : str):
		responses = {
			start_config_message : configuration_channel_message,
			app_title_message : configuration_title_message,
			app_custom_id_message : configuration_custom_id_message,
			app_button_name_message : configuration_button_name_message,
			app_embed_name_message : configuration_embed_name_message,
			app_embed_description_message : configuration_embed_description_message
		}
		return responses[question]

	async def return_question_response_(self, question : str):
		responses = {
			question_message : configuration_question_message,
			placeholder_message : configuration_placeholder_message,
			required_message : configuration_required_message,
			style_message : configuration_style_message,
			input_style_message : configuration_input_style_message,
			question_custom_id_message : configuration_custom_id_message
		}
		return responses[question]

	# Parse Answer Type (question : str)
	async def return_answer_type(self, type_ : str):
		types = {
			start_config_message : int,
			app_title_message : str,
			app_custom_id_message : str,
			app_button_name_message : str,
			app_embed_name_message : str,
			app_embed_description_message : str
		}
		return types[type_]

	async def return_answer_type_(self, type_ : str):
		types = {
			question_message : str,
			placeholder_message : str,
			required_message : bool,
			style_message : str,
			input_style_message : str,
			question_custom_id_message : str
		}
		return types[type_]

	# Parse Dict
	async def return_question_dict_key(self, question : str):
		dicts = {
			question_message : "question",
			placeholder_message : "placeholder",
			required_message : "required",
			style_message : "style",
			input_style_message : "input_style",
			question_custom_id_message : "custom_id"
		}
		return dicts[question]

	# Ask Question Function (question : str, type : str = "config" or "question")
	async def ask_config_question(self, question : str):
		await self.ctx.send(question)

		self.alive = True
		self.configurator = self.ctx.author.id

		msg : nextcord.Message = await self.bot.wait_for("message", check = lambda m: m.author == self.ctx.author and m.channel == self.ctx.channel)

		try:
			if msg.content.lower() == "cancel":
				from modules.bot_commands import ConfirmationView
				
				view = ConfirmationView(self.ctx.author.id)

				view.message = await self.ctx.send(configuration_cancel_confirmation_message, view = view)

				await view.wait()

				if view.value == None:
					self.alive = True
					self.configurator = self.ctx.author.id
					return self.alive

				elif view.value == True:
					self.alive = False
					self.configurator = None
					return self.alive

				else:
					self.alive = True
					self.configurator = self.ctx.author.id
					return self.alive
			else:
				answer = await self.return_question_answer(question)
				response = await self.return_question_response(question)
				type_ = await self.return_answer_type(question)

				self.alive = True
				self.configurator = self.ctx.author.id

				app_config[answer] = type_(msg.content)

				with open("./config/application_config.json", "w") as f:
					json.dump(app_config, f, indent = 4)			

				await self.ctx.send(response.format(app_config[answer]))

				return self.alive

		except asyncio.TimeoutError:
			self.alive = False
			self.configurator = None

			await self.ctx.send(questions_timed_out_message.format(questions_timeout))

			return self.alive

	# Ask Question Function (question : str, type : str = "config" or "question")
	async def ask_questions(self, question : str):
		await self.ctx.send(question)

		self.alive = True
		self.configurator = self.ctx.author.id

		msg : nextcord.Message = await self.bot.wait_for("message", check = lambda m: m.author == self.ctx.author and m.channel == self.ctx.channel)

		try:
			if msg.content.lower() == "cancel":
				from modules.bot_commands import ConfirmationView
				
				view = ConfirmationView(self.ctx.author.id)

				view.message = await self.ctx.send(configuration_cancel_confirmation_message, view = view)

				await view.wait()

				if view.value == None:
					self.alive = True
					self.configurator = self.ctx.author.id
					return self.alive

				elif view.value == True:
					self.alive = False
					self.configurator = None
					return self.alive

				else:
					self.alive = True
					self.configurator = self.ctx.author.id
					return self.alive
			else:
				response = await self.return_question_response_(question)
				type_ = await self.return_answer_type_(question)
				key = await self.return_question_dict_key(question)

				if key == "question":
					self.alive = True
					self.configurator = self.ctx.author.id

					question_dict = {
						str(key) : type_(msg.content)
					}

					app_config["questions"].append(question_dict)

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await self.ctx.send(response.format(app_config["questions"][-1]["question"]))

					return self.alive

				else:
					self.alive = True
					self.configurator = self.ctx.author.id

					app_config["questions"][-1][key] = type_(msg.content)

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await self.ctx.send(response.format(app_config["questions"][-1][key]))

					return self.alive

		except asyncio.TimeoutError:
			self.alive = False
			self.configurator = None

			await self.ctx.send(questions_timed_out_message.format(questions_timeout))

			return self.alive