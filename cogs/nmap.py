import discord
from discord.ext import commands
import re
import subprocess

class nmap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def check_valid(self, pattern):
        ip_pattern = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
        if ip_pattern.search(str(pattern)):
            return 'IP'
    def scan(self, ip):
        return subprocess.check_output(['nmap', ip]).decode('UTF-8')

    # Define nmap command
    @commands.command()
    async def nmap(self, ctx, ip=None):
        if ip == None:
            await ctx.reply("Syntax: nmap [IP]")
        # Check if IP given is valid
        if self.check_valid(ip) == "IP":
            await ctx.reply("Valid IP, scan starting..")
            await ctx.send(f'SCAN RESULTS:\n```{self.scan(ip)}```')
        else:
            await ctx.reply("Invalid IP, try again with a valid IP")
