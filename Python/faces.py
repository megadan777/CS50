# Creating an input from the user
message = input("Enter some text: ")


# convert emoticons to emoji automatically
message = message.replace(":)", "🙂").replace(":(","🙁")

print(message)

