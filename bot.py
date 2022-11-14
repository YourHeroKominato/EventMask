import discord
from discord import app_commands
import requests
import os
from dotenv import load_dotenv
import nftDemoImageGenerator
import os
from discord.utils import get
from discord_buttons_plugin import *
import asyncpg
from discordEvent import DiscordEvents
from calendar import c
from operator import imod, truediv
import json
from json.decoder import JSONDecoder
from os import error
import requests
import time
import qr_generator
import re
from discord.ext import tasks, commands

load_dotenv()
token = os.getenv("TOKEN")


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print({self.user})
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("----------------------------------------")
        # while not self.is_closed():
        #     auto_invite_batch(self.guilds)
        # auto_invite(interaction=discord.Interaction).start()
        # cog = MyCog(self)
        # cog.batch_update()


client = aclient()
client2 = discord.Client(intents=discord.Intents.all())

tree = app_commands.CommandTree(client=client)


@tree.command(name="help")
async def helpcommand(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"This is ..."
        f"\n/confirmnft : " + f"\n/createeventlobby  : " + f"\n/showticket : "
    )


@tree.command(
    name="confirmnft",
    description="For Organizer: Confirm NFT design and sign with your wallet",
)
async def confirmnft(interaction: discord.Interaction):

    eventattendee = interaction.user.name
    Channel = interaction.channel
    Guild = interaction.guild
    daoName = interaction.guild
    channelName = interaction.channel.name

    eventName = ""
    eventStartDate = ""
    organaizer_name = ""

    try:
        print(1)
        eventList = await DiscordEvents(token).list_guild_events(Guild.id)
        print(2)
    except UnboundLocalError:
        await interaction.response.send_message(
            f"Too many requests! please wait a minute....", ephemeral=True
        )
        return
    isPrivateEventChannel = False

    def geteventidfromlobby(interaction):
        Channel = interaction.channel
        print("func return2 :{}".format(Channel.overwrites.keys()))
        for n in Channel.overwrites.keys():
            if str(n) != "@everyone":
                eventID = n
                return eventID

    for event in eventList:
        if str(event["id"]) == str(geteventidfromlobby(interaction)):
            eventName = event["name"]
            eventStartDate = event["scheduled_start_time"]
            isPrivateEventChannel = True
            organaizerName = event["creator"]

    eventdate = eventStartDate[:9]

    ev = (
        "?organaizerName="
        + str(organaizerName)
        + "&eventName="
        + str(eventName)
        + "&eventStartDate="
        + str(eventStartDate)
    )

    if isPrivateEventChannel == False:
        await interaction.response.send_message(
            f"Sorry, you cannot use this command at this channel. you can use event private channel",
            ephemeral=True,
        )
        return
    print(eventName)

    ### main function
    nftDemoImageGenerator.nftDemoImageGenerator(
        eventattendee,
        eventName,
        daoName,
        eventStartDate[:9],
        #####future######
        base_img_path=r"image/base/certificate01.png",
        medium_font_path=r"font/Open_Sans/static/OpenSans/OpenSans-Medium.ttf",
        creepster_font_path=r"font/Creepster/Creepster-Regular.ttf",
        #################
    )

    file = discord.File("image/output/{}/cop.png".format(eventName))
    embed = discord.Embed(title="{}_NFT".format(eventName), color=discord.Colour.red())
    embed.set_image(url="attachment://{}_NFT.png".format(eventName))

    await interaction.response.send_message(
        "Clink on link to approve NFT desingn",
        file=file,
        embed=embed,
        ephemeral=True,
        view=HogeButton(),
    )
    return


@tree.command(
    name="showticket",
    description="For Attendee: input your wallet address here to get event nft by showing QR code to organaizer!",
)
async def showticket(interaction: discord.Interaction, walletaddress: str):

    try:
        walletAddress = walletaddress

        # temporary variable

        if re.search(r"^0x[a-zA-Z0-9]{40}$", walletAddress) == None:
            await interaction.response.send_message(
                f"Sorry, It's not walletAddress! \nPlease check it again\n{walletAddress}"
            )
            return

        user_display_name = "TestAccount"
        sent_from_channel_name = "TestChannel"
        qr_generator.Qr_generator(
            user_display_name, sent_from_channel_name, walletAddress
        )

        # upload QR to discord
        file = discord.File(
            "./image/output/some_file.jpg",
            filename="some_file.jpg",
        )
        embed = discord.Embed(title="Here is a title")
        embed.set_image(url="attachment://some_file.jpg")

        await interaction.response.send_message(
            f"Your wallet address is {walletAddress}. Show QR to a host to apply for mint",
            file=file,
            embed=embed,
            ephemeral=True,
        )
    except UnboundLocalError:
        await interaction.response.send_message(
            f"Too many requests! please wait a minute....", ephemeral=True
        )


class HogeButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HugaButton())


class HugaButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="txt",
            style=discord.ButtonStyle.red,
            url="https://globalhouseteam-web3.bubbleapps.io/",
        )

    async def callback(self, interaction: discord.Interaction):
        Guild = interaction.guild

        # eventList = await DiscordEvents(token).list_guild_events(Guild.id)

        # def geteventidfromlobby(interaction):
        #     Channel = interaction.channel
        #     print("func return2 :{}".format(Channel.overwrites.keys()))
        #     for n in Channel.overwrites.keys():
        #         if str(n) != "@everyone":
        #             eventID = n
        #             return eventID

        # for event in eventList:
        #     if str(event["id"]) == str(geteventidfromlobby(interaction)):
        #         eventName = event["name"]
        #         eventStartDate = event["scheduled_start_time"]
        #         isPrivateEventChannel = True
        #         eventName = event.eventName
        #         eventStartDate = event.eventStartdate
        #         account_name = event.creator

        # event = self.custom_id.split("|")

        # account_name = event[0]
        # eventName= event[1]
        # eventStartDate = event[2]

        # Send(account_name, eventName, eventStartDate)

        await interaction.response.send_message(
            f"{interaction.user.display_name}は{self.label}を押しました"
        )


def Send(account_name, event_name, event_date):
    url = "https://globalhouseteam-web3.bubbleapps.io/"
    response = requests.post(
        url,
        json={
            "discord_account_name": account_name,
            "discord_event_name": event_name,
            "discord_event_date": event_date,
        },
    )
    print(response.text)
    return response.text


@tree.command(
    name="createeventlobby",
    description="For Organizer: Find eventname and create private event lobby",
)
async def createEventLobby(interaction: discord.Interaction, eventname: str):
    Guild = interaction.guild
    eventName = eventname
    eventID = None
    eventList = await DiscordEvents(token).list_guild_events(Guild.id)
    for event in eventList:
        if event["name"] == eventName:
            eventID = event["id"]
    if eventID == None:
        interaction.response.defer()
        await interaction.response.send_message(
            f"{eventname} event is not exist. cannot create private channel."
        )
        return

    eventRole = await DiscordEvents.createrole(interaction, eventID)
    await DiscordEvents.createprivatelobby(interaction, eventName, eventRole)

    await interaction.response.send_message(f"{eventName} private lobby created.")


@client.event
async def on_scheduled_event_create(event):
    print("created!")


@client.event
async def on_scheduled_event_delete(event):
    print("deleted!")


@client.event
async def on_scheduled_event_user_add(event, user):
    print("added!")
    await DiscordEvents.updateMemberRole(event.guild, user.id, event.id, True)


@client.event
async def on_scheduled_event_user_remove(event, user):
    print("removed!")
    await DiscordEvents.updateMemberRole(event.guild, user.id, event.id, False)


@tree.command(name="createevent", description="createevent12345")
async def createevent(interaction: discord.Interaction):
    await DiscordEvents.create_guild_event(
        guild_id=interaction.guild_id,
        event_name="test20221105",
        event_description="testDesc",
        event_start_time="2022-11-11T00:00:00",
        event_end_time="2022-11-12T00:00:00",
        event_metadata={"location": "YOUR_LOCATION_NAME"},
    )


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = []
        self.batch_update.add_exception_type(asyncpg.PostgresConnectionError)
        self.batch_update.start()

    def cog_unload(self):
        self.batch_update.cancel()

    @tasks.loop(minutes=1)
    async def batch_update(self):
        print("hello!")
        await update_user_role(discord.Interaction)


# @tree.command(name="forceupdateprivatechannelmember", description="'force update private channel memmber'")
async def update_user_role(interaction):
    Guild = interaction.guild
    eventList = await DiscordEvents(token).list_guild_events(Guild.id)
    if eventList == None:
        return
    eventIDList = [event["id"] for event in eventList]
    for eventID in eventIDList:
        eventUserList = await DiscordEvents(token).get_guild_event_user(
            Guild.id, eventID
        )
        for eventUser in eventUserList:
            eventUser = eventUser["user"]
            eventUserID = eventUser["id"]
            # update members' role with eventUserID
            await DiscordEvents.updateMemberRole(interaction, eventUserID, eventID)
    return


# @tree.command(name="forcestartautoinvitebatch", description="force start auto invite batch")
# async def auto_invite_batch(interaction: discord.Interaction):
#     while 1:
#         update_user_role(interaction)
#         time.sleep(300)


# async def update_user_role(interaction):
#     Guild = interaction.guild
#     eventList = await DiscordEvents(token).list_guild_events(Guild.id)
#     if eventList == None:
#         return
#     eventIDList = [event['id'] for event in eventList]
#     for eventID in eventIDList:
#         eventUserList = await DiscordEvents(token).get_guild_event_user(Guild.id, eventID)
#         for eventUser in eventUserList:
#             eventUser = eventUser['user']
#             eventUserID = eventUser['id']
#             # update members' role with eventUserID
#             await DiscordEvents.updateMemberRole(interaction, eventUserID, eventID)
#             return

client.run(token)
