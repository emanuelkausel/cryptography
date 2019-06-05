# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:42:12 2019

@author: Emanuel

A little function that takes a ".csv" file with all the transaction-data exported from Kraken.com and
calculates the average buy-in/break-even price and total holdings of Bitcoin, Ethereum & Ripple
and the total buying cost.

"""

def cryptoreader(file):
    Txid=[]; Ordertxid=[]; Pair=[]; Time=[]; Type=[]; Ordertype=[]; Price=[]; Cost=[]; Fee=[]; Vol=[];
    
    file=open(file,"r")
    #file=str(file)
    for line in file:
        line=line.replace('"', "")
        line=line.split(",")
        
        Txid.append(line[0])
        Ordertxid.append(line[1])
        Pair.append(line[2])
        Time.append(line[3])
        Type.append(line[4])
        Ordertype.append(line[5])
        Price.append(line[6])
        Cost.append(line[7])
        Fee.append(line[8])
        Vol.append(line[9])
        
    BTCAverage=0
    BTCTotVol=0
    ETHAverage=0
    ETHTotVol1=0
    ETHTotVol2=0
    XRPAverage=0
    XRPTotVol=0
    LTCAverage=0
    LTCTotVol=0
    EOSAverage=0
    EOSTotVol=0
    ADAAverage=0
    ADATotVol=0
    
        
    for i in range(len(Txid)):  
        #print (BTCTotVol)
        if Pair[i]=="XXBTZEUR":
            
            if Type[i]=="buy":
                BTCAverage+=float(Price[i])*float(Vol[i])
                BTCTotVol+=float(Vol[i])
            else: 
                BTCAverage-=float(Price[i])*float(Vol[i])
                BTCTotVol-=float(Vol[i])
        
        elif Pair[i]=="XETHZEUR":
            if Type[i]=="buy":
                ETHAverage+=float(Price[i])*float(Vol[i])
                ETHTotVol1+=float(Vol[i])
            else: 
                ETHAverage-=float(Price[i])*float(Vol[i])
                ETHTotVol1-=float(Vol[i])
                
        elif Pair[i]=="XXRPZEUR":
            if Type[i]=="buy":
                XRPAverage+=float(Price[i])*float(Vol[i])
                XRPTotVol+=float(Vol[i])
            else: 
                XRPAverage-=float(Price[i])*float(Vol[i])
                XRPTotVol-=float(Vol[i])
                
                 
        elif Pair[i]=="XLTCZEUR":
            if Type[i]=="buy":
                LTCAverage+=float(Price[i])*float(Vol[i])
                LTCTotVol+=float(Vol[i])
            else: 
                LTCAverage-=float(Price[i])*float(Vol[i])
                LTCTotVol-=float(Vol[i])
                
        elif Pair[i]=="EOSEUR":
            if Type[i]=="buy":
                EOSAverage+=float(Price[i])*float(Vol[i])
                EOSTotVol+=float(Vol[i])
            else: 
                EOSAverage-=float(Price[i])*float(Vol[i])
                EOSTotVol-=float(Vol[i])
       
        elif Pair[i]=="ADAEUR":
            if Type[i]=="buy":
                ADAAverage+=float(Price[i])*float(Vol[i])
                ADATotVol+=float(Vol[i])
            else: 
                ADAAverage-=float(Price[i])*float(Vol[i])
                ADATotVol-=float(Vol[i])
                   
        elif Pair[i]=="XETHXXBT":
            if Type[i]=="buy":
                ETHTotVol2+=float(Vol[i])
                BTCTotVol-=float(Cost[i])
            else:
                ETHTotVol2-=float(Vol[i])
                BTCTotVol+=float(Cost[i])
        
        
        else: pass
    
    BTCAverage=(BTCAverage/BTCTotVol)
    ETHAverage=(ETHAverage/ETHTotVol1)
    XRPAverage=(XRPAverage/XRPTotVol)
    LTCAverage=(LTCAverage/LTCTotVol)
    EOSAverage=(EOSAverage/EOSTotVol)
    ADAAverage=(ADAAverage/ADATotVol)
    

    
    TotalCost= BTCAverage*BTCTotVol+ETHAverage*(ETHTotVol1+ETHTotVol2)+XRPAverage*XRPTotVol+LTCAverage*LTCTotVol+EOSAverage*EOSTotVol
    
    print("BTC Avg.Price: ",round(BTCAverage,4),"€","   BTC Holdings: ",round(BTCTotVol,4),"      Cost: ",round(BTCAverage*BTCTotVol,2),"€")
    print("ETH Avg.Price:  ",round(ETHAverage,4),"€","   ETH Holdings: ",round(ETHTotVol1+ETHTotVol2,4),"     Cost:  ",round(ETHAverage*(ETHTotVol1+ETHTotVol2),2),"€")
    print("XRP Avg.Price:    ",round(XRPAverage,4),"€","   XRP Holdings: ",round(XRPTotVol,4),"      Cost:   ",round(XRPAverage*XRPTotVol,2),"€")
    print("LTC Avg.Price:     ",round(LTCAverage,4),"€","   LTC Holdings: ",round(LTCTotVol,4),"      Cost:   ",round(LTCAverage*LTCTotVol,2),"€")
    print("EOS Avg.Price:    ",round(EOSAverage,4),"€","   EOS Holdings: ",round(EOSTotVol,4),"     Cost:   ",round(EOSAverage*EOSTotVol,2),"€")
    print("ADA Avg.Price:    ",round(ADAAverage,4),"€","   ADA Holdings: ",round(ADATotVol,4),"   Cost:   ",round(ADAAverage*ADATotVol,2),"€")
    print()
    print("                                                     Total Cost: ",round(TotalCost,2),"€")
        #print (Txid[i]+";"+Pair[i]+";"+Time[i]+";"+Type[i]+";"+Ordertype[i]+";"+Price[i]+";"+Cost[i]+";"+Fee[i]+";"+Vol[i])


if __name__ == "__main__":
    cryptoreader("trades.csv")