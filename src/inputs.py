def getInput(array, question):
    userInput = input(question)
    print()

    while True:
        # Check input is acceptable
        if userInput == '':
            return False
        elif not userInput.isdigit() or int(userInput) < 1 or int(userInput) > len(array):
            print(f"Input has to be a number 1-{len(array)}")
            userInput = input(question)
            continue
        else:
            # Chooses file
            userInput = int(userInput)
            return userInput
        

def yesNo(question):
    userInput = input(question)
    print()

    while True:
        # Check input is acceptable
        if userInput == '':
            print(f"Don't leave me empty!")
        elif userInput.lower() in ['y', 'ye', 'yes', 'yeah']:
            return True
        elif userInput.lower() in ['n', 'no', 'nop', 'nope']:
            return False