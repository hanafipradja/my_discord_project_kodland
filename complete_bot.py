import discord
from bot_logic import gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$pasw'):
        await message.channel.send("Password kamu " + gen_pass(10))
    elif message.content.startswith('$deleteme'):
        await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0) #ini untuk menghapus pesan
    else:
        await message.channel.send(message.content)

@client.event
async def on_message_delete(message):
    msg = f'{message.author} has deleted the message: {message.content}'
    await message.channel.send(msg)

client.run("MTExMDU1Nzk1OTYwMTI3MDg4NQ.GlBRe0.167rhAcm4VhT7gRBjpE1uDM7zu1AVPB8ZMOf0A")
