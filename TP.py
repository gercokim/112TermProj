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
    app.ground = (0, app.height-app.height/10, 150, app.height)
    app.finalPlatform = (app.width//2+app.width, app.height-app.height//10,
                                int(app.width//1.5+app.width), app.height-app.height//10+20)
    app.platformCells = []
    randomizePlatform(app)
    app.platforms = []
    platformBoundsfromCell(app)
    app.platforms.append(app.finalPlatform)
    app.platformColor = ['black'] * len(app.platforms)
    app.rows = app.height//10
    app.cols = app.width//10
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
    app.enemyDict = {}
    app.enemyDirection = {}
    randomizeEnemies(app)
    app.originalenemies = []
    app.modifiedenemies = []
    app.enemyMovement = []
    enemyBoundsFromCell(app)
    app.speedPowerRandomX = 0
    app.speedPowerRandomY = 0
    app.itemIntersection = True
    isValidPowerPosition(app)
    app.tppoweritems = []
    app.tppowerTouch = [False, False, False]
    app.tppower = False
    randomizeTPItem(app)
    app.freezepowerTouch = False
    app.freezePowerRandomX = 0
    app.freezePowerRandomY = 0
    app.freezeTime = 0
    app.enemyFreeze = False
    randomizeFreeze(app)
    app.heartpowerTouch = False
    app.heartPowerRandomX = 0
    app.heartPowerRandomY = 0
    randomizeHeart(app)
    app.playerDied = False
    app.level = 1
    isSolvable3(app)
    app.direction = 1
    backgroundURL = 'https://t3.ftcdn.net/jpg/02/16/90/02/360_F_216900207_Qzsnl42GZPn6tRa86DeI1ioY4M0pz0eF.jpg'
    app.background = app.loadImage(backgroundURL)
    platformURL = 'https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/8a5f786d108adca.png'
    app.ogplatform = app.loadImage(platformURL)
    app.platform = app.scaleImage(app.ogplatform, 1/3.25)
    finalteleportURL = 'finaltp.png'
    app.finalTP = app.loadImage(finalteleportURL)
    app.finalTPhelp = app.scaleImage(app.finalTP, 1/1.5)
    app.rightidleSprites = []
    app.leftidleSprites = []
    app.rightjumpSprites = []
    app.leftjumpSprites = []
    idleAndJump(app)
    app.leftfallSprites = []
    app.rightfallSprites = []
    fall(app)
    app.rightrunSprites = []
    app.leftrunSprites = []
    run(app)
    file = f'adventurer-die-06.png'
    imgR = app.loadImage(file)
    app.img2R = app.scaleImage(imgR, 1.75)
    app.imgL = app.img2R.transpose(Image.FLIP_LEFT_RIGHT)
    app.rightidleCounter = 0
    app.leftidleCounter = 0
    app.rightjumpCounter = 0
    app.leftjumpCounter = 0
    app.rightrunCounter = 0
    app.leftrunCounter = 0
    app.leftfallCounter = 0
    app.rightfallCounter = 0
    app.spriteDirection = 0
    app.spriteX = 0
    app.spriteY = 0
    app.peak = False
    speed = 'speed.png'
    app.speedsprite2 = app.loadImage(speed)
    app.speedsprite = app.scaleImage(app.speedsprite2, 1/20)
    app.speedHelp = app.scaleImage(app.speedsprite2, 1/10)
    tpItem = 'tp.png'
    app.tpSprite2 = app.loadImage(tpItem)
    app.tpSprite = app.scaleImage(app.tpSprite2, 1/10)
    app.tpHelp = app.scaleImage(app.tpSprite2, 1/3)
    app.enemySpritesR = []
    app.enemySpritesL = []
    enemy(app)
    app.rightEnemy = 0
    app.leftEnemy = 0
    freeze = 'freeze.png'
    app.freezesprite2 = app.loadImage(freeze)
    app.freezesprite = app.scaleImage(app.freezesprite2, 1/5.5)
    app.freezeHelp = app.scaleImage(app.freezesprite2, 1/3)
    app.lives = 0
    heart = 'heart.png'
    app.heartsprite2 = app.loadImage(heart)
    app.heartsprite = app.scaleImage(app.heartsprite2, 1/16)
    app.heartHelp = app.scaleImage(app.heartsprite2, 1/10)
    app.mainmenu = True
    title = 'title.png'
    app.title2 = app.loadImage(title)
    app.title = app.scaleImage(app.title2, 4/5)
    play = 'play.png'
    app.play2 = app.loadImage(play)
    app.play = app.scaleImage(app.play2, 3/4)
    help = 'help.png'
    app.help2 = app.loadImage(help)
    app.help = app.scaleImage(app.help2, 3/4)
    app.enemyHelp = []
    app.enemycounter = 0
    helpenemy(app)
    app.showhelp = False
    app.layer = 0
    help1 = 'help1.png'
    app.help12 = app.loadImage(help1)
    app.help1 = app.scaleImage(app.help12, 1/2.5)
    space = 'space.png'
    app.space2 = app.loadImage(space)
    app.space = app.scaleImage(app.space2, 1/4)
    help2 = 'help2.png'
    app.help22 = app.loadImage(help2)
    app.help2 = app.scaleImage(app.help22, 1/5)
    help3 = 'help3.png'
    app.help32 = app.loadImage(help3)
    app.help3 = app.scaleImage(app.help32, 1/4.5)
    helpv2 = 'helpv2.png'
    app.helpv22 = app.loadImage(helpv2)
    app.helpv2 = app.scaleImage(app.helpv22, 1/4.5)
    speedtxt = 'speedtxt.png'
    app.speedtxt1 = app.loadImage(speedtxt)
    app.speedtxt = app.scaleImage(app.speedtxt1, 1/4)
    freezetxt = 'freezetxt.png'
    app.freezetxt1 = app.loadImage(freezetxt)
    app.freezetxt = app.scaleImage(app.freezetxt1, 1/4)
    hearttxt = 'hearttxt.png'
    app.hearttxt1 = app.loadImage(hearttxt)
    app.hearttxt = app.scaleImage(app.hearttxt1, 1/4)
    powerups = 'powerups.png'
    app.powerups1 = app.loadImage(powerups)
    app.powerups = app.scaleImage(app.powerups1, 1/2)
    exit = 'exit.png'
    app.exit1 = app.loadImage(exit)
    app.exit = app.scaleImage(app.exit1, 1/5)

# all picture text is from 'https://fontmeme.com/pixel-fonts/'
# all adventurer sprites from 'https://rvros.itch.io/animated-pixel-hero'

# loads idle and jumping animations
def idleAndJump(app):
    for i in range(4):
        file = f'adventurer-idle-0{i}.png'
        fileJump = f'adventurer-jump-0{i}.png'
        imgr = app.loadImage(file)
        img2r = app.scaleImage(imgr, 1.75)
        imgL = img2r.transpose(Image.FLIP_LEFT_RIGHT)
        imgJr = app.loadImage(fileJump)
        imgJ2r = app.scaleImage(imgJr, 1.75)
        imgJL = imgJ2r.transpose(Image.FLIP_LEFT_RIGHT)
        app.rightidleSprites.append(img2r)
        app.leftidleSprites.append(imgL)
        app.rightjumpSprites.append(imgJ2r)
        app.leftjumpSprites.append(imgJL)

# loads fall animation
def fall(app):
    for i in range(2):
        file = f'adventurer-fall-0{i}.png'
        imgr = app.loadImage(file)
        img2r = app.scaleImage(imgr, 1.75)
        imgL = img2r.transpose(Image.FLIP_LEFT_RIGHT)
        app.rightfallSprites.append(img2r)
        app.leftfallSprites.append(imgL)

# loads running animation
def run(app):
    for i in range(6):
        file = f'adventurer-run-0{i}.png'
        imgR = app.loadImage(file)
        img2R = app.scaleImage(imgR, 1.75)
        imgL = img2R.transpose(Image.FLIP_LEFT_RIGHT)
        app.rightrunSprites.append(img2R)
        app.leftrunSprites.append(imgL)

# code based on Images and PIL Mini Lecture
def enemy(app):
    enemy = 'WarriorRightWalk.png'
    spritestrip2 = app.loadImage(enemy)
    spritestrip = app.scaleImage(spritestrip2, 1.5)
    spritestripL = spritestrip.transpose(Image.FLIP_LEFT_RIGHT)
    imageWidth, imageHeight = spritestrip.size
    for i in range(9):
        x0 = i*imageWidth/8
        x1 = (i+1)*imageWidth/8
        x0L = (9-i)*imageWidth/8
        x1L = (8-i)*imageWidth/8
        sprite = spritestrip.crop((x0, 0, x1, imageHeight))
        spriteL = spritestripL.crop((x1L, 0, x0L, imageHeight))
        app.enemySpritesR.append(sprite)
        app.enemySpritesL.append(spriteL)
    app.enemySpritesR.pop()
    app.enemySpritesL.pop(0)

def helpenemy(app):
    enemy = 'WarriorRightWalk.png'
    spritestrip2 = app.loadImage(enemy)
    spritestrip = app.scaleImage(spritestrip2, 3.5)
    spritestripL = spritestrip.transpose(Image.FLIP_LEFT_RIGHT)
    imageWidth, imageHeight = spritestrip.size
    for i in range(9):
        x0L = (9-i)*imageWidth/8
        x1L = (8-i)*imageWidth/8
        spriteL = spritestripL.crop((x1L, 0, x0L, imageHeight))
        app.enemyHelp.append(spriteL)
    app.enemyHelp.pop(0)

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

# returns the bounds of freeze power
def freezepowerBounds(app):
    cx0, cy0 = (app.speedpowerX - app.speedpowerR+app.freezePowerRandomX*10, app.speedpowerY - 2*app.speedpowerR-app.freezePowerRandomY*10)
    cx1, cy1 = (app.speedpowerX + app.speedpowerR+app.freezePowerRandomX*10, app.speedpowerY-app.freezePowerRandomY*10)
    return (cx0, cy0, cx1, cy1)

# returns the bounds of heart power
def heartpowerBounds(app):
    cx0, cy0 = (app.speedpowerX - app.speedpowerR+app.heartPowerRandomX*10, app.speedpowerY - 2*app.speedpowerR-app.heartPowerRandomY*10)
    cx1, cy1 = (app.speedpowerX + app.speedpowerR+app.heartPowerRandomX*10, app.speedpowerY-app.heartPowerRandomY*10)
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
    while len(app.platformCells) < 6:
        x0 = random.randint(7, 27)
        x1 = x0+2
        y0 = random.randint(15, 80)
        y1 = y0+random.randint(8, 15)
        if len(app.platformCells) != 0 and platformIntersects(app, x0, x1, y0, y1):
            continue
        app.platformCells.append((x0, y0, x1, y1))

# checks if the randomized platform intersects with the latest platform added to the list
def platformIntersects(app, x0, x1, y0, y1):
    for platform in app.platformCells:
        if ((platform[0]-2 <= x0 <= platform[2]+2 or 
        platform[0]-2 <= x1 <= platform[2]+2)and 
        (platform[1]-7 <= y0 <= platform[3]+7 or
        platform[1]-7 <= y1 <= platform[3]+7)):
            return True
    return False

# returns the actual coordinates of the platforms from the cell bounds
def platformBoundsfromCell(app):
    for platform in app.platformCells:
        x0, y0, x1, y1 = platform
        app.platforms.append((y0*10, x0*10, y1*10, x1*10))

# randomizes positions of enemies
def randomizeEnemies(app):
    #randomizes positions of platform enemies
    while len(app.enemyCells) < 6:
        platform = random.randint(0, 5)
        if platform not in app.enemyOnPlatform:
            app.enemyOnPlatform.append(platform)
            x1 = app.platformCells[platform][0]
            x0 = x1-3
            y0 = app.platformCells[platform][1]
            y1 = y0+2
            app.enemyCells.append((x0, y0, x1, y1))
            app.enemyDict[(y0*10, x0*10, y1*10, x1*10)] = platform
            app.enemyDirection[(y0*10, x0*10, y1*10, x1*10)] = 1

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
        app.enemyMovement.append([y0*10, x0*10, y1*10, x1*10])

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

# randomizes position of freeze powerup
def randomizeFreeze(app):
    app.freezePowerRandomX = random.randint(8, 30)
    app.freezePowerRandomY = random.randint(5, 20)
    x0, y0, x1, y1 = freezepowerBounds(app)
    while itemIntersects(app, app.freezePowerRandomX, app.freezePowerRandomY) == True:
        randomizeFreeze(app)

# randomizes position of heart powerup
def randomizeHeart(app):
    app.heartPowerRandomX = random.randint(8, 30)
    app.heartPowerRandomY = random.randint(5, 20)
    x0, y0, x1, y1 = heartpowerBounds(app)
    while itemIntersects2(app, app.heartPowerRandomX, app.heartPowerRandomY) == True:
        randomizeHeart(app)

# checks if the heart powerup itersect with each other or any other object
def itemIntersects2(app, x, y):
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
    
    px0, pyo, px1, py1 = freezepowerBounds(app)
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
    

# randomzies all randomized objects
def randomizeAll(app):
    app.platformCells = []
    randomizePlatform(app)
    app.platforms = []
    platformBoundsfromCell(app)
    app.platforms.append(app.finalPlatform)
    app.platformColor = ['black'] * len(app.platforms)
    app.enemyCells = []
    app.enemyOnPlatform = []
    app.enemyDict = dict()
    app.enemyDirection = dict()
    randomizeEnemies(app)
    app.originalenemies = []
    app.modifiedenemies = []
    app.enemyMovement = []
    enemyBoundsFromCell(app)
    app.itemIntersection = True
    isValidPowerPosition(app)
    app.tppoweritems = []
    app.tppowerTouch = [False, False, False]
    randomizeTPItem(app)
    randomizeFreeze(app)
    randomizeHeart(app)

# checks if the level is solvable
def isSolvable3(app):
    while BFS(app) == False:
        randomizeAll(app)
        BFS(app)
    
# checks if all platforms are reachable from start to end using BFS
def BFS(app):
    queue = []
    queue.append(app.ground)
    platformDict = {}
    # adds all platforms to dict with respective counter set to 0
    for platform in app.platforms:
        platformDict[platform] = 0
    # loops through the queue and adds all children of current platform (children are all reachable platforms)
    while len(queue) != 0:
        current = queue.pop()
        # when final platform is reached, break out of queue
        if current == app.finalPlatform:
            break
        # obtains all children of current platform 
        nearPlatforms = platformPerim(app, current)
        # if no reachable platforms exists on the current platform, then level is not solvable
        if nearPlatforms == []:
            return False
        # orders platforms by x0 value
        newList = orderPlatform(app, nearPlatforms)
        # adds all reachable platforms to the queue if they have not been reached already
        for plat in newList:
            if platformDict[plat] == 0:
                queue.insert(0, plat)
                platformDict[plat] = 1
    # checks if any platforms have not been reached (part of winning condition)
    for plat in platformDict:
        if platformDict[plat] == 0:
            return False
    return True

# returns all reachable platforms of given platform
def platformPerim(app, platform):
    x0, y0, x1, y1 = platform
    L = []
    for plat in app.platforms:
        if ((plat[0]-160 <= x0 <= plat[2]+160 or plat[0]-180 <= x1 <= plat[2]+160)
        and plat[3]-120 <= y1 <= plat[3]+100):
            L.append(plat)
    return L

# non destructively orders the list of reachable platforms of current platform by x0 value
# this ensures that the last added platform in the queue is the final platform because it has the furthermost x0 value
def orderPlatform(app, L):
    orderL = copy.deepcopy(L)
    # employing bubble sort to sort the list of platform tuples
    for i in range(len(orderL)):
        for j in range(len(orderL)-1):
            if orderL[j][0] > orderL[j+1][0]:
                sortTuple = orderL[j]
                orderL[j] = orderL[j+1]
                orderL[j+1] = sortTuple
    return orderL

# checks if the player and platform intersect
def boundsIntersect(app, player, platform):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = platform
    # the reason for the 0 to 5 bounds because the incrementing of the jump animation
    # does not evenly match with the bounds of platforms
    return (0 <= dy1-py0 < 8) and (px0 <= (dx1+dx0)/2+app.scrollX <= px1)
    
# checks if the enemy has collided with the player
def enemyHitPlayer(app, player, enemy):
    (dx0, dy0, dx1, dy1) = player
    (px0, py0, px1, py1) = enemy
    return (dx1 > px0) and (dx0 < px1) and (py1 <= dy1) and (py0 >= dy0)

# checks if the player is on ground
def touchGround(app, player):
    (dx0, dy0, dx1, dy1) = player
    return 0 <= dy1 - app.ground[1] < 5 and app.ground[0] <= (dx1+dx0)/2+app.scrollX <= app.ground[2]

# checks if final platform is touched
def touchFinal(app, player):
    (dx0, dy0, dx1, dy1) = player
    return 0 <= dy1 - app.finalPlatform[1] < 5 and app.finalPlatform[0] <= (dx1+dx0)/2+app.scrollX <= app.finalPlatform[2]

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

def mousePressed(app, event):
    # if player hits 'play' main menu disappears
    if 60 <= event.x <= 240 and 150 <= event.y <= 250:
        app.mainmenu = False
    # if player hits 'help' then instructions appear
    if 360 <= event.x <= 540 and 150 <= event.y <= 250:
        app.mainmenu = False
        app.layer = 0
        app.showhelp = True

def keyPressed(app, event):
    # allows player to restart if hit by enemy
    if app.playerDied and event.key == 'r':
        appStarted(app)
    
    # allows player to continue playing after beating a level
    if app.isGameOver and event.key == 'c':
        appStarted(app)
        app.mainmenu = False
        app.level+=1
    
    # allows player to play again
    if app.isGameOver and app.level == 2 and event.key == 'r':
        appStarted(app)
    
    # flips though instruction screens
    if app.showhelp and event.key == 'Space':
        app.layer += 1
    
    # after the last instruction page, return to main menu
    if app.showhelp == True and app.layer > 3:
        app.mainmenu = True
        app.showhelp = False

    #if app.speedpowerTouch == False and touchSpeed(app, playerBounds(app), speedpowerBounds(app)):

    # grants the power of teleportation to player if three purple items are collected
    if app.tppowerTouch == [True, True, True] and app.tppower == False:
        app.scrollSpeed = 10
        app.tppower = True
        app.playerColor = 'purple'

    # moves player when player is at center
    if not app.isGameOver and isPlayerCenter(app) and not app.playerDied:
        if event.key == 'Left':
            app.spriteDirection = -1
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
                app.spriteX -= app.scrollSpeed
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
            app.spriteDirection = 1
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
                app.spriteX += app.scrollSpeed
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
        elif event.key == 'r' and app.tppowerTouch == [True, True, True]:
            app.playerY -= 112
            app.spriteY -= 112
            app.scrollX += 50
            app.gameMargin += 50
            app.speedpowerX -= 50
            for enemy in range(len(app.modifiedenemies)):
                app.modifiedenemies[enemy][0] -= 50
                app.modifiedenemies[enemy][2] -= 50
        elif event.key == 'Space' and app.mainmenu == False and app.showhelp == False:
            app.playerTimer = 28
            app.paused = True
    

    # Moves player if player is not at center
    elif not app.isGameOver and not app.playerDied:
        if event.key == 'Left':
            app.spriteDirection = -1
            #app.gameTimer += 10
            app.playerScrollX -= app.scrollSpeed
            app.playerX -= app.scrollSpeed
            app.spriteX -= app.scrollSpeed
            if app.playerScrollX <= 0:
                app.playerX += app.scrollSpeed
                app.spriteX += app.scrollSpeed
                app.playerScrollX += app.scrollSpeed
        elif event.key == 'Right':
            app.spriteDirection = 1
            playerBound = playerBounds(app)
            #app.gameTimer += 10
            app.playerScrollX += app.scrollSpeed
            app.playerX += app.scrollSpeed
            app.spriteX += app.scrollSpeed
            # ends game if they reached the final platform and retrieved all three tp items
            if (app.playerScrollX >= app.width/1.15 and touchFinal(app, playerBound) and 
            app.tppowerTouch == [True, True, True] and 
            app.platformColor == ['blue']*len(app.platforms)):
                app.playerX -= app.scrollSpeed
                app.spriteX -= app.scrollSpeed
                app.playerScrollX -= app.scrollSpeed
                app.isGameOver = True
        # if teleportation power is consumed, space activates teleporting
        elif event.key == 'r' and app.tppowerTouch == [True, True, True]:
            app.playerY -= 112
            app.spriteY -= 112
            app.playerX += 50
            app.spriteX += 50
            app.playerScrollX += 50
            #app.paused = True
        elif event.key == 'Space' and app.mainmenu == False and app.showhelp == False:
            app.playerTimer = 28
            app.paused = True
        

# check if the player is currently on any platform
def isPlayerOnAnyPlatform(app, player):
    for platform in app.platforms:
        if boundsIntersect(app, player, platform):
            return True
    return False

def timerFired(app):
    app.gameTimer += 1

    # adapted from course notes (animation part 4)
    app.rightidleCounter = (1+app.rightidleCounter) % len(app.rightidleSprites)
    app.leftidleCounter = (1+app.leftidleCounter) % len(app.leftidleSprites)
    app.rightrunCounter = (1+app.rightrunCounter) % len(app.rightrunSprites)
    app.leftrunCounter = (1+app.leftrunCounter) % len(app.leftrunSprites)
    app.leftEnemy = (1 + app.leftEnemy) % len(app.enemySpritesL)
    app.rightEnemy = (1 + app.rightEnemy) % len(app.enemySpritesR)
    app.enemycounter = (1+app.enemycounter) % len(app.enemyHelp)

    # increases speed if the player consumes speed powerup
    if app.speedpowerTouch == False and touchSpeed(app, playerBounds(app), speedpowerBounds(app)):
        app.scrollSpeed = 20
        app.speedpowerTouch = True
        app.playerColor = 'blue'
        app.timeTouched = app.gameTimer # keeps track of the time when speed powre is consumed

    # cancels speed powerup after a certain amount of time
    if app.speedpowerTouch and app.gameTimer > app.timeTouched + 30:
        app.playerColor = 'red'
        app.scrollSpeed = 10
    # freezes enemies once powerup is consumed
    if app.freezepowerTouch == False and touchSpeed(app, playerBounds(app), freezepowerBounds(app)):
        app.freezepowerTouch = True
        app.freezeTime = app.gameTimer
        app.playerColor = 'white'
        app.enemyFreeze = True
    
    # cancels the freeze on enemies after a certain amount of time
    if app.freezepowerTouch and app.gameTimer > app.freezeTime + 30:
        app.enemyFreeze = False
        app.playerColor = 'red'

    # Grants player extra life once consumed
    if app.heartpowerTouch == False and touchSpeed(app, playerBounds(app), heartpowerBounds(app)):
        app.heartpowerTouch = True
        app.lives += 1

    # checks all the items to see if they have been touched
    for item in range(len(app.tppoweritems)):
        if touchTP(app, playerBounds(app), tppowerBounds(app,item)):
            app.tppowerTouch[item] = True

    # initiates enemy movement
    for enemy in range(len(app.modifiedenemies)):
        if not app.playerDied and app.enemyFreeze == False:
            enemyStep(app, enemy)
        # checks if enemy has hit player
        if enemyHitPlayer(app, playerBounds(app), app.modifiedenemies[enemy]):
            # if player has consumed heart powerup, then the enemy that hit player disappears
            if app.lives > 0:
                app.lives -= 1
                app.modifiedenemies[enemy] = [500, 500, 500, 500]
            # otherwise, player dies
            elif app.lives == 0:
                app.playerDied = True 

    # turns platforms blue once stepped on
    for platform in range(len(app.platforms)):
        if boundsIntersect(app, playerBounds(app), platformBounds(app, platform)):
            app.platformColor[platform] = 'blue'

    # initiates jump animation if app.paused = true
    if app.paused:
        doStep(app)

    # if player on ground
    # if yes, return
    # if player on platform, stop jump animation
    # otherwise continue jump animation
    playerBound = playerBounds(app)
    if touchGround(app, playerBound):
        app.peak = False
        app.paused = False
        return
    if touchFinal(app, playerBound):
        app.peak = False
        app.paused = False
        return
    
    if playerBound[1] >= app.height:
        app.playerDied = True
    
    # if player is on a platform, paused = False i.e. stop jumping
    if isPlayerOnAnyPlatform(app, playerBound):
        app.peak = False
        app.paused = False
        return

    # if paused = false and player is in air i.e. not on ground or platform, move down
    if not app.paused:
        downStep(app)
    

# Player jumps after space is pressed
def doStep(app):
    playerBound = playerBounds(app)
    if app.playerTimer >= 0:
        app.playerY -= app.playerTimer
        app.spriteY -= app.playerTimer
        app.playerTimer -= 4
        app.leftjumpCounter = (1+app.leftjumpCounter) % len(app.leftjumpSprites)
        app.rightjumpCounter = (1+app.rightjumpCounter) % len(app.rightjumpSprites)
    elif not touchGround(app, playerBound):
            app.peak = True
            app.playerY += 8
            app.spriteY += 8
            app.leftfallCounter = (1+app.leftfallCounter) % len(app.leftfallSprites)
            app.rightfallCounter = (1+app.rightfallCounter) % len(app.rightfallSprites)
       
# Player falls if not standing on a surface
def downStep(app):
    playerBound = playerBounds(app)
    if not touchGround(app, playerBound):
        app.peak = True
        app.playerY += 8
        app.spriteY += 8
        app.leftfallCounter = (1+app.leftfallCounter) % len(app.leftfallSprites)
        app.rightfallCounter = (1+app.rightfallCounter) % len(app.rightfallSprites)

# checks if the given enemy is a platform enemy
def isEnemyOnAnyPlatform2(app, enemy):
    if app.originalenemies[enemy] not in app.enemyDict:
        return False
    return True

# for given enemy, check if that enemy is on any platform
# if so, then we proceed
# retrieve the platform that the enemy is currently on 

# moves enemy
def enemyStep(app, enemy):
    if not isEnemyOnAnyPlatform2(app, enemy):
        return
    direction = app.enemyDirection[app.originalenemies[enemy]]
    platform = app.enemyDict[app.originalenemies[enemy]]
    platformBound = platformBounds(app, platform)
    # we check enemyMovement here because modifiedenemies is changing due to side scrolling
    if app.enemyMovement[enemy][2] == platformBound[2]:
        direction = -2
        app.enemyDirection[app.originalenemies[enemy]] = -2
    if app.enemyMovement[enemy][0] == platformBound[0]:
        direction = 2
        app.enemyDirection[app.originalenemies[enemy]] = 2
    app.enemyMovement[enemy][0] += direction
    app.enemyMovement[enemy][2] += direction
    app.modifiedenemies[enemy][0] += direction
    app.modifiedenemies[enemy][2] += direction
        
def redrawAll(app, canvas):
    if app.mainmenu == False and app.showhelp == False:
        # Basic ground level
        canvas.create_rectangle(0-app.scrollX, app.height-app.height/10, 150-app.scrollX, app.height, fill='green', outline='black')

        # draws background image
        # image comes from 'https://stock.adobe.com/search?k=pixel+city'
        canvas.create_image(app.width/2, app.height/1.8, image=ImageTk.PhotoImage(app.background))
            
        # draws all the randomized platforms
        count = 0
        for platform in app.platformCells:
            row0, col0, row1, col1 = platform
            for row in range(row0, row1):
                for col in range(col0, col1):
                    (x0, y0, x1, y1) = getCellBounds(app, row, col)
                    canvas.create_rectangle(x0-app.scrollX, y0, x1-app.scrollX, y1, outline='purple', fill=app.platformColor[count])
            count += 1

        # draws image for the ground platform
        # image comes from 'http://pixelartmaker.com/art/8a5f786d108adca'
        canvas.create_image(75-app.scrollX, 285, image=ImageTk.PhotoImage(app.platform))
        canvas.create_image(90-app.scrollX, 285, image=ImageTk.PhotoImage(app.platform))

        # Final platform to end game
        # turns blue and player is able to escape once all conditions are complete
        solution = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'black']
        if app.platformColor == solution and app.tppowerTouch == [True, True, True]:
            canvas.create_rectangle(app.width/2+app.width-app.scrollX, app.height-app.height/10,
                                    app.width/1.5+app.width-app.scrollX, app.height-app.height/10+20, fill='blue', outline='black')
        
        # otherwise the final platform is 'locked' at red
        else:
            canvas.create_rectangle(app.width/2+app.width-app.scrollX, app.height-app.height/10,
                                    app.width/1.5+app.width-app.scrollX, app.height-app.height/10+20, fill='red', outline='black')
        
        # draws final teleporter image 
        # image comes from 'https://starbounder.org/Teleporters'
        canvas.create_image(950-app.scrollX, 190, image=ImageTk.PhotoImage(app.finalTP))

        # Drawing randomized enemies
        # enemy image from 'https://foozlecc.itch.io/lucifer-4-direction-warrior-pixel-art-free'
        for enemy in range(len(app.modifiedenemies)):
            ex0, ey0, ex1, ey1 = enemyBounds(app, enemy)
            #canvas.create_rectangle(ex0, ey0, ex1, ey1, fill='yellow', outline='black')
            if app.enemyDirection[app.originalenemies[enemy]] == 2:
                enemyR = app.enemySpritesR[app.rightEnemy]
                canvas.create_image((ex0+ex1)/2, (ey0+ey1)/2, image=ImageTk.PhotoImage(enemyR))
            else:
                enemyL = app.enemySpritesL[app.leftEnemy]
                canvas.create_image((ex0+ex1)/2, (ey0+ey1)/2, image=ImageTk.PhotoImage(enemyL))

        # Drawing PowerUps/Items

        # Blue is speed
        if app.itemIntersection == False and app.speedpowerTouch == False: 
            px0, py0, px1, py1 = speedpowerBounds(app)
            canvas.create_oval(px0, py0, px1, py1, fill='blue', outline='white')
            # powerup image from 'https://www.pinclipart.com/maxpin/iRoxwRJ/'
            canvas.create_image((px0+px1)/2, (py0+py1)/2, image=ImageTk.PhotoImage(app.speedsprite))

        # White is freeze
        if app.freezepowerTouch == False :
            fx0, fy0, fx1, fy1 = freezepowerBounds(app)
            canvas.create_oval(fx0, fy0, fx1, fy1, fill='white')
            # powerup image from 'http://pixelartmaker.com/art/d6e55b4f17d7d6a'
            canvas.create_image((fx0+fx1)/2, (fy0+fy1)/2, image=ImageTk.PhotoImage(app.freezesprite))

        # Red is heart
        if app.heartpowerTouch == False :
            hx0, hy0, hx1, hy1 = heartpowerBounds(app)
            canvas.create_oval(hx0, hy0, hx1, hy1, fill='red')
            # heart image from 'https://shop.bitgem3d.com/products/pixel-hearts'
            canvas.create_image((hx0+hx1)/2, (hy0+hy1)/2, image=ImageTk.PhotoImage(app.heartsprite))

        # Purple is are items to repair teleportation machine i.e. teleports player up and slightly forward
        for item in range(len(app.tppoweritems)):
            if app.tppowerTouch[item] == False and app.tppower == False:
                tx0, ty0, tx1, ty1 = tppowerBounds(app, item) 
                #canvas.create_oval(tx0, ty0, tx1, ty1, fill='purple', outline='white')
                # tp item image from 'https://frackinuniverse.fandom.com/wiki/Copper_Cog'
                canvas.create_image((tx0+tx1)/2, (ty0+ty1)/2, image=ImageTk.PhotoImage(app.tpSprite))

        # Animations for player
        if app.spriteDirection == 0:
            rightIdle = app.rightidleSprites[app.rightidleCounter]
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(rightIdle))
        elif app.spriteDirection == 1 and app.playerDied == True:
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(app.img2R))
        elif app.spriteDirection == -1 and app.playerDied == True:
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(app.imgL))
        elif app.spriteDirection == 1 and app.peak == True:
            rightFall = app.rightfallSprites[app.rightfallCounter]
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(rightFall))
        elif app.spriteDirection == 1 and app.paused == True:
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(app.rightjumpSprites[2]))
        elif app.spriteDirection == -1 and app.peak == True:
            leftFall = app.leftfallSprites[app.leftfallCounter]
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(leftFall))
        elif app.spriteDirection == -1 and app.paused == True:
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(app.leftjumpSprites[2]))
        elif app.spriteDirection == 1:
            rightRun = app.rightrunSprites[app.rightrunCounter]
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(rightRun))
        elif app.spriteDirection == -1:
            leftRun = app.leftrunSprites[app.leftrunCounter]
            canvas.create_image(30+app.spriteX, 240+app.spriteY, image=ImageTk.PhotoImage(leftRun))
        
        # Game started text
        if app.gameTimer <= 10:
            canvas.create_text(app.width/2, app.height/5, text='Level Start!', font='Helvetica 25 bold', fill='white')
        
        # Level Complete text
        if app.isGameOver and app.level != 2:
            canvas.create_text(app.width/2, app.height/5, text='Level Complete!', font='Helvetica 25 bold', fill='white')
            canvas.create_text(app.width/2, app.height/3, text="Press 'C' to continue!", font='Helvetica 25 bold', fill='white')
        
        # Game Beaten text
        if app.level == 2 and app.isGameOver:
            canvas.create_text(app.width/2, app.height/5, text='You have Escaped!', font='Helvetica 25 bold', fill='white')
            canvas.create_text(app.width/2, app.height/3, text="Press 'R' to play again!", font='Helvetica 25 bold', fill='white')

        # Player Death text
        if app.playerDied:
            canvas.create_text(app.width/2, app.height/5, text='Game Over!', font='Helvetica 25 bold', fill='white')
            canvas.create_text(app.width/2, app.height/3, text="Press 'R' to restart!", font='Helvetica 25 bold', fill='white')

    # draws main menu screen
    if app.mainmenu == True:
        canvas.create_image(app.width/2, app.height/1.8, image=ImageTk.PhotoImage(app.background))
        canvas.create_image(app.width/2, app.height/4, image=ImageTk.PhotoImage(app.title))
        canvas.create_image(app.width/4, app.height/1.5, image=ImageTk.PhotoImage(app.play))
        canvas.create_rectangle(60, 150, 240, 250, outline='purple')
        canvas.create_image(app.width*(3/4), app.height/1.5, image=ImageTk.PhotoImage(app.help))
        canvas.create_rectangle(360, 150, 540, 250, outline='purple')
    
    # draws instructions
    if app.showhelp == True and app.layer == 0:
        canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
        canvas.create_rectangle(app.width*1/3, 25, app.width*2/3, app.height/1.75, outline='purple', width=3)
        enemyhelp = app.enemyHelp[app.enemycounter]
        canvas.create_image(app.width/2, app.height/3.25, image=ImageTk.PhotoImage(enemyhelp))
        canvas.create_image(app.width/2, app.height/1.5, image=ImageTk.PhotoImage(app.help1))
        canvas.create_image(app.width/2, app.height/1.25, image=ImageTk.PhotoImage(app.space))
    elif app.showhelp == True and app.layer == 1:
        canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
        canvas.create_rectangle(app.width*1/3, 25, app.width*2/3, app.height/1.75, outline='purple', width=3)
        canvas.create_image(app.width/2, app.height/3.25, image=ImageTk.PhotoImage(app.tpHelp))
        canvas.create_image(app.width/2, app.height/1.5, image=ImageTk.PhotoImage(app.help2))
        canvas.create_image(app.width/2, app.height/1.25, image=ImageTk.PhotoImage(app.space))
    elif app.showhelp == True and app.layer == 2:
        canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
        canvas.create_rectangle(app.width*1/3, 25, app.width*2/3, app.height/1.75, outline='purple', width=3)
        canvas.create_image(app.width/2, app.height/3.25, image=ImageTk.PhotoImage(app.finalTPhelp))    
        canvas.create_image(app.width/2, app.height/1.5, image=ImageTk.PhotoImage(app.help3))
        canvas.create_image(app.width/2, app.height/1.35, image=ImageTk.PhotoImage(app.helpv2))
        canvas.create_image(app.width/2, app.height/1.15, image=ImageTk.PhotoImage(app.space))
    elif app.showhelp == True and app.layer == 3:
        canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
        canvas.create_image(app.width/6, app.height/3, image=ImageTk.PhotoImage(app.speedHelp))
        canvas.create_image(app.width/1.75, app.height/3, image=ImageTk.PhotoImage(app.speedtxt))
        canvas.create_image(app.width/6, app.height/1.75, image=ImageTk.PhotoImage(app.freezeHelp))
        canvas.create_image(app.width/1.85, app.height/1.75, image=ImageTk.PhotoImage(app.freezetxt))
        canvas.create_image(app.width/6, app.height/1.25, image=ImageTk.PhotoImage(app.heartHelp))
        canvas.create_image(app.width/2, app.height/1.25, image=ImageTk.PhotoImage(app.hearttxt))
        canvas.create_image(app.width/2, app.height/6, image=ImageTk.PhotoImage(app.powerups))
        canvas.create_image(app.width/2, app.height/1.1, image=ImageTk.PhotoImage(app.exit))
       
runApp(width=600, height=300) 
