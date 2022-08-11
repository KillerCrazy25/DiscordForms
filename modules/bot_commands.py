import nextcord, asyncio
from nextcord.ext import commands
from bot import FormView

from utils.config import *

from utils.questions_generator import Question

# Confirmation Buttons View
class ConfirmationView(nextcord.ui.View):

	def __init__(self, user : nextcord.Member):
		super().__init__(timeout = confirmation_timeout)
		self.value = None
		self.user = user

	# Timeout Event
	async def on_timeout(self):
		for child in self.children:
			child.disabled = True

		await self.message.edit(content = configuration_timeout_confirmation_message, view = self)

		self.stop()

	# Confirm Button
	@nextcord.ui.button(label = "I'm sure, exit.", style = nextcord.ButtonStyle.red)
	async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		if self.user == interaction.user.id:
			await interaction.response.send_message(configuration_cancel_message, ephemeral = True)
			self.value = True
			for child in self.children:
				child.disabled = True
			await interaction.message.edit(content = configuration_cancel_message, view = self)

			self.stop()
		else:
			return await interaction.response.send_message("This is not for you!", ephemeral = True)

	# Cancel Button
	@nextcord.ui.button(label = "Never mind, let's keep it up.", style = nextcord.ButtonStyle.green)
	async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		if self.user == interaction.user.id:
			await interaction.response.send_message(configuration_not_cancelled_message, ephemeral = True)
			self.value = False
			for child in self.children:
				child.disabled = True
			await interaction.message.edit(content = configuration_not_cancelled_message, view = self)

			self.stop()
		else:
			return await interaction.response.send_message("This is not for you!", ephemeral = True)

# Configuration Cog	
class Configuration(commands.Cog, name = "Bot Configuration Command"):
	"""Bot commands module."""
	
	# Configuration Constructor
	def __init__(self, bot : commands.Bot):
		self.bot = bot
		self.configurator = None

	# Config Command
	@commands.command(name = "config", description = "Configure the bot.")
	@commands.guild_only()
	@commands.has_permissions(administrator = True)
	async def config_bot(self, ctx : commands.Context):
		if self.configurator != None and self.configurator != ctx.author.id:
			return await ctx.send(configuration_error_message)

		self.configurator = ctx.author.id

		question = Question(ctx, self.bot)
		alive = await question.ask_config_question(start_config_message)

		if alive == True:
			alive = await question.ask_config_question(app_title_message)

		if alive == True:
			alive = await question.ask_config_question(app_custom_id_message)

		if alive == True:
			alive = await question.ask_config_question(app_button_name_message)

		if alive == True:
			alive = await question.ask_config_question(app_embed_name_message)

		if alive == True:
			alive = await question.ask_config_question(app_embed_description_message)

		if alive == True:	
			alive = False	

			return await ctx.send(config_end.format(PREFIX, PREFIX))

	# Add Questions Command
	@commands.command(name = "addquestion", description = "Adds questions to the application form.")
	@commands.has_permissions(administrator = True)
	async def add_question(self, ctx : commands.Context):
		if self.configurator != None and self.configurator != ctx.author.id:
			return await ctx.send(configuration_error_message)
		
		self.configurator = ctx.author.id

		question = Question(ctx, self.bot)
		alive = await question.ask_questions(question_message)

		if alive == True:
			alive = await question.ask_questions(placeholder_message)

		if alive == True:
			alive = await question.ask_questions(required_message)

		if alive == True:
			alive = await question.ask_questions(style_message)

		if alive == True:
			alive = await question.ask_questions(input_style_message)

		if alive == True:
			alive = await question.ask_questions(question_custom_id_message)

		if alive == True:	
			alive = False	

			return await ctx.send(questions_end)

	# Send Form Command
	@commands.command(name = "sendform", description = send_button_to_channel_description)
	@commands.has_permissions(administrator = True)
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

	# Force Leave Command
	@commands.command(name = "forceleave", description = "Force Leave Configuration Mode.")
	@commands.has_permissions(administrator = True)
	async def force_leave(self, ctx : commands.Context):
		if self.configurator == ctx.author.id:
			self.configurator = None

			global questions_alive
			questions_alive = False

			await ctx.send("Forcing configuration mode to end...")
		else:
			await ctx.send("Only the person who started the configuration mode can force it to end.")
			return

	# Command To Add Commands
	@commands.command(name = "addcommand", description = "Add a command to the bot.")
	@commands.has_permissions(administrator = True)
	async def add_command(self, ctx : commands.Context, command : str):
		if command in self.bot.commands:
			await ctx.send("That command already exists.")
			return

		self.bot.add_command(command)
		await ctx.send("Command added.")

# Setup Function
def setup(bot : commands.Bot):
	bot.add_cog(Configuration(bot))