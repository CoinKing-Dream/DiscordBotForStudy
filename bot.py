
import discord
from discord.ext import commands
from discord.ext.commands import Context
from urllib.request import urlopen
import json
import datetime
import config
from dotenv import load_dotenv()

load_dotenv()

token = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

#--- Bot Start
@bot.event
async def on_ready():
    print(f'Logged in As {bot.user}')

@bot.event
async def on_message(message):
    if message.content.lower().startswith("hello"):
        await message.reply("How are you?")
    else:
        await bot.process_commands(message)

@bot.command(name='onboard')
async def onboard(ctx):
    await ctx.send('Welcome! Let\'s get started with the onboarding process.')

    # Step 1: Verify email address
    await ctx.send('Please enter your email address:')
    email_response = await bot.wait_for('message', timeout=30)

    await ctx.send(email_response)
    
    # email = email_response.content.strip()

    # # Step 2: Perform 2FA verification
    # await ctx.send('Please enter the verification code sent to your email.')
    # verification_code_response = await bot.wait_for('message', timeout=30.0)
    
    # verification_code = verification_code_response.content.strip()

    # # Step 3: Update nickname
    # await ctx.send('Please enter your full name:')
    # name_response = await bot.wait_for('message', timeout=30.0)
    
    # name = name_response.content.strip()
    # await ctx.author.edit(nick=name)

    # # Step 4: Assign roles based on user type
    # await ctx.send('Which best describes you? (Parent or Coder)')
    # user_type_response = await bot.wait_for('message', timeout=30.0)
    
    # user_type = user_type_response.content.strip().lower()

    # if user_type == 'parent':
    #     await ctx.author.add_roles(discord.Object(id='ROLE_ID_PARENT'))
    #     await ctx.send(f'Welcome, Parent! You have been added to #general-parents.')
    # elif user_type == 'coder':
    #     await ctx.author.add_roles(discord.Object(id='ROLE_ID_CODER'))
    #     await ctx.send(f'Welcome, Coder! You have been added to #general-coders.\n\nPlease introduce yourself in #introduce-yourself.')
    # else:
    #     await ctx.send('Invalid option. Please try again.')


@bot.command()
async def Help(ctx):
# #Help CMD
    """Help - Bot Commands"""
    #Webhook
    data = {
        "title": "Bot Commands",
        "description": "Use **/Help** to bring up this menu anytime.",
        "color": 15856113,
            "fields": [{
                    "name": "/track_product",
                    "value": "Track a product(s) sales.\nRequires: `Product Link`"
                },{
                    "name": "/check_product_data",
                    "value": "Check total sales & data for product.\nRequires: `Product Link`"
                },{
                    "name": "Product Link",
                    "value": "EX: `https://lavester.in/products/nezuko-regular-t-shirt`"
                },{
                    "name": "/check_store_data (Unavailable version)",
                    "value": "Check total sales & data for store\nRequires: `Website Link`"
                },
            ],
        "footer": {
            "text": "If you're tracking a new store, you must first use /track_product."
        },
    }

    embed = discord.Embed.from_dict(data)
    await ctx.send(embed = embed)
    
bot.run(token) 

