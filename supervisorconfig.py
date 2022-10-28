import os
 #counts
fullfilecount_workterms=0
fullfilecount_assignment=0
fullfilecount_assignmentsupervisor=0

#relative paths
lookupfilepath = os.path.relpath("SupervisorLookup/Lookup.txt")
fullfilepath = os.path.relpath("SupervisorFullFile/FullFile.dat", start=os.curdir)

tempfilepath = os.path.relpath("SupervisorTempFiles")
tempworktermsfilepath = os.path.relpath("SupervisorTempFiles/worktermstemp.txt")
tempassignmentfilepath = os.path.relpath ("SupervisorTempFiles/assignmenttemp.txt")
tempassignmentsupervisorfilepath = os.path.relpath ("SupervisorTempFiles/assignmentsupervisortemp.txt")

finalfilepath = os.path.relpath("SupervisorFinalFiles")
finalfilespacespath = os.path.relpath("SupervisorFinalFiles/final_file_spaces.dat")
finaldatfilepath=os.path.relpath("SupervisorFinalFiles/SupervisorparsedfromSBX.dat")
finallogfilepath=os.path.relpath("SupervisorFinalFiles/Log.txt")