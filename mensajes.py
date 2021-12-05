import csv
import webbrowser
import time
import datetime
import pyautogui as pg

with open('datos.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        time.sleep(2)
        numero = '+505' + row['celular']
        webbrowser.open("https://web.whatsapp.com/send?phone="+numero+"&text="+row['mensaje'])
        time.sleep(20)    
        pg.press('enter')
        time.sleep(5)
        pg.hotkey('ctrl', 'w')
        pg.press('enter')
