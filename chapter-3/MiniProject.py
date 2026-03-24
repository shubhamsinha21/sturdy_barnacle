# Convert text based emotions into emojis
# emoji converter - no if, no loop

msg = input("Enter your message: ")
msg = msg.replace(":)", "😊").replace(":(", "😞").replace("<3", "❤️")
print(msg)