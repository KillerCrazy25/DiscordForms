import nextcord, asyncio
from nextcord.ext import commands
from bot import FormView

from config.config import *

class ConfirmationView(nextcord.ui.View):

	def __init__(self):
		super().__init__(timeout = confirmation_timeout)
		self.value = None

	async def on_timeout(self):
		for child in self.children:
			child.disabled = True

		await self.message.edit(content = configuration_timeout_confirmation_message, view = self)

	@nextcord.ui.button(label = "I'm sure, exit.", style = nextcord.ButtonStyle.red)
	async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		await interaction.response.send_message(configuration_cancel_message, ephemeral = True)
		self.value = True
		for child in self.children:
			child.disabled = True
		await interaction.message.edit(content = configuration_cancel_message, view = self)

	# This one is similar to the confirmation button except sets the inner value to `False`
	@nextcord.ui.button(label = "Never mind, let's keep it up.", style = nextcord.ButtonStyle.green)
	async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		await interaction.response.send_message(configuration_not_cancelled_message, ephemeral = True)
		self.value = False
		for child in self.children:
			child.disabled = True
		await interaction.message.edit(content = configuration_not_cancelled_message, view = self)

# Configuration Cog
	
class Configuration(commands.Cog, name = "Bot Configuration Command"):
	"""Bot commands module."""
	
	# Configuration Constructor

	def __init__(self, bot : commands.Bot):
		self.bot = bot

	# Config Command

	@commands.command(name = "config", description = "Configure the bot.")
	@commands.guild_only()
	async def config_bot(self, ctx : commands.Context):
		config_alive = True
		await ctx.reply(configuration_started_message)

		# Form Channel Configuration

		await ctx.author.send(start_config_message)

		msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

		try:
			if msg.content.lower() != "default" and msg.content.lower() != "cancel":
				app_config["submit_channel_id"] = int(msg.content)

				with open("./config/application_config.json", "w") as f:
					json.dump(app_config, f, indent = 4)			

				await ctx.author.send(configuration_channel_message.format(app_config["submit_channel_id"]))
			elif msg.content.lower() == "default":
				app_config["submit_channel_id"] = self.bot.get_guild(ctx.guild.id).system_channel.id

				with open("./config/application_config.json", "w") as f:
					json.dump(app_config, f, indent = 4)	

				await ctx.author.send(configuration_channel_message.format(app_config["submit_channel_id"]) + f"({ctx.guild.name}'s System Channel)")

			elif msg.content.lower() == "cancel":
				view = ConfirmationView()

				view.message = await ctx.author.send(configuration_cancel_confirmation_message, view = view)

				await view.wait()

				if view.value == None:
					config_alive = True
					return

				elif view.value == True:
					config_alive = False
					return

				else:
					config_alive = True
					return

		except asyncio.TimeoutError:
			await ctx.author.send(configuration_timed_out_message)
			return

		# Application Title Configuration

		if config_alive == True:
			await ctx.author.send(app_title_message)

			msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

			try:
				if msg.content.lower() != "default" and msg.content.lower() != "cancel":
					app_config["app_title"] = msg.content

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["app_title"]))

				elif msg.content.lower() == "default":
					app_config["app_title"] = "Dummy Server Application"

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["app_title"]))

				elif msg.content.lower() == "cancel":
					view = ConfirmationView()

					view.message = await ctx.author.send(configuration_cancel_confirmation_message, view = view)

					await view.wait()

					if view.value == None:
						config_alive = True
						return

					elif view.value == True:
						config_alive = False
						return

					else:
						config_alive = True
						return

			except asyncio.TimeoutError:
				await ctx.author.send(configuration_timed_out_message)
				return

		# Custom ID Configuration

		if config_alive == True:
			await ctx.author.send(app_custom_id_message)

			msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

			try:
				if msg.content.lower() != "default" and msg.content.lower() != "cancel":
					app_config["app_custom_id"] = msg.content

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["app_custom_id"]))

				elif msg.content.lower() == "default":
					app_config["app_custom_id"] = "dummy_server:app"

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["app_custom_id"]))

				elif msg.content.lower() == "cancel":
					view = ConfirmationView()

					view.message = await ctx.author.send(configuration_cancel_confirmation_message, view = view)

					await view.wait()

					if view.value == None:
						config_alive = True
						return

					elif view.value == True:
						config_alive = False
						return

					else:
						config_alive = True
						return

			except asyncio.TimeoutError:
				await ctx.author.send(configuration_timed_out_message)
				return

		# Button Name Configuration
		if config_alive == True:
			await ctx.author.send(app_button_name_message)

			msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

			try:
				if msg.content.lower() != "default" and msg.content.lower() != "cancel":
					app_config["button_name"] = msg.content

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["button_name"]))

				elif msg.content.lower() == "default":
					app_config["button_name"] = "Apply to Dummy Server"

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["button_name"]))

				elif msg.content.lower() == "cancel":
					view = ConfirmationView()

					view.message = await ctx.author.send(configuration_cancel_confirmation_message, view = view)

					await view.wait()

					if view.value == None:
						config_alive = True
						return

					elif view.value == True:
						config_alive = False
						return

					else:
						config_alive = True
						return

			except asyncio.TimeoutError:
				await ctx.author.send(configuration_timed_out_message)
				return

		# Embed Name Configuration
		if config_alive == True:
			await ctx.author.send(app_embed_name_message)

			msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

			try:
				if msg.content.lower() != "default" and msg.content.lower() != "cancel":
					app_config["embed_name"] = msg.content

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["embed_name"]))

				elif msg.content.lower() == "default":
					app_config["embed_name"] = "Apply to Dummy Server"

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["embed_name"]))

				elif msg.content.lower() == "cancel":
					view = ConfirmationView()

					view.message = await ctx.author.send(configuration_cancel_confirmation_message, view = view)

					await view.wait()

					if view.value == None:
						config_alive = True
						return

					elif view.value == True:
						config_alive = False
						return

					else:
						config_alive = True
						return

			except asyncio.TimeoutError:
				await ctx.author.send(configuration_timed_out_message)
				return

		# Embed Description Configuration
		if config_alive == True:
			await ctx.author.send(app_embed_description_message)

			msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

			try:
				if msg.content.lower() != "default" and msg.content.lower() != "cancel":
					app_config["embed_description"] = msg.content

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["embed_description"]))

				elif msg.content.lower() == "default":
					app_config["embed_description"] = "To apply to Dummy Server, click the button below and fill out the form."

					with open("./config/application_config.json", "w") as f:
						json.dump(app_config, f, indent = 4)	

					await ctx.author.send(configuration_title_message.format(app_config["embed_description"]))

				elif msg.content.lower() == "cancel":
					view = ConfirmationView()

					view.message = await ctx.author.send(configuration_cancel_confirmation_message, view = view)

					await view.wait()

					if view.value == None:
						config_alive = True
						return

					elif view.value == True:
						config_alive = False
						return

					else:
						config_alive = True
						return

			except asyncio.TimeoutError:
				await ctx.author.send(configuration_timed_out_message)
				return

		# Questions Configuration

		"""
		{
			"question": "Where do you live?",
			"placeholder": "Example: Bogota, Colombia. (Don't specify anymore)",
			"required": false,
			"style": "input",
			"input_style": "short",
			"custom_id": "location"
		}
		"""
		if config_alive == True:
			await ctx.author.send(question_message)

			msg = await self.bot.wait_for("message", check = lambda m: m.author == ctx.author, timeout = questions_timeout)

			try:
				...

			except asyncio.TimeoutError:
				await ctx.author.send(configuration_timed_out_message)
				return

	# Send Form Command

	@commands.command(name = "sendform", description = send_button_to_channel_description)
	async def send_modal(self, ctx : commands.Context, channel : nextcord.TextChannel = None):
		if not channel:
			channel = ctx.channel

		embed = nextcord.Embed(
			title = embed_name,
			description = embed_description,
			color = nextcord.Color.green()
		)

		await ctx.reply(sent_button_to_channel_message)
		await channel.send(embed = embed, view = FormView())

# Setup Function

def setup(bot : commands.Bot):
	bot.add_cog(Configuration(bot))