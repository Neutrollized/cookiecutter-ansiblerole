import os
import sys


# listing directories
#print "The current working dir is: %s" %os.getcwd()

# listing directories
#print "The dir contains: %s" %os.listdir(os.getcwd())


# if it's a redhat/linux role, remove test/ansible.cfg
if "{{ cookiecutter.os_family | lower }}" == "redhat":
  os.chdir("test")
  os.remove("ansible.cfg")


# listing directories after removing path
#print "The dir now contains: %s" %os.listdir(os.getcwd())
