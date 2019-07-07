def create_phone_number(n):
    #your code here
    print(n)
    s = "({}) {}-{}"
    n = list(map(lambda item : str(item),n))
    return s.format( "".join(n[0:3]), "".join(n[4:6]), "".join(n[-4:]) )