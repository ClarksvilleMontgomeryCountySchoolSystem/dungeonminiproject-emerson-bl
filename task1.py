print("You wake up on a cold stone floor. Your torch may be lit - and that changes everything.")
torch_lit =  True
if torch_lit:
    Flicker = ("you light the torch with a lighter.")
    print(Flicker)
    outcome = ("You may continue")
else:
    Doom = ("You couldnt find a lighter.")
    print(Doom)
    outcome = ("You are dead")
print(outcome)
