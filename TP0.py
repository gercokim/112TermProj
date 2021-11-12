from cmu_112_graphics import *

def redrawAll(app, canvas):
    # Basic map with platforms
    canvas.create_rectangle(0, app.height-app.height/10, app.width, app.height, 
                            fill='green', outline='black')
    canvas.create_rectangle(app.width/1.5+1.5*app.width/10, app.height/2.25, 
                            app.width/2+1.5*app.width/10, app.height/2, 
                            fill='black', outline='black')
    canvas.create_rectangle(app.width/1.5-app.width/5, app.height/2.25+app.height/5, 
                            app.width/2-app.width/5, app.height/2+app.height/5, 
                            fill='black', outline='black')


runApp(width=600, height=300) 