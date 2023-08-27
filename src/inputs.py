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
