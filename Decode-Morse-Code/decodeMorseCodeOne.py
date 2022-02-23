'''
Date: 07/2021

@author Filip J. Cierkosz
'''

# Function to decode a message written in Morse Code.
def decodeMorse(mCode):
    # Dictionary: {'morseCodeRepresentation' : 'alphanumericRepresentation'}.
    MORSE_CODE = {'..-.': 'F', '-..-': 'X','.--.': 'P', '-': 'T',
                  '..---': '2', '....-': '4', '-----': '0', '--...': '7', 
                  '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J', 
                  '---': 'O', '-.-': 'K', '----.': '9', '..': 'I', 
                  '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y', 
                  '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', 
                  '.-.': 'R', '-...': 'B', '---..': '8', '--..': 'Z', 
                  '-..': 'D', '--.-': 'Q', '--.': 'G', '--': 'M', 
                  '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
    MORSE_CODE[''] = ' '

    # Decode and return the message in alphanumeric representation.
    messageArr = [i.replace(i, MORSE_CODE[i]) for i in mCode.split(' ')]
    messageDecoded = ''.join([j for j in messageArr])

    return messageDecoded

# Test harness.
print(decodeMorse('.----  - . ... - .. -. --.  - .... .  -.-. --- -.. .'))