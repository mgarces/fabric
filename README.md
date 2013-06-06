fabric
======

My fabric files, for sysadmin


alias
======
I added this to my __.zshrc__ file (you can use __.bashrc__ to)

<code>
alias f="fab --fabfile=/Users/marco.garces/SysAdmin/fabric/fabfile.py \<br/>
             --skip-bad-hosts \ <br/>
             -i /Users/marco.garces/.ssh/keys/id_rsa \<br/>
             --parallel \<br/>
             --pool-size=20 \<br/>
             set_hosts"<br/>
</code>


suggestions
===========

This is a work in progress, and any help or suggestion is welcomed.

If you are a sysadmin, you can tell me in what cases you use fabric to automate your work.


mgarces [at] sysadmin [dot] pt
