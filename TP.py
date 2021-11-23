from cmu_112_graphics import *
import math
import random

def appStarted(app):
    app.cx = app.width/3
    app.cy = app.width/3
    app.r = 20
    app.playerX = app.cx+app.r-app.width/3.5
    app.playerY = app.cy+app.r+app.width/12
    app.playerColor = 'red'
    app.playerScrollX = 0
    app.scrollX = 0
    app.gameMargin = 0
    app.gameTimer = 0
    app.isGameOver = False
    app.paused = False
    app.playerTimer = 28 
    app.ground = (0, app.height-app.height/10, app.width, app.height)
    app.platformCells = []
    randomizePlatform(app)
    app.platforms = []
    platformBoundsfromCell(app)
    app.rows = app.height//10
    app.cols = app.width//10
    app.platformNum = len(app.platforms)
    app.platformSpacing = 90
    app.onPlatform = False
    app.speedpowerR = 10
    app.speedpowerX = app.width/6
    app.speedpowerY = app.height-app.height/10
    app.speedpowerTouch = False
    app.scrollSpeed = 10
    app.timeTouched = 0
    app.enemyX = app.width/5
    app.enemyY = app.width/5
    app.enemyCells = []
    app.enemyOnPlatform = []
    randomizeEnemies(app)
    app.originalenemies = []
    app.modifiedenemies = []
    enemyBoundsFromCell(app)
    app.speedPowerRandomX = 0
    app.speedPowerRandomY = 0
    app.itemIntersection = True
    isValidPowerPosition(app)
    app.tppoweritems = []
    app.tppowerTouch = [False, False, False]
    app.tppower = False
    randomizeTPItem(app)
    app.playerDied = False
    app.level = 1
    app.levelCounter = 1
    isSolvable(app)

# returns bounds of the player
def playerBounds(app):
    cx0, cy0 = (app.playerX - 2*app.r, app.playerY - 2*app.r)
    cx1, cy1 = (app.playerX, app.playerY) 
    return (cx0, cy0, cx1, cy1)

# returns the bounds of a given platform
def platformBounds(app, platform):
    return app.platforms[platform]

# returns the current enemy bounds
def enemyBounds(app, enemy):
    return app.modifiedenemies[enemy]

# returns the bounds of speed power
def speedpowerBounds(app):
    cx0, cy0 = (app.speedpowerX - app.speedpowerR+app.speedPowerRandomX*10, app.speedpowerY - 2*app.speedpowerR-app.speedPowerRandomY*10)
    cx1, cy1 = (app.speedpowerX + app.speedpowerR+app.speedPowerRandomX*10, app.speedpowerY-app.speedPowerRandomY*10)
    return (cx0, cy0, cx1, cy1)

# returns the bounds of teleportation power
def tppowerBounds(app, item):
    return app.tppoweritems[item]

# retrieves the bounds of the cell in coordinates
def getCellBounds(app, row, col):
    cellWidth = app.width / app.cols
    cellHeight = app.height / app.rows
    x0 = col*cellWidth
    x1 = (col+1)*cellWidth
    y0 = row*cellHeight
    y1 = (row+1)*cellHeight
    return (x0, y0, x1, y1)

# randomizes the positions of the platforms at the start of each level
def randomizePlatform(app):
    while len(app.platformCells) < 5:
        x0 = random.randint(7, 21)
        x1 = x0+2
        y0 = random.randint(5, 75)
        y1 = y0+random.randint(8, 15)
        print(x0, y0, x1, y1, app.platformCells)
        if len(app.platformCells) != 0 and platformIntersects(app, x0, x1, y0, y1):
            continue
        app.platformCells.append((x0, y0, x1, y1))

# checks if the randomized platform intersects with the latest platform added to the list
def platformIntersects(app, x0, x1, y0, y1):
    # for platform in app.platformCells:
    #     if (platform[1] <= y0 < (platform[3]+3) or 
    #         (y1+3) > platform[1]):
    #         return True
    #     if (platform[0] <= x0 <= platform[2]+1 or 
    #         platform[0]-1 <= x1 <= platform[2]):
    #         return True

    # for platform in range(0, len(app.platformCells), 2):
    #     if (app.platformCells[platform][1] <= y0 < (app.platformCells[platform][3]) or 
    #         (y1) > app.platformCells[platform][1]):
    #         return True
    #     if (app.platformCells[platform][0] <= x0 <= app.platformCells[platform][2] or 
    #         app.platformCells[platform][0] <= x1 <= app.platformCells[platform][2]):
    #         return True

    # if app.platformCells[-1][0] <= x0 <= app.platformCells[-1][2]+2 and app.platformCells[-1][0]-2 <= x1 <= app.platformCells[-1][2]:
    #     return True
    if ((app.platformCells[-1][0] <= x0 <= app.platformCells[-1][2]+2 and 
        app.platformCells[-1][0]-2 <= x1 <= app.platformCells[-1][2])and 
        (app.platformCells[-1][1] <= y0 <= app.platformCells[-1][2]+2 and
        app.platformCells[-1][1]-2 <= y1 <= app.platformCells[-1][2])):
        return True

    if len(app.platformCells) > 1:
        if (((app.platformCells[-1][0] <= x0 <= app.platformCells[-1][2]+2 and 
        app.platformCells[-1][0]-2 <= x1 <= app.platformCells[-1][2]) or
        (app.platformCells[-2][0] <= x0 <= app.platformCells[-2][2]+2 and 
        app.platformCells[-2][0]-2 <= x1 <= app.platformCells[-2][2]))and 
        ((app.platformCells[-1][1] <= y0 <= app.platformCells[-1][3]+2 and
           app.platformCells[-1][1]-2 <= y1 <= app.platformCells[-1][3]) or 
           (app.platformCells[-2][1] <= y0 <= app.platformCells[-2][3]+2 and 
           app.platformCells[-2][1]-2 <= y1 <= app.platformCells[-2][3]))):
            return True
            
        # if ((app.platformCells[-1][1] <= y0 <= app.platformCells[-1][2]+2 and
        #    app.platformCells[-1][1]-2 <= y1 <= app.platformCells[-1][2]) or 
        #    (app.platformCells[-2][1] <= y0 <= app.platformCells[-2][2]+2 and 
        #    app.platformCells[-2][1]-2 <= y1 <= app.platformCells[-2][2])):
        #    return True
    return False

# returns the actual coordinates of the platforms from the cell bounds
def platformBoundsfromCell(app):
    for platform in app.platformCells:
        x0, y0, x1, y1 = platform
        app.platforms.append((y0*10, x0*10, y1*10, x1*10))

# randomizes positions of enemies
def randomizeEnemies(app):
    #randomizes positions of platform enemies
    while len(app.enemyCells) < 3:
        platform = random.randint(0, 4)
        if platform not in app.enemyOnPlatform:
            app.enemyOnPlatform.append(platform)
            x1 = app.platformCells[platform][0]
            x0 = x1-3
            y0 = app.platformCells[platform][1]
            y1 = y0+3
            app.enemyCells.append((x0, y0, x1, y1))
    print(app.enemyOnPlatform)
    
    #randomizes positions of ground enemies
    while 3 <= len(app.enemyCells) < 6:
        x1 = 27
        x0 = x1-3
        y0 = random.randint(8, 80)
        y1 = y0+3
        if len(app.enemyCells) != 3 and enemyIntersects(app, x0, x1, y0, y1):
            continue
        app.enemyCells.append((x0, y0, x1, y1))

# checks if ground enemies intersect when randomized
def enemyIntersects(app, x0, x1, y0, y1):
    if len(app.enemyCells) == 3:
        return True
    for enemy in range(3, 6):
        if enemy < len(app.enemyCells):
            if (app.enemyCells[enemy][1] < y0 < app.enemyCells[enemy][3]+2 or 
                app.enemyCells[enemy][1]-2 < y1 < app.enemyCells[enemy][3]):
                return True           
    return False

# returns the actual coordinates of the enemies from the cell bounds
def enemyBoundsFromCell(app):
    for enemy in app.enemyCells:
        x0, y0, x1, y1 = enemy
        app.originalenemies.append((y0*10, x0*10, y1*10, x1*10)) 
        app.modifiedenemies.append([y0*10, x0*10, y1*10, x1*10])

# randomizes positional values for speed power up
def randomizeSpeedPower(app):
    app.speedPowerRandomX = random.randint(8, 30)
    app.speedPowerRandomY = random.randint(5, 20)

# checks if the randomly generated position of the powerup is valid
def isValidPowerPosition(app):
    while app.itemIntersection:
        randomizeSpeedPower(app)
        if powerIntersects(app):
            continue
        else:
            app.itemIntersection = False

# checks if the powerup intersects with an enemy or platform
def powerIntersects(app):
    x0, y0, x1, y1 = speedpowerBounds(app)
    # checks intersection with platform
    for platform in app.platforms:
        if ((platform[1] <= y0 <= platform[3] or platform[1] <= y1 <= platform[3]) and 
            (platform[0] <= x0 <= platform[2] or platform[0] <= x1 <= platform[2])):
            return True
    
    # checks intersection with enemy
    for enemy in app.originalenemies:
        if ((enemy[1] <= y0 <= enemy[3] or enemy[1] <= y1 <= enemy[3]) and 
            (enemy[0] <= x0 <= enemy[2] or enemy[0] <= x1 <= enemy[2])):
            return True
    return False

# randomizes positions of the 3 tp items
def randomizeTPItem(app):
    while len(app.tppoweritems) < 3:
        x = random.randint(8, 50)
        y = random.randint(5, 20)
        if len(app.tppoweritems) != 0 and itemIntersects(app, x, y):
            continue
        app.tppoweritems.append([app.speedpowerX - app.speedpowerR+x*10, app.speedpowerY - 2*app.speedpowerR - y*10,
                                 app.speedpowerX + app.speedpowerR+x*10, app.speedpowerY - y*10])

    # for platform in range(len(app.platforms)):
    #     if platform in app.enemyOnPlatform:
    #         continue
    #     print(app.platforms[platform])
    #     x = (app.platforms[platform][2] - app.platforms[platform][0])//2
    #     y = app.platforms[platform][1]-20
    #     app.tppoweritems.append([app.speedpowerX - app.speedpowerR+x, app.speedpowerY - 2*app.speedpowerR - y,
    #                              app.speedpowerX + app.speedpowerR+x, app.speedpowerY - y])

# checks if the tp items itersect with each other or any other object
def itemIntersects(app, x, y):
    x0 = app.speedpowerX - app.speedpowerR + x*10
    x1 = app.speedpowerX + app.speedpowerR + x*10
    y0 = app.speedpowerY - 2*app.speedpowerR - y*10
    y1 = app.speedpowerY - y*10

    # checks intersection with platform
    for platform in app.platforms:
        if ((platform[1] <= y0 <= platform[3] or platform[1] <= y1 <= platform[3]) and 
            (platform[0] <= x0 <= platform[2] or platform[0] <= x1 <= platform[2])):
            return True

    # checks intersection with enemy
    for enemy in app.originalenemies:
        if ((enemy[1] <= y0 <= enemy[3] or enemy[1] <= y1 <= enemy[3]) and 
            (enemy[0] <= x0 <= enemy[2] or enemy[0] <= x1 <= enemy[2])):
            return True
    
    # checks intersection with powerup
    dx0, dy0, dx1, dy1 = speedpowerBounds(app)
    if ((dy0 <= y0 <= dy1 or dy0 <= y1 <= dy1) and 
        (dx0 <= x0 <= dx1 or dx0 <= x1 <= dx1)): 
            return True
    
    # checks intersection with other tp items
    for tp in app.tppoweritems:
        tx0, ty0, tx1, ty1 = tp
        if ((ty0 <= y0 <= ty1 or ty0 <= y1 <= ty1) and 
            (tx0 <= x0 <= tx1 or tx0 <= x1 <= tx1)):
            return True

    return False

# checks if the level is solvable
def isSolvable(app):
    # deterimines the shortest platform
    minimumPlat = -1000
    for platform in app.platforms:
        if platform[1] > minimumPlat:
            minimumPlat = platform[1]
    
    # if the shortest platform does not reach player max jump height, check if any 
    if minimumPlat < app.playerY+112:
        for tp in app.tppoweritems:
            if tp[3] < app.playerY-2*app.r-112:
                # if there exists a tp item that is out of reach, than randomize all objects again
                app.platformCells = []
                randomizePlatform(app)
                app.platforms = []
                platformBoundsfromCell(app)
                app.enemyCells = []
                app.enemyOnPlatform = []
                randomizeEnemies(app)
                app.originalenemies = []
                app.modifiedenemies = []
                enemyBoundsFromCell(app)
                app.itemIntersection = True
                isValidPowerPosition(app)
                app.tppoweritems = []
                randomizeTPItem(app)
    
# checks if the player and platform intersect
def boundsIntersect(app, player, platform):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = platform
    # the reason for the 0 to 5 bounds because the incrementing of the jump animation
    # does not evenly match with the bounds of platforms
    return (0 <= dy1-py0 < 5) and (px0 <= (dx1+dx0)/2+app.scrollX <= px1)
    
#(px0 <= dx1+app.scrollX <= px1)

# checks if the enemy has collided with the player
def enemyHitPlayer(app, player, enemy):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = enemy
    return (dx1 > px0) and (dx0 < px1) and (py1 <= dy1) and (py0 >= dy0)

# checks if the player is on ground
def touchGround(app, player):
    (dx0, dy0, dx1, dy1) = player
    return 0 <= dy1 - app.ground[1] < 5

# Testing boundsIntersect conditions
#(py0 <= dy1 <= py1)    
#((dx1 >= px0) and (px1 >= dx0) and (dy1 >= py0) and (py1 >= dy0))

# checks if the speed powerup has been consumed by player
def touchSpeed(app, player, power):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = power
    return (dx1 > px0) and (dx0 < px1) and (py1 <= dy1) and (py0 >= dy0)

# checks if the teleportation powerup has been consumed by player
def touchTP(app, player, power):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = power
    return (dx1 > px0) and (dx0 < px1) and (py1 <= dy1) and (py0 >= dy0)

# Checks if the player is at center
def isPlayerCenter(app):
    if 0 <= app.playerScrollX - app.width/2 <= 10:
        return True
    else:
        return False

# Other isPlayerCenter condition
# if app.playerScrollX != app.width/2:
#         return False
#     else:
#         return True

def keyPressed(app, event):
    print(app.playerY)
    # allows player to restart if hit by enemy
    if app.playerDied and event.key == 'r':
        appStarted(app)
    
    # allows player to continue playing after beating a level
    if app.isGameOver and event.key == 'c':
        appStarted(app)
        app.level+=1
    
    # allows player to play again
    if app.isGameOver and app.level == 2 and event.key == 'r':
        appStarted(app)

    # increases speed if the player consumes speed powerup
    if app.speedpowerTouch == False and touchSpeed(app, playerBounds(app), speedpowerBounds(app)):
        app.scrollSpeed = 20
        app.speedpowerTouch = True
        app.playerColor = 'blue'
        app.timeTouched = app.gameTimer # keeps track of the time when speed powre is consumed
    
    # cancels speed powerup after a certain amount of time
    if app.speedpowerTouch and app.playerColor == 'blue' and app.gameTimer > app.timeTouched + 30:
        app.playerColor = 'red'
        app.scrollSpeed = 10

    # grants the power of teleportation to player if three purple items are collected
    if app.tppowerTouch == [True, True, True] and app.tppower == False:
        app.scrollSpeed = 10
        app.tppower = True
        app.playerColor = 'purple'

    # cancels tp powerup after a certain amount of time
    # if app.tppowerTouch and app.playerColor == 'purple' and app.gameTimer > app.timeTouched + 50:
    #     app.playerColor = 'red' 
    
    # moves player when player is at center
    if not app.isGameOver and isPlayerCenter(app) and not app.playerDied:
        if event.key == 'Left':
            app.scrollX -= app.scrollSpeed
            #app.gameTimer += 10
            app.speedpowerX += app.scrollSpeed
            #moves the tp items as the player moves
            for item in range(len(app.tppoweritems)):
                app.tppoweritems[item][0] += app.scrollSpeed
                app.tppoweritems[item][2] += app.scrollSpeed
            #moves the tp items as the player moves
            for enemy in range(len(app.modifiedenemies)):
                app.modifiedenemies[enemy][0] += app.scrollSpeed
                app.modifiedenemies[enemy][2] += app.scrollSpeed
            if app.gameMargin <= 0: # prevents player as well as any other items from going beyond game margins
                app.scrollX += app.scrollSpeed
                app.playerX -= app.scrollSpeed
                app.playerScrollX -= app.scrollSpeed
                app.speedpowerX -= app.scrollSpeed
                for item in range(len(app.tppoweritems)):
                    app.tppoweritems[item][0] -= app.scrollSpeed
                    app.tppoweritems[item][2] -= app.scrollSpeed
                for enemy in range(len(app.modifiedenemies)):
                    app.modifiedenemies[enemy][0] -= app.scrollSpeed
                    app.modifiedenemies[enemy][2] -= app.scrollSpeed
            else:
                app.gameMargin -= app.scrollSpeed
        elif event.key == 'Right':
            app.scrollX += app.scrollSpeed
            #app.gameTimer += 10
            app.speedpowerX -= app.scrollSpeed
            # keeps items in a constant position while player moves
            for item in range(len(app.tppoweritems)):
                app.tppoweritems[item][0] -= app.scrollSpeed
                app.tppoweritems[item][2] -= app.scrollSpeed
            # keeps enemies in a constant position while player moves
            for enemy in range(len(app.modifiedenemies)):
                app.modifiedenemies[enemy][0] -= app.scrollSpeed
                app.modifiedenemies[enemy][2] -= app.scrollSpeed
            if app.gameMargin > app.width/1.5: # prevents player as well as any other itemsfrom going beyond game margins
                app.scrollX -= app.scrollSpeed
                app.playerX += app.scrollSpeed
                app.playerScrollX += app.scrollSpeed
                app.speedpowerX += app.scrollSpeed
                for item in range(len(app.tppoweritems)):
                    app.tppoweritems[item][0] += app.scrollSpeed
                    app.tppoweritems[item][2] += app.scrollSpeed
                for enemy in range(len(app.modifiedenemies)):
                    app.modifiedenemies[enemy][0] += app.scrollSpeed
                    app.modifiedenemies[enemy][2] += app.scrollSpeed
            else:
                app.gameMargin += app.scrollSpeed
        # if teleportation power is consumed, space activates teleporting
        elif event.key == 'r' and app.playerColor == 'purple':
            app.playerY -= 112
            app.scrollX += 50
            app.gameMargin += 50
            app.speedpowerX -= 50
            for enemy in range(len(app.modifiedenemies)):
                app.modifiedenemies[enemy][0] -= 50
                app.modifiedenemies[enemy][2] -= 50
        elif event.key == 'Space':
            app.playerTimer = 28
            app.paused = True

    # Moves player if player is not at center
    elif not app.isGameOver and not app.playerDied:
        if event.key == 'Left':
            #app.gameTimer += 10
            app.playerScrollX -= app.scrollSpeed
            app.playerX -= app.scrollSpeed
            if app.playerScrollX <= 0:
                app.playerX += app.scrollSpeed
                app.playerScrollX += app.scrollSpeed
        elif event.key == 'Right':
            playerBound = playerBounds(app)
            #app.gameTimer += 10
            app.playerScrollX += app.scrollSpeed
            app.playerX += app.scrollSpeed
            # ends game if they reached the final platform and retrieved all three tp items
            if app.playerScrollX >= app.width/1.15 and touchGround(app, playerBound) and app.tppowerTouch == [True, True, True]:
                app.playerX -= app.scrollSpeed
                app.playerScrollX -= app.scrollSpeed
                app.isGameOver = True
        # if teleportation power is consumed, space activates teleporting
        elif event.key == 'r' and app.playerColor == 'purple':
            app.playerY -= 112
            app.playerX += 50
            app.playerScrollX += 50
            #app.paused = True
        elif event.key == 'Space':
            app.playerTimer = 28
            app.paused = True

def timerFired(app):
    app.gameTimer += 1 # keeps track of time passed as game starts
    #print(playerBounds(app))
    if app.paused:
        doStep(app)
    playerBound = playerBounds(app)
    # checks all the items to see if they have been touched
    for item in range(len(app.tppoweritems)):
        if touchTP(app, playerBounds(app), tppowerBounds(app,item)):
            app.tppowerTouch[item] = True
    
    # initiates enemy movement
    for enemy in range(len(app.modifiedenemies)):
        if not app.playerDied:
            enemyStep(app, enemy)
        if enemyHitPlayer(app, playerBound, app.modifiedenemies[enemy]):
            app.playerDied = True

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
# def downStep2(app):
#     playerBound = playerBounds(app)
#     bounds = app.platforms[1][1] <= playerBound[3] <= app.platforms[1][3]
#     if app.platforms[1][1] <= playerBound[3] <= app.platforms[1][3]:
#         pass
#     else:
#         if not touchGround(app, playerBound):
#             app.playerY += 1

# moves enemy
def enemyStep(app, enemy):
    for platform in range(app.platformNum):
        platformBound = platformBounds(app, platform)    
        if boundsIntersect(app, app.originalenemies[enemy], platformBound):
            if app.modifiedenemies[enemy][2] < platformBound[2]-5:
                app.modifiedenemies[enemy][0] += 1
                app.modifiedenemies[enemy][2] += 1
            elif app.originalenemies[enemy][0] == platformBound[0]:
                app.modifiedenemies[enemy][0] -= 1
                app.modifiedenemies[enemy][2] -= 1
        
    # app.modifiedenemies[enemy][0] += 1
    # app.modifiedenemies[enemy][2] += 1
        

def redrawAll(app, canvas):
    # More efficient platform drawing
    for platform in app.platformCells:
        row0, col0, row1, col1 = platform
        for row in range(row0, row1):
            for col in range(col0, col1):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0-app.scrollX, y0, x1-app.scrollX, y1, outline='black', fill='black')

    # Basic ground level
    canvas.create_rectangle(0, app.height-app.height/10, app.width, app.height, 
                            fill='green', outline='black')

    # Final platform to end game
    canvas.create_rectangle(app.width/2+app.width-app.scrollX, app.height/2.25+app.height/2.2,
                            app.width/1.5+app.width-app.scrollX, app.height/2+app.height/2.2, fill='blue', outline='black')
    
    # Drawing PowerUps/Items

    # Blue is speed
    if app.itemIntersection == False and app.speedpowerTouch == False: 
        px0, py0, px1, py1 = speedpowerBounds(app)
        canvas.create_oval(px0, py0, px1, py1, fill='blue', outline='black')

    # Purple is are items to repair teleportation machine i.e. teleports player up and slightly forward
    for item in range(len(app.tppoweritems)):
        if app.tppowerTouch[item] == False and app.tppower == False:
            tx0, ty0, tx1, ty1 = tppowerBounds(app, item) 
            canvas.create_oval(tx0, ty0, tx1, ty1, fill='purple', outline='black')
    
   
    # Drawing randomized enemies
    for enemy in range(len(app.modifiedenemies)):
        ex0, ey0, ex1, ey1 = enemyBounds(app, enemy)
        canvas.create_rectangle(ex0, ey0, ex1, ey1, fill='yellow', outline='black')
    
    # Debugging Text
    canvas.create_text(app.width/2, app.height/10, text=f'Level : {app.level}', font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, app.height/20, text=f'gameMargin = {app.timeTouched}', font='Arial 15 bold', fill='black')

    # Temporary dot character
    (cx0, cy0, cx1, cy1) = playerBounds(app)
    canvas.create_oval(cx0, cy0, cx1, cy1, fill=app.playerColor, outline='black')
    
    # Game started text
    if app.gameTimer <= 10:
        canvas.create_text(app.width/2, app.height/5, text='Level Start!', font='Didot 25 bold', fill='purple')
    
    # Level Complete text
    if app.isGameOver and app.level != 2:
        canvas.create_text(app.width/2, app.height/5, text='Level Complete!', font='Didot 25 bold', fill='purple')
        canvas.create_text(app.width/2, app.height/3, text="Press 'C' to continue!", font='Didot 25 bold', fill='purple')
    
    # Game Beaten text
    if app.level == 2 and app.isGameOver:
        canvas.create_text(app.width/2, app.height/5, text='You have Escaped!', font='Didot 25 bold', fill='purple')
        canvas.create_text(app.width/2, app.height/3, text="Press 'R' to play again!", font='Didot 25 bold', fill='purple')

    # Player Death text
    if app.playerDied:
        canvas.create_text(app.width/2, app.height/5, text='Game Over!', font='Didot 25 bold', fill='purple')
        canvas.create_text(app.width/2, app.height/3, text="Press 'R' to restart!", font='Didot 25 bold', fill='purple')

    # For debugging purposes
        # canvas.create_line(280, 0, 280, app.height, fill='black')
        # canvas.create_line(180, 0, 180, app.height, fill='purple')
        # canvas.create_line(0, 193.333, app.width, 193.333, fill='blue')
        # canvas.create_line(0, 210, app.width, 210, fill='red')
    
    # Drawing grid
    # for row in range(app.rows):
    #     for col in range(app.cols):
    #         (x0, y0, x1, y1) = getCellBounds(app, row, col)
    #         canvas.create_rectangle(x0, y0, x1, y1, outline='black')

runApp(width=600, height=300) 

