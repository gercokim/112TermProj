from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/3
    app.cy = app.width/3
    app.r = 20
    app.scrollX = 0

def keyPressed(app, event):
    if event.key == 'Left':
        app.scrollX -= 5
    elif event.key == 'Right':
        app.scrollX += 5

def redrawAll(app, canvas):
    # Basic map with platforms
    platformX, platformY = 0, app.height
    canvas.create_rectangle(0, app.height-app.height/10, app.width, app.height, 
                            fill='green', outline='black')
    canvas.create_rectangle(app.width/1.5+1.5*app.width/10-app.scrollX, app.height/2.25, 
                            app.width/2+1.5*app.width/10-app.scrollX, app.height/2, 
                            fill='black', outline='black')
    canvas.create_rectangle(app.width/1.5-app.width/5-app.scrollX, app.height/2.25+app.height/5, 
                            app.width/2-app.width/5-app.scrollX, app.height/2+app.height/5, 
                            fill='black', outline='black')

    # Temporary dot character
    canvas.create_oval(app.cx+app.r, app.cy+app.r, app.cx-app.r, app.cy-app.r, fill='red', outline='black')

runApp(width=600, height=300) 