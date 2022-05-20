#Written with love by poppy
#2022-05-19
def cap():
    global sdCap
    sdCap = input("SD Capacity > ")
    try:
        int(sdCap)
        return
    except:
        print("Error! Is the capacity a whole number?")
        cap()
def price():
    global sdPrice
    sdPrice= input("SD Price (in $USD) > ")
    try:
        float(sdPrice)
        return
    except:
        print("Error! Is the price a number? Please don't include the $")
        price()
def writeToFile():
    
    IDsW = open('_cards.txt', 'a')
    IDsR = open('_cards.txt', 'r')
    lnChk = IDsR.readlines()

    ppg = (float(sdPrice)/int(sdCap))
    roundPPG = round(ppg, 3)
    txtToWrite = f"Card Name: {sdName}\nCard Capacity: {sdCap}gb\nCard Price: ${sdPrice}\nCard $/GB: {roundPPG}\n"
    print("\n"+txtToWrite)
    
    try:
        lnChk[0]
        IDsW.writelines(f"\n{txtToWrite}")
        IDsW.close()
        IDsR.close()
    except IndexError:
        IDsW.writelines(f"sdCard Comparison Tool\nBy poppy\nCreated: 2022-05-19\n--Output Log--\n\n")
        IDsW.writelines(f"{txtToWrite}")
        IDsW.close()
        IDsR.close()

print("sdCard Comparison Tool\nBy poppy\n2022-05-19")
sdName = input("Name Of SD > ")
cap()
price()
writeToFile()