hotels =  [    {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}
,
{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}
,
    {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}
]

def is_vacant(hotel, room_number):
#add an if-the-room-exists loop
    #because of how Python treats Falsey key values like errors, we need to only work with Truthy key-values
    try: 
        #if there is a value here, it's because there's a guest staying there!
        if hotel[room_number]:
            print("Hotel room is full")
            return False
        else:
            print("Hotel room is empty.")
            return True
            #it's not empty, so is-vacant/is-empty is false, basically
    except KeyError:
        #this gets around the error thrown when Python deals with a Falsey key-value - an empty room.
        print("Hotel room non-existant.")
        return False
        #it is empty so we return true

def check_in(hotel, room_number, guest_name):
    #if that room number is empty
    if is_vacant(hotel, room_number) == True:
        #assign our guest to it
        hotel[room_number] = guest_name
        return hotel
    else:
        print("Nope, no room here")
        return hotel

def check_out(hotel, checkoutroom):
    #replaces anything in the key-value (room) with nothing (an empty dictionary)
    hotel[checkoutroom] = {}
    #this sends back the modified hotel list
    return hotel
print(check_out(hotels[0], '101'))

while True:
    #this should print a list of empty rooms
    emptyrooms = []
    for hotel in hotels:
        for room in hotel.keys():
            if is_vacant(hotel, room):
                emptyrooms.append(room)
    print(f'These {emptyrooms} are empty.')
    #this should ask you which empty room you want to stay in

    checkin_name = input("What's your name?")
    checkin = input("Which room would you like?")
    check_in(hotels[0], checkin, checkin_name)
    """
    for hotel in hotels:
        for room in hotel.keys():
            if room in checkin:
                check_in(hotel, checkin, checkin_name)
            else:
                checkin = input("Stop trying to break the program plz.")
                """