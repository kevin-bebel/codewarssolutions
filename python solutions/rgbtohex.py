def rgb(r, g, b):
    #your code here :)
    
    #check r 
    _r = ''
    if r == 0:
        _r ="00"
    else:
        _r = getHex(r)
    #check g 
    _g = ''
    if r == 0:
        _g ="00"
    else:
        _g = getHex(g)

    #check b
    _b = ''
    if b == 0:
        _b ="00"
    else:
        _b = getHex(b)
    
    return _r + _g + _b

def getHex(num):

    if num < 0 :
        return "00"
    
    if num > 255:
        return "FF"

    real_hex = hex(num)
    _hex = real_hex.split("x")[1]

    if len(_hex) == 1 :
        _hex = "0" + _hex

    return _hex.upper()

print(rgb(255, 275, 234))

'''
    
'''