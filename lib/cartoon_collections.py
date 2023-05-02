def roll_call_dwarves(dwarves):
    # for index, dwarf in enumerate(dwarves):
    #     print(f"{index + 1}. {dwarf}")
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    # call_list = []
    # for call in planeteer_calls:
    #     call_list.append(call.title() + "!")
    # return call_list
    return[call.title() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) < 4:
            return True
        else:
            return False



def find_the_cheese(strings):

    cheeses = ["cheddar", "gouda", "camembert"]

    for string in strings:
        if string in cheeses:
            return string
        # else:
        #     return None
            
            
