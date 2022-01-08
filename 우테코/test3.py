import sys

def solution(ings, menu, sell):
    ingredient ={}
    menuToIng = {}
    menuToSell = {}
    profit = 0
    for i in ings:
        dient, dprice = map(str, i.split())
        ingredient[dient] = int(dprice)

    for i in range(len(menu)):
        name, needed, sellPrice = map(str, menu[i].split())
        menuToIng[name] = needed
        menuToSell[name] = int(sellPrice)

    for i in sell:
        soldName, soldNum = map(str, i.split())
        salary = menuToSell[soldName] * int(soldNum)
        thisIng = menuToIng[soldName]
        madePrice = 0
        for j in thisIng:
            madePrice += ingredient[j]
        profit += salary - (madePrice*int(soldNum))
    return profit



solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"])