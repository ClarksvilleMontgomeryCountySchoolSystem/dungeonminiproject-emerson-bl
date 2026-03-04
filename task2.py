print("The door is ahead. Whether you make it through depends on one thing - do you have the key?")
has_key = True
if has_key:
    Click = ("You find the key laying around. You put the key through the hole.")
    print(Click)
    outcome = ("You may continue")
else:
    Doom = ("You could not find the key.")
    print(Doom)
    outcome = ("You are dead")
print(outcome)

