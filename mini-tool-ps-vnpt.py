def tac2naptr(tac):
    tacHex = str(hex(tac))[2:].rjust(4,"0")
    naptr = "tac-lb" + tacHex[2:4]+".tac-hb" + tacHex[0:2] + ".tac.epc.mnc002.mcc452.3gppnetwork.org"
    return naptr

def checkDnsTacCmmNokia(tac):
    tacNaptr = tac2naptr(tac)
    commandCheck1 = "dig any @10.149.165.194 -b 10.204.135.21 " + tacNaptr
    commandCheck2 = "dig any @10.149.165.210 -b 10.204.135.21 " + tacNaptr
    return [commandCheck1, commandCheck2]
    
def checkDnsTacMmeEricsson(tac):
    tacNaptr = tac2naptr(tac)
    commandCheck1 = "test_dns_resolve -n " + tacNaptr + """ -s "x-3gpp-mme:x-s10\""""
    commandCheck2 = "test_dns_resolve -n " + tacNaptr + """ -s "x-3gpp-sgw:x-s5-gtp\""""
    commandCheck3 = "dig -t naptr " + tacNaptr + " +short"
    return [commandCheck1, commandCheck2, commandCheck3]

def checkDnsTac(tac):
    print(checkDnsTacCmmNokia(tac))
    print(checkDnsTacMmeEricsson(tac))
    
def checkDnsTacArray(tacList):
    commandNokiaCheck1Array = []
    commandNokiaCheck2Array = []
    commandEricssonCheck1Array = []
    commandEricssonCheck2Array = []
    commandEricssonCheck3Array = []

    
    print("############Program Start############")
    for tac in tacList:
        checkDnsNokiaTacArray = checkDnsTacCmmNokia(tac)
        checkDnsEricssonTacArray = checkDnsTacMmeEricsson(tac)
        commandNokiaCheck1Array.append(checkDnsNokiaTacArray[0] + "   #tac-" + str(tac))
        commandNokiaCheck2Array.append(checkDnsNokiaTacArray[1] + "   #tac-" + str(tac))
        commandEricssonCheck1Array.append(checkDnsEricssonTacArray[0] + "   #tac-" + str(tac))
        commandEricssonCheck2Array.append(checkDnsEricssonTacArray[1] + "   #tac-" + str(tac))
        commandEricssonCheck3Array.append(checkDnsEricssonTacArray[2] + "   #tac-" + str(tac))

    print("############checkDnsNokiaTacArray############")
    print("\n".join(commandNokiaCheck1Array))
    print("\n".join(commandNokiaCheck2Array))
    print("############checkDnsEricssonTacArray############")
    print("############Check S10-MME############")
    print("\n".join(commandEricssonCheck1Array))
    print("############Check S5-SGW############")
    print("\n".join(commandEricssonCheck2Array))
    print("############Check by dig############")
    print("\n".join(commandEricssonCheck3Array))
    print("############Success summary############")
    print("--- Number of tac generate " + str(len(tacList)))
    print("############Program Exit############")        
