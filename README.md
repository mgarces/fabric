fabric
======

My fabric files, for sysadmin


alias
======
I added this to my __.zshrc__ file (you can use __.bashrc__ to)

<code>
alias f="fab --fabfile=/Users/marco.garces/SysAdmin/fabric/fabfile.py --skip-bad-hosts -i /Users/marco.garces/.ssh/keys/id_rsa --parallel --pool-size=20 set_hosts"
</code>


this way
