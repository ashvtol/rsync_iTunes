import os
import glob
import sys
# name = "Az"
# phone_storage = "/storage/9016-4EF8/Music"
name = sys.argv[1];
phone_storage = sys.argv[2];

#####################################################
################## Print to shell ###################
def printtoshell(s):
	length = len(s);
	str = "|";
	# this -> "----------------------------Files to be pushed----------------------------" has a length of 74.
	# front "|" and back "|", so total space needed to add is 72.
	if(length<72):
		diff = 72-length;
		if(diff%2):
			for i in range(0,int(diff/2)):
				str = str + " ";
			str = str + s;
			for i in range(0,int(diff/2)+1):
				str = str + " ";
			str = str + "|";
		else:
			for i in range(0,int(diff/2)):
				str = str + " ";
			str = str + s;
			for i in range(0,int(diff/2)):
				str = str + " ";
			str = str + "|";
	return str;
#####################################################
#####################################################
#####################################################


#####################################################
################## Parse Path #######################
def parsepath(oldpath):
    path = "";
    for i in range(len(oldpath)):
        if(not((oldpath[i].isalnum()) or (oldpath[i]=='/') or (oldpath[i]=="."))):
            path = path +"\\"+oldpath[i] 
        else:
            path = path + oldpath[i];
    return path;       
#####################################################
#####################################################
#####################################################



#####################################################
############## Map the phone entries ################
with open('./phone_log',"r", encoding="utf-8") as f:
    plog = {}
    for line in f:
        line = line.strip();
        line = line.split('/');
        line = line[-1]
        plog.update({line:1})
f.close();
#####################################################
#####################################################
#####################################################


#####################################################
################# Remap Process #####################
updatedct = 0
shell = open('./del.sh','wb')
print(" ___________________________Files To be DELETE___________________________");
counter = 1;
com_dictionary = {}
for filename in glob.glob('/Users/'+name+'/Music/iTunes/iTunes Media/Music/**/*.m*', recursive=True):
    name = filename
    #path = parsepath(filename)
    name = name.split('/')
    com_dictionary.update({name[-1]:1})

for key in plog:
    try:
        com_dictionary[key]

    except KeyError:
        print(printtoshell(key));
        shell.write(('adb shell "rm -f' + ' /'+phone_storage+'/'+ parsepath((key))+'"\n').encode('utf-8'));
        #name = (name[-1] + '\n').encode('utf-8')
        updatedct = updatedct + 1;

print("|------------------------------------------------------------------------|");
final = "Total Files to be Deleted = " + str(updatedct);
print(printtoshell(final));
print("|________________________________________________________________________|");


#####################################################
#####################################################
#####################################################


#####################################################
################### File Close ######################
shell.write(("\necho '**********************AZ**********************' \n").encode('utf-8'))
shell.write(("  echo '*          File Modification Complete         *'\n").encode('utf-8'))
shell.write(("echo   '**********************************************' \n").encode('utf-8'))
shell.close()
#####################################################