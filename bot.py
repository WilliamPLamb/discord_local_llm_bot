import discord
from discord.ext import commands
from dotenv import load_dotenv
import psycopg2

import os

load_dotenv()
DISCORD_BOT_SECRET = os.getenv('DISCORD_BOT_SECRET')


# Connect to your PostgreSQL database
# conn = psycopg2.connect(
#     dbname='your_dbname',
#     user='your_username',
#     password='your_password',
#     host='your_host'
# )
# cur = conn.cursor()

# Define the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Avoid bot replying to itself
    if message.author == bot.user:
        return
    
    print(f'Message from {message.author}: {message.content}')

    if str.lower(message.content) == "hello":
        await message.reply("world!")

    # Insert message into the PostgreSQL database
    # cur.execute('INSERT INTO messages (discord_message_id, content, author_id, channel_id) VALUES (%s, %s, %s, %s)',
                # (message.id, message.content, message.author.id, message.channel.id))
    # conn.commit()

    # Process commands
    # await bot.process_commands(message)

bot.run(DISCORD_BOT_SECRET)