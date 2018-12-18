places = {}
active = True
while active:
    name = input("\nInput your name: ")
    place = input("\nIf you could visit one place in the world,where would you go? ")
    places[name] = place

    repeat = input("\nWould you like to let another person to respond? Input 'no' or 'yes' : ")
    if repeat == 'no':
        active = False
# 打印调查结果
print("\n......Poll Results......")
for poll_name, poll_place in places.items():
    print(poll_name + " would like to visit " + poll_place)
