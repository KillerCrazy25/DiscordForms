import nextcord, asyncio
from nextcord.ext import commands

from config.config import *

from datetime import datetime, timedelta
from pytz import timezone

# Form Modal Class

class FormModal(nextcord.ui.Modal):

	# Form Modal Constructor

	def __init__(self):
		super().__init__(
			title = title,
			custom_id = app_custom_id,
			timeout = None
		)

		# Form Modal Fields

		for i in range(0, len(questions)):
			if questions[i]["style"] == "input":
				self.field = nextcord.ui.TextInput(
					label = questions[i]["question"], 
					placeholder = questions[i]["placeholder"], 
					required = questions[i]["required"],
					style = nextcord.TextInputStyle.short if questions[i]["style"] == "short" else nextcord.TextInputStyle.paragraph,
					custom_id = questions[i]["custom_id"],			
				)

			self.add_item(self.field)

	# Modal Callback

	async def callback(self, interaction: nextcord.Interaction) -> None:
		embed = nextcord.Embed(
			color = nextcord.Color.blurple(),
			timestamp = datetime.now(timezone("US/Eastern"))
		).set_author(
			name = f"{interaction.user}'s Application",
			icon_url = interaction.user.avatar.url
		)

		# Form Embed Fields

		for question, answer in zip(questions, self.children):
			embed.add_field(
				name = question["question"],
				value = answer.value if answer.value else question_not_answered_message,
				inline = False
			)

		# Sending Form Embed

		await interaction.response.send_message(submit_message, ephemeral = True)
		submit_channel = await bot.fetch_channel(submit_channel_id)
		await submit_channel.send(embed = embed)

# Form View Class

class FormView(nextcord.ui.View):

	# Form View Constructor

	def __init__(self):
		super().__init__(timeout = None)

	# Form View Button Callback

	@nextcord.ui.button(label = button_name, style = nextcord.ButtonStyle.green, emoji = "✅", custom_id = "forms:button")
	async def button_callback(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		await interaction.response.send_modal(FormModal())

# Bot Instance

bot = commands.Bot(command_prefix = PREFIX, intents = nextcord.Intents.all())

# Ready Event

@bot.event
async def on_ready():
	persistant_modals_added = False
	persistant_views_added = False

	if persistant_modals_added == False:
		persistant_modals_added = True
		bot.add_modal(FormModal())
	
	if persistant_views_added == False:
		persistant_views_added = True
		bot.add_view(FormView())

	print("Persistant views added.")
	print("Persistant modals added.")
	
	print(f"Bot is ready! | Logged in as {bot.user} (ID: {bot.user.id})")

# Load Modules

for file in os.listdir("./modules"):
	if file.endswith(".py"):
		bot.load_extension(f"modules.{file[:-3]}")
		print("Loaded module: " + file)



# Run Bot
if __name__ == "__main__":	
	bot.run(TOKEN)