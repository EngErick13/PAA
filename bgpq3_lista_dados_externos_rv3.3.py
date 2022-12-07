#!/bin/bash
#################### DADOS SOBRE O SOFTWARE ####################
### AUTOR: ERICK FERNANDES
### ARQUIVOS NECESSÁRIOS ASN: ASN_T_v4_%device%.txt & ASN_T_v6_%device%.txt
### ARQUIVOS NECESSÁRIOS ROUTE POLICY NAME: RP_T_v4_%device%.txt & RP_T_v6_%device%.txt
### A variável %device% segue o padrão "Sigla Cidade + Sigla Site + Numeração da Borda" Ex: CAH-CCL-01
################################################################
import os
from time import sleep
def bgpq3 (_AS_,_InBGPQ3_,_prefix_):                        #Função que realiza a execução das consultas por meio da aplicação BGPQ3
  cmd = _InBGPQ3_ + " " + _AS_ + " >> " + _prefix_
  os.popen(cmd)
  sleep(1)
  return None

def bgpq3_del (_AS_,_InBGPQ3_,_prefix_):                        #Função que realiza a execução das consultas por meio da aplicação BGPQ3 
  os.popen(_InBGPQ3_ + " " + _AS_  + " > asn_del/temp_del.txt")
  sleep(1)
  lista = import_txt_list("asn_del/temp_del.txt")
  os.popen("echo " + lista[0] + " >> " + _prefix_)
  return None

def import_txt_list (_nomeArquivo_):                        #Função de coleta dos dados de arquivos e salvar em variávell lista
  o = open(_nomeArquivo_, 'r')
  temp = o.readlines()
  o.close()
  k=0
  lista=[]
  while k<=len(temp)-1:
    lista.insert(k,temp[k].replace("\n", ""))
    k=k+1
  return lista
device = import_txt_list ('devices/DEVICE_GWC.txt')                 #Chamando a função para coletar os dados de Devices
x = len(device)-1                                           #Inicio da execução para a atualização dps prefixos lists trânsito de bordas
i = 0
while i<=x:
  os.popen(" > listas_prefix/PREFIX_T_v4_" + device[i] + ".txt")          #Utilizado para zerar os dados do arquivo prefix_list_bgp_cah.txt
  os.popen(" > listas_prefix/PREFIX_T_v6_" + device[i] + ".txt")          #Utilizado para zerar os dados do arquivo prefix_list_ipv6_bgp_cah.txt
  #Alimentação das variáveis para execução IPv4
  in_bgpq3 = "bgpq3 -R 24 -Ul"                                            #Código para consultar ip-prefix modelo Huawei IPv4
  Prefix_List = "listas_prefix/PREFIX_T_v4_" + device[i] + ".txt"                 #Nome do arquivo a ser gerado
  ClienteASNv4 = import_txt_list ('asn_add/ASN_T_v4_' + device[i] + '.txt') #Leitura do arquivo dos Nomes das ASNs IPv4
  y=0                                                               #Rotina de repetição para executar a consulta de todos os clientes IPv4 com o While
  while y<=len(ClienteASNv4)-1:
   bgpq3 (ClienteASNv4[y],in_bgpq3,Prefix_List)
   y=y+1
 
  y=0
  lista = import_txt_list('asn_del/ASN_T_v4_DEL_' + device[i] + '.txt')
  while y<=len(lista)-1:
    bgpq3_del (lista[y],in_bgpq3,Prefix_List)
    y = y+1
  #Alimentação das variáveis para execução IPv6
  in_bgpq3 = "bgpq3 -R 48 -U6l"
  Prefix_List = "listas_prefix/PREFIX_T_v6_" + device[i] + ".txt"                   #Nome do arquivo a ser gerado
  ClienteASNv6 = import_txt_list ('asn_add/ASN_T_v6_' + device[i] + '.txt')   #Leitura do arquivo dos Nomes das ASNs IPv6
  y=0                                                                 #Rotina de repetição para executar a consulta de todos os clientes IPv6 com o While
  while y<=len(ClienteASNv6)-1:
   bgpq3 (ClienteASNv6[y],in_bgpq3,Prefix_List)
   y = y+1


  y=0
  lista = import_txt_list('asn_del/ASN_T_v6_DEL_' + device[i] + '.txt')
  while y<=len(lista)-1:
   bgpq3_del (lista[y],in_bgpq3,Prefix_List)
   y = y+1

  #print ("Foi executado o device: "+device[i])

  i=i+1
print("Dados coletados e atualizado a listagem de prefixos!")