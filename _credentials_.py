#!/usr/local/bin/python3
import sys
username=""
storage=""
########### Declare two holders for username (OSX) and storage (destination on the phone). ###
try:
	########### Check if arguments are given while running. ##################################
	username = sys.argv[1];
	storage = sys.argv[2];

except IndexError:
	########### If not, assign defaults. #####################################################
	username = "Az"
	storage = "/storage/9016-4EF8/Music"

if(username=="" and storage==""):
	########### If arguments are not understood. #############################################
	########### Ask again for the same. ######################################################
	username = str(input("Enter your username  : "))
	storage = str(input("Enter DESTINATION_TO_COPY : \n Note: It can be found using a file explorer on your phone such as ESPlorer\nDESTINATION_TO_COPY : "))

else:
	########### If arguments are understood. #################################################
	print(username,"\n","Storing at:", storage,sep='');
	import subprocess, time
	make = open('./Makefile','w')
	get_phone_log = open('./get_phone_log.sh','w')

	########### Creating get_phone_log script to get the songs already on the Phone. #########
	########### This script will be executed in the Make file. ###############################
	get_phone_log.write("adb shell find " + storage + " -name *.mp3* > phone_log \n")
	get_phone_log.write("adb shell find " + storage + " -name *.m4a* >> phone_log \n")
	get_phone_log.close()

	########### Creating the Make file. ######################################################
	make.write("all:\n")
	make.write("\tsh get_phone_log.sh\n")
	make.write("\tpython3 _2_push_diffreneces_to_shell_.py " + username +" " + storage + "\n")
	make.close()

	########### Call to the make file. #######################################################
	########### This displays the process in the terminal as it gets executed. ###############
	p  = subprocess.Popen('make', stdout=subprocess.PIPE, shell=True)
	print(p.stdout.read().decode())

	
	########### Writing push.sh on to the Make file ##########################################
	make = open('./Makefile','w')
	make.write("all:\n")
	make.write("\tsh push.sh\n")
	make.close();
	p  = subprocess.Popen('make', stdout=subprocess.PIPE, shell=True)
	print(p.stdout.read().decode())

	make = open('./Makefile','w')
	make.write("all:\n")
	print("Want to Delete del_annoying_songs ? > Y/N");
	ans = str(input());
	if(ans == "n" or ans == "No" or ans == "0" or ans == "no"):
		make.close();
		print("Quiting ... ");
	else:
		make.write("\tclear\t\n\tpython3 del_annoying_songs.py " + username +" " + storage + "\n")
		make.write("\tsh del.sh\n")
		make.close()
	########### Make file rewritten, don't know why I did this. ##############################
	########### push.sh could have been written earlier in the make file #####################
	########### Call to the make file. #######################################################
	########### This displays the process in the terminal as it gets executed. ###############
		p  = subprocess.Popen('make', stdout=subprocess.PIPE, shell=True)
		print(p.stdout.read().decode())




