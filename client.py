import discord
import asyncio

TOKEN = 'Add-Your-Token-Here'  # Your bot's token
CHANNEL_ID = 1234567890123456789  # Your target channel ID

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True  # Enable access to message content

client = discord.Client(intents=intents)

async def count_clicks():
    channel = client.get_channel(CHANNEL_ID)
    total_clicks = 0
    async for message in channel.history(limit=None):
        try:
            total_clicks += int(message.content)
        except ValueError:
            continue
    return total_clicks

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    asyncio.create_task(terminal_input())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        int(message.content)  # Check if the message content is an integer
        total_clicks = asyncio.run(count_clicks())
        asyncio.create_task(message.channel.send(f'Total clicks: {total_clicks}'))
    except ValueError:
        pass

async def send_clicks(clicks):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(str(clicks))
    total_clicks = await count_clicks()
    print(f'Total clicks: {total_clicks}')

async def terminal_input():
    while True:
        input("Press Enter to simulate a button click...")
        await send_clicks(1)

client.run(TOKEN)
cls()