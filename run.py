#!/usr/bin/python3
import os
if(os.path.isfile('password')):
          os.system("chmod +x password")
          os.system("./password")
elif(os.path.isfile('main.py')):
          os.system('python3 main.py')
          
