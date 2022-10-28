#description

#import custom modules
import re
import supervisorconfig
import supervisorparsingloops
import supervisorfinalwritefiles

#user input, confirm case
actionflag=True
while actionflag:
    global action
    action = input("Please input action to perform for Supervisor file. CaseSensitive: 'HIRE' 'REHIRE' 'MGR_CHANGE' : ")
    if action == "HIRE":
        actionflag = False
        print("You want to HIRE supervisor record to create a HIRE file with 3 metadatas.")
    elif action == "REHIRE":
        actionflag = False
        print("You want to REHIRE supervisor record to create a REHIRE file with 3 metadatas. Full file record has RH suffix.")
    elif action == "MGR_CHANGE":
        actionflag = False
        print("You want to create a MGR_CHANGE supervisor record to create a MGR_CHANGE supervisor file.")
    else:
        print("Please select one of the input actions")
        print (action)

confirmflag=True
while confirmflag:
    confirm= input("Please confirm 'Lookup.txt' file in supervisor lookup folder and 'FullFile.dat' in supervisor fullfile folder and enter 'Y': ")
    if confirm == "Y":
        confirmflag = False
    else:
        print(confirm)

#main parsing calls
if action == "HIRE":
    supervisorparsingloops.fullFileQuery()
    supervisorparsingloops.writeLogLookupFiles()
    supervisorparsingloops.hire()
    supervisorfinalwritefiles.writeHire()
    supervisorfinalwritefiles.writeLogTempFiles()
if action == "REHIRE":
    supervisorparsingloops.fullFileQuery()
    supervisorparsingloops.writeLogLookupFiles()
    supervisorparsingloops.rehire()
    supervisorfinalwritefiles.writeRehire()
    supervisorfinalwritefiles.writeLogTempFiles()



