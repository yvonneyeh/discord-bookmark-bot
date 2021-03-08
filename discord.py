import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
# client = discord.Client()

    id = message.channel.client.user.id

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
# if (message.mentions.users.some(user => user.id === id))
    if message.mentions.users.some(user.id == id):
        message.channel.send:a
            "--- global-bookmarks helper ---",
            "Make *#bookmarks* channel first, then you can bookmark and unbookmark any messages with emoji actions.",
            "* React any messages with :bookmark: to create bookmark in the #bookmarks channel!",
            "* React to my messages (include bookmarks) with :x: to delete those bookmarks.",
            .join("\n")

client.run(os.getenv('DISCORD_TOKEN'))