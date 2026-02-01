#Welcome to 3D-game!!
#Move around with arrow keys, up and down to move, left and right to rotate
#Press "k" to stop

import time
import turtle
import math
import keyboard

rayDis = []
screenW = 1300
screenH = 1000
playerX = 2
playerY = 2
playerHeading = 0
s = 0.001
rayS = 0.001
desiredPlayerY = playerY
desiredPlayerX = playerX

turtle.clear()
turtle.setup(width=screenW, height=screenH)
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(1)
turtle.tracer(0)
turtle.penup()

#The map to generate 1 is a wall and 0 is nothing

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#Function to help draw map

def Square():
    turtle.penup()
    turtle.goto(turtle.xcor() + 25, turtle.ycor() + 25)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.begin_fill()
    for n in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

#Raycast function

def SendRay(x, y, heading):
    desiredRayX = 0
    desiredRayY = 0
    rayX = x
    rayY = y
    rayHeading = heading
    while True:
        if 0 < rayHeading <= 90:
            desiredRayY = -math.degrees(math.sin(math.radians(90 - abs(rayHeading)))) * rayS
            desiredRayX = math.degrees(math.cos(math.radians(90 - abs(rayHeading)))) * rayS
        elif 90 < rayHeading <= 180:
            desiredRayY = math.degrees(math.cos(math.radians(180 - abs(rayHeading)))) * rayS
            desiredRayX = math.degrees(math.sin(math.radians(180 - abs(rayHeading)))) * rayS
        elif -180 < rayHeading <= -90:
            desiredRayY = math.degrees(math.cos(math.radians(180 - abs(rayHeading)))) * rayS
            desiredRayX = -math.degrees(math.sin(math.radians(180 - abs(rayHeading)))) * rayS
        elif -90 < rayHeading <= 0:
            desiredRayY = -math.degrees(math.sin(math.radians(90 - abs(rayHeading)))) * rayS
            desiredRayX = -math.degrees(math.cos(math.radians(90 - abs(rayHeading)))) * rayS
        if map[round(rayY + desiredRayY)][round(rayX)] == 0 and map[round(rayY)][round(rayX + desiredRayX)] == 0:
            rayY += desiredRayY
            rayX += desiredRayX
        else:
            break
    rayDis.append(math.sqrt((rayX - x)**2 + (rayY - y)**2))

#Collision detection functions for the player

def CollisionDetX(desX, desY):
    if map[round(playerY)][round(playerX + desX)] == 0:
        return desX
    return 0
    
def CollisionDetY(desX, desY):
    if map[round(playerY + desY)][round(playerX)] == 0:
        return desY
    return 0

def DrawLine(index, dis):
    if dis != 0:
        size = 1000/dis
    else:
        size = 100
    turtle.penup()
    turtle.setheading(90)
    turtle.goto((index * 2 - screenW//10)*5 + 5, -size/2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()


#Main loop, will sleep for 0.05 seconds to reduce lag

while True:
    turtle.clear()

    #Rotation
    if keyboard.is_pressed("left arrow"):
        playerHeading -= 10
    if keyboard.is_pressed("right arrow"):
        playerHeading += 10
    
    if playerHeading > 180:
        playerHeading -= 360
    elif playerHeading <= -180:
        playerHeading += 360

    #Movement
    if keyboard.is_pressed("up arrow"):
        if 0 < playerHeading <= 90:
            desiredPlayerY = -math.degrees(math.sin(math.radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = math.degrees(math.cos(math.radians(90 - abs(playerHeading)))) * s
        elif 90 < playerHeading <= 180:
            desiredPlayerY = math.degrees(math.cos(math.radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = math.degrees(math.sin(math.radians(180 - abs(playerHeading)))) * s
        elif -180 < playerHeading <= -90:
            desiredPlayerY = math.degrees(math.cos(math.radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = -math.degrees(math.sin(math.radians(180 - abs(playerHeading)))) * s
        elif -90 < playerHeading <= 0:
            desiredPlayerY = -math.degrees(math.sin(math.radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = -math.degrees(math.cos(math.radians(90 - abs(playerHeading)))) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)
    elif keyboard.is_pressed("down arrow"):
        if 0 < playerHeading <= 90:
            desiredPlayerY = math.degrees(math.sin(math.radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = -math.degrees(math.cos(math.radians(90 - abs(playerHeading)))) * s
        elif 90 < playerHeading <= 180:
            desiredPlayerY = -math.degrees(math.cos(math.radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = -math.degrees(math.sin(math.radians(180 - abs(playerHeading)))) * s
        elif -180 < playerHeading <= -90:
            desiredPlayerY = -math.degrees(math.cos(math.radians(180 - abs(playerHeading)))) * s
            desiredPlayerX = math.degrees(math.sin(math.radians(180 - abs(playerHeading)))) * s
        elif -90 < playerHeading <= 0:
            desiredPlayerY = math.degrees(math.sin(math.radians(90 - abs(playerHeading)))) * s
            desiredPlayerX = math.degrees(math.cos(math.radians(90 - abs(playerHeading)))) * s
        playerX += CollisionDetX(desiredPlayerX, desiredPlayerY)
        playerY += CollisionDetY(desiredPlayerX, desiredPlayerY)

    #Stop script

    if keyboard.is_pressed("k"):
        exit()
        break

    rayDis.clear()
    #Send the rays and draw them
    for n in range (-screenW // 20, screenW // 20 + 1):
        rayHeading = n + playerHeading
        if rayHeading > 180:
            rayHeading -= 360
        elif rayHeading <= -180:
            rayHeading += 360
        SendRay(playerX, playerY, rayHeading)

    for dis_index, dis in enumerate(rayDis):
        DrawLine(dis_index, dis)
    turtle.update()
    time.sleep(0.05)