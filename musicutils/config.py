from discord.ext import commands
from collections import Counter
from collections import OrderedDict, deque, Counter
from datetime import datetime as dt

#from .utils import checks, db

import time
import logging
import aiohttp
import discord
import sys
import asyncio
import datetime
import traceback
import copy
import unicodedata
import inspect
import os
import json

bot_token = "MzcyNjAzMTk4ODYwNDI3MjY0.DQPHCw.JFQu3Yw88k3uDW5Frd8LjUyf-UU"
bot_owner = 127883523829923840
dev_discord = "https://discord.gg/UBC5MmP"
embed_color = 0x00FFFF

def setup(bot):
    bot.add_cog(Config(bot))