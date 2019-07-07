def balance(left, right):
    #check_left
    lW = calcWeight(left)
    rW = calcWeight(right)
    
    if lW == rW:
        return "Balance"
    elif lW > rW:
        return "Left"
    else:
        return "Right"

def calcWeight(s):
    qW = 3
    eW = 2
    
    q = s.count("?")
    e = s.count("!")
    
    return (q * qW) + (e * eW)