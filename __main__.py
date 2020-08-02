import discord
import re

# Discord Bot Token - Controls (PCT Esports Bot#9903)
with open('token.txt') as inp:
    token = inp.readline()
client = discord.Client()

# The following are the discord developer IDs for each channel (THESE SHOULD BE INTS EXCEPT clip_submissions) If any channels are made, deleted or renamed new IDs should be found!
clip_submissions = #[InsertYourOwnChannelIDsHere]
clip_main = #[InsertYourOwnChannelIDsHere]
test = #[InsertYourOwnChannelIDsHere]
bot_id = #[InsertYourOwnChannelIDsHere] # PCT Esports Bot Discord ID

# This function finds any and all characters associated with links and selects each individual link it finds and assigns it to an array element. (ur is an array)
def url(message):
   ur = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
   return(ur)

@client.event

async def on_message(message):
    cmd = message.content.startswith
    member = message.author

    if str(message.channel.id) in clip_submissions:                      # If a message is in any clip_submissions channel, check for a URL
        if message.author.id != bot_id:
            video_link = url(message.content)
            if video_link == []:
                pass
            else:
                channel = client.get_channel(id=clip_main)               # id must be an int NOT a string
                new_clip = "**" + str(member) + '** submitted in **' + str(message.channel) + '**\r' + str(video_link[0])
                await channel.send(new_clip)

#TODO: Weekly reoccuring polls - "What type of video for next weeks {Insert Date Here} video? "
    # if message.content.startswith(".poll"):
        # if message.content

client.run(token)




