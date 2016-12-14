import os
import glob
import sys
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
shell = open('./push.sh','wb')
shell.write(('\n').encode('utf-8'))
print(" ___________________________Files To be PUSHED___________________________");
counter = 1;
for filename in glob.glob('/Users/'+name+'/Music/iTunes/iTunes Media/Music/**/*.m*', recursive=True):
    name = filename
    path = parsepath(filename)
    name = name.split('/')

    try:
       plog[name[-1]]
        
    except KeyError:
        ## if key not found, update olog and push it to the device 
        ## i.e if the song is not found, push it to the device and update old_log
        
        ################## Printing the songs that needs to be pushed ##############
        #print(counter,". ", sep='', end='');
        print(printtoshell(name[-1]));
        ############################################################################

        ################## Writing to shell script and updating old_log ############	
        shell.write(('adb push -p ' + path + ' /'+phone_storage+'\n').encode('utf-8'));
        name = (name[-1] + '\n').encode('utf-8')
        updatedct = updatedct + 1;
print("|------------------------------------------------------------------------|");
final = "Total Files to be Pushed = " + str(updatedct);
print(printtoshell(final));
print("|________________________________________________________________________|");


#####################################################
#####################################################
#####################################################


#####################################################
################### File Close ######################
shell.write(("\necho '**********************AZ**********************' \n").encode('utf-8'))
shell.write(("  echo '*             File Transfer Complete         *'\n").encode('utf-8'))
shell.write(("echo   '**********************************************' \n").encode('utf-8'))
shell.close()
#####################################################


