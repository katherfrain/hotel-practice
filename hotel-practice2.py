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

def is_vacant(room_number):
    #because of how Python treats Falsey key values like errors, we need to only work with Truthy key-values
    try:
        for hotelroom in hotels:
            if room_number in hotels: 
                
        #if there is a value here, it's because there's a guest staying there!
        if hotels[room_number] == True:
            print("Hotel room is full")
            return False
            #it's not empty, so is-vacant/is-empty is false, basically
    except KeyError:
        #this gets around the error thrown when Python deals with a Falsey key-value - an empty room.
        print("Hotel room is empty")
        return True
        #it is empty so we return true

def check_in(room_number, guest_name):
    #if that room number is empty
    if is_vacant(room_number) == True:
        #assign our guest to it
        hotels[room_number] = guest_name
        return hotels
    else:
        print("Nope, no room here")
        return hotels

def check_out(checkoutroom):
    #replaces anything in the key-value (room) with nothing (an empty dictionary)
    hotels[checkoutroom] = {}
    #this sends back the modified hotel list
    return hotels

while True:
    #this should print a list of empty rooms
    emptyrooms = []
    for rooms in hotels:
        if is_vacant(rooms):
            emptyrooms.append(rooms.keys())
    print(f'These {emptyrooms} are empty.')
    #this should ask you which empty room you want to stay in
    checkin = int(input("Which room would you like?"))
    if checkin in emptyrooms:
        check_in(checkin, guest_name)
    else:
        checkin = int(input("Stop trying to break the program plz."))