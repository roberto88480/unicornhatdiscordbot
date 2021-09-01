# Unicorn HAT Discord Bot
This Pyhton3 sccript acts as a discord bot to get all members of a Discord server and lights up LEDs in the members's color.
I made this for a **Raspberry Pi Zero** with a [Unicorn pHAT](https://shop.pimoroni.com/products/unicorn-phat). A full Unicorn Hat should aswell.

## Requirements
 - Python3 (apt install pythpn3 python3-pip)
 - [pimoroni/unicorn-hat](https://github.com/pimoroni/unicorn-hat) (pip3 install unicornhat)
 - [discordpy](https://discordpy.readthedocs.io/) (pip3 install discordpy)
 - [Discord Bot](https://discord.com/developers/applications) Token

## Configuration
Put your Discord bot token and your guild id into a **.env** file.
```bash
DISCORD_TOKEN=aabbccddeeffgghhiijjkkllmm
DISCORD_GUILD_ID=111111111111111
```
