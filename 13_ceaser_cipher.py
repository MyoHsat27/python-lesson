# Ceaser Cipher (using Functions)

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, action):
    result = ""

    if action == "decode":
        shift = shift * -1

    for char in text:
        if char in characters:
            index = characters.index(char)
            new_index = index + shift
            result += characters[new_index]
        else:
            result += char

    return result


# def encode(text, shift):
#     result = ""
#     for char in text:
#         if char in text:
#             index = characters.index(char)
#             new_index = index + shift
#             result += characters[new_index]
#         else:
#             result += char
#     return result

# def decode(text, shift):
#     result = ""
#     for char in text:
#         if char in text:
#             index = characters.index(char)
#             new_index = index - shift
#             result += characters[new_index]
#         else:
#             result += char
#     return result

while True:
    input_action = input("Choose [ encode | decode ] : ").lower()
    input_text = input("Enter the message : ")
    input_shift = int(input("Enter the shift value : "))
    input_shift = input_shift % 26
    final_result = caesar(input_text, input_shift, input_action)
    print(f"Message : {final_result}")

    continue_action = input("Do you want to continue? [ yes | no ] : ").lower()

    if continue_action == "no":
        break
