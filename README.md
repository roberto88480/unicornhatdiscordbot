# Unicorn HAT Discord Bot
Connects a Discord Guild to an RGB-LED-Pixel-Matrix. Each online Guild-Member lights up one Pixel. Pixel-color is defined by the Members Discord-Role.

## Hardware Requirements
 - [Unicorn HAT](http://shop.pimoroni.com/products/unicorn-hat) or [Unicorn pHAT](http://shop.pimoroni.com/products/unicorn-phat)
 - Raspberry Pi

I developed this for a **Raspberry Pi Zero** with a [Unicorn pHAT](https://shop.pimoroni.com/products/unicorn-phat). A full Unicorn Hat should work aswell.

## Installation (Debian / Raspberry Pi OS)
```bash
# Python 3
apt install pythpn3 python3-pip python3-dotenv

# Unicornhat Library (github.com/pimoroni/unicorn-hat)
pip3 install unicornhat 

# Discord Bot Library
pip3 install discord.py
```

## Configuration
Create your Discord Bot at <https://discord.com/developers/applications>.
Put your Discord bot token and your guild id into a **.env** file.
```bash
DISCORD_TOKEN=xxxxxxxxxxxxxxxxxx
DISCORD_GUILD_ID=111111111111111
```
