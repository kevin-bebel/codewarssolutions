def men_still_standing(cards):
    # your code
    teams = {
        "A" : { 
            "total" : 11,
            "yellows" : [],
            "sentOff" : []
        },
         "B" : { 
            "total" : 11,
            "yellows" : [],
            "sentOff" : []
        },
    }

    for c in cards:
        #print(c)
        team, player, _card = ( c[0],c[1:-1], c[-1] )
        
        if teams[team]["sentOff"].count(player) > 0:
                continue
        #print(_card)
        if _card == "R" :
            #red card
                teams[team]["sentOff"].append(player)
                teams[team]["total"] = teams[team]["total"] - 1
        else:
            _exists = False
            if teams[team]["yellows"].count(player) > 0:
                teams[team]["sentOff"].append(player)
                teams[team]["total"] = teams[team]["total"] - 1
                _exists = True
            
            if _exists is False:
                teams[team]["yellows"].append(player)

        if teams["A"]["total"] <= 6 or teams["B"]["total"] <= 6  :
            break
    #print(teams)
    A = teams["A"]["total"]
    B = teams["B"]["total"]
    return (A,B) 

print(men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"]))