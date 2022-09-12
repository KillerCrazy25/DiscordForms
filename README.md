# Introduction

Simple Discord Bot that uses discord modals to create applications like Google Forms.

# Creating Application On Discord Developers

1) Go to [Discord Developers](https://discord.com/developers/applications) website, login into your account and create a **New Application**.
2) Select the name that you want for your application (not discord bot).
3) Then, go to **Bot** section and click **Add Bot** -> **Yes, do it!** button.
4) Once created your bot, go to **OAuth2** -> **URL Generator** section.
5) For the application scopes, select **bot** and **application.commands**.
6) Then, select the permissions that the bot needs.
7) Once selected your bot permissions, just click on **Copy** button.
8) Open a new tab on your web browser and paste the link.
9) Select the server that you want to invite the bot.
10) Go again to **Bot** section and click **Reset Token** -> **Yes, do it!**. 
11) Then click **Copy** and that's your bot's token ***DO NOT SHARE***.

If you did that steps correctly, the bot should have joined the server that you selected and should appear offline.

# Installation

1) Ensure that you have [Python 3.10](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed in the machine that the bot is gonna run.
2) Clone the repository using `git clone https://github.com/KillerCrazy25/DiscordForms` or just download it.
3) Then install all the requirements with the command below:
    ```py
    Linux / Mac OS
    python3 -m pip install -r requirements.txt

    Windows
    python -m pip install -r requirements.txt
    ```

**Ensure that you have developer mode enabled on discord. (That's gonna be useful because you will be able to copy guild ids, channel ids, etc.)**

# Configuration

**RENAME ALL `.example.json` TO `.json`.**

## Creating environment file with bot's token

1) Rename **.example.env** to **.env**.
2) Open that file with any text editor and write the next text: `TOKEN=PASTE_HERE_YOUR_BOT_TOKEN_THAT_YOU_GOT_FROM_DISCORD_DEVELOPERS_WITHOUT_QUOTES`.

## `config.json` Configuration

  * `prefix` -> The prefix you would like to use when running commands.
  * `guild_ids` -> Paste there your server id. That's for slash commands faster loading.
  * `questions_timeout` -> The time that the user needs to answer `$config` questions.
  * `confirmation_timeout` -> The time that the user needs to click the `$config` confirmation buttons.
  * `admin_role_id` -> The role that is needed to execute bot's admin commands. Paste there the ID of the role.
  
## `application_config.json` Configuration

  #### If you don't know [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp), it's better to configure the bot using the `$config` command.**

  * `app_title` -> The title of discord modal (form).
  * `app_custom_id` -> The custom of discord modal (form).
  * `button_name` -> The name of the button that's gonna open the form to the user that clicked it.
  * `embed_name` -> The name of the embed that contains the button explained before.
  * `embed_description` -> The description of the embed that contains the button explained before.
  * `submit_channel_id` -> The channel that the bot is gonna send the application answers. Paste there the ID of the channel.
  
  #### Questions config field is a List, so if you want to change the questions via JSON File, **PLEASE FOLLOW THE CORRECT [SYNTAX](https://www.w3schools.com/js/js_json_syntax.asp)**
  
  * `questions` -> For every question, add the rows below:
  
      * `question` -> The question that you want to ask in your application.
      * `placeholder` -> The placeholder that your answer field is gonna have.
      * `required` -> The answer is necessary to submit the application?
      * `style` -> The style of the answer field.
      * `input_style` -> If the row above is `input`, select the type of input of your answer field.
      * `custom_id` -> The custom id of your question.  
      
# Running Bot

To run the bot you need to run the following command:
    ```py
    Linux / Mac OS
    python3 bot.py

    Windows
    python bot.py
    ```
      
## Contributing

For contributing, please read [this article](https://github.com/KillerCrazy25/DiscordForms/wiki/contributing/)
