# Engeto-projekt-3 - Election data 
- Autor: Vícha Dominik 
- discord: Dominik V
- email: dominik.vicha@gmail.com

### Project Description ###
- This is the final project from the ENGETO Online Python Academy for beginners. Its a tool for scrape the election data from the Czech election from 2017. The results is in the csv file, which can be use in other programms. The determinator is ";". When you want to work with the data in the excel, every value after ";" will have new cell. 


### Requiremts ###
- Python 3.5 + 
- Libraries
    - pip install -r requirements.txt 
    - or pip install bs4 
    - pip instal requests
- other libraries are standart Python libraries you dont need to install 

### Function of the script ###
- The scrip is operated by two arguments. 
1. is the URL page such as: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" 
2. is the output file, which is praha.csv and so on. Depends on the selected unit. 

Dont forget to put the main.py before the URL! 

### CSV ouput data ###
- The results is the csv file with the data: 
    - indentifier: disctrict code
    - name: name of the district 
    - registered_users: number of registred voters
    - envelopes: number of voting envelopes
    - valid votes: number of valid votes 
    - candidate_parties: votes for each party with the party name 

### Usage ### 
- To run the code, will place the URL and then the name of the ouput data CSV file.
    - python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" praha.csv
        - this will download the election data from the selected URL and save it to as file praha.csv

- to get some help 
    1. python main.py -h 
    2. python main.oy --help 

### Example of the ouput ###


### Basic errors ###
- the code has some basic error handling which is: 
    1. Wrong URL adress 
    2. Wrong ouput data format
    3. First must be URL then the name of the csv file 
