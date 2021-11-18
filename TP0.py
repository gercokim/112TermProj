from cmu_112_graphics import *
import math

def appStarted(app):
    app.cx = app.width/3
    app.cy = app.width/3
    app.r = 20
    app.playerX = app.cx+app.r-app.width/3.5
    app.playerY = app.cy+app.r+app.width/12
    app.playerScrollX = 0
    app.scrollX = 0
    app.gameMargin = 0
    app.gameTimer = 0
    app.isGameOver = False
    app.paused = False
    app.playerTimer = 28 
    app.ground = (0, app.height-app.height/10, app.width, app.height)
    app.platforms = [(app.width/2+1.5*app.width/10, app.height/2.25, 
                     app.width/1.5+1.5*app.width/10, app.height/2), 
                     (app.width/2-app.width/5, app.height/2.25+app.height/5, 
                     app.width/1.5-app.width/5, app.height/2+app.height/5),
                     (app.width/2+app.width/2, app.height/2.25+app.height/5, 
                     app.width/1.5+app.width/2, app.height/2+app.height/5)]
    app.platformNum = len(app.platforms)
    app.platformSpacing = 90
    app.onPlatform = False

# returns bounds of the player
def playerBounds(app):
    cx0, cy0 = (app.playerX - 2*app.r, app.playerY - 2*app.r)
    cx1, cy1 = (app.playerX, app.playerY) 
    return (cx0, cy0, cx1, cy1)

# returns the bounds of a given platform
def platformBounds(app, platform):
    return app.platforms[platform]

# checks if the player and platform intersect
def boundsIntersect(app, player, platform):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = platform
    # the reason for the 0 to 5 bounds because the incrementing of the jump animation
    # does not evenly match with the bounds of platforms
    return (0 < dy1-py0 < 5) and (px0 <= (dx1+dx0)/2+app.scrollX <= px1)
    
#(px0 <= dx1+app.scrollX <= px1)

# checks if the player is on ground
def touchGround(app, player):
    (dx0, dy0, dx1, dy1) = player
    return dy1 == app.ground[1]

# Testing boundsIntersect conditions
#(py0 <= dy1 <= py1)    
#((dx1 >= px0) and (px1 >= dx0) and (dy1 >= py0) and (py1 >= dy0))

# Checks if the player is at center
def isPlayerCenter(app):
    if app.playerScrollX != app.width/2:
        return False
    else:
        return True

def keyPressed(app, event):
    if not app.isGameOver and isPlayerCenter(app):
        if event.key == 'Left':
            app.scrollX -= 10
            app.gameTimer += 10
            if app.gameMargin <= 0: # prevents player from going beyond game margins
                app.scrollX += 10
                app.playerX -= 10
                app.playerScrollX -= 10
            else:
                app.gameMargin -= 10
        elif event.key == 'Right':
            app.scrollX += 10
            app.gameTimer += 10
            if app.gameMargin > app.width/1.5: # prevents player from going beyond game margins
                app.scrollX -= 10
                app.playerX += 10
                app.playerScrollX += 10
            else:
                app.gameMargin += 10
        elif event.key == 'Space':
            app.playerTimer = 28
            app.paused = True

    # Moves player if player is not at center
    elif not app.isGameOver:
        if event.key == 'Left':
            app.gameTimer += 10
            app.playerScrollX -= 10
            app.playerX -= 10
            if app.playerScrollX <= 0:
                app.playerX += 10
                app.playerScrollX += 10
        elif event.key == 'Right':
            app.gameTimer += 10
            app.playerScrollX += 10
            app.playerX += 10
            if app.playerScrollX >= app.width/1.15:
                app.playerX -= 10
                app.playerScrollX -= 10
                app.isGameOver = True
        elif event.key == 'Space':
            app.playerTimer = 28
            app.paused = True

def timerFired(app):
    if app.paused:
        doStep(app)
    playerBound = playerBounds(app)
    # checks if player is standing on ground
    # if so, then there's no need to check if player's on platform
    if touchGround(app, playerBound):
        app.onPlatform = True
        return
    for platform in range(app.platformNum):
        platformBound = platformBounds(app, platform)
        # if player is standing on platform, the player stops the jump animation
        if boundsIntersect(app, playerBound, platformBound) == True:
            app.paused = False
            app.onPlatform = True
            return
        # if player is not on platform, the player falls to the ground
        if app.onPlatform==False and app.paused==False and boundsIntersect(app, playerBound, platformBounds(app, platform))==False:
            downStep(app)
    # in the case that the player is not standing on any surface, onPlatform is false
    app.onPlatform = False

        
# Player jumps after space is pressed
def doStep(app):
    playerBound = playerBounds(app)
    if app.playerTimer >= 0:
        app.playerY -= app.playerTimer
        app.playerTimer -= 4
    elif not touchGround(app, playerBound):
            app.playerY += 8
            
# Player falls if not standing on a surface
def downStep(app):
    playerBound = playerBounds(app)
    if not touchGround(app, playerBound):
        app.playerY += 8

# testing different versions of downStep 
def downStep2(app):
    playerBound = playerBounds(app)
    bounds = app.platforms[1][1] <= playerBound[3] <= app.platforms[1][3]
    print(app.platforms[1][1], playerBound[3], app.platforms[1][3], bounds)
    if app.platforms[1][1] <= playerBound[3] <= app.platforms[1][3]:
        print('stop down')
    else:
        if not touchGround(app, playerBound):
            app.playerY += 1

def redrawAll(app, canvas):
    # Game started text
    if app.gameTimer <= 70:
        canvas.create_text(app.width/2, app.height/5, text='Level Start!', font='Didot 25 bold', fill='purple')
    
    # Game finished text
    if app.isGameOver:
        canvas.create_text(app.width/2, app.height/5, text='Level Complete!', font='Didot 25 bold', fill='purple')
   
    # Three platforms
    # canvas.create_rectangle(app.width/1.5+1.5*app.width/10-app.scrollX, app.height/2.25, 
    #                         app.width/2+1.5*app.width/10-app.scrollX, app.height/2, 
    #                         fill='black', outline='black')
    # canvas.create_rectangle(app.width/1.5-app.width/5-app.scrollX, app.height/2.25+app.height/5, 
    #                         app.width/2-app.width/5-app.scrollX, app.height/2+app.height/5, 
    #                         fill='black', outline='black')
    # canvas.create_rectangle(app.width/1.5+app.width/2-app.scrollX, app.height/2.25+app.height/5, 
    #                         app.width/2+app.width/2-app.scrollX, app.height/2+app.height/5, 
    #                         fill='black', outline='black')

    # More efficient platform drawing
    for platform in range(app.platformNum):
        (x0, y0, x1, y1) = platformBounds(app, platform)
        canvas.create_rectangle(x0-app.scrollX, y0, x1-app.scrollX, y1, fill='black', outline='black')

    # Basic ground level
    canvas.create_rectangle(0, app.height-app.height/10, app.width, app.height, 
                            fill='green', outline='black')

    # Final platform to end game
    canvas.create_rectangle(app.width/1.5+app.width-app.scrollX, app.height/2.25+app.height/2.2, 
                            app.width/2+app.width-app.scrollX, app.height/2+app.height/2.2, 
                            fill='blue', outline='black')

    # Debugging Text
    canvas.create_text(app.width/2, app.height/10, text=f'ScrollX = {app.scrollX}', font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, app.height/20, text=f'gameMargin = {app.gameMargin}', font='Arial 15 bold', fill='black')

    # Temporary dot character
    (cx0, cy0, cx1, cy1) = playerBounds(app)
    canvas.create_oval(cx0, cy0, cx1, cy1, fill='red', outline='black')

    # canvas.create_line(280, 0, 280, app.height, fill='black')
    # canvas.create_line(180, 0, 180, app.height, fill='purple')
    # canvas.create_line(0, 193.333, app.width, 193.333, fill='blue')
    # canvas.create_line(0, 210, app.width, 210, fill='red')

runApp(width=600, height=300) 