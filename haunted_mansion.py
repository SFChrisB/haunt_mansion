#Haunted Mansion Text Adventure
#Vers 0.1
#
#
# ------       --------------
# |  4 |       |   7  |   8  |
# ------       --------------
# |  3 |       |   6  |
# --------------------
# |  2 |   1   |   5  |
# --------------------
#      |   0   |      
#      ---------
#
#       N = North
#       E = East
#       S = South
#       W = West
#
#       Q = Quit
#

room_list = []
room = ["You are in the courtyard overlooking the huge mansion. The front door is to the north.",1,None,None,None]
room_list.append(room)
room = ["This is the front hall of the mansion. South leads outside the mansion. There are rooms leading both East and West leading to the living room and study room.",None,5,0,2]
room_list.append(room)
room = ["You are in the living room. To the East is the front hallway, and to the North is the dining room.",3,1,None,None]
room_list.append(room)
room = ["You are in the dining room. To the South leads to the living room and to the North is the kitchen.",4,None,2,None]
room_list.append(room)
room = ["This is the kitchen. To the South is the dining room.",None,None,3,None]
room_list.append(room)
room = ["This is the study room. To the West leads back to the front hall. To the North leads to the patio.",6,None,None,1]
room_list.append(room)
room = ["You are in the Patio. To the South leads to the study room. To the North leads to the garden.",7,None,5,None]
room_list.append(room)
room = ["You are standing in the garden. To the South leads to the patio. To the East you see a rather large garden shed.",None,8,6,None]
room_list.append(room)
room = ["You are standing in a very large garden shed. To the West leads back to the garden.",None,None,None,7]
room_list.append(room)

current_room = 0
done = False

while done is not True:
    print()
    print(room_list[current_room][0])
    choice = input("Where do you want to go? ")
    if choice.upper() == "N" or choice.upper == "NORTH":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif choice.upper() == "E" or choice.upper == "EAST":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif choice.upper() == "S" or choice.upper == "SOUTH":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif choice.upper() == "W" or choice.upper == "WEST":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    elif choice.upper() == "Q" or choice.upper == "QUIT":
        print("Exiting the program.")
        done = True
    else:
        print("I dont understand the command. Try N,E,S or W for the direction.")
        
