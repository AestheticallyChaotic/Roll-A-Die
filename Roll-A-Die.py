import random

#response = int(input("Roll a Die? : "))

#def roll(response):
#    while response != 'y':
#        response
#    number = random.randint(1,6)
        
#reroll_response = int(input("Press 'y' to Roll Again OR 'n' to Exit : "))

response ='y'

#if response == 'n':
#    response

while response == 'y':
    number = random.randint(1,6)

    if number == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        
    if number == 2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")

    if number == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")

    if number == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")

    if number == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")

    if number == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")

    response = input("Press 'y' to roll again OR Press 'n' to exit : ")