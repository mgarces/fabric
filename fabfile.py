__author__ = 'marco.garces'

from fabric.api import *

#config variables
hostsHome = '/Users/marco.garces/SysAdmin/fabric/hosts'
userNameDefault = "mgarces"

#configuring which hosts to operate. Full list
def set_hosts():
    env.hosts = open(hostsHome, 'r').readlines()
    env.user = userNameDefault

#simple operations, to test fabric
#hello world
def hello(name="world"):
    print("Hello %s!" % name)
#hostname
def host_name():
    run('hostname -s')
#host type
def host_type():
    run('uname -s')
#uptime
def uptime():
    run('uptime')

#slightly more advanced operations

#install package via yum
def install(pkg=None):
    if pkg is not None:
        env["pkg"] = pkg
    elif pkg is None and env.get("pkg") is None:
        env["pkg"] = prompt("Which package? ")
    sudo('yum install -y %s' % env["pkg"])

#show all network interfaces, or single one
def show_interfaces(iface=""):
    run('ip a s %s' % iface)
