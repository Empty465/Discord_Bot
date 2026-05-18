import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(massage):
    if massage.content == "엄":
        await massage.channel.send("준식")

client.run("봇 토큰 입력 필요")