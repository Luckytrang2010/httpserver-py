# httpserver-py
*Made by pr0xy, with the help of 0x74ngly (me) and bash0x0*

# What is HTTP?

HyperText Transfer Protocol - used for websites to interact as a protocol.

# Is this just a repository?

No, it will soon be a module, and come up in pypi website.

# How do you use this?

**Short instructions for this repo**
---

```py
import httpserver
"""<!DOCTYPE HTML>
<html>
    <head>
        <title>nice cock bro</script>
    </head>
    <body>
        <center><h1>nice cock bro</h1></center>
    </body>
</html>
"""
indexhtml = open("./index.html","r")
server = httpserver.HttpServer()
html = indexhtml.read()
server.listen(html) # Port 8089
```

Must be able to run the script in current directory where the httpserver.py is, because this isn't a module yet. :3

---

Works on any devices on your network too. (Not 100% sure)

![](https://media.discordapp.net/attachments/769313530544783411/770765787630665738/unknown.png?width=893&height=475)
