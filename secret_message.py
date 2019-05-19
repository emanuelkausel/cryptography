# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:18:47 2019

@author: Emanuel

Encrypting and Decrypting Messages. Easy to use GraphicalUserInterface
"""


def enc(message, key):
       
    message=str(message) #unicode in python2
    key=str(key)
    
    import re
    message = ("".join(re.findall(r"[A-Za-z]*", message)))
    key = ("".join(re.findall(r"[A-Za-z]*", key)))
    key=key.lower()
    message=message.lower()
       
    letters_lower="qwertzuiopasdfghjklyxcvbnm"
    key_list=[]
    message_list=[]
    cypher=""
        
    for letter in message:
        index=letters_lower.find(letter)
        message_list.append(index)
        
    for letter in key:
        index=letters_lower.find(letter)
        key_list.append(index)
         
    while len(key_list) < len(message_list):
        key_list.extend(key_list)
            
    for i in range(len(message_list)):
        message_list[i]+=key_list[i]
        if message_list[i]>25: message_list[i]-=26
         
    for x in message_list:
        cypher+=letters_lower[x]
    
    return cypher  
    


def dec(cypher, key):
    
    cypher = str(cypher) #unicode in python2
    key = str(key)
    
    import re
    cypher = ("".join(re.findall(r"[A-Za-z]*", cypher)))
    key = ("".join(re.findall(r"[A-Za-z]*", key)))
    key=key.lower()
    cypher = cypher.lower()
    
    cypher_list=[]
    key_list=[]
    letters_lower="qwertzuiopasdfghjklyxcvbnm"
    message=""
    
    for letter in cypher:
        index=letters_lower.find(letter)
        cypher_list.append(index)
    
    for letter in key:
        index=letters_lower.find(letter)
        key_list.append(index)
         
    while len(key_list) < len(cypher_list):
        key_list.extend(key_list)
    
    for i in range(len(cypher_list)):
        cypher_list[i]-=key_list[i]
        if cypher_list[i]<0: cypher_list[i]+=26
         
    for x in cypher_list:
        message+=letters_lower[x]
    
    return message
    
        
if __name__ == "__main__" :
   
   """   
   # program without Tkinter
   k = raw_input("enter your key:   " )
   m = raw_input("enter a message to encrypt:   ")
   c = raw_input("enter a message to decrypt:   ")
   print
   en = enc(m,k)
   
   print "Verschlüsselter Code: ",en
   print
   de = dec(c,k)
   print "Entschlüsselter Code: ",de
    
   """  
  
    
   import tkinter as tk


   def show_enc():
        c=enc(e2.get(),e1.get())
        root = tk.Tk()
        T = tk.Text(root, height=5, width=100)
        T.pack()
        T.insert(tk.END,"Encrypted Message:\n\n"+c)
        
   def show_dec():
        m=dec(e3.get(),e1.get())
        root = tk.Tk()
        T = tk.Text(root, height=5, width=100)
        T.pack()
        T.insert(tk.END,"Decrypted Message:\n\n"+m)
        
   window = tk.Tk()
   window.title("Program to encrypt or decrypt messages and feel like a real secret-agent...")
   window.geometry("1000x200")  
   window.configure(background='grey')

   tk.Label(window, bg="grey").grid(row=0)
   tk.Label(window, font=("Arial", 12, "bold"), text="Enter your Key-Word:").grid(row=1, padx=8, pady=8)
   tk.Label(window, bg="grey").grid(row=2)
   tk.Label(window, font=("Arial", 12, "bold"), text="Enter a message to encrypt:").grid(row=3, padx=8)
   tk.Label(window, font=("Arial", 12, "bold"), text="or").grid(row=4)
   tk.Label(window, font=("Arial", 12, "bold"), text="Enter a message to decrypt:").grid(row=5, padx=8)
    
   e1 = tk.Entry(window, width=100) #key
   e2 = tk.Entry(window, width=100) #message
   e3 = tk.Entry(window, width=100) #cypher
       
   e1.grid(row=1, column=1, sticky=tk.W)
   e2.grid(row=3, column=1, sticky=tk.W)
   e3.grid(row=5, column=1, sticky=tk.W)
 
   tk.Button(window, font=("Arial", 12, "bold"), text='Encrypt', width=12, command=show_enc).grid(row=3, column=2, sticky=tk.W, padx=8)
   tk.Button(window, font=("Arial", 12, "bold"), text='Decrypt', width=12, command=show_dec).grid(row=5, column=2, sticky=tk.W, padx=8)
     
   window.mainloop( )
        

    
        
    
            
         
