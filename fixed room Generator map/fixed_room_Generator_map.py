import random
mapGrid = [[0 for i in range(10)]for j in range (10)]
a = [1,-1]
xpos = random.randrange(0, 9)
ypos = random.randrange(0, 9)

def roomDesc(roomnum):
    if roomnum == 1:
        print("You're in the spawn area")
    elif roomnum == 2:
        print("You are in a crew cabin. You see several bunk beds on both sides of the room, neatly made with tighly tucked-in wool blankets. A folding table with several chairs sits in the middle of the room, covered with cards, empty cups, and bubblegum wrappers. It appears that nobody has been in this room for quite some time")
    elif roomnum == 3:
        print("You are in the engine room, you see several reactors alongside a simon says")
    elif roomnum == 4:
        print("You are in the storage area, theres lots of boxes around and dust, looks like people havent been here in a while")
    elif roomnum == 5:
        print("You are in the kitchen, you see knives and kitchen objects around, theres a sink, refridgerator and an oven")
room = 0
mapGrid[xpos][ypos] = 1
while room < 10:
    aaa = random.choices(a)
    num = random.randrange(0, 2)
    #walk randomly
    if num == 0:
        xpos += aaa[0]
    else:
        ypos += aaa[0]
    #go back if too far
    if ypos > 9:
        ypos -= aaa[0]
    if xpos > 9:
        xpos -= aaa[0]
        #make sure thing is 0
    if mapGrid[xpos][ypos] == 0:
        mapGrid[xpos][ypos] = random.randrange(2, 6)
        room += 1

for i in range (10):
    for j in range(10):
        if mapGrid[i][j] ==0:
            print("[ ]", end = "")
        else:
            print("[",end = "")
            print(mapGrid[i][j], end = "")
            print("]",end = "")
    print()


