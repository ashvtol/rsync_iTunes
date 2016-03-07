# rsync_iTunes

Sync Music from iTunes to your Android Device


###What does this program do ?
Pushes all the songs that are not on your phone to your android device. Provides rsync like functionality without the need of setting up a SSH server.

That is what this program does!

###How to run it ?

 Prerequisite installation/requirements

 1. Android Stand-alone SDK Tools only link <a href="http://developer.android.com/sdk/installing/index.html">here</a>
 2. Python v.3.X
 3. Make Utility
 4. Linux/Unix based environment to support shell scripts


 After you installed 1. Android Stand-alone SDK Tools place it you Documents folder, make sure to set the adb path, this is how it's done on a MAC
 ```
 1. Open Your Terminal

 2. cd ~/
 3. vim .bash_profile
 paste this with your user name in place inside .bash_profile

 -> export PATH=$PATH:/Users/"__Your__user__name"/Documents/android-sdk-macosx/platform-tools

 4. Save the profile and restart it.

 ```

 Try running 'adb' command in your terminal, you should see adb running.
 Run 'adb devices' to see the list of connected devices.

 If you've reached till here, then it's a cake-walk from here.
 1. Download the repository and unzip it.
 2. In terminal, navigate to the unzipped folder.

 ### YOU CAN EITHER RUN ```_credentials_.py``` using python3 
 ```
 In your terminal, just hit
 
 python3 _credentials_.py

you will be prompted to give your Username & DESTINATION_TO_COPY
 ```
Caution
 ```
 DESTINATION_TO_COPY ->storage/sdcard1/
 					  ->storage/sdcard0/
 					  ->storage/emulated/0
 					  ->storage/9016-4EF/ (this was mine ... can be used by USING ESPLORER)
 					 or whatever is the name of your sdcard.

 DESTINATION_TO_COPY can diifer on a LINUX machine, to know your destination(after you connected your phone), drag the folder(inside your phone, where you wish to copy) into the Linux terminal.
 ```

 ## OR MANUALLY do the following

1. You have to do is run the make command but before that provide the arguments to the files in the make file, suitable to your machine.
 ```
 Open make file and make the following changes:
 
 python3 _2_push_diffreneces_to_shell_.py" __YOUR__USER__NAME DESTINATION_TO_COPY
 
 Example:
 python3 _2_push_diffreneces_to_shell_.py theDragonSlayer storage/sdcard1/Music

 save the file and close it.
 ```	


2. Also, open ```get_phone_log.sh```
 replace DESTINATION_TO_COPY to your reqirements
 ```
 General: 

 adb shell find DESTINATION_TO_COPY -name *.mp3* > phone_log 

 Example:

 existing:

 adb shell find /storage/9016-4EF8/Music -name *.mp3* > phone_log 
 adb shell find /storage/9016-4EF8/Music -name *.m4a* >> phone_log 

 modified: 
 adb shell find storage/sdcard1/Music -name *.mp3* > phone_log 
 adb shell find storage/sdcard1/Music -name *.m4a* >> phone_log 

 ```

3. When even-ever you feel to copy the new songs in your library, all you gotta do is
 navigate to the musync solder in the terminal
 ```
 just hit:

 make
 ```
 If _2_push_diffreneces_to_shell_.py runs successfully then you should see the output
 that appears something like this:
 <img src="https://github.com/ashvtol/musync/blob/master/images/terminal.png" width="595px"></img>

 Final Output, after the new songs are pushed:
 <img src="https://github.com/ashvtol/musync/blob/master/images/end.png" width="595px"></img>

 That's it folks. Fork it! ..... 
 Feel free to ask anything.




