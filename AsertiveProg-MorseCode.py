# This is dictionary
CODE = {
" " : " ",
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",

"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"0" : "-----",
' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.',     
}

def lettersToMorseCode(message):
    encode = ''
    for letter in message:
        if letter != ' ':
            
            encode += CODE[letter] + ' '
        else:
            encode += ' '
    return encode

def morseCodeToLetters(message):
    
    message += ' '
    
    decode_text = ''
    encode_text = ''
    
    for letter in message:
        
        if (letter != ' '):
            
            alphabet = 0
            encode_text += letter
        
        else:
            alphabet += 1
            
            if alphabet == 2:
                
                decode_text += ' '
            
            else:
                decode_text += list(CODE.keys())[list(CODE.values()) .index(encode_text)]
                encode_text = ''
                
    return decode_text

def main():
    
    message = "Hi there"
    result = lettersToMorseCode(message.upper())
    assert len(message) != 0, "You can't encode a blank space"
    print(result)
    
    message = ".... ..  - .... . .-. ."
    message_length = list(message.split(' '))
    result = morseCodeToLetters(message)
    assert len(message) != 0
    
    print(result)
    print(len(message_length))

if __name__ ==  '__main__':
    main()