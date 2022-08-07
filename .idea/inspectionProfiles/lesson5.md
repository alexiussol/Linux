alexei@alexei-VirtualBox:~$ echo hello world > file1

alexei@alexei-VirtualBox:~$ ll

итого 120

drwxr-x--- 17 alexei alexei 4096 авг  6 21:37  ./

drwxr-xr-x  3 root   root   4096 июл  8 01:37  ../

-rw-------  1 alexei alexei 5927 июл 18 23:03  .bash_history

-rw-r--r--  1 alexei alexei  220 июн 25 13:27  .bash_logout

-rw-r--r--  1 alexei alexei 3771 июн 25 13:27  .bashrc

drwx------ 17 alexei alexei 4096 июл  7 22:38  .cache/

drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

-rw-rw-r--  1 alexei alexei   12 авг  6 21:37  file1

drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

-rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

drwx------  3 alexei alexei 4096 июн 25 13:40  .local/

-rw-r--r--  1 alexei alexei  807 июн 25 13:27  .profile

drwx------  4 alexei alexei 4096 июн 25 13:44  snap/

drwx------  2 alexei alexei 4096 июл  7 22:36  .ssh/

-rw-r--r--  1 alexei alexei    0 июн 25 14:24  .sudo_as_admin_successful

-rw-r-----  1 alexei alexei    5 авг  6 21:34  .vboxclient-clipboard.pid

-rw-r-----  1 alexei alexei    5 авг  6 21:34  .vboxclient-display-svga-x11.pid

-rw-r-----  1 alexei alexei    5 авг  6 21:34  .vboxclient-draganddrop.pid

-rw-r-----  1 alexei alexei    5 авг  6 21:34  .vboxclient-seamless.pid

-rw-------  1 alexei alexei 2655 июн 30 00:15  y

-rw-r--r--  1 alexei alexei  578 июн 30 00:15  y.pub

drwxr-xr-x  2 alexei alexei 4096 июн 25 13:40  Видео/

drwxr-xr-x  2 alexei alexei 4096 июн 25 13:40  Документы/

drwxr-xr-x  3 alexei alexei 4096 июн 25 13:44  Загрузки/

drwxr-xr-x  2 alexei alexei 4096 июн 25 13:40  Изображения/

drwxr-xr-x  2 alexei alexei 4096 июн 25 13:40  Музыка/

drwxr-xr-x  2 alexei alexei 4096 июн 25 13:40  Общедоступные/

drwxr-xr-x  3 alexei alexei 4096 июн 25 15:35 'Рабочий стол'/

drwxr-xr-x  2 alexei alexei 4096 июн 25 13:40  Шаблоны/

alexei@alexei-VirtualBox:~$ cat file1

hello world

alexei@alexei-VirtualBox:~$ cp file1 file2

alexei@alexei-VirtualBox:~$ cat file2

hello world

alexei@alexei-VirtualBox:~$ ln -s file1 file3

alexei@alexei-VirtualBox:~$ ll


-rw-rw-r--  1 alexei alexei   12 авг  6 21:37  file1

-rw-rw-r--  1 alexei alexei   12 авг  6 21:39  file2

lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

alexei@alexei-VirtualBox:~$ ln file1 file4

alexei@alexei-VirtualBox:~$ ll -i

1205962 drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

 280540 drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

1206367 -rw-rw-r--  2 alexei alexei   12 авг  6 21:37  file1

1206373 -rw-rw-r--  1 alexei alexei   12 авг  6 21:39  file2

1206329 lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

1206367 -rw-rw-r--  2 alexei alexei   12 авг  6 21:37  file4

1206340 drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

1206303 -rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

alexei@alexei-VirtualBox:~$ rm file1

alexei@alexei-VirtualBox:~$ ll -i

итого 124

1205962 drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

 280540 drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

1206373 -rw-rw-r--  1 alexei alexei   12 авг  6 21:39  file2

1206329 lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

1206367 -rw-rw-r--  1 alexei alexei   12 авг  6 21:37  file4

1206340 drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

alexei@alexei-VirtualBox:~$ cat file3

cat: file3: Нет такого файла или каталога

alexei@alexei-VirtualBox:~$ cat file2

hello world

alexei@alexei-VirtualBox:~$ cat file4

hello world

alexei@alexei-VirtualBox:~$ 

alexei@alexei-VirtualBox:~$ mv file2 file5

alexei@alexei-VirtualBox:~$ mv file4 file6

alexei@alexei-VirtualBox:~$ ll

итого 124

drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

-rw-rw-r--  1 alexei alexei   12 авг  6 21:39  file5

-rw-rw-r--  1 alexei alexei   12 авг  6 21:37  file6

drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

-rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

alexei@alexei-VirtualBox:~$ ln file5 hardlink5

alexei@alexei-VirtualBox:~$ ln file6 hardlink6

alexei@alexei-VirtualBox:~$ ll -i

итого 132

1179713 drwx------ 17 alexei alexei 4096 июл  7 22:38  .cache/

1205962 drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

 280540 drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

1206329 lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

1206373 -rw-rw-r--  2 alexei alexei   12 авг  6 21:39  file5

1206367 -rw-rw-r--  2 alexei alexei   12 авг  6 21:37  file6

1206340 drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

1206373 -rw-rw-r--  2 alexei alexei   12 авг  6 21:39  hardlink5

1206367 -rw-rw-r--  2 alexei alexei   12 авг  6 21:37  hardlink6

1206303 -rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

1205959 drwx------  3 alexei alexei 4096 июн 25 13:40  .local/

1188357 -rw-r--r--  1 alexei alexei  807 июн 25 13:27  .profile

alexei@alexei-VirtualBox:~$ mkdir temporary

alexei@alexei-VirtualBox:~$ ll

итого 136

drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

-rw-rw-r--  2 alexei alexei   12 авг  6 21:39  file5

-rw-rw-r--  2 alexei alexei   12 авг  6 21:37  file6

drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

-rw-rw-r--  2 alexei alexei   12 авг  6 21:39  hardlink5

-rw-rw-r--  2 alexei alexei   12 авг  6 21:37  hardlink6

-rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

drwx------  3 alexei alexei 4096 июн 25 13:40  .local/

-rw-r--r--  1 alexei alexei  807 июн 25 13:27  .profile

drwx------  4 alexei alexei 4096 июн 25 13:44  snap/

drwx------  2 alexei alexei 4096 июл  7 22:36  .ssh/

-rw-r--r--  1 alexei alexei    0 июн 25 14:24  .sudo_as_admin_successful

drwxrwxr-x  2 alexei alexei 4096 авг  6 21:50  temporary/

alexei@alexei-VirtualBox:~$ mv hardlink5 ./temporary

alexei@alexei-VirtualBox:~$ ll -i

1205962 drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

 280540 drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

1206329 lrwxrwxrwx  1 alexei alexei    5 авг  6 21:40  file3 -> file1

1206373 -rw-rw-r--  2 alexei alexei   12 авг  6 21:39  file5

1206367 -rw-rw-r--  2 alexei alexei   12 авг  6 21:37  file6

1206340 drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

1206367 -rw-rw-r--  2 alexei alexei   12 авг  6 21:37  hardlink6

1206303 -rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

1205959 drwx------  3 alexei alexei 4096 июн 25 13:40  .local/

1188357 -rw-r--r--  1 alexei alexei  807 июн 25 13:27  .profile

1205950 drwx------  4 alexei alexei 4096 июн 25 13:44  snap/

1206338 drwx------  2 alexei alexei 4096 июл  7 22:36  .ssh/

1206146 -rw-r--r--  1 alexei alexei    0 июн 25 14:24  .sudo_as_admin_successful

 538770 drwxrwxr-x  2 alexei alexei 4096 авг  6 21:54  temporary/

lexei@alexei-VirtualBox:~$ touch empty{1..2}

alexei@alexei-VirtualBox:~$ ll

итого 116

drwxr-x--- 17 alexei alexei 4096 авг  6 21:57  ./

drwxr-xr-x  3 root   root   4096 июл  8 01:37  ../

-rw-------  1 alexei alexei 5927 июл 18 23:03  .bash_history

-rw-r--r--  1 alexei alexei  220 июн 25 13:27  .bash_logout

-rw-r--r--  1 alexei alexei 3771 июн 25 13:27  .bashrc

drwx------ 17 alexei alexei 4096 июл  7 22:38  .cache/

drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

-rw-rw-r--  1 alexei alexei    0 авг  6 21:57  empty1

-rw-rw-r--  1 alexei alexei    0 авг  6 21:57  empty2

drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

chmod

0 - никаких прав;
1 - только выполнение;
2 - только запись;
3 - выполнение и запись;
4 -  только чтение;
5 - чтение и выполнение;
6 - чтение и запись;
7 - чтение запись и выполнение.

alexei@alexei-VirtualBox:~$ chmod 664 empty1

alexei@alexei-VirtualBox:~$ chmod 600 empty2

alexei@alexei-VirtualBox:~$ ll

итого 116

drwx------ 17 alexei alexei 4096 июл  7 22:38  .cache/

drwx------ 15 alexei alexei 4096 июл  7 22:38  .config/

drwxr-x---  2 root   root   4096 июн 25 14:56  desktop/

-rw-rw-r--  1 alexei alexei    0 авг  6 21:57  empty1

-rw-------  1 alexei alexei    0 авг  6 21:57  empty2

drwx------  2 alexei alexei 4096 июл  7 22:36  .gnupg/

-rw-------  1 alexei alexei   20 июл 18 22:39  .lesshst

drwx------  3 alexei alexei 4096 июн 25 13:40  .local/

-rw-r--r--  1 alexei alexei  807 июн 25 13:27  .profile

alexei@alexei-VirtualBox:~$ sudo groupadd developer

[sudo] пароль для alexei: 

alexei@alexei-VirtualBox:~$ sudo useradd -G developer user_1

alexei@alexei-VirtualBox:~$ sudo useradd -G developer user_2

alexei@alexei-VirtualBox:~$ grep developer /etc/group

developer:x:1002:user_1,user_2

alexei@alexei-VirtualBox:~$ mkdir developer

alexei@alexei-VirtualBox:~$ mkdir developer

alexei@alexei-VirtualBox:~$ tail /etc/group

pulse-access:x:132:

gdm:x:133:

lxd:x:134:alexei

alexei:x:1000:

sambashare:x:135:alexei

vboxsf:x:999:alexei

groupuser:x:1001:

developer:x:1002:user_1,user_2

user_1:x:1003:

user_2:x:1004:

alexei@alexei-VirtualBox:~$ cd developer

alexei@alexei-VirtualBox:~/developer$ echo hello world > file1

alexei@alexei-VirtualBox:~/developer$ ll

итого 12

drwxrwxr-x  2 alexei alexei 4096 авг  6 23:07 ./

drwxr-x--- 18 alexei alexei 4096 авг  6 22:32 ../

-rw-rw-r--  1 alexei alexei   12 авг  6 23:07 file1

alexei@alexei-VirtualBox:~/developer$ 

alexei@alexei-VirtualBox:~/developer$ chmod ugo+rwx file1

alexei@alexei-VirtualBox:~/developer$ ll

итого 12

drwxrwxr-x  2 alexei alexei 4096 авг  6 23:07 ./

drwxr-x--- 18 alexei alexei 4096 авг  6 22:32 ../

-rwxrwxrwx  1 alexei alexei   12 авг  6 23:07 file1*

alexei@alexei-VirtualBox:~/developer$ sudo chmod g+s ~/developer

lexei@alexei-VirtualBox:~/developer$ mkdir subdeveloper

alexei@alexei-VirtualBox:~/developer$ ll

итого 16

drwxrwsr-x  3 alexei alexei 4096 авг  6 23:23 ./

drwxr-x--- 18 alexei alexei 4096 авг  6 22:32 ../

-rwxrwxrwx  1 alexei alexei   12 авг  6 23:07 file1*

drwxrwsr-x  2 alexei alexei 4096 авг  6 23:23 subdeveloper/

alexei@alexei-VirtualBox:~/developer$ chmod 1777 ~/developer/subdeveloper

lexei@alexei-VirtualBox:~/developer$ cd
alexei@alexei-VirtualBox:~$ 

alexei@alexei-VirtualBox:~$ mkdir exersise6

alexei@alexei-VirtualBox:~$ cd exersise6

alexei@alexei-VirtualBox:~/exersise6$ touch file{1..2}

alexei@alexei-VirtualBox:~/exersise6$ ll

итого 8

drwxrwxr-x  2 alexei alexei 4096 авг  6 23:35 ./

drwxr-x--- 18 alexei alexei 4096 авг  6 23:32 ../

-rw-rw-r--  1 alexei alexei    0 авг  6 23:35 file1

-rw-rw-r--  1 alexei alexei    0 авг  6 23:35 file2

Калькулятор chmod:
Chmod 331 (chmod a + rwx, u-r, g-r, o-rw) устанавливает разрешения таким образом, 
чтобы (U) пользователь / владелец не мог читать, записывать и выполнять. (G) roup не может читать,
не может записывать и не может выполнять. (O) они не могут читать, не могут писать и не могут выполнять.

alexei@alexei-VirtualBox:~/exersise6$ cd

alexei@alexei-VirtualBox:~$ chmod 331 ~/exersise6

alexei@alexei-VirtualBox:~$ ls -la ./exersise6

ls: невозможно открыть каталог './exersise6': Отказано в доступе

alexei@alexei-VirtualBox:~$