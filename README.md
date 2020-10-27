# httpserver-py
*Made by pr0xy, with the help of 0x74ngly (me) and bash0x0*

# Update logs
10/27/2020 - httpserver.py can now be used as a command. (pr0xy)

# What is HTTP?

HyperText Transfer Protocol - used for websites to interact as a protocol.

# Is this just a repository?

No, it will soon be a module, and come up in pypi website.

# How do you use this?

**Short instructions for this repo**
---

Not only it's a command, you also can interact with httpserver in the script.

```py
import httpserver

html = open("index.html","r").read()
port = 80 # change if you want
server = httpserver.HttpServer()
server.listen(html,port)
```

Must be able to run the script in current directory where the httpserver.py is, because this isn't a module yet. :3

---

Works on any devices on your network too. (Not 100% sure)

![](https://media.discordapp.net/attachments/769313530544783411/770765787630665738/unknown.png?width=893&height=475)
