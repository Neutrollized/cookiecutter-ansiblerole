import os
import sys
import random

# set env variable 'winrm_host_port' to a random in between 55986 and 59986
p = randint(55986, 59986)
os.environ["winrm_host_port"] = p
