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
server = HttpServer()
html = indexhtml.read()
server.listen(html) # Port 8089
