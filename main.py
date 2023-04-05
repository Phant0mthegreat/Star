import random
import itertools
import string
import os
import time
import random
import math
import socket
import requests
import random 
import colorama
from colorama import Fore
from colorama import Style
from os import system
import sys
import time
import secrets
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
import random 



minusculo = "abcdefghijklmnopqrstuvxyz"


maiusculo = "ABCDEFGHIJKLMNOPQRSTUVXYZ"


numeros= "1234567890"


especiais= "!_-.;:[]()"


tudo = minusculo+maiusculo+numeros+especiais

while True:
  system('clear')
  print(Fore.MAGENTA + '''.▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄  
▐█ ▀. •██  ▐█ ▀█ ▀▄ █·
▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄ 
▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌
 ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀''')
  print('    Feito pôr: Phant0m The Great 🧪')
  print(Fore.RESET + '=' * 47)
  print(' ')
  print(Fore.MAGENTA +'[ENTER]', Fore.RESET + 'Para fazer sua senha.')
  a = input('>')
  print(' ')
  tamanho = int(input('(Apenas números inteiros) Digite o tamanho da senha: '))
  if tamanho > 70:
    print('O número máximo de características são 70.')
    print('Inicie o programa novamente.')
    exit()
  
  senha="".join(random.sample(tudo,tamanho))
  print("=========================================")
  print(Fore.MAGENTA + 'Senha gerada com sucesso !')
  print(Fore.RESET + "Senha: ", senha)
  
  print("=========================================")
  aa=input('Deseja fazer mais uma senha ? se sim, aperte em enter.')
