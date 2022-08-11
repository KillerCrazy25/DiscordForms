import nextcord
from nextcord.ext import commands

from datetime import datetime
from pytz import timezone

from utils.config import *

from traceback import print_exception

class ErrorHandler(commands.Cog, name = "Error Handler"):
	"""Basic error handler, can be improved a lot."""

	# ErrorHandler Constructor

	def __init__(self, bot : commands.Bot):
		self.bot = bot

	# Embed Builder

	async def error_embed_builder(self, ctx : commands.Context) -> nextcord.Embed:
		embed = nextcord.Embed(
			title = error_message,
			color = nextcord.Color.dark_red(),
			timestamp = datetime.now(tz = timezone("US/Eastern"))
		)

		embed.set_footer(text = f"Command executed by: {ctx.author}", icon_url = ctx.author.avatar.url)

		return embed

	# Error Handler

	@commands.Cog.listener()
	async def on_command_error(self, ctx : commands.Context, error):
		if isinstance(error, commands.CommandNotFound):
			return print(f"Ignoring exception in command {ctx.command}")

		if isinstance(error, commands.BadArgument):
			embed = await self.error_embed_builder(ctx)
			
			args = ", ".upper().join(error.args)
		
			embed.add_field(name = "Bad Argument", value = f"**Error description:** Argument(s) `{args}` is not valid.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.ChannelNotFound):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Channel Not Found", value = f"**Error description:** Channel `{error.argument}` was not found in `{ctx.guild.name}`.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.ChannelNotReadable):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Channel Not Readable", value = f"**Error description:** Channel `{error.argument}` is not readable as channel.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.GuildNotFound):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Guild Not Found", value = f"**Error description:** Guild `{error.argument}` was not found.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.MissingPermissions):
			embed = await self.error_embed_builder(ctx)

			perms = ", ".upper().join(error.missing_permissions)

			embed.add_field(name = "Missing Permissions", value = f"**Error description:** You are missing `{perms}` permission(s).")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.BotMissingPermissions):
			embed = await self.error_embed_builder(ctx)

			perms = ", ".upper().join(error.missing_permissions)

			embed.add_field(name = "Bot Missing Permissions", value = f"**Error description:** I'm missing `{perms}` permission(s).")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.NoPrivateMessage):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Guild Only", value = f"**Error description:** This command only works inside a guild.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.PrivateMessageOnly):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Private Message Only", value = f"**Error description:** This command doesn't works outside a guild.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.MissingRequiredArgument):
			embed = await self.error_embed_builder(ctx)

			args = ", ".upper().join(error.args)

			embed.add_field(name = "Missing Required Argument", value = f"**Error description:** You are missing `{args}` arguments that are needed to execute this command.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.TooManyArguments):
			embed = await self.error_embed_builder(ctx)

			args = ", ".upper().join(error.args)

			embed.add_field(name = "Too Many Arguments", value = f"**Error description:** You specified too many arguments. Arguments: `{args}`")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.MissingAnyRole):
			embed = await self.error_embed_builder(ctx)

			roles = ", ".upper().join(error.missing_roles)

			embed.add_field(name = "Missing Any Role", value = f"**Error description:** You are missing `{roles}` role(s).")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.BotMissingAnyRole):
			embed = await self.error_embed_builder(ctx)

			roles = ", ".upper().join(error.missing_roles)

			embed.add_field(name = "Bot Missing Any Role", value = f"**Error description:** I'm missing `{roles}` role(s).")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.MissingRole):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Missing Role", value = f"**Error description:** You are missing `{error.missing_role.upper()}` role.")

			await ctx.send(embed = embed)

		elif isinstance(error, commands.BotMissingRole):
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Bot Missing Role", value = f"**Error description:** I'm missing `{error.missing_role}` role.")

			await ctx.send(embed = embed)

		else:
			embed = await self.error_embed_builder(ctx)

			embed.add_field(name = "Error Not Handled | Unknown Error", value = "**Error description:** Error is not handled by the bot. I can't provide more information about your error :(.")

			await ctx.send(embed = embed)
			print_exception(error)

def setup(bot : commands.Bot):
	bot.add_cog(ErrorHandler(bot))