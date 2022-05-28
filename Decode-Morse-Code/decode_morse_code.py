'''
Decode a message written in Morse Code.

decode_morse_code.py

Date: 07/2021

Author: Filip J. Cierkosz
'''

def decode_morse(m_code):
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
    message_arr = [i.replace(i, MORSE_CODE[i]) for i in m_code.split(' ')]
    message_decoded = ''.join([j for j in message_arr])

    return message_decoded
