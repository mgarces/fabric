__author__ = 'marco.garces'

from fabric.api import *

def set_hosts():
    env.hosts = open('/Users/marco.garces/SysAdmin/fabric/hosts', 'r').readlines()
    env.user = "mgarces"

def hello(name="world"):
    print("Hello %s!" % name)

def host_name():
    run('hostname -s')

def host_type():
    run('uname -s')

def uptime():
    run('uptime')

def install(pkg=None):.
    if pkg is not None:.
        env["pkg"] = pkg
    elif pkg is None and env.get("pkg") is None:.
        env["pkg"] = prompt("Which package? ")
    sudo('yum install -y %s' % env["pkg"])

def show_interfaces(iface=""):
    run('ip a s %s' % iface)
