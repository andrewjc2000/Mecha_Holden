# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import pandas as pd
import string
import operator
from collections import Counter
from collections import OrderedDict
import matplotlib.pylab as plt
import os
import glob
from random import randint


#Dear anyone who reads this. I'm so sorry. 

df = pd.read_csv("GT22general.csv")

def activityVisual(person, timeInterval): #method for creating the graph of a person's activity
    nametemp = df.Author
    name = nametemp.tolist()
    datetemp =df.Date
    date = datetemp.tolist()
    totalMessages = 0
    
    dateDict = OrderedDict()
    dateDict2 = OrderedDict()
    length = len(date)
    
    date3 = date
    y = 6
    ##############################################
    
    channel = "#General"
    persony = False
    
    
    ##############################################
    if (person != "server"):
        persony = True
    
    
    
    if (timeInterval == "Day"):
        x = 0
    if (timeInterval == "Month"):
        x = 3
        
    if (timeInterval == "Year"):
        y = 9
        x = 3
    
    
    if(persony):
        for i in range (0, len(name)):
            if (name[i] != person):
                date[i] = None
    
        date = list(filter(None, date))
    
    date1 = date
    
    
    
    newLen = len(date)
    for i in range(0, newLen):
        date[i] = date[i][x:y]
    
    countDay = Counter(date) #counts total # of messages sent per day
    
    def unique(sequence):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))] #unique list items method
        
    date1 = unique(date1) #makes a pretty short list of dates in the right order
    
    for i in range(0, len(date1)):
        for key in countDay.keys():
            if(key == date1[i]):
                dateDict.update({date1[i]:countDay.get(key)})

    plt.bar(range(len(dateDict)), list(dateDict.values()), align = 'center')
    plt.xticks(range(len(dateDict)), list(dateDict.keys()))
    plt.title(person + "'s Number of Messages in " + channel +" Per " + timeInterval, fontsize = 12)
    plt.savefig('E:\Python\Discord bot\\Pictures\\picture.png')
    plt.close()

    
def wordAnalysis(person1): #method for finding distinctive words
    date10 = df.Date
    lengthy = len(date10) # length number
    commonWords = ["", "nan","a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your", "ain't", "aren't", "can't", "could've", "couldn't", "didn't", "doesn't", "don't", "hasn't", "he'd", "he'll", "he's", "how'd", "how'll", "how's", "i'd", "i'll", "i'm", "i've", "isn't", "it's", "might've", "mightn't", "must've", "mustn't", "shan't", "she'd", "she'll", "she's", "should've", "shouldn't", "that'll", "that's", "there's", "they'd", "they'll", "they're", "they've", "wasn't", "we'd", "we'll", "we're", "weren't", "what'd", "what's", "when'd", "when'll", "when's", "where'd", "where'll", "where's", "who'd", "who'll", "who's", "why'd", "why'll", "why's", "won't", "would've", "wouldn't", "you'd", "you'll", "you're", "you've"]
    countperson1 = {}
        
    person1 = person1.lower()    
    counts1 = Counter()
    counts2 = Counter()
        
    stringList1 = []
    stringList2 = []
        
    totalcount = Counter()
    count1Speaks = 0
        
    name = df.Author #authors stored in list
    content = df.Content #messages stored in list, index matches
    content.tolist()  
    name.tolist()
        
        
    length = len(name)
        
    namesLowercase = [] #array of lowercasenames
    contentLowercase = [] #array of lowercasecontent
    for i in name:
        lower_name = i.lower()
        namesLowercase.append(lower_name) #lowercases
    
    for i in content:
        i = str(i)
        lower_content = i.lower()
        contentLowercase.append(lower_content) #lowercases

    for i in range(0,length): #creates a seperate list for each person
        if namesLowercase[i] == person1 and "http" not in namesLowercase[i]:
            stringList1.append(contentLowercase[i])
    
    for i in range(0,length): #creates a seperate list for everybody
            stringList2.append(contentLowercase[i])
    
    
    for sentence in stringList1: #counts the number of each word in each set of strings
        counts1.update(word.strip('.,?!"\'').lower() for word in sentence.split())
    
    for sentence in stringList2: #counts the number of each word in each set of strings
        counts2.update(word.strip('.,?!"\'').lower() for word in sentence.split())
    
    totalcount.update(counts2)
    
    for name in namesLowercase: #counts # of times a person speaks
        if (name == person1):
            count1Speaks += 1
    
    totalSpeaks = len(name)
    
    newcounts1 = counts1
    
    for k in newcounts1.keys():
        newcounts1[k] = newcounts1[k] * newcounts1[k]
        
    newercounts1 = newcounts1
    
    for key in newcounts1.keys():
        for key2 in totalcount.keys():
            if (key == key2):
                newercounts1[key] = (newcounts1[key] / totalcount[key]) * (totalSpeaks / count1Speaks)*1000 


    for key in newercounts1.keys():
        for word in commonWords:
            if( key == word or key.find("http") == 0 or key.find("xe") != -1 or key.find("\\") != -1):
                newercounts1[key] = 0
    
    
    newercounts1 = { k:v for k, v in newercounts1.items() if v >20}

    for value in newercounts1:
        for k, v in newercounts1.items():
            newercounts1[k] = round(v)
    
    testCounter = Counter(newercounts1)
    return(testCounter.most_common())

bot =commands.Bot(command_prefix="holden ")


@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on "+ bot.user.name)
    print ("with the ID: " + bot.user.id)

    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("AAAAAAAAAAAAAAAAAAAAA IM ON FIRE SOMEONE PUT ME OUT")

    
@bot.command(pass_context = True)
async def info(ctx, user: discord.Member):
    await bot.say("The username is: {}".format(user.name))
    await bot.say("The user's ID is: {}".format(user.id))
    await bot.say("The user's status is: {}".format(user.status))
    await bot.say("The user's highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: : {}".format(user.joined_at))
    
@bot.command(pass_context = True)
async def stalkday(ctx, user: discord.Member):
    activityVisual(user.name + "#" + user.discriminator, "Day")
    await bot.send_file(ctx.message.channel,"E:\\Python\\Discord bot\\Pictures\\picture.png")
    await bot.say("Their most distinctive words are: " + str(wordAnalysis(user.name + "#" + user.discriminator)))
    

@bot.command(pass_context = True)
async def stalk(ctx, user: discord.Member):
    activityVisual(user.name + "#" + user.discriminator, "Month")
    await bot.send_file(ctx.message.channel,"E:\\Python\Discord bot\\Pictures\\picture.png")
    await bot.say("Their most distinctive words are: " + str(wordAnalysis(user.name + "#" + user.discriminator)))  


@bot.command(pass_context = True)
async def stalkServer(ctx):
    activityVisual("server")
    await bot.send_file(ctx.message.channel,"E:\\Python\Discord bot\\Pictures\\picture.png") 
    

@bot.command(pass_context = True)    
async def whois(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Discriminator", value = user.discriminator)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)    
    

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="*you are feeling very sleepy*")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def blend(ctx):
    await bot.say("Uh... SUGOI KAWAII DESU CHAN B-BAKA!~~~~ :3")


@bot.command(pass_context=True)
async def pls(ctx):
    await bot.say("I'M SORRY, THEY MADE ME DO IT") 


@bot.command(pass_context=True)
async def code(ctx):
    await bot.say("<https://github.com/Lennnoxy/Mecha_Holden>")
    await bot.say("https://images-gmi-pmc.edge-generalmills.com/8890dc0a-ec93-4adf-b496-d6b264b56818.jpg")
    
    
@bot.command(pass_context=True)
async def rate(ctx):
    x = randint(0,11)
    if x == 0:
        await bot.say("Worse than writing college essays in wet socks. " + str(x) + "/10")
    if x == 2:
        await bot.say("Absolutely disgusting. " + str(x) + "/10")
    if x == 3:
        await bot.say("Not a fan. " + str(x) + "/10")
    if x == 1:
        await bot.say("Makes me want to die. " + str(x) + "/10")
    if x == 4:
        await bot.say("Meh. " + str(x) + "/10")
    if x == 5:
        await bot.say("Tolerable, I suppose " + str(x) + "/10")
    if x == 6:
        await bot.say("Probably worth at least a dollar. " + str(x) + "/10")
    if x == 7:
        await bot.say("Preeeeeeeetty good. " + str(x) + "/10")
    if x == 8:
        await bot.say("What a glorious specimen. " + str(x) + "/10")
    if x == 9:
        await bot.say("The best thing since sliced bread. " + str(x) + "/10")
    if x == 10:
        await bot.say("*screeches*. " + str(x) + "/10")
    if x == 11:
        await bot.say("no")
       

@bot.command(pass_context=True)
async def marissa(ctx):
    await bot.say("m'risa")
    await bot.say("*tips fedora*")
    

@bot.command(pass_context=True)
async def lerk(ctx):
    await bot.say("banned")
    

@bot.command(pass_context=True)
async def leg(ctx):
    await bot.say("https://thumbs.dreamstime.com/b/hairy-leg-17861352.jpg")
    
   
@bot.command(pass_context=True)
async def sleep(ctx):
    await bot.say("no u")
    

@bot.command(pass_context=True)
async def words(ctx):
    await bot.say("Number beside words =/= # of times you said a word. It is a weighted value of the distinctiveness of a word relative to the amount of times you've said it/ the number of time other people have said it.")
    
    
@bot.command(pass_context=True)
async def wisdom(ctx):
    x = randint(0,11)
    if x == 0:
        await bot.say("Verbal agreements aren't worth the paper they're written on.")
    if x == 1:
        await bot.say("Just because you're paranoid doesn't mean they aren't after you.")
    if x == 3:
        await bot.say("You know that thing you've been thinking about doing? maybe don't do it.")
    if x == 4:
        await bot.say("Eat your drugs, stay in vegetables, don't do school.")
    if x == 11:
        await bot.say("Doing a job *right* the first time gets the job done. Doing the job *wrong* fourteen times gives you job security.")
    if x == 5:
        await bot.say("If at first you dont succeed, try majoring in business instead.")
    if x == 6:
        await bot.say("The early bird may get the worm, but the second mouse gets the cheese.")
    if x == 7:
        await bot.say("If you run everywhere you go, you will get places faster.")
    if x == 8:
        await bot.say("If you never leave the house, nothing can hurt you. Except for all the things that can. Like brain aneurysms.")
    if x == 9:
        await bot.say("Lennox is the real MVP") 
    if x == 10:
        await bot.say("no")       

@bot.command(pass_context=True)
async def snowfish(ctx):
    await bot.send_file(ctx.message.channel,"Discord bot\\snowfish.png")


@bot.command(pass_context=True)
async def why(ctx):
    await bot.say("Why not?")
    

@bot.command(pass_context=True)
async def cat(ctx):
    await bot.say("https://media1.tenor.com/images/fff400ed54a68629210f414b79df0e73/tenor.gif?itemid=3532340") 
    

@bot.command(pass_context=True)
async def attack(ctx):
    await bot.say("https://i.imgur.com/SYx9WXe.gifv") 


@bot.command(pass_context=True)
async def bun(ctx):
    await bot.say("https://i.imgur.com/d4cwnkb.gifv") 
    
