username = ""
storage = ""

username = str(input("Enter your username  : "))
storage = str(input("Enter DESTINATION_TO_COPY : \n Note: It can be found using a file explorer on your phone such as ESPlorer\nDESTINATION_TO_COPY : "))



import subprocess, time
make = open('./Makefile','w')
get_phone_log = open('./get_phone_log.sh','w')


get_phone_log.write("adb shell find " + storage + " -name *.mp3* > phone_log \n")
get_phone_log.write("adb shell find " + storage + " -name *.m4a* >> phone_log \n")
get_phone_log.close()

make.write("all:\n")
make.write("\tsh get_phone_log.sh\n")
make.write("\tpython3 _2_push_diffreneces_to_shell_.py " + username +" " + storage + "\n")
# make.write("\tsh push.sh\n")
make.close()

p  = subprocess.Popen('make', stdout=subprocess.PIPE, shell=True)
print(p.stdout.read().decode())

make = open('./Makefile','w')
make.write("all:\n")
make.write("\tsh push.sh\n")
make.close()

p  = subprocess.Popen('make', stdout=subprocess.PIPE, shell=True)
print(p.stdout.read().decode())