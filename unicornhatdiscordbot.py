#!/usr/bin/env python3
import os
import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",action="store_true" , help="More output")
parser.add_argument("--sort",action="store_true" , help="Sort users by their color")
parser.add_argument("--horizontal",action="store_true" , help="Display in horizontal rows")
parser.add_argument("--includebotmembers",action="store_true" , help="Include bots in user-list")
parser.add_argument("--includesystemmembers",action="store_true" , help="Include system users  (i.e. Discord officially) in user-list")
args = parser.parse_args()

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILDID = int(os.getenv('DISCORD_GUILD_ID'))

import discord

intents = discord.Intents.none()
intents.guilds = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

import unicornhat

unicornhat.set_layout(unicornhat.AUTO)
unicornhat.brightness(0.7)

if args.horizontal:
	unicornhat.rotation(90)
else:
	unicornhat.rotation(0)

unicornhatwidth,unicornhatheight=unicornhat.get_shape()

def redraw_unicornpihat(members):
	i = 0;
	if args.sort:
		members.sort(key=lambda member: member.color.value, reverse=True)
	if args.verbose: print(f'len(members): {len(members)}')
	unicornhat.clear()
	for member in members:
		if (member.bot and not(args.includebotmembers)) or (member.system and not(args.includesystemmembers)) or member.status == discord.Status.offline: continue
		if args.verbose: print(f'Member: {member.name}; RGB: {member.color.r}, {member.color.g}, {member.color.b}; VALUE: {member.color.value}')
		r,g,b=member.color.r,member.color.g,member.color.b
		if member.color.value < 100:
			r,g,b = 150,150,150
		unicornhat.set_pixel(math.floor(i/unicornhatheight),math.floor(i%unicornhatheight),r,g,b)
		i+=1
		if i >= unicornhatheight*unicornhatwidth: break
	unicornhat.show()

@client.event
async def on_ready():
	guild = client.get_guild(GUILDID)
	if args.verbose:
		print(f'{client.user} is connected to the following guild: {guild.name} (id: {guild.id})')
		members = '; '.join([member.name for member in guild.members])
		print(f'Guild Members: {members}')
	redraw_unicornpihat(guild.members)

@client.event
async def on_member_update(before, after):
	if before.status == discord.Status.offline or after.status == discord.Status.offline or str(before.roles) != str(after.roles):
		if args.verbose: print(f'{str(before.name)}: {str(before.status)} -> {str(after.status)}')
		guild = client.get_guild(GUILDID)
		redraw_unicornpihat(guild.members)

client.run(TOKEN)
