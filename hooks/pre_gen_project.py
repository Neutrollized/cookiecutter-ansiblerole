import os
import sys
from random import *

#context = {{cookiecutter}}
#context['rand_winrm_port'] = {{cookie.cutter.rand_winrm_port}}
# set env variable 'rand_winrm_port' to a random in between 55986 and 59986
p = randint(55986, 59986)
#os.environ["rand_winrm_port"] = str(p)

#cookiecutter(
#    'cookiecutter-ansiblerole',
#    extra_context={'rand_winrm_port': randint(55986, 59986)}
#)
