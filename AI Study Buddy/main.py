import datetime # to know users date and time
import time

name = input("Swagat hai, enter you name: ")
presentHours = datetime.datetime.now().hour # method in datetime module to get exact hours(time)

if 3 <= presentHours <= 11:
    print("Good morning ", name)

elif 11 < presentHours <=17 :
    print("Good afternoon ", name)
    
elif 17 < presentHours <= 20:
    print("Good evening ", name)

else:
    print("Good night ", name)
    

print("\nNamaste! Welcome to Your Study Buddy chatbot\n")
print("You can ask me basic question, type 'bye' to exit from the bot")

# chatbot memory creation ( we will use dictionary)
responses = {
    "hello": "Hi, Welcome. How i can help you",
    "how are you": "I'm fine, thank you",
    "who are you": "I'm smart AI assistant",
    "motivate me": "Keep going. Every bug of project make your skills sharp",
    "happy": "Great to hear that",
    "function explain kro": "go to chapter-7 and read the code and details",
    "are you begineer or expert in python": "professional",
    "are you enjoying learning": "yes"
}

# reply - response of bot
def getResponse(userQuestion):
    userQuestion = userQuestion.lower()
    for key in responses:
        if key == userQuestion:
            time.sleep(1)
            return responses[key]
        
    return "I'm not able to answer this question"

# take user input
while True:
    userInput= input("please ask your question: ")
    reply = getResponse(userInput)
    print("Bot Responds:", reply)
    
    # break the flow
    if "bye" in userInput.lower():
        break