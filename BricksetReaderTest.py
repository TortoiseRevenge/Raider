import BricksetReader as BR

apiKey = input("Please Enter Your Brickset API Key:")
print("Checking Key")
while(BR.checkAPIKey(apiKey) != "success"):
    print("API Key Not Correct")
    print("Server Response is " + BR.checkAPIKey(apiKey))
    print("If you do not have an API Key, either message me (Adam), or get one at https://brickset.com/tools/webservices/requestkey")
    apiKey = input("Please Enter Your Correct Brickset API Key: ")
    
print("Key Successful")

userInput = 0
defaultTest = 0
inQuestionAnswer = 1
setList = []

while(userInput != "10"):
    print("\n1:Get Set Instructions\n2: Get Multiple Set's Instructions \n3: Get All Lego Themes \n4: Get Theme's Subthemes \n5: Get Theme's Years of Production \n6: Get all of a Theme's sets \n10: Quit")
    userInput = input("Please Enter Your Choice: ")
    #Python (as of 3.9.2) does not contain a switch statement, which would be ideal in the below case
    defaultTest = 0
    if userInput == "1":
        defaultTest = 1
        inQuestionAnswer = input("Please Enter in Set Numbers: ")
        directory = input("Where do you want these instructions stored?: ")     
        print(BR.getSingleInstruction(apiKey,inQuestionAnswer,directory))
        
    if userInput == "2":
        defaultTest = 1
        setList = []
        loop = 0
        while inQuestionAnswer != "0":
            if loop != 0:
                setList.append(inQuestionAnswer)
            loop += 1
            inQuestionAnswer = input("Please Enter in a Single Set Number, or 0 to countinue: ")
        directory = input("Where do you want these instructions stored?: ")     
        if length(setList) > 0:
            print(BR.getMultipleInstruction(apiKey,setList,directory))

    if userInput == "3":
        defaultTest = 1
        print(BR.getThemes(apiKey))

    if userInput == "4":
        defaultTest = 1
        inQuestionAnswer = input("What Theme?: ")
        print(BR.getSubthemes(apiKey,inQuestionAnswer))

    if userInput == "5":
        defaultTest = 1
        inQuestionAnswer = input("What Theme?: ")
        print(BR.getThemesYear(apiKey,inQuestionAnswer))

    if userInput == "6":
        defaultTest = 1
        inQuestionAnswer = input("What Theme?: ")
        print(BR.getSets(apiKey,inQuestionAnswer))
    
    if userInput == "10":
        defaultTest = 1
        print("Quitting")
        
    if defaultTest == 0:
        print("Entered Number does not follow guidelines")
        
