# Engeto-projekt-3 - Election data 
- Autor: Vícha Dominik 
- discord: Dominik V
- email: dominik.vicha@gmail.com

---

### Project Description ###
- This is the final project from the ENGETO Online Python Academy for beginners. Its a tool for scrape the election data from the Czech election from 2017. The results is in the csv file, which can be use in other programms. The determinator is ";". When you want to work with the data in the excel, every value after ";" will have new cell. 

---
### Requiremts ###
- Python 3.5 + 
- Libraries
    - pip install -r requirements.txt 
    - or pip install bs4 
    - pip instal requests
- other libraries are standart Python libraries you dont need to install 
---
### Function of the script ###
- The scrip is operated by two arguments. 
1. is the URL page such as: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" 
2. is the output file, which is praha.csv and so on. Depends on the selected unit. 

Dont forget to put the main.py before the URL! 
---
### CSV ouput data ###
- The results is the csv file with the data: 
    - indentifier: disctrict code
    - name: name of the district 
    - registered_users: number of registred voters
    - envelopes: number of voting envelopes
    - valid votes: number of valid votes 
    - candidate_parties: votes for each party with the party name 
---
### Usage ### 
- To run the code, will place the URL and then the name of the ouput data CSV file.
```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" "praha.csv"
```  

- to get some help 
```bash
python main.py -h
python main.py --help
```
---
### Example of the ouput ###
```csv
indentifier;Name;Registered Users;Envelopes;Valid Votes;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Volte Pr.Blok www.cibulka.net;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Společ.proti výst.v Prok.údolí;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;OBČANÉ 2011-SPRAVEDL. PRO LIDI;Unie H.A.V.E.L.;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů;-
500054;Praha 1;21556;14167;14036;2770;9;13;657;12;1;774;392;514;41;6;241;14;44;2332;5;0;12;2783;1654;1;7;954;3;133;11;2;617;34;0
500224;Praha 10;79964;52277;51895;8137;40;34;3175;50;17;2334;2485;1212;230;15;1050;35;67;9355;9;8;30;6497;10856;37;53;2398;12;477;69;53;2998;162;0
```
---
### Basic errors ###
- the code has some basic error handling which is: 
    1. Wrong URL adress 
    2. Wrong ouput data format
    3. First must be URL then the name of the csv file 


### Enjoy the data and feel free to contatc me. ###