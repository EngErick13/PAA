#!/bin/bash
from netmiko import ConnectHandler
from getpass import getpass
import os
import datetime

def openTxt_SetDevice (_nomeArquivo_):
    x = open(_nomeArquivo_, 'r')
    arquivo = x.readlines()
    x.close()
    output = net_connect.send_config_set(arquivo)
    output = "echo '" + output.replace("\n", "' >> log/log_"+str(datahora.day)+"_"+str(datahora.month)+"_"+str(datahora.year)+"_"+str(datahora.hour)+"h_"+str(datahora.minute)+"m_"+device[i]+".txt \n echo '") + " >> log/log_"+str(datahora.day)+"_"+str(datahora.month)+"_"+str(datahora.year)+"_"+str(datahora.hour)+"h_"+str(datahora.minute)+"m_"+device[i]+".txt'"
    os.popen(output)
    #print(output)
    return None
def import_txt_list (_nomeArquivo_):                                            #Função de coleta dos dados de arquivos e salvar em variávell lista
  o = open(_nomeArquivo_, 'r')
  temp = o.readlines()
  o.close()
  k=0
  lista=[]
  while k<=len(temp)-1:
    lista.insert(k,temp[k].replace("\n", ""))
    k=k+1
  return lista
def import_txt_list_to_dic (_nomeArquivo_):                                     #Função de coleta dos dados de arquivos e salvar em variávell dicionário
  o = open(_nomeArquivo_, 'r')
  temp = o.readlines()
  o.close()
  k=0
  lista = []
  dic = {}
  while k<=len(temp)-1:
    lista.insert(k,temp[k].replace("\n", ""))
    k=k+1
  k=0
  dic = {lista[k]: lista[k+1] for k in range(0, len(lista)-1, 2)}
  return dic
datahora = datetime.datetime.now()                                              #Coletando a hora e data atual
device = import_txt_list ('devices/DEVICE_GWC.txt')                                     #Importando os dados dos equipamentos a serem configurados
x = len(device)-1                                                               #Inicio da execução para a atualização dps prefixos lists trânsito de bordas
i = 0
while i<=x:
    device_conect = import_txt_list_to_dic ("devices/DEVICE_" + device[i] + ".txt")     #Importa os dados do Dicionário
    net_connect = ConnectHandler(**device_conect)                               #Realizar a conexão com o equipamento
    dados = "listas_prefix/PREFIX_T_v4_" + device[i] + ".txt"                                 #Adicionando os dados do arquivo IPv4 referente ao equipamento    
    openTxt_SetDevice(dados)                                                    #Chamando a função para envio ao equipamento com os dados IPv4
    dados = "listas_prefix/PREFIX_T_v6_" + device[i] + ".txt"                                 #Adicionando os dados do arquivo IPv6 referente ao equipamento                         
    openTxt_SetDevice(dados)                                                    #Chamando a função para envio ao equipamento com os dados IPv6
    i=i+1
print("Rotina Finalizada!")