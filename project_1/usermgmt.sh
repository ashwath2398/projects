#!/bin/bash

#user add new user
add_user() {
	read -p "enter username:" uname
	if id "$uname" &>/dev/null 
	then
		echo "user $uname already exist."
	else
		sudo useradd "$uname"
		read -p "enter password: " pword
		echo "$uname:$pword" | sudo  chpasswd
		echo "username $uname added successfully."
	fi
}

#user delete
user_del(){
	read -p "enter username to delete:" uname
	if id "$uname" &>/dev/null
	then
	sudo userdel $uname
	echo "username $uname has been deleted."
else
	echo "user $uname doesnt exist."
	fi

}

#list users
list_user(){
	echo list of users: 
	cut -d: -f1 /etc/passwd
}

#modify password
change_passwd(){
	read -p "enter username of which to change password:" username
	if id="$username" &>/dev/null
	then
		read -p "enter new password: " password
		echo "$username:$password" | sudo chpasswd
		echo password modified successfully
	else
		echo username does not exist
	fi
}

#take backup of this folder 	
create_backup(){
	src_dir="/home/ubuntu/ash/project_1"
	tgt_dir="/home/ubuntu/ash/project_1/backups"
	if [ -d "tgt_dir" ]
	then
		echo Directory already exists.
	else
		mkdir -p "$tgt_dir"
		echo "Directory did not exist, now created"
	fi
	backup_filename="backup_$(date +%d%m%Y_%H%M%S).tar.gz"
	tar -czvf "${tgt_dir}/${backup_filename}" "$src_dir" 
	echo "Backup created successfully: $backup_filename"
}

while true;do
	echo " "
	echo 1. add user
	echo 2. delete user
	echo 3. list users
	echo 4. modify password 
	echo 5. create backup of this script
	echo 6. exit
	read -p "enter your choice number: " choice

	case $choice in
		1) add_user ;;
		2) user_del ;;
		3) list_user ;;
		4) change_passwd ;;
		5) create_backup ;;
		6) exit ;;
esac
done
