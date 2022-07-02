#alexei@alexei-VirtualBox:~$ mkdir mentors

#alexei@alexei-VirtualBox:~$ mkdir students

#alexei@alexei-VirtualBox:~$ rm -rf mentors

#alexei@alexei-VirtualBox:~$ rm -rf students

#alexei@alexei-VirtualBox:~$ mkdir {mentors,students}

#alexei@alexei-VirtualBox:~$ cd mentors

#alexei@alexei-VirtualBox:~/mentors$ echo>mentors_list.txt

#alexei@alexei-VirtualBox:~/mentors$ cd

#alexei@alexei-VirtualBox:~$

#alexei@alexei-VirtualBox:~$ cd students

#alexei@alexei-VirtualBox:~/students$ echo>students_list.txt

#alexei@alexei-VirtualBox:~/mentors$ nano mentors_list.txt

#Elena Fedotova

#Roman Kislov

#Valentin Birukov

#alexei@alexei-VirtualBox:~/mentors$ cd

#alexei@alexei-VirtualBox:~$

#alexei@alexei-VirtualBox:~$ cd students

#alexei@alexei-VirtualBox:~/students$ nano students_list.txt

#Alexei Soloviev

#Nelli Molodkina

#Maxim Dudka

#Andrey Ushakov

#alexei@alexei-VirtualBox:~$ mv mentors_list.txt -t students

#alexei@alexei-VirtualBox:~$ rm -rf mentors

#alexei@alexei-VirtualBox:~$ mv students students_and_mentors

#alexei@alexei-VirtualBox:~$ rm -r students_and_mentors