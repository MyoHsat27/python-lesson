# Emoji Convertor
emojis = {":)" : "😊", ":(" : "😞", ":D" : "😁"}
message = input("Enter a message : ") # :)
words = message.split(" ") # [":)"]
new_message = ""

for word in words :
    new_message += emojis.get(word, word) + " "
    
print(new_message)