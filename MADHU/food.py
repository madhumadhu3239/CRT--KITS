def washhands():
    print("washing hands")
def servefood():
    print("serve food")
def eatfood():
    washhands()
    servefood()
    print("Eating food")
    washhands()
eatfood()