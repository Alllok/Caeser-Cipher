def caesar_cipher(text, shift, direction):  
    result = ""  
  
    for char in text:  
        if char.isalpha():  
            ascii_offset = 65 if char.isupper() else 97  
            result += chr((ord(char) - ascii_offset + shift * direction) % 26 + ascii_offset)  
        else:  
            result += char  
  
    return result  
  
def main():  
    direction = input("Do you want to (E)ncrypt or (D)ecrypt? ")  
    text = input("Enter the message: ")  
    shift = int(input("Enter the shift value: "))  
  
    if direction.upper() == 'E':  
        direction_value = 1  
    elif direction.upper() == 'D':  
        direction_value = -1  
    else:  
        print("Invalid direction. Please enter E for encryption or D for decryption.")  
        return  
  
    result = caesar_cipher(text, shift, direction_value)  
    print("Result: ", result)  
  
if __name__ == "__main__":  
    main()  
