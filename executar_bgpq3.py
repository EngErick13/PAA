#!/bin/bash
import os
import datetime

dhI = datetime.datetime.now()
os.system("python3.9 bgpq3_lista_dados_externos_rv3.3.py")
os.system("python3.9 netmiko_bgpq3_r1.2.py")
dhF = datetime.datetime.now()
print("Tempo total de execução: " + str(dhF-dhI))

