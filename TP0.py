from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/3
    app.cy = app.width/3
    app.r = 20
    app.scrollX = 0
    app.playerScroll = 0
    app.gameMargin = 0
    app.gameTimer = 0
    app.isGameOver = False

# Checks if the player is at center
def isPlayerCenter(app):
    if app.playerScroll != app.width/2:
        return False
    else:
        return True

def keyPressed(app, event):
    print(app.width/1.5)
    if not app.isGameOver and isPlayerCenter(app):
        if event.key == 'Left':
            app.scrollX -= 10
            app.gameTimer += 10
            if app.gameMargin <= 0: # prevents player from going beyond game margins
                app.scrollX += 10
                app.playerScroll -= 10
            else:
                app.gameMargin -= 10
        elif event.key == 'Right':
            app.scrollX += 10
            app.gameTimer += 10
            if app.gameMargin > app.width/1.5: # prevents player from going beyond game margins
                app.scrollX -= 10
                app.playerScroll += 10
            else:
                app.gameMargin += 10

    # Moves Dot if dot is not at center
    elif not app.isGameOver:
        if event.key == 'Left':
            app.gameTimer += 10
            app.playerScroll -= 10
            if app.playerScroll <= 0:
                app.playerScroll += 10
        elif event.key == 'Right':
            app.gameTimer += 10
            app.playerScroll += 10
            if app.playerScroll >= app.width/1.15:
                app.playerScroll -= 10

def redrawAll(app, canvas):
    # Game started text
    if app.gameTimer <= 70:
        canvas.create_text(app.width/2, app.height/5, text='Level Start!', font='Didot 20 bold', fill='purple')
    
    # Game finished text
    

    # Basic map
    platformX, platformY = 0, app.height
    canvas.create_rectangle(0, app.height-app.height/10, app.width, app.height, 
                            fill='green', outline='black')
    
    # Three platforms
    canvas.create_rectangle(app.width/1.5+1.5*app.width/10-app.scrollX, app.height/2.25, 
                            app.width/2+1.5*app.width/10-app.scrollX, app.height/2, 
                            fill='black', outline='black')
    canvas.create_rectangle(app.width/1.5-app.width/5-app.scrollX, app.height/2.25+app.height/5, 
                            app.width/2-app.width/5-app.scrollX, app.height/2+app.height/5, 
                            fill='black', outline='black')
    canvas.create_rectangle(app.width/1.5+app.width/2-app.scrollX, app.height/2.25+app.height/5, 
                            app.width/2+app.width/2-app.scrollX, app.height/2+app.height/5, 
                            fill='black', outline='black')
    
    # Final platform to end game
    canvas.create_rectangle(app.width/1.5+app.width-app.scrollX, app.height/2.25+app.height/2.2, 
                            app.width/2+app.width-app.scrollX, app.height/2+app.height/2.2, 
                            fill='blue', outline='black')

    # Debugging Text
    canvas.create_text(app.width/2, app.height/10, text=f'ScrollX = {app.scrollX}', font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, app.height/20, text=f'gameMargin = {app.gameMargin}', font='Arial 15 bold', fill='black')

    # Temporary dot character
    canvas.create_oval(app.cx+app.r-app.width/3.5+app.playerScroll, app.cy+app.r+app.width/12,
                       app.cx-app.r-app.width/3.5+app.playerScroll, app.cy-app.r+app.width/12, 
                       fill='red', outline='black')

runApp(width=600, height=300) 