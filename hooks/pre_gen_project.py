import os
import sys
from random import *
from cookiecutter.main import cookiecutter

# set env variable 'winrm_host_port' to a random in between 55986 and 59986
#p = randint(55986, 59986)
#os.environ["winrm_host_port"] = str(p)

cookiecutter(
    'cookiecutter-django',
    extra_context={'rand_winrm_port': randint(55986, 59986)}
)
