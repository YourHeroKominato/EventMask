"""
@bot.command(name='geteventinfo',description="geteventinfoを実行させる")
async def getEventInfo(ctx:discord.Interaction):
    Guild = ctx.guild

    eventList = await DiscordEvents(token).list_guild_events(Guild.id)
    print(eventList)

    eventIDList = [event['id'] for event in eventList]
    print(eventIDList)

    eventNameList = [event['name'] for event in eventList]
    print(eventNameList)
    await ctx.response.send_message(eventNameList)


    # need to show more event info, such as description
# 参考：https://gist.github.com/adamsbytes/8445e2f9a97ae98052297a4415b5356f


# @bot.command(name='listmylobby')
# async def listmylobby(ctx):

#     Guild = ctx.guild
#     Mylobby = await Guild.fetch_channels()
#     Mylobbylist = 
#     # Mylobbyname = [lobby.name for lobby in Mylobby]
#     print (Mylobby)
#     await ctx.send(
#         "Here is your lobby list {}".format(Mylobbyname)
#     )

@bot.command(name='geteventinfo2',description="geteventinfoを実行させる")
async def getEventInfo(ctx:discord.Interaction):
    Guild = ctx.guild

    eventList = await DiscordEvents(token).list_guild_events(Guild.id)
    print(eventList)

    eventIDList = [event['id'] for event in eventList]
    print(eventIDList)

    eventNameList = [event['name'] for event in eventList]
    print(eventNameList)
    await ctx.response.send_message(eventNameList)
    # need to show more event info, such as description

@bot.command(name='search_event2' ,description="searchEventを実行させる")
async def searchEvent(ctx:discord.Interaction):
    Guild = ctx.guild

    eventList = await DiscordEvents(token).list_guild_events(Guild.id)
    print(eventList)

    eventIDList = [event['id'] for event in eventList]
    print(eventIDList)
    await ctx.response.send_message(eventIDList)
    
    eventNameList = [event['name'] for event in eventList]
    print(eventNameList)
    await ctx.response.send_message(eventNameList)

    eventUserList = await DiscordEvents(token).get_guild_event_user(Guild.id, "1035455752388751370")
    print(eventUserList)
    eventUserList

    await ctx.response.send_message(f"{ctx.user.name}さんがsearchEventを実行させました。")

@bot.command(name='createlobby',description="ロビーの名前を入力してテキストチャンネルとヴォイスチャンネルを作る")
async def createlobby(ctx:discord.Interaction, ロビーの名前:str):
    LobbyName = ロビーの名前
    Guild = ctx.guild

    Category = await Guild.create_category(LobbyName)
    await Category.create_text_channel("text channel")
    await Category.create_voice_channel("voice channel")

    await ctx.response.send_message(f"{ctx.user.name}さんが{LobbyName}ロビーをつくりました。",ephemeral=True)


@bot.command(name="ねこ" ,description="猫のイメージを出す（テスト）")
async def imageload(ctx:discord.Interaction):
    file = discord.File(r"./image/cat.jpg", filename="NFT.png")

    embed = discord.Embed(title="NFT")
    embed.set_image(url="attachment://NFT.png")
    await ctx.response.send_message("Clink on link to approve NFT desingn", file=file, embed=embed,ephemeral=True)


@bot.command(name='showticket2' ,description="input your wallet address here to get evnet TOKEN!")
async def showticket2(ctx:discord.Interaction, walletaddress:str):
    Guild = ctx.guild
    walletAddress = walletaddress
    if re.search(r"^0x[a-zA-Z0-9]{40}$",walletAddress) == None:
        await ctx.response.send_message(f"Sorry, It's not walletAddress! \nPlease check it again\n{walletAddress}")
        return
    await ctx.response.send_message(f"This is right!! your wallet address is {walletAddress}")
    # makeQRCode(walletAddress)
    # make QR code with the walletAddress
    # walletAddress is String and use it in function here
    return

################test#################
@bot.command(name="testcommand1", description="Testing ephemeral")
async def testcommand1(ctx: discord.Interaction):
    print("confirmyournft")
    await ctx.response.send_message("Hello World!", ephemeral=True)


#####################################



class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SetButton())

class SetButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Click!",
            style=discord.ButtonStyle.green,
            url="https://www.google.com/"
        )

    async def callback(self, interaction:discord.Interaction):
        # Guild = interaction.guild
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

        
        # Send(account_name, eventName, eventStartDate)

        # await interaction.response.send_message(f'{interaction.user.display_name}は{self.label}を押しました')

"""