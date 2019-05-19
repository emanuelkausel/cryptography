# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:42:12 2019

@author: Emanuel

A little function that takes a ".csv" file with all the transaction-data exported from Kraken.com and
calculates the average buy-in/break-even price and total holdings of Bitcoin, Ethereum & Ripple
and the total buying cost.

"""

def cryptoreader(file):
    Txid=[]; Pair=[]; Time=[]; Type=[]; Ordertype=[]; Price=[]; Cost=[]; Fee=[]; Vol=[];
    
    file=open(file,"r")
    #file=str(file)
    for line in file:
        line=line.split(",")
        
        Txid.append(line[0])
        Pair.append(line[1])
        Time.append(line[2])
        Type.append(line[3])
        Ordertype.append(line[4])
        Price.append(line[5])
        Cost.append(line[6])
        Fee.append(line[7])
        Vol.append(line[8])
        
    BTCAverage=0
    BTCTotVol=0
    ETHAverage=0
    ETHTotVol1=0
    ETHTotVol2=0
    XRPAverage=0
    XRPTotVol=0
        
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
    
    TotalCost= BTCAverage*BTCTotVol+ETHAverage*(ETHTotVol1+ETHTotVol2)+XRPAverage*XRPTotVol
    
    print("Bitcoin Average Price = ",round(BTCAverage,2),"€",";  Bitcoin Holdings:  ",round(BTCTotVol,7))
    print("Ethereum Average Price = ",round(ETHAverage,2),"€",";  Ethereum Holdings:  ",round(ETHTotVol1+ETHTotVol2,7))
    print("Ripple Average Price = ",round(XRPAverage,5),"€",";  Ripple Holdings:  ",XRPTotVol)
    print("Total Cost = ",round(TotalCost,2),"€")
        #print (Txid[i]+";"+Pair[i]+";"+Time[i]+";"+Type[i]+";"+Ordertype[i]+";"+Price[i]+";"+Cost[i]+";"+Fee[i]+";"+Vol[i])


if __name__ == "__main__":
    cryptoreader("KrakenTradesUnformatiert.csv")