from string import ascii_letters

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
letters = ascii_letters
for ch in message:
    if letters.find(ch) != -1:
        A = ord("A") if ch.isupper() else ord("a")
        pos = ord(ch) - A 
        pos = (pos + offset) % 26
        new_char = chr(pos + A)
    else:
        new_char = ch    
    encoded_message = encoded_message + new_char

print(encoded_message)
