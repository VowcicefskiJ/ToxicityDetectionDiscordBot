import discord
from discord import Intents  # Importing the Intents class
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import torch

# Load pre-trained model and tokenizer
model_name = "unitary/toxic-bert"
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

def is_toxic(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = softmax(logits, dim=1)
    toxic_prob = probs[0][1].item()
    return toxic_prob > 0.5  # Adjust this threshold as needed

# Create an instance of the Intents class and set the required intents
intents = Intents.default()
intents.messages = True

# Pass the intents instance to the Client constructor
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check for the word "Ugly" and react
    if "Ugly" in message.content.lower():
        await message.add_reaction("🚫")

    # Check for toxicity using the model
    elif is_toxic(message.content):
        await message.delete()  # Delete the toxic message
        await message.channel.send(f"Message from {message.author.mention} was removed due to inappropriate content.")

client.run('MTE2NDIzNTk2OTY2MzM1NzA0MA.Ge_9qp.q4OLtwtCy_w_MthoQd7V9A9Fb33G6561X2VYBk')  # Replace with your actual bot token
