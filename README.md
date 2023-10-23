Overview

This script provides a Discord bot that monitors messages in a server for toxic content. It uses the BERT model from the transformers library to detect and classify potentially harmful messages. If a message is deemed toxic, the bot will automatically delete it and notify the channel about the removal.

Dependencies

discord.py
transformers
torch

Features

BERT Model for Toxicity Detection: The bot uses a pre-trained BERT model (unitary/toxic-bert) to identify toxic messages.
React to Specific Words: The bot will react with a "🚫" emoji if the word "Ugly" is present in a message.
Automatic Message Deletion: If a message is classified as toxic, the bot will delete it and send a notification to the channel.


Setup & Usage
1. Install Dependencies
Before running the bot, ensure you have the required libraries installed:

bash
Copy code
pip install discord.py transformers torch


2. Adjust the Toxicity Threshold
The function is_toxic determines whether a message is toxic based on a threshold. You can adjust this threshold as needed:

return toxic_prob > 0.5  # Adjust this threshold as needed


3. Set Up Intents
The bot uses Discord's Intents feature to specify which events it wants to receive. In this script, the bot is set up to receive message events:


intents = Intents.default()
intents.messages = True


4. Replace the Bot Token
Replace the placeholder bot token in the client.run() function with your actual bot token:


client.run('YOUR_BOT_TOKEN_HERE')



This code is a work in progress and changes a lot due to discord updates, it make it hard to maintain the fuctionality of the bot
