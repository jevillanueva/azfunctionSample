from typing import List
import requests
import json
from .config import DISCORD_CHANNEL_ID, DISCORD_BOT_TOKEN
def getTopNMessages(size:int=5):
    # type: (int) -> List
    payload={}
    url = "https://discordapp.com/api/channels/{0}/messages?limit={1}".format(DISCORD_CHANNEL_ID,size)  
    headers = {
    'Authorization': 'Bot {0}'.format(DISCORD_BOT_TOKEN)
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code  == 200):
        data = response.json()
        return data
    else:
        return None
