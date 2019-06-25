# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:42:12 2019

@author: Emanuel

A little function that takes a ".csv" file with all the transaction-data exported from Kraken.com and
calculates the average buy-in/break-even price and total holdings of Bitcoin, Ethereum & Ripple
and the total buying cost. Recently I also added a feature that tells you how much of your holdings
you can sell without paying capital-gains-tax (1 Year holding).

"""

def cryptoreader(file):
    
    import time
    from datetime import datetime,timedelta
    Txid=[]; Ordertxid=[]; Pair=[]; Time=[]; Type=[]; Ordertype=[]; Price=[]; Cost=[]; Fee=[]; Vol=[];
    
    file=open(file,"r")
    text=file.readlines()
    file.close()
    del text[0] #delete first line of csv file with the headers
    
    for line in text:
        line=line.replace('"', "")
        line=line.split(",")
        
        Txid.append(line[0])
        Ordertxid.append(line[1])
        Pair.append(line[2])
        
        x=line[3][:19] #getting rid of microseconds
        datetime_object = datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
        Time.append(datetime_object)
        
        Type.append(line[4])
        Ordertype.append(line[5])
        Price.append(float(line[6]))
        Cost.append(float(line[7]))
        Fee.append(float(line[8]))
        Vol.append(float(line[9]))
        
    lt = time.localtime(time.time())  #Localtime
    Localtime=datetime(lt[0], lt[1], lt[2], hour=lt[3], minute=lt[4], second=lt[5])    
    TaxFreeDay=Localtime-timedelta(days=365) #Tax-Free-Day

       
    BTCAverage=0; BTCTotVol=0;                BTCTaxFreeVol=0;
    ETHAverage=0; ETHTotVol1=0; ETHTotVol2=0; ETHTaxFreeVol=0;
    XRPAverage=0; XRPTotVol=0;                XRPTaxFreeVol=0;
    LTCAverage=0; LTCTotVol=0;                LTCTaxFreeVol=0;
    EOSAverage=0; EOSTotVol=0;                EOSTaxFreeVol=0;
    ADAAverage=0; ADATotVol=0;                ADATaxFreeVol=0;
    
        
    for i in range(len(Txid)):  
        #print (BTCTotVol)
        if Pair[i]=="XXBTZEUR":
            
            if Type[i]=="buy":
                BTCAverage+=Price[i]*Vol[i]
                BTCTotVol+=Vol[i]
                if Time[i]<TaxFreeDay: BTCTaxFreeVol+=Vol[i]
            else: 
                BTCAverage-=Price[i]*Vol[i]
                BTCTotVol-=Vol[i]
                if Time[i]<TaxFreeDay: BTCTaxFreeVol-=Vol[i]
        
        elif Pair[i]=="XETHZEUR":
            if Type[i]=="buy":
                ETHAverage+=Price[i]*Vol[i]
                ETHTotVol1+=Vol[i]
                if Time[i]<TaxFreeDay: ETHTaxFreeVol+=Vol[i]
            else: 
                ETHAverage-=Price[i]*Vol[i]
                ETHTotVol1-=Vol[i]
                if Time[i]<TaxFreeDay: ETHTaxFreeVol-=Vol[i]
                
        elif Pair[i]=="XXRPZEUR":
            if Type[i]=="buy":
                XRPAverage+=Price[i]*Vol[i]
                XRPTotVol+=Vol[i]
                if Time[i]<TaxFreeDay: XRPTaxFreeVol+=Vol[i]
            else: 
                XRPAverage-=Price[i]*Vol[i]
                XRPTotVol-=Vol[i]
                if Time[i]<TaxFreeDay: XRPTaxFreeVol-=Vol[i]
                                 
        elif Pair[i]=="XLTCZEUR":
            if Type[i]=="buy":
                LTCAverage+=Price[i]*Vol[i]
                LTCTotVol+=Vol[i]
                if Time[i]<TaxFreeDay: LTCTaxFreeVol+=Vol[i]
            else: 
                LTCAverage-=Price[i]*Vol[i]
                LTCTotVol-=Vol[i]
                if Time[i]<TaxFreeDay: LTCTaxFreeVol-=Vol[i]
                
        elif Pair[i]=="EOSEUR":
            if Type[i]=="buy":
                EOSAverage+=Price[i]*Vol[i]
                EOSTotVol+=Vol[i]
                if Time[i]<TaxFreeDay: EOSTaxFreeVol+=Vol[i]
            else: 
                EOSAverage-=Price[i]*Vol[i]
                EOSTotVol-=Vol[i]
                if Time[i]<TaxFreeDay: EOSTaxFreeVol-=Vol[i]
       
        elif Pair[i]=="ADAEUR":
            if Type[i]=="buy":
                ADAAverage+=Price[i]*Vol[i]
                ADATotVol+=Vol[i]
                if Time[i]<TaxFreeDay: ADATaxFreeVol+=Vol[i]
            else: 
                ADAAverage-=Price[i]*Vol[i]
                ADATotVol-=Vol[i]
                if Time[i]<TaxFreeDay: ADATaxFreeVol-=Vol[i]
                   
        elif Pair[i]=="XETHXXBT":
            if Type[i]=="buy":
                ETHTotVol2+=Vol[i]
                BTCTotVol-=Cost[i]
                if Time[i]<TaxFreeDay: 
                    ETHTaxFreeVol+=Vol[i] 
                    BTCTaxFreeVol-=Cost[i]
            else:
                ETHTotVol2-=Vol[i]
                BTCTotVol+=Cost[i] #stimmt das Cost hier?
                if Time[i]<TaxFreeDay: 
                    ETHTaxFreeVol-=Vol[i] 
                    BTCTaxFreeVol+=Cost[i]
       
        else: pass
    
    BTCTotVol-=0.45 #Korrektur
    ADATotVol+=3000 #Korrektur
    
    BTCAverage=(BTCAverage/BTCTotVol)
    ETHAverage=(ETHAverage/ETHTotVol1); ETHTotVol=ETHTotVol1+ETHTotVol2
    XRPAverage=(XRPAverage/XRPTotVol)
    LTCAverage=(LTCAverage/LTCTotVol)
    EOSAverage=(EOSAverage/EOSTotVol)
    ADAAverage=(ADAAverage/ADATotVol)
    
    TotalCost= BTCAverage*BTCTotVol+ETHAverage*(ETHTotVol1+ETHTotVol2)+XRPAverage*XRPTotVol+LTCAverage*LTCTotVol+EOSAverage*EOSTotVol
    
    print()
    print("BTC Avg.Price: ",round(BTCAverage,4),"€","   BTC Holdings: ",round(BTCTotVol,4),"      Cost: ",round(BTCAverage*BTCTotVol,2),"€")
    print("ETH Avg.Price:  ",round(ETHAverage,4),"€","   ETH Holdings: ",round(ETHTotVol,4),"     Cost:  ",round(ETHAverage*(ETHTotVol1+ETHTotVol2),2),"€")
    print("XRP Avg.Price:    ",round(XRPAverage,4),"€","   XRP Holdings: ",round(XRPTotVol,4),"      Cost:   ",round(XRPAverage*XRPTotVol,2),"€")
    print("LTC Avg.Price:     ",round(LTCAverage,4),"€","   LTC Holdings: ",round(LTCTotVol,4),"      Cost:   ",round(LTCAverage*LTCTotVol,2),"€")
    print("EOS Avg.Price:    ",round(EOSAverage,4),"€","   EOS Holdings: ",round(EOSTotVol,4),"     Cost:   ",round(EOSAverage*EOSTotVol,2),"€")
    print("ADA Avg.Price:    ",round(ADAAverage,4),"€","   ADA Holdings: ",round(ADATotVol,4),"   Cost:   ",round(ADAAverage*ADATotVol,2),"€")
    print()
    print("                                                     Total Cost: ",round(TotalCost,2),"€")
       
    print()
    print("Local Time:   ",Localtime)
    print("Tax-Free-Day: ",TaxFreeDay)
    print()
    print()
    print("BTC Tax-free: ",round(BTCTaxFreeVol,4),"(",round(100*BTCTaxFreeVol/BTCTotVol,2),"% )")
    print("ETH Tax-free: ",round(ETHTaxFreeVol,4),"(",round(100*ETHTaxFreeVol/ETHTotVol,2),"% )")
    print("XRP Tax-free: ",round(XRPTaxFreeVol,4),"(",round(100*XRPTaxFreeVol/XRPTotVol,2),"% )")
    print("LTC Tax-free: ",round(LTCTaxFreeVol,4),"(",round(100*LTCTaxFreeVol/LTCTotVol,2),"% )")
    print("EOS Tax-free: ",round(EOSTaxFreeVol,4),"(",round(100*EOSTaxFreeVol/EOSTotVol,2),"% )")
    print("ADA Tax-free: ",round(ADATaxFreeVol,4),"(",round(100*ADATaxFreeVol/ADATotVol,2),"% )")
    
if __name__ == "__main__":
      cryptoreader("trades.csv")
    
    
