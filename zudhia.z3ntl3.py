'''
Programmed by Z3NTL3 t.me/z3ntl3 & t.me/lowkeypanelme

Don't sell this shit otherwise s*ck ma d*ck
'''

import threading as th
import time
import sys
import subprocess as sp
import json

try:
    import blessed as colorful
except:
    sp.run("pip3 install blessed", shell=True)
try:
    import requests as browser
except:
    sp.run("pip3 install requests", shell=True)

def clear():
    sp.run("clear", shell=True, stderr=sp.DEVNULL)
    sp.run("cls", shell=True, stderr=sp.DEVNULL)

terminal = colorful.Terminal()

class coloring:
    
    kleur1 = terminal.color_rgb(64, 17, 173)
    kleur2 = terminal.color_rgb(95, 44, 212)
    kleur3 = terminal.color_rgb(119, 75, 219)
    kleur4 = terminal.color_rgb(143, 107, 227)
    kleur5 = terminal.color_rgb(109, 113, 227)

    kleur6 = terminal.color_rgb(109, 152, 227)
    kleur7 = terminal.color_rgb(109, 192, 227)
    kleur8 = terminal.color_rgb(224, 130, 144)
    kleur9 = terminal.color_rgb(222, 87, 107)
    kleur10 = terminal.color_rgb(219, 64, 87)
    kleur11 = terminal.color_rgb(109, 113, 227)
    kleur12 = terminal.color_rgb(109, 113, 227)
    kleur13 = terminal.color_rgb(95, 44, 212)

    red = terminal.color_rgb(222, 20, 50)
    blue = terminal.color_rgb(108, 204, 245)
    
class gateway_scraper:
    
    try:
        
        connection = browser.get("https://raw.githubusercontent.com/Z3NTL3/Zudhia/main/always-updated-api-gateways.json", headers={'Cache-Control': 'no-cache'}, timeout=20)
        conn = json.loads(connection.text)
        gateway = conn['gateway']
    except:
        file = open('always-updated-api-gateways.json','r')
        conn = json.loads(file)
        gateway = conn['gateway']

def detector():
    d = subprocess.getoutput("echo $TERM")

    while True:
        if d == "xterm-256color":
            break
        else:
            clear()
            print(f"\033[31mYour Terminal Does not Support 256 Color RGB\n\nTo FIX:\n> sudo apt install xterm\n>export TERM=xterm256-color\n\n")
            sys.exit()
            
logo = f"""
       {coloring.kleur9}╔\033[0m{coloring.kleur9}═\033[0m{coloring.kleur9}╗\033[0m{coloring.kleur9}╦ ╦╔╦╗╦ ╦╦╔═╗
       {coloring.kleur8}╔{coloring.kleur8}═{coloring.kleur8}╝\033[0m{coloring.kleur8}║ ║ ║║╠═╣║╠═╣
       {coloring.kleur7}╚\033[0m{coloring.kleur7}═{coloring.kleur7}╝\033[0m{coloring.kleur7}╚\033[0m{coloring.kleur7}═╝═╩╝╩ ╩╩╩ ╩

   {coloring.kleur1}[{coloring.kleur9}Cr{coloring.kleur8}edi{coloring.kleur7}tca{coloring.kleur6}rd {coloring.kleur5}& {coloring.kleur4}Bin{coloring.kleur3} Che{coloring.kleur2}ck{coloring.kleur1}er{coloring.kleur1}]
           {coloring.kleur1}>{coloring.kleur2}>{coloring.kleur3}>{coloring.kleur6}B{coloring.kleur7}Y{coloring.kleur3}<{coloring.kleur2}<{coloring.kleur1}<   
         {coloring.kleur1}[{coloring.kleur9}t.m{coloring.kleur8}e/z{coloring.kleur7}3n{coloring.kleur6}tl{coloring.kleur5}3{coloring.kleur1}]
"""

try:
    sys.argv[1] = "-check"
    api = f"{gateway_scraper.gateway}{sys.argv[2]}"
except:
    print(logo)
    sys.exit(f"\033[1m{coloring.kleur1}U{coloring.kleur2}sa{coloring.kleur3}g{coloring.kleur4}e{coloring.kleur5}:\n{coloring.red}python3 \033[0m{coloring.blue}zudhia.z3ntl3.py {coloring.red}-check creditcard/bin")

def start(process): 
    data = browser.get(api, headers={'Cache-Control': 'no-cache'})
    try:
        load = json.loads(data.text)
    except:
        clear()
        print(logo)
        sys.exit(f"{coloring.kleur1}[ {coloring.kleur9}Err{coloring.kleur8}or {coloring.kleur7}can{coloring.kleur6}not {coloring.kleur5}con{coloring.kleur4}nect{coloring.kleur3} to {coloring.kleur2}API {coloring.kleur1}]\033[0m")
    try:
        global card
        card = load['scheme']
    except:
        card = "NULL"

    try:
        global type
        type = load['type']
    except:
        type = "NULL"

    try:
        global prepaid
        prepaid = load['prepaid']
    except:
        prepaid = "No Prepaid"

    try:
        global countr
        z3ntl3 = load['country']
        country = z3ntl3['name']
    except:
        country = "No Country Available"

    try:
        global bank
        z3ntl3 = load['bank']
        bank = z3ntl3['name']
    except:
        bank = "No Bankname Available"


    
    valid = "Valid"
    try:
        global phone
        z3ntl3 = load['bank']
        phone = z3ntl3['phone']
    except:
        phone = "No Phone Available"

    try:
        global city
        z3ntl3 = load['bank']
        city = z3ntl3['city']
    except:
        city = "No City Available"

    try:
        global url
        z3ntl3 = load['bank']
        url = z3ntl3['url']
    except:
        url = "No URL Available"

    try:
        global currency
        z3ntl3 = load['country']
        currency = z3ntl3['currency']
    except:
        currency = "No currency Available"
    


    print(logo)
    print(f"""{coloring.kleur4}╔═{coloring.kleur3}══{coloring.kleur2}══{coloring.kleur1}════{coloring.kleur2}════{coloring.kleur3}═══{coloring.kleur4}══{coloring.kleur5}═══{coloring.kleur6}═══{coloring.kleur7}═══{coloring.kleur8}═══{coloring.kleur9}╗
{coloring.kleur12}║ \033[1m{coloring.kleur1}IN{coloring.kleur2}FOR{coloring.kleur3}MA{coloring.kleur4}TI{coloring.kleur5}ON
{coloring.kleur13}║  
{coloring.kleur1}║\033[0m {coloring.kleur9}Validity: \033[0m{coloring.kleur7}{valid}
{coloring.kleur1}║\033[0m {coloring.kleur9}Card: \033[0m{coloring.kleur7}{card}
{coloring.kleur2}║\033[0m {coloring.kleur9}Type: \033[0m {coloring.kleur7}{type}
{coloring.kleur3}║ \033[0m{coloring.kleur9}Prepaid: \033[0m {coloring.kleur7}{prepaid}
{coloring.kleur4}║\033[0m {coloring.kleur9}Country: \033[0m {coloring.kleur7}{country}
{coloring.kleur5}║\033[0m {coloring.kleur9}Bank: \033[0m {coloring.kleur7}{bank}
{coloring.kleur6}║\033[0m {coloring.kleur9}Bank URL: \033[0m {coloring.kleur7}{url}
{coloring.kleur7}║\033[0m {coloring.kleur9}City: \033[0m {coloring.kleur7}{city}
{coloring.kleur8}║\033[0m {coloring.kleur9}Phone: \033[0m {coloring.kleur7}{phone}
{coloring.kleur8}║\033[0m {coloring.kleur9}Currency: \033[0m {coloring.kleur7}{currency}
{coloring.kleur4}╚═{coloring.kleur3}══{coloring.kleur2}══{coloring.kleur1}════{coloring.kleur2}═════{coloring.kleur3}═══{coloring.kleur4}══{coloring.kleur5}═══{coloring.kleur6}═══{coloring.kleur7}═══{coloring.kleur8}═══{coloring.kleur9}╝

""")
if __name__ == '__main__':
    detector()
    start_check = th.Thread(target=start(api))   
    start_check.start()
    start_check.join()
