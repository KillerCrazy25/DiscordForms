from async_timeout import timeout
import nextcord
from nextcord.ext import commands

from config import *

# Subclassing the Bot class

class FormsBot(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#self.persistent_modals_added = False
		#self.persistent_views_added = False

	async def on_ready(self):
		#if not self.persistent_modals_added:
			#self.add_modal(FormModal())
			#self.persistent_modals_added = True

		#if not self.persistent_views_added:
			#self.add_view(FormView())
			#self.persistent_views_added = True

		print(f"Bot is ready! | Logged in as {self.user} (ID: {self.user.id})")

		submit_channel : nextcord.TextChannel = self.get_channel(submit_channel_id)

# Form Modal Class

class FormModal(nextcord.ui.Modal):

	def __init__(self):
		super().__init__(
			title = title, 
			timeout = None
		)

		# for each question in questions, add a text input field to the modal with his label, placeholder, custom id, required and style

		for i in range(len(questions)):
			self.field = nextcord.ui.TextInput(
				label = questions[i], 
				placeholder = placeholders[i], 
				required = required[i], 
				style = nextcord.TextInputStyle.short
			)
			self.add_item(self.field)

	async def callback(self, interaction: nextcord.Interaction):	
		await interaction.response.send_message(submit_message, ephemeral = True)

# Form View Class

class FormView(nextcord.ui.View):

	def __init__(self):
		super().__init__(timeout = None)

	@nextcord.ui.button(label = button_name, style = nextcord.ButtonStyle.green, emoji = "✅", custom_id = "forms:button")
	async def button_callback(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		await interaction.response.send_modal(FormModal())

# Bot Instance

bot = FormsBot(command_prefix = PREFIX, intents = nextcord.Intents.all())

# Ping Command

@bot.command()
async def ping(ctx : commands.Context):
	await ctx.reply(f"Pong! Latency: {bot.latency * 100:.0f}ms")

# Send Form Command

@bot.command(name = "sendform")
async def send_modal(ctx : commands.Context, channel : nextcord.TextChannel = None):
	if not channel:
		channel = ctx.channel

	embed = nextcord.Embed(
		title = embed_name,
		description = embed_description,
		color = nextcord.Color.green()
	)
	
	await channel.send(embed = embed, view = FormView())
	
bot.run(TOKEN)