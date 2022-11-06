import json
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get

import aiohttp


class DiscordEvents:
    """Class to create and list Discord events utilizing their API"""

    def __init__(self, discord_token: str) -> None:
        self.base_api_url = "https://discord.com/api/v8"
        self.auth_headers = {
            "Authorization": f"Bot {discord_token}",
            "User-Agent": "DiscordBot (https://your.bot/url) Python/3.9 aiohttp/3.8.1",
            "Content-Type": "application/json",
        }

    async def list_guild_events(self, guild_id: str) -> list:
        """Returns a list of upcoming events for the supplied guild ID
        Format of return is a list of one dictionary per event containing information."""
        event_retrieve_url = f"{self.base_api_url}/guilds/{guild_id}/scheduled-events"
        async with aiohttp.ClientSession(headers=self.auth_headers) as session:
            try:
                async with session.get(event_retrieve_url) as response:
                    response.raise_for_status()
                    assert response.status == 200
                    response_list = json.loads(await response.read())
            except Exception as e:
                print(f"EXCEPTION: {e}")
            finally:
                await session.close()
        return response_list

    async def get_guild_event_user(self, guild_id: str, guild_event_id: str):
        """Returns a list of upcoming events for the supplied guild ID
        Format of return is a list of one dictionary per event containing information."""
        event_retrieve_url = f"{self.base_api_url}/guilds/{guild_id}/scheduled-events/{guild_event_id}/users?with_member=true"
        async with aiohttp.ClientSession(headers=self.auth_headers) as session:
            try:
                async with session.get(event_retrieve_url) as response:
                    response.raise_for_status()
                    assert response.status == 200
                    response_list = json.loads(await response.read())
            except Exception as e:
                print(f"EXCEPTION: {e}")
            finally:
                await session.close()
        return response_list

    ######here#######
    async def get_guild_event_start_time(self, guild_id: str, guild_event_id: str):
        """Returns a list of upcoming events time for the supplied guild ID
        Format of return is a list of one dictionary per event containing information."""
        event_retrieve_url = f"{self.base_api_url}/guilds/{guild_id}/scheduled-events/{guild_event_id}/users?with_member=true"
        async with aiohttp.ClientSession(headers=self.auth_headers) as session:
            try:
                async with session.get(event_retrieve_url) as response:
                    response.raise_for_status()
                    assert response.status == 200
                    response_list = json.loads(await response.read())
            except Exception as e:
                print(f"EXCEPTION: {e}")
            finally:
                await session.close()
        return response_list

    #################

    async def create_guild_event(
        self,
        guild_id: str,
        event_name: str,
        event_description: str,
        event_start_time: str,
        event_end_time: str,
        event_metadata: dict,
        event_privacy_level=2,
        channel_id=None,
    ) -> None:
        """Creates a guild event using the supplied arguments
        The expected event_metadata format is event_metadata={'location': 'YOUR_LOCATION_NAME'}
        The required time format is %Y-%m-%dT%H:%M:%S"""
        event_create_url = f"{self.base_api_url}/guilds/{guild_id}/scheduled-events"
        event_data = json.dumps(
            {
                "name": event_name,
                "privacy_level": event_privacy_level,
                "scheduled_start_time": event_start_time,
                "scheduled_end_time": event_end_time,
                "description": event_description,
                "channel_id": channel_id,
                "entity_metadata": event_metadata,
                "entity_type": 3,
            }
        )

        async with aiohttp.ClientSession(headers=self.auth_headers) as session:
            try:
                async with session.post(event_create_url, data=event_data) as response:
                    response.raise_for_status()
                    assert response.status == 200
            except Exception as e:
                print(f"EXCEPTION: {e}")
            finally:
                await session.close()

    async def createrole(ctx, arg):
        Guild = ctx.guild
        NewRole = await Guild.create_role(reason = 'for_event', name = arg)
        print(NewRole)
        return NewRole

    async def createprivatelobby(ctx, eventname ,eventrole):
        Guild = ctx.guild
        LobbyName = eventname
        Role = get(Guild.roles, name=str(eventrole))
        overwrites = {
            Guild.default_role: discord.PermissionOverwrite(read_messages=False),
            Role: discord.PermissionOverwrite(read_messages=True)
        }
        Category = await Guild.create_category(LobbyName)
        if Category != None:
            await Category.create_text_channel("text channel", overwrites=overwrites)
            await Category.create_voice_channel("voice channel", overwrites=overwrites)

        return "success"

    async def updateMemberRole(guild, userID, eventID, flag):
        Guild = guild
        userID = int(userID)
        eventID = str(eventID)
        print('updateMemberRole'+eventID)
        # roles = discord.utils.get(Guild.roles)
        # print(roles)
        roleID = None
        for role in Guild.roles:
            print(role.name)
            print(type(role.name))
            print(eventID)
            print(type(eventID))
            print('--------')
            if role.name == eventID:
                roleID = role.id
                break
        if roleID == None:
            return
        role = Guild.get_role(roleID)
        print(role)

        for member in Guild.members:
            print(member.id)
            print(type(member.id))
            print(userID)
            print(type(userID))
            print('=======')
            if member.id == userID:
                if flag == True:
                    await member.add_roles(role)
                if flag == False:
                    await member.remove_roles(role)


