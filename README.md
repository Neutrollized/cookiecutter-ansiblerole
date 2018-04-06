# cookiecutter-ansiblerole

cookiecutter Ansible role template with test-kitchen config for Linux (Red Hat) and Windows.  This is a modified/updated from one I use at work, but contains extra functionality (namely Windows Ansible testing with test-kitchen) that I've added as well as updates to the template to allow for Windows Ansible role...uh...stuff.

## Requirements

[cookiecutter](https://github.com/audreyr/cookiecutter)

[Python](https://www.python.org/downloads/) (required to run the post-Python script hook)

### For test-kitchen

inspec

test-kitchen

kitchen-vagrant

kitchen-ansible

#### Additional packages needed for Windows testing

kitchen-ansiblepush

[pywinrm](https://pypi.python.org/pypi/pywinrm)

If you want to see how the Windows testing works, check out my other [repo](https://github.com/Neutrollized/test-kitchen_windows-ansible-inspec)

### How to use

`cookiecutter https://github.com/Neutrollized/cookiecutter-ansiblerole`

```
repo_name [myrole]:
os_family [redhat]:
maintainer [Glen Yu]:
email [glen.yu@gmail.com]:
license [MIT]:
```

#### Notes

Acceptable `os_family` values would be: `redhat`, `debian`, and `windows`

For Windows: .kitchen.yml file will have a host winrm port randomly generated so you won't encounter port conflicts when trying to do multiple kitchen testing at the same time
