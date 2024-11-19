# Engetop-projekt-3 - Election data 
Autor: Vícha Dominik 
discord: Dominik V
email: dominik.vicha@gmail.com

Project Description 
This is the final project from the ENGETO Online Python Academy for beginners. Its a tool for scrape the election data from the Czech election from 2017. The results is in the csv file, which can be use in other programms. 


Requiremts 
- Python 3.5 + 
- Libraries
    - pip install -r requirements.txt 
    - or pip install bs4 
    - pip instal requests
- other libraries are starnadrt Python libraries you dont need to install 

Function of the script
The scrip is operated by two arguments. 
1. is the URL page such as: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" 
2. is the output file, which is praha.csv and so on. Depends on the selected unit. 

Dont forget to put the main.py before the URL! 

CSV ouput data 
The results is the scv file with the data: 
- indentifier 
- name
- registered_users
- envelopes
- valid votes  
- candidate_parties


