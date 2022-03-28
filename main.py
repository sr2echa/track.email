import flask
from flask import request,Flask,redirect,render_template,flash, request, send_file
from flask_mail import Mail, Message

import base64
import requests
import datetime
import random

import env # import env.py

app = flask.Flask(__name__, template_folder='.', static_folder='assets')
app.config["DEBUG"] = False

app.config.update(
    DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER = env.get("MAIL_SERVER"),
	MAIL_PORT = env.get("MAIL_PORT"),
	MAIL_USE_SSL = env.get("MAIL_USE_SSL"),
	MAIL_USERNAME = env.get("MAIL_USERNAME"),
	MAIL_PASSWORD = env.get("MAIL_PASSWORD")
)
mail=Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track/secure/')
def track():
    ##### Getting Required Information #####

    # Mode of informing the user
    if "email" in request.args:
        email=base64.b64decode(request.args["email"]).decode("utf-8")
    else:
        email=False
    if 'webhook' in request.args:
        webhook=base64.b64decode(request.args["webhook"]).decode("utf-8")
    else:
        webhook=False
    ######

    # Getting The Tracking Content Info
    if "to" in request.args:
        to=base64.b64decode(request.args.get('to').decode('utf-8'))
    else:
        to=None
    if "from" in request.args:
        from_=base64.b64decode(request.args.get('from').decode('utf-8'))
    else:
        from_=None
    if "subject" in request.args:
        subject=base64.b64decode(request.args.get('subject').decode('utf-8'))
    else:
        subject=None
    if "info" in request.args:
        info=base64.b64decode(request.args.get('info').decode('utf-8'))
    else:
        info="None"
    ######

    if webhook:
        #send a post request to the webhook
        '''
        data = {
                "username" : "track.email"
            }

        data["embeds"] = [
            {
                "title" : "Your email was opened",
                "description" : "",
                "fields" : [
                    {
                        "name":"To",
                        "value":f"{to}",
                        "inline":"true"
                    },
                    {
                        "name":"From",
                        "value":f"{from_}",
                        "inline":"true"
                    },
                    {
                        "name":"Location",
                        "value":f"**ip** : ({request.remote_addr})[https://ipinfo.io/{request.remote_addr}] \n**Device** : {request.user_agent.platform} \n**Browser** : {request.user_agent.browser}",
                    },
                    {
                        "name":"Subject",
                        "value":f"{subject}"
                    },
                    {
                        "name":"Content",
                        "value":f"{content}"
                    }
                ],
                "timestamp": f"{datetime.datetime.utcnow()}"
            }
        ]
        '''
        data = {
                "content": None,
                "embeds": [
                     {      
                            "title": "Your Email Was Opened !",
                            "description": "",
                            "url": f"https://trackemail.sreecha.me",
                            "color": f"{random.choice([])}",
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
                                    "value": f"** **\n>>> {info}"
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
                                "text": f"Opened at : {datetime.datetime.utcnow()}"
                                },
                            "timestamp": f"{datetime.datetime.utcnow()}"
                                }
                        ],
                    "username": "track.email",
                    "avatar_url": r"https://cdn.dont-ping.me/api/%F0%9F%98%B4%F0%9F%A4%96%F0%9F%A4%96%F0%9F%A6%96%F0%9F%98%8A.webp"
                }

        result = requests.post(webhook, json = data)

    if email:
        msg = Message(
            'Your Mail Was Opened',
            sender = env.get("MAIL_USERNAME"),
            recipients = [email]
            )
        msg.body = f'''<b>To    : </b> {to} <br>
        <b>From  : </b> {from_} <br> 
        <br> 
        <b>Subject : </b> {subject} <br> 
        <b>Content : </b> {info} <br> 
        <br> 
        <b>Location : </b> {request.remote_addr} <a herf="https://ipinfo.io/{request.remote_addr}">More Info</a> <br> 
        <b>Device : </b> {request.user_agent.platform} <br> 
        <b>Browser : </b> {request.user_agent.browser}'''
        mail.send(msg)

    return send_file('assets/totallynotsuspicious.png', mimetype='image/gif')





#return (flask.render_template('home.html', srch=srch, default=default))

@app.route('/track/', methods=['GET'])
def track_():
    ### Getting Required Information ###
    if "email" in request.args:
        email=request.args["email"]
    else:
        email=None
    if 'webhook' in request.args:
        webhook=request.args["webhook"]
    else:
        webhook=None
    ###

    # Getting The Tracking Content Info
    if "to" in request.args:
        to=request.args["to"]
    else:
        to=None
    if "from" in request.args:
        from_=request.args["from"]
    else:
        from_=None
    if "subject" in request.args:
        subject=request.args["subject"]
    else:
        subject=None
    if "info" in request.args:
        info=request.args["info"]
    else:
        info="None"
    ###

    if webhook:
        #send a post request to the webhook
        data = {
                "content": None,
                "embeds": [
                     {      
                            "title": "Your Email Was Opened !",
                            "description": "",
                            "url": f"https://trackemail.sreecha.me",
                            "color": f"{''.join(random.sample('1234567890ABCDEF',6))}",
                            "fields": [
                                {
                                    "name": "To",
                                    "value": f"{to}",
                                    "inline": "true"
                                },
                                {
                                    "name": "From",
                                    "value": f"{from_}",
                                    "inline": "true"
                                },
                                {
                                    "name": "Subject",
                                    "value": f"```{subject}```"
                                },
                                {
                                    "name": "Identifier",
                                    "value": f"** **\n>>> {info}"
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
                                "text": f"Opened at : {datetime.datetime.utcnow()}"
                                },
                            "timestamp": f"{datetime.datetime.utcnow()}"
                                }
                        ],
                    "username": "track.email",
                    "avatar_url": r"https://cdn.dont-ping.me/api/%F0%9F%98%B4%F0%9F%A4%96%F0%9F%A4%96%F0%9F%A6%96%F0%9F%98%8A.webp"
                }

        result = requests.post(webhook, json = data)

    if email:
        msg = Message(
            'Your Mail Was Opened',
            sender = env.get("MAIL_USERNAME"),
            recipients = [email]
            )
        msg.html = f'''<html>
        <b>To    : </b> {to} <br>
        <b>From  : </b> {from_} <br> 
        <br> 
        <b>Subject : </b> {subject} <br> 
        <b>Content : </b> {info} <br> 
        <br> 
        <b>Location : </b> {request.remote_addr} <a herf="{'https://ipinfo.io/' + request.remote_addr}">More Info</a> <br> 
        <b>Device : </b> {request.user_agent.platform} <br> 
        <b>Browser : </b> {request.user_agent.browser}
        </html>'''
        msg.body = ""
        mail.send(msg)

    return send_file('assets/totallynotsuspicious.png', mimetype='image/gif')


@app.route('/track/simple/')
def track_simple():
    ### Getting Required Information ###
    if "email" in request.args:
        email=request.args["email"]
    else:
        email=None
    if 'webhook' in request.args:
        webhook=request.args["webhook"]
    else:
        webhook=None
    ###

    if webhook:
        #send a post request to the webhook
        data = {
                "username" : "track.email"
            }

        data["embeds"] = [
            {
                "title" : "Your email was opened",
                "description" : "",
                "fields" : [
                    {
                        "name":"IP",
                        "value":f"({request.remote_addr})[https://ipinfo.io/{request.remote_addr}]",
                    },
                    {
                        "name":"Device",
                        "value":f"{request.user_agent.platform}"
                    },
                    {
                        "name":"Browser",
                        "value":f"{request.user_agent.browser}"
                    }
                ],
                "timestamp": f"{datetime.datetime.utcnow()}"
            }
        ]

        result = requests.post(webhook, json = data)

    if email:
        msg = Message(
            'Your Mail Was Opened',
            sender = env.get("MAIL_USERNAME"),
            recipients = [email]
            )
        msg.body = f'''<b>IP    : </b> {request.remote_addr} <a herf="https://ipinfo.io/{request.remote_addr}">More Info</a> <br> 
        <b>Device : </b> {request.user_agent.platform} <br> 
        <b>Browser : </b> {request.user_agent.browser}'''
        mail.send(msg)

    return send_file('assets/totallynotsuspicious.png', mimetype='image/gif')

@app.route('/track/link/simple/', methods=['GET'])
def track_link():
    if "href" in request.args:
        href=request.args["href"]
    else:
        href="https://youtube.com/watch?v=dQw4w9WgXcQ"
    
    if "webhook" in request.args:
        webhook=request.args["webhook"]
    else:
        webhook=None
    if "email" in request.args:
        email=request.args["email"]
    else:
        email=None

    if webhook:
        #send a post request to the webhook
        data = {
                "username" : "track.email"
            }

        data["embeds"] = [
            {
                "title" : "Your Link was Clicked",
                "description" : "",
                "fields" : [
                    {
                        "name":"Link",
                        "value":f"{href}",
                    },
                    {
                        "name":"IP",
                        "value":f"({request.remote_addr})[https://ipinfo.io/{request.remote_addr}]",
                    },
                    {
                        "name":"Device",
                        "value":f"{request.user_agent.platform}"
                    },
                    {
                        "name":"Browser",
                        "value":f"{request.user_agent.browser}"
                    }
                ],
                "timestamp": f"{datetime.datetime.utcnow()}"
            }
        ]

        result = requests.post(webhook, json = data)

    if email:
        msg = Message(
            'Your Mail Was Opened',
            sender = env.get("MAIL_USERNAME"),
            recipients = [email]
            )
        msg.body = f'''<b>Link    : </b> {href} <br> 
        <b>Location : </b> {request.remote_addr} <a herf="https://ipinfo.io/{request.remote_addr}">More Info</a> <br> 
        <b>Device : </b> {request.user_agent.platform} <br> 
        <b>Browser : </b> {request.user_agent.browser}'''
        mail.send(msg)


@app.route('/track/link/', methods=['GET'])
def tracklink():
    if "href" in request.args:
        href=request.args["href"]
    else:
        href="https://youtube.com/watch?v=dQw4w9WgXcQ"
    
    if "webhook" in request.args:
        webhook=request.args["webhook"]
    else:
        webhook=None
    if "email" in request.args:
        email=request.args["email"]
    else:
        email=None

    if webhook:
        #send a post request to the webhook
        data = {
                "username" : "track.email"
            }

        data["embeds"] = [
            {
                "title" : "Your Link was Clicked",
                "description" : "",
                "fields" : [
                    {
                        "name":"Link",
                        "value":f"{href}",
                    },
                    {
                        "name":"IP",
                        "value":f"({request.remote_addr})[https://ipinfo.io/{request.remote_addr}]",
                    },
                    {
                        "name":"Device",
                        "value":f"{request.user_agent.platform}"
                    },
                    {
                        "name":"Browser",
                        "value":f"{request.user_agent.browser}"
                    }
                ],
                "timestamp": f"{datetime.datetime.utcnow()}"
            }
        ]

        result = requests.post(webhook, json = data)

    if email:
        msg = Message(
            'Your Mail Was Opened',
            sender = env.get("MAIL_USERNAME"),
            recipients = [email]
            )
        msg.body = f'''<b>Link    : </b> {href} <br> 
        <b>Location : </b> {request.remote_addr} <a herf="https://ipinfo.io/{request.remote_addr}">More Info</a> <br> 
        <b>Device : </b> {request.user_agent.platform} <br>
        <b>Browser : </b> {request.user_agent.browser}'''
        mail.send(msg)

    return redirect(href)

app.run()