def encode(string):
    chars = list(map(lambda item : item, string))
    
    index = 0; 
    s = ""
    
    while index < len(chars):
        char = chars[index]
        _chars = list(filter(lambda item : item == char,chars))
        s = s + str(len(_chars)) + char
        chars = list(filter(lambda item : item != char,chars))
        
    return s
    
def decode(string):
    print(string)
    _string_copy = string
    s = ""
    #3A3B3C1A
    while len(_string_copy) > 0:
        ec = _string_copy[:2]
        
        for i in range(1, int(ec[0]) + 1):
            s = s + ec[1]
        
        _string_copy = _string_copy[2:]
         
    print(s)