





import supervisorconfig
import re
#from datetime import datetime
#global sysdate

#oracle format sysdate
#sysdate = (datetime.today().strftime('%Y/%m/%d'))

#write temp files in order into final file with spaces
def writeHire():
    with open(supervisorconfig.finalfilespacespath, "w+") as final_file_spaces:
        global loglength_workterms
        loglength_workterms=0
        with open(supervisorconfig.tempworktermsfilepath) as tempworkterms:
            for line in tempworkterms:
                final_file_spaces.write(line)
                loglength_workterms=loglength_workterms+1
        with open(supervisorconfig.tempassignmentfilepath) as tempassignment:
            for line in tempassignment:
                final_file_spaces.write(line)
        with open(supervisorconfig.tempassignmentsupervisorfilepath) as tempassignmentsupervisor:
            for line in tempassignmentsupervisor:
                final_file_spaces.write(line)

#read final file with spaces
    with open(supervisorconfig.finalfilespacespath, 'r+') as final_file_spaces:
        lines = final_file_spaces.readlines()

    #write final file
    with open(supervisorconfig.finaldatfilepath, 'w+') as final_file:
        final_file.seek(0)
        final_file.writelines(line for line in lines if line.strip())
        final_file.truncate()


#rehire. needs conversion to function and transfer of final file builds
def writeRehire():
    with open(supervisorconfig.finalfilespacespath, "w+") as final_file_spaces:
        global loglength_workterms
        loglength_workterms=0
        with open(supervisorconfig.tempworktermsfilepath) as tempworkterms:
            for line in tempworkterms:
                final_file_spaces.write(line)
                loglength_workterms=loglength_workterms+1
        with open(supervisorconfig.tempassignmentfilepath) as tempassignment:
            for line in tempassignment:
                final_file_spaces.write(line)
        with open(supervisorconfig.tempassignmentsupervisorfilepath) as tempassignmentsupervisor:
            for line in tempassignmentsupervisor:
                final_file_spaces.write(line)

#read final file with spaces
    with open(supervisorconfig.finalfilespacespath, 'r+') as final_file_spaces:
        lines = final_file_spaces.readlines()

    #write final file
    with open(supervisorconfig.finaldatfilepath, 'w+') as final_file:
        final_file.seek(0)
        final_file.writelines(line for line in lines if line.strip())
        final_file.truncate()

def writeLogTempFiles():
    with open(supervisorconfig.finallogfilepath, "a+") as log:
        log.write("\n" + str(loglength_workterms) + " records in workterms")