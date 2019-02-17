import socket
import sys
from datetime import datetime
from time import *
print("""


,:oho/-.
   mMMMMMMMMMMMNmmdhy
   dMMMMMMMMMMMMMMMMMMs.
   +MMsohNMMMMMMMMMMMMMm/
   .My   .+dMMMMMMMMMMMMMh.
    +       :NMMMMMMMMMMMMNo
             ryMMMMMMMMMMMMMm:
              /NMMMMMMMMMMMMMy.
                .hMMMMMMMMMMMMMN+
                    ``-NMMMMMMMMMd-
                      /MMMMMMMMMMMs.
                       mMMMMMMMsyNMN/
                       +MMMMMMMo  :sNh.
                       +NMMMMMMm     yn/
                        oMMMMMMM.
                        -NMMMMMM+
                         +MMd/NMh
                          mMm -mN*
                          /MM  *h:
                           dM*   .
                           :M-
                            d:
                           -+

""")
print("coded by sofi")
ip=input("Enter IP :")
t1=datetime.now()
print("Scanning start for the target ip ===>  %s ..."% ip)
sleep(1)
try:
   
   
   host=socket.gethostbyaddr(ip)
   print(host)
except socket.herror:
   
   print("not found host name")
try:
   
  for port in range(0,65335):
     
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.settimeout(5)
     if (s.connect_ex((ip,port))==0):
        try:
         
         
           serv = socket.getservbyport(port)
        except socket.error:
         

          serv="not-found"
     
         
         
         
   
        
     
        print(("the PORT %s:OPEN  Service:%s  "%(port,serv)))
        s.close()
  t2=datetime.now()
  t3=t2-t1
  print("Scanning Completed Good By :)  %s!!"%t3)
  

        
except KeyboardInterrupt:
   print("You Pressed CTRL+C =====>think you for use the script :)<==== ")
   sys.exit
