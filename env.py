import os
env={}
with open(".env","r") as f:
    for line in f:
        if "=" in line:
            key,value=line.split("=")
            env[key]=value.strip()

def get(key):
    return env[key]
    
'''
{
  "content": None,
  "embeds": [
    {
      "title": "Your Email Was Opened !",
      "description": "`Email Sent on` {sent_time}",
      "url": f"{url}",
      "color": f"{colour}",
      "fields": [
        {
          "name": "To",
          "value": "offering@terrorist.services",
          "inline": "true"
        },
        {
          "name": "From",
          "value": "5r33ch4@fbi.ac",
          "inline": "true"
        },
        {
          "name": "Subject",
          "value": "```{subject}```"
        },
        {
          "name": "Identifier",
          "value": "```json\n{\n  \"sent at\" : {date},\n  \"keyword\" : \"anti terror operation notification\"\n}\n```"
        },
        {
          "name": "IP",
          "value": f"[192.168.0.1](https://ipinfo.io/{request.remote_addr}) {(20-len(request.remote_addr))*'᲼'}",
          "inline": "true"
        },
        {
          "name": "Device",
          "value": f"{request.user_agent.platform} {(20-len(request.user_agent.platform))*'᲼'}",
          "inline": "true"
        },
        {
          "name": "Browser",
          "value": f"{request.user_agent.browser} {request.user_agent.version} {(20-len(request.user_agent.browser)-len(request.user_agent.version)-1)*'᲼'}",
          "inline": "true"
        }
      ],
      "footer": {
        "text": "Opened at : {time}"
      },
      "timestamp": f"{}"
    }
  ],
  "username": "track.email",
  "avatar_url": "https://cdn.dribbble.com/users/1322735/screenshots/14134247/media/a3c84750d3fbaf4759bec145cc48ced5.png?compress=1&resize=400x300&vertical=top"
}'''