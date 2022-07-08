#alexei@alexei-VirtualBox:~$ sudo useradd -s /bin/bash -m -d /home/user1 user1

#alexei@alexei-VirtualBox:~$ ls /home

#alexei  user1

#alexei@alexei-VirtualBox:~$ sudo userdel user1 -r

#alexei@alexei-VirtualBox:~$ ls /home

#alexei

#alexei@alexei-VirtualBox:~$ sudo groupadd groupuser

#alexei@alexei-VirtualBox:~$ cat /etc/group | grep groupuser

#groupuser:x:1001:

#alexei@alexei-VirtualBox:~$ sudo useradd -s /bin/bash -m -d /home/user1 user1

#alexei@alexei-VirtualBox:~$ usermod -aG groupuser user1

#alexei@alexei-VirtualBox:~$ sudo usermod -aG groupuser user1

#alexei@alexei-VirtualBox:~$ cat /etc/group | grep groupuser

#groupuser:x:1001:user1

#alexei@alexei-VirtualBox:~$ cat /etc/group | grep user1

#groupuser:x:1001:user1

#user1:x:1002:

#alexei@alexei-VirtualBox:~$ id user1

#uid=1001(user1) gid=1002(user1) группы=1002(user1),1001(groupuser)

#alexei@alexei-VirtualBox:~$ sudo gpasswd -d user1 groupuser

#Удаление пользователя user1 из группы groupuser

#alexei@alexei-VirtualBox:~$ cat /etc/group | grep user1

#user1:x:1002:

#alexei@alexei-VirtualBox:~$ sudo usermod -aG sudo user1

#alexei@alexei-VirtualBox:~$ cat /etc/group | grep sudo

#sudo:x:27:alexei,user1

#alexei@alexei-VirtualBox:~$ sudo deluser user1 sudo

#Удаляется пользователь «user1» из группы «sudo» ...

#Готово.

#alexei@alexei-VirtualBox:~$ cat /etc/group | grep sudo

#sudo:x:27:alexei