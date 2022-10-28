import re

#open read lines of full supervisor file
with open ("Supervisor_20222603_SBX.dat", "r") as file_object:
    lines = file_object.readlines()

#read and prepare employee IDs with _
eid_list_underscored=[]
with open("test_employee_ids_from_Evan.txt", "r") as employee_id_file:
    employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_"
        eid_list_underscored.append(eid_string)

print("There are" + str(len(eid_list_underscored)) + "employees in Evan's list")

#print("List of EIDs" + eid_list_underscored)

#test_eid="_" + str(7146)+ "_"
# pulls in all eids test_eid=str(7146)
count=0
wt_hire_count=0
wt_rehire_count=0
assgn_hire_count=0
assgn_rehire_count=0
assgnsup_hire_count=0
assgnsup_rehire_count=0
index=0

#create files
with open ("worktermstemp.txt", "w") as worktermstemp:
    worktermstemp.write("METADATA|WorkTerms|ActionCode|SourceSystemOwner|SourceSystemId|PeriodOfServiceId(SourceSystemId)|EffectiveEndDate|EffectiveLatestChange|EffectiveSequence|EffectiveStartDate|PrimaryWorkTermsFlag\n")
with open ("assignmenttemp.txt", "w") as assignmenttemp:
    assignmenttemp.write("METADATA|Assignment|SourceSystemOwner|SourceSystemId|PersonId(SourceSystemId)|ActionCode|EffectiveStartDate|EffectiveEndDate|EffectiveSequence|EffectiveLatestChange|WorkTermsAssignmentId(SourceSystemId)|AssignmentStatusTypeCode|PrimaryAssignmentFlag\n")
with open("assignmentsupervisortemp.txt", "w") as assignmentsupervisortemp:
    assignmentsupervisortemp.write("METADATA|AssignmentSupervisor|SourceSystemOwner|SourceSystemId|EffectiveStartDate|ActionCode|ManagerAssignmentNumber|ManagerPersonNumber|ManagerType|NewManagerPersonNumber|NewManagerType|PrimaryFlag|AssignmentId(SourceSystemId)|NewManagerAssignmentNumber\n")

#main parsing loop
for emp_id in eid_list_underscored:

#RH workterms loop
    for line in lines:
        if emp_id in line[30:42] and "WorkTerms" in line and len(line)>79:
    #historical action code find - positional action code        sliced_workterms_line = line[:17] + "HIRE|" + line[17:]
            sliced_workterms_line=re.sub(r"Terms\|","Terms|REHIRE",line)
            #print(sliced_workterms_line)
            with open ("worktermstemp.txt", "a") as worktermstemp:
                worktermstemp.write(sliced_workterms_line + "\n")
            #wt_rehire_count=wt_rehire_count+1
    #print("WT rehire count is " + str(wt_rehire_count))

#HIRE workterms loop
    for line in lines:
        if emp_id in line[30:44] and "WorkTerms" in line and len(line)<81:
            sliced_workterms_line=re.sub(r"Terms\|","Terms|HIRE",line)
            #print(sliced_workterms_line)
            with open("worktermstemp.txt", "a") as worktermstemp:
                worktermstemp.write(sliced_workterms_line + "\n")
#            wt_hire_count=wt_hire_count+1
#    print("WT hire count is " + str(wt_hire_count))

#assignment hire loop
    for line in lines:
        if emp_id in line[30:41] and "Assignment" in line and len(line) < 112:
            sliced_assignment_line = re.sub(r"\|20", "HIRE|20", line)
            #print(sliced_assignment_line)
            with open ("assignmenttemp.txt", "a") as assignmenttemp:
                assignmenttemp.write(sliced_assignment_line + "\n")
#            assgn_hire_count=assgn_hire_count+1
#    print("Assignment hire count is " + str(assgn_hire_count))

#assignment rehire loop
    for line in lines:
        if emp_id in line[30:41] and "Assignment" in line and len(line) > 112:
            sliced_assignment_line = re.sub(r"\|20", "REHIRE|20", line)
            #print(sliced_assignment_line)
            with open ("assignmenttemp.txt", "a") as assignmenttemp:
                assignmenttemp.write(sliced_assignment_line + "\n")
#            assgn_rehire_count=assgn_rehire_count+1
#    print("Assignment rehire count is " + str(assgn_rehire_count))

#assignment supervisor hire loop
    for line in lines:
        if emp_id in line[40:51] and "AssignmentSupervisor" in line and len(line)<123:
    #positional action code        sliced_assignmentsupervisor_line = line[:71] + "HIRE|" + line[71:]
            sliced_assignmentsupervisor_line = re.sub(r"\|E", "HIRE|E", line)
            #print(sliced_assignmentsupervisor_line)
            with open ("assignmentsupervisortemp.txt", "a") as assignmentsupervisortemp:
                assignmentsupervisortemp.write(sliced_assignmentsupervisor_line+ "\n")
 #           assgnsup_hire_count=assgnsup_hire_count+1
#    print("Assignment supervisor hire count is " + str(assgnsup_hire_count))

#assignment supervisor rehire loop
    for line in lines:
        if emp_id in line[40:51] and "AssignmentSupervisor" in line and len(line)>123:
            sliced_assignmentsupervisor_line = re.sub(r"\|E", "REHIRE|E", line)
            #print(sliced_assignmentsupervisor_line)
            with open ("assignmentsupervisortemp.txt", "a") as assignmentsupervisortemp:
                assignmentsupervisortemp.write(sliced_assignmentsupervisor_line + "\n")
#            assgnsup_rehire_count=assgnsup_rehire_count+1
#    print("Assignment supervisor rehire count is "+ str(assgnsup_rehire_count))
    #close files
#work_terms_file.close()
#assignment_file.close()
#assignment_supervisor_file.close()

temp_filenames = ["worktermstemp.txt", "assignmenttemp.txt", "assignmentsupervisortemp.txt"]
with open("Supervisor_Chris_HIRE.dat", "w") as final_file_spaces:
    for fname in temp_filenames:
        with open(fname) as infile:
            for line in infile:
                final_file_spaces.write(line)

with open ("Supervisor_Chris_HIRE.dat", 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.writelines(line for line in lines if line.strip())
    f.truncate()


#final_file = open('Supervisor_CJ_Test.dat', 'r')
#for line in final_file.readlines():
  #  if re.search('\S', line):
 #       print (line),
#final_file.close()

#with open('Supervisor_CJ_Test.dat','r+') as final_file:
#    for line in final_file:
#        if not line.isspace():
#            final_file.write(line)