from cmu_112_graphics import *
import random

# Ideas about generating levels
    # creating grid to place platforms
    # floor height remains constant
    # randomize lengths of floor sections? so that there are pit falls
    # app width and height are constant (for now)
    # width=600, height=300

# floor height = 270 (27th row cell)

# have to calculate grid size i.e. length and width of each grid cell

# platform ideas
    # for now, spawn max 5 platforms
    # when spawning platforms, must be <= 270 (floor height) (27th row)
    # platforms cannot intersect
    # platforms shouldn't be exactly at the top or exactly at the floor level
    # generate random lengths for platforms 
    # limit to number of platforms?
    # platform height = 20 (2 cells)
    # platform width shold vary (can't be less than 50 (5 cells), but should be less than 150 (15 cells))

# in the actual game file, max level x distance is 1200, so platform columns should be limited to <= 108 cells

# enemy ideas
    # max enemies will be 6 for now
    # enemy rows = 4
    # enemy cols = 2

def appStarted(app):
    app.rows = app.height//10
    app.cols = app.width//10
    app.platformCells = [] 
    randomizePlatform(app)
    app.enemyCells = []
    app.enemyOnPlatform = []
    randomizeEnemies(app)
    app.speedpowerX = app.width/6
    app.speedpowerY = app.height-app.height/10
    app.speedpowerR = 10
    app.speedPowerRandomX = 0
    app.speedPowerRandomY = 0
    app.itemIntersection = True
    randomizeSpeedPower(app)
    app.tppoweritems = []

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
        x0 = random.randint(7, 20)
        x1 = x0+2
        y0 = random.randint(8, 45)
        y1 = y0+random.randint(5, 15)
        print(x0, y0, x1, y1, app.platformCells)
        if len(app.platformCells) != 0 and platformIntersects(app, x0, x1, y0, y1):
            continue
        app.platformCells.append((x0, y0, x1, y1))

# checks if the randomized platform intersects with the latest platform added to the list
def platformIntersects(app, x0, x1, y0, y1):
    if (app.platformCells[-1][0] < x0 < app.platformCells[-1][2] or 
        app.platformCells[-1][0] < x1 < app.platformCells[-1][2]):
        return True
    # if (app.platforms[-1][1] <= y0 < (app.platforms[-1][3]+3) or 
    #     (y1+3) > app.platforms[-1][1]):
    #     return True
    return False

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
    
    #randomizes positions of ground enemies
    while 3 <= len(app.enemyCells) < 6:
        x1 = 27
        x0 = x1-3
        y0 = random.randint(5, 57)
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
            if app.enemyCells[enemy][1] < y0 < app.enemyCells[enemy][3]+2 or app.enemyCells[enemy][1]-2 < y1 < app.enemyCells[enemy][3]:
                return True
    return False

# randomizes positional values for speed power up
def randomizeSpeedPower(app):
    app.speedPowerRandomX = random.randint(8, 30)
    app.speedPowerRandomY = random.randint(5, 20)

# checks if the randomly generated position of the item is valid
# def isValidItemPosition(app):
#     while app.itemIntersection:
#         randomizeSpeedPower(app)
#         if itemsIntersect(app):
#             continue
#         app.itemIntersection = False

# def itemsIntersect(app):
#     x0 = app.speedpowerX - app.speedpowerR+app.speedPowerRandomX*10
#     x1 = app.speedpowerX + app.speedpowerR+app.speedPowerRandomX*10
#     y0 = app.speedpowerY - 2*app.speedpowerR-app.speedPowerRandomY*10
#     y1 = app.speedpowerY-app.speedPowerRandomY*10

# randomizes positions of the 3 tp items
def randomizeTPItem(app):
    while len(app.tppoweritems) < 3:
        x = random.randint(8, 50)
        y = random.randint(5, 20)
        if len(app.tppoweritems) != 0 and not itemIntersects(app, x, y):
            continue
        app.tppoweritems.append([app.speedpowerX - app.speedpowerR+x*10, app.speedpowerY - 2*app.speedpowerR - y*10,
                                 app.speedpowerX + app.speedpowerR+x*10, app.speedpowerY - y*10])


# def randomizeTPItem(app):
#     while len(app.tppoweritems) < 3:
#         platform = random.randint(0, 5)
#         if platform in app.enemyOnPlatform:
#             continue
#         elif platform not in app.tppowerOnPlatform:
#             app.tppowerOnPlatform.append(platform)
#             x = (app.platformCells[platform][0] + app.platformCells[platform][2])/2
#             y = app.platformCells[platform][1] + 20
#             if len(app.tppoweritems) != 0 and itemIntersects(app, x, y):
#                 continue
#             app.tppoweritems.append([app.speedpowerX - app.speedpowerR+x*10, app.speedpowerY - 2*app.speedpowerR - y*10,
#                                      app.speedpowerX + app.speedpowerR+x*10, app.speedpowerY - y*10])

#     for platform in range(len(app.platforms)):
#         if platform not in app.enemyOnPlatform:
#             x = (app.platformCells[platform][0] + app.platformCells[platform][2])/2
#             y = app.platformCells[platform][1] - 20
#             if len(app.tppoweritems) != 0 and itemIntersects(app, x, y):
#                 continue
#             app.tppoweritems.append([app.speedpowerX - app.speedpowerR+x*10, app.speedpowerY - 2*app.speedpowerR - y*10,
#                                     app.speedpowerX + app.speedpowerR+x*10, app.speedpowerY - y*10])

# checks if the tp items itersect with each other or any other object
def itemIntersects(app, x, y):
    return

def backtracking(app, L):
    # must copy platform list into another list to non destructively modify platform list
    if len(L) == 0:
        return True
    else:
        for platform in L:
            # check if its the lowest platform and only has 1 surrounding platorm
            #solution = backtracking(app, L)
            print(platform, L)
            if platform[1] == findLowestPlatform(app): 
                if checkPlatformPerim(app, platform) == 1:
                    L.remove(platform)
                    solution = backtracking(app, L)
                    if solution != False:
                        return True
                    L.append(platform)
            else:
                if checkPlatformPerim(app, platform) == 2:
                    L.remove(platform)
                    solution = backtracking(app, L)
                    if solution != False:
                        return True
                    L.append(platform)
        return False


def BFS(app):
    queue = []
    queue.append(app.ground)
    count = 0
    while len(queue) != 0:
        current = queue.pop()
        if current == app.finalPlatform and count == len(app.platforms)-1:
            return True
        nearPlatforms = platformPerim(app, current)
        if nearPlatforms == []:
            return False
        newList = orderPlatform(app, nearPlatforms)
        for plat in newList:
            queue.insert(plat)
            count += 1
    return False

def platformPerim(app, platform):
    x0, y0, x1, y1 = platform
    L = []
    for plat in app.platforms:
        if ((plat[0]-200 <= x0 <= plat[2]+200 or plat[0]-200 <= x1 <= plat[2]+200)
        and plat[3]-132 <= x0 <= plat[3]+112):
            L.append(plat)
    return L

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
    

# check 
def checkPlatformPerim(app, platform):
    x0, y0, x1, y1 = platform
    count = 0
    for plat in app.platforms:
        if ((plat[0]-200 <= x0 <= plat[2]+200 or plat[0]-200 <= x1 <= plat[2]+200)
        and plat[3]-132 <= x0 <= plat[3]+112):
            count += 1
    return count
    


def findLowestPlatform(app):
    minimumPlat = -10000
    for platform in app.platforms:
        if platform[1] > minimumPlat:
            minimumPlat = platform[1]
    return minimumPlat

def redrawAll(app, canvas):
    # Drawing grid
    # for row in range(app.rows):
    #     for col in range(app.cols):
    #         (x0, y0, x1, y1) = getCellBounds(app, row, col)
    #         canvas.create_rectangle(x0, y0, x1, y1, outline='black')

    # drawing the floor with cells
    for row in range(27, 30):
        for col in range(60):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, outline='green', fill='green')

   # draws all the randomized platforms
    for platform in app.platformCells:
        row0, col0, row1, col1 = platform
        for row in range(row0, row1):
            for col in range(col0, col1):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, outline='red', fill='black')
    
    # Drawing randomized enemies
    for enemy in app.enemyCells:
        row0, col0, row1, col1 = enemy
        for row in range(row0, row1):
            for col in range(col0, col1):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='yellow')

    # canvas.create_oval(app.speedpowerX - app.speedpowerR+app.speedPowerRandomX*10, app.speedpowerY - 2*app.speedpowerR-app.speedPowerRandomY*10, 
    #               app.speedpowerX + app.speedpowerR+app.speedPowerRandomX*10, app.speedpowerY-app.speedPowerRandomY*10, fill='blue')
    canvas.create_oval(app.speedpowerX - app.speedpowerR, app.speedpowerY - 2*app.speedpowerR-50, 
                  app.speedpowerX + app.speedpowerR, app.speedpowerY-50, fill='blue')
    canvas.create_rectangle(app.speedpowerX - app.speedpowerR, app.speedpowerY - 2*app.speedpowerR-50, 
                            app.speedpowerX + app.speedpowerR, app.speedpowerY-50, outline='red')

    canvas.create_oval(app.speedpowerX - app.speedpowerR, app.speedpowerY - 2*app.speedpowerR, app.speedpowerX + app.speedpowerR, app.speedpowerY, fill='purple')
runApp(width=600, height=300)