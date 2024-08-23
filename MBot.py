import discord
from discord.ext import commands
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=hfapi,
)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot je prijavljen kao {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('#'):
        user_message = message.content[1:]

        response = client.chat_completion(
            messages=[{"role": "user", "content": user_message}],
            max_tokens=500
        )
        
        if response.choices:
            await message.channel.send(response.choices[0].message['content'])
    
    await bot.process_commands(message)

bot.run(discordapi)
