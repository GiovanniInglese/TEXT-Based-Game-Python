#GIOVANNI INGLESE
# THIS IS THE INTRODUCTION TO THE GAME

def instructions():
    print('WELOCME TO THE SPACE ADVENTURE GAME')
    print('COLLECT 6 ITEMS TO DEFEAT THE ALIEN')
    print('MOVE COMMANDS: go north, go east, go south, go west')
    print('ADD TO INVENTORY: get "item name"')


# CREATES DICTIONARY TO PUT ROOMS WITH DIRECTIONS
rooms = {
     'spaceship corridor':{'north':'laboratory','south':'weapons vault','west':'equipment room','east':'fuel cell room','item':'no item'},
    'equipment room':{'east':'spaceship corridor','item':'repair kit'},
    'laboratory':{'east':'air lock','south':'spaceship corridor','item':'electro sword'},
    'air lock':{'west':'laboratory','item':'space shield'},
    'weapons vault':{'north':'spaceship corridor','east':'food storage','item':'laser'},
    'food storage':{'west':'weapons vault','item':'energy potion'},
    'fuel cell room':{'north':'control room','west':'spaceship corridor','item':'space suit'},
    'control room':{'south':'fuel cell room','item':'alien'}
}
#INITIALIZES THE PLAYERS STARTING ROOM
starting_room= 'spaceship corridor'
#PRINTS THE INSTRUCTIONS
instructions()
#INITIALIZED CURRENT_ROOM VARIABLE
current_room = starting_room
#CREATES PLAYER STAT TO SHOW LOCATION
inventory = []  #DEFINES INVENTORY AS A LIST
def player_stat(rooms,current_room,inventory):
    print('Inventory: ',inventory)
    print('You are in {}'.format(current_room))
#FOREVER LOOP TO RUN THE GAME
while True:
    player_stat(rooms,current_room,inventory)
    player_move = input('Make your move\n') #GETS PLAYERS INPUT
    next_move = player_move.split()  #BREAKS UP PLAYERS INPUT
    if player_move =='exit': #DEFINES AN EXIT IF PLAYER ENTERS EXIT
        print('GAME OVER')
        break


    elif len(player_move)>=1:
        action_move = next_move[0]  # DEFINES MOVEMENT VARIABLE
        item = next_move[1:] #DEFINES AN ITEM IN THE GAME
        direction = next_move[1] #DEFINES THE DIRECTION CALL NORTH,EAST,SOUTH,AND WEST

    if action_move == 'go':
        try: #TRIES TO MOVE IN THE DIRECTION
            current_room = rooms[current_room][direction]
        except: #IF THE MOVE IS NOT IN THAT DIRECTION OR THERE IS NO MOVE THERE THEN IT WILL PRINT CANT GO THAT WAY
            print('CANT GO THAT WAY')
    elif player_move =='exit':
        print('GAME OVER')
        break





