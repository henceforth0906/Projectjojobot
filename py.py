import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("눼눼")

client.run("NzIwMTcxODY0NDU4MjY0NjY2.XuCfXQ.MF7srlgbTlmGzBwEiyP4EkUa2pk")
