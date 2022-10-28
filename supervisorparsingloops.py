import re
import supervisorconfig
import os

def fullFileQuery():
    #read in full file
    with open(supervisorconfig.fullfilepath, "r") as file_object:
        global full_file_lines
        full_file_lines = file_object.readlines()
        global log_length_of_fullfile
        log_length_of_fullfile = len(full_file_lines)
        #for line in full_file_lines:
        for line in full_file_lines:
            if "MERGE|WorkTerms" in line:
                supervisorconfig.fullfilecount_workterms=supervisorconfig.fullfilecount_workterms+1
            if "MERGE|Assignment" in line:
                supervisorconfig.fullfilecount_assignment=supervisorconfig.fullfilecount_assignment+1
            if "MERGE|AssignmentSupervisor" in line:
                supervisorconfig.fullfilecount_assignmentsupervisor=supervisorconfig.fullfilecount_assignmentsupervisor+1
    
def writeLogLookupFiles():
    with open(supervisorconfig.finallogfilepath, "w+") as log:
        log.write("Length of full file is: " + str(log_length_of_fullfile))
        log.write("\n\nNumber of WorkTerms records in the full file is: "+str(supervisorconfig.fullfilecount_workterms))
        log.write("\nNumber of PERSONNAME records in the full file is: " + str(supervisorconfig.fullfilecount_assignment))
        log.write("\nNumber of PERSONEMAIL records in the full file is: " + str(supervisorconfig.fullfilecount_assignmentsupervisor))
     


def hire ():
    #create files
    with open (supervisorconfig.tempworktermsfilepath, "w") as worktermstemp:
        worktermstemp.write("METADATA|WorkTerms|ActionCode|SourceSystemOwner|SourceSystemId|PeriodOfServiceId(SourceSystemId)|EffectiveEndDate|EffectiveLatestChange|EffectiveSequence|EffectiveStartDate|PrimaryWorkTermsFlag\n")
    with open (supervisorconfig.tempassignmentfilepath, "w") as assignmenttemp:
        assignmenttemp.write("METADATA|Assignment|SourceSystemOwner|SourceSystemId|PersonId(SourceSystemId)|ActionCode|EffectiveStartDate|EffectiveEndDate|EffectiveSequence|EffectiveLatestChange|WorkTermsAssignmentId(SourceSystemId)|AssignmentStatusTypeCode|PrimaryAssignmentFlag\n")
    with open(supervisorconfig.tempassignmentsupervisorfilepath, "w") as assignmentsupervisortemp:
        assignmentsupervisortemp.write("METADATA|AssignmentSupervisor|SourceSystemOwner|SourceSystemId|EffectiveStartDate|ActionCode|ManagerAssignmentNumber|ManagerPersonNumber|ManagerType|NewManagerPersonNumber|NewManagerType|PrimaryFlag|AssignmentId(SourceSystemId)|NewManagerAssignmentNumber\n")

    #read full file
    with open (supervisorconfig.fullfilepath, "r") as file_object:
        lines = file_object.readlines()

    #read and prepare employee IDs with _
    eid_list_underscored_workterms=[]
    with open(supervisorconfig.lookupfilepath, "r") as employee_id_file:
        employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_WT"
        eid_list_underscored_workterms.append(eid_string)

    eid_list_underscored_assignment=[]
    with open(supervisorconfig.lookupfilepath, "r") as employee_id_file:
        employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_ASG"
        eid_list_underscored_assignment.append(eid_string)

    eid_list_underscored_assignmentsupervisor=[]
    with open(supervisorconfig.lookupfilepath, "r") as employee_id_file:
        employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_EMP_SUP"
        eid_list_underscored_assignmentsupervisor.append(eid_string)


    print("There are " + str(len(eid_list_underscored_workterms)) + " employees in lookup file")
    
    #hire workterms parsing loops
    for emp_id in eid_list_underscored_workterms:
        for line in lines:
            if emp_id in line[32:52] and "WorkTerms" in line:
                sliced_workterms_line=re.sub(r"Terms\|","Terms|HIRE",line)
                with open(supervisorconfig.tempworktermsfilepath, "a") as worktermstemp:
                    worktermstemp.write(sliced_workterms_line + "\n")
                #wt_hire_count=wt_hire_count+1
                #print("WT hire count is " + str(wt_hire_count))

    #hire assignment parsing loops
    for emp_id in eid_list_underscored_assignment:
        for line in lines:
            if emp_id in line[32:52] and "Assignment" in line:
                sliced_assignment_line = re.sub(r"\|20", "HIRE|20", line)
                with open (supervisorconfig.tempassignmentfilepath, "a") as assignmenttemp:
                    assignmenttemp.write(sliced_assignment_line + "\n")
                #assgn_hire_count=assgn_hire_count+1
                #print("Assignment hire count is " + str(assgn_hire_count))

    #hire assignment supervisor parsing loops
    for emp_id in eid_list_underscored_assignmentsupervisor:
        for line in lines:
            if emp_id in line[40:64] and "AssignmentSupervisor" in line:
                sliced_assignmentsupervisor_line = re.sub(r"\|E", "HIRE|E", line)
                #print(sliced_assignmentsupervisor_line)
                with open (supervisorconfig.tempassignmentsupervisorfilepath, "a") as assignmentsupervisortemp:
                    assignmentsupervisortemp.write(sliced_assignmentsupervisor_line+ "\n")
                #assgnsup_hire_count=assgnsup_hire_count+1
                #print("Assignment supervisor hire count is " + str(assgnsup_hire_count))
                #print ("assignment supervisor EID search" + emp_id)
                #print ("sliced line" + sliced_assignmentsupervisor_line)


def rehire ():
    #create files
    with open (supervisorconfig.tempworktermsfilepath, "w") as worktermstemp:
        worktermstemp.write("METADATA|WorkTerms|ActionCode|SourceSystemOwner|SourceSystemId|PeriodOfServiceId(SourceSystemId)|EffectiveEndDate|EffectiveLatestChange|EffectiveSequence|EffectiveStartDate|PrimaryWorkTermsFlag\n")
    with open (supervisorconfig.tempassignmentfilepath, "w") as assignmenttemp:
        assignmenttemp.write("METADATA|Assignment|SourceSystemOwner|SourceSystemId|PersonId(SourceSystemId)|ActionCode|EffectiveStartDate|EffectiveEndDate|EffectiveSequence|EffectiveLatestChange|WorkTermsAssignmentId(SourceSystemId)|AssignmentStatusTypeCode|PrimaryAssignmentFlag\n")
    with open(supervisorconfig.tempassignmentsupervisorfilepath, "w") as assignmentsupervisortemp:
        assignmentsupervisortemp.write("METADATA|AssignmentSupervisor|SourceSystemOwner|SourceSystemId|EffectiveStartDate|ActionCode|ManagerAssignmentNumber|ManagerPersonNumber|ManagerType|NewManagerPersonNumber|NewManagerType|PrimaryFlag|AssignmentId(SourceSystemId)|NewManagerAssignmentNumber\n")

    #read full file
    with open (supervisorconfig.fullfilepath, "r") as file_object:
        lines = file_object.readlines()

    #read and prepare employee IDs with _
    eid_list_underscored_workterms_rh=[]
    with open(supervisorconfig.lookupfilepath, "r") as employee_id_file:
        employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_WT_RH"
        eid_list_underscored_workterms_rh.append(eid_string)

    eid_list_underscored_assignment_rh=[]
    with open(supervisorconfig.lookupfilepath, "r") as employee_id_file:
        employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_ASG_RH"
        eid_list_underscored_assignment_rh.append(eid_string)

    eid_list_underscored_assignmentsupervisor_rh=[]
    with open(supervisorconfig.lookupfilepath, "r") as employee_id_file:
        employee_ids=employee_id_file.readlines()
    for employee_id in employee_ids:
        employee_id=employee_id.rstrip()
        eid_string = "_" + str(employee_id) + "_EMP_SUP_RH"
        eid_list_underscored_assignmentsupervisor_rh.append(eid_string)

    print("There are" + str(len(eid_list_underscored_workterms_rh)) + "employees in lookup file")

    #workterms rehire loop
    for emp_id in eid_list_underscored_workterms_rh:
        for line in lines:
            if emp_id in line[31:49] and "WorkTerms" in line and len(line)>79:
            #historical action code find - positional action code        sliced_workterms_line = line[:17] + "HIRE|" + line[17:]
                sliced_workterms_line=re.sub(r"Terms\|","Terms|REHIRE",line)
                #print(sliced_workterms_line)
                with open (supervisorconfig.tempworktermsfilepath, "a") as worktermstemp:
                    worktermstemp.write(sliced_workterms_line + "\n")
                #wt_rehire_count=wt_rehire_count+1
                #print("WT rehire count is " + str(wt_rehire_count))

    #assignment rehire loop
    for emp_id in eid_list_underscored_assignment_rh:
        for line in lines:
            if emp_id in line[30:49] and "Assignment" in line and len(line) > 112:
                sliced_assignment_line = re.sub(r"\|20", "REHIRE|20", line)
                #print(sliced_assignment_line)
                with open (supervisorconfig.tempassignmentfilepath, "a") as assignmenttemp:
                    assignmenttemp.write(sliced_assignment_line + "\n")
                #assgn_rehire_count=assgn_rehire_count+1
                #print("Assignment rehire count is " + str(assgn_rehire_count))

    #assignment supervisor rehire loop
    for emp_id in eid_list_underscored_assignmentsupervisor_rh:
        for line in lines:
            if emp_id in line[40:64] and "AssignmentSupervisor" in line and len(line)>123:
                sliced_assignmentsupervisor_line = re.sub(r"\|E", "REHIRE|E", line)
                #print(sliced_assignmentsupervisor_line)
                with open (supervisorconfig.tempassignmentsupervisorfilepath, "a") as assignmentsupervisortemp:
                    assignmentsupervisortemp.write(sliced_assignmentsupervisor_line + "\n")
                #assgnsup_rehire_count=assgnsup_rehire_count+1
                #print("Assignment supervisor rehire count is "+ str(assgnsup_rehire_count))
   

#mgr change


    #close files
    #work_terms_file.close()
    #assignment_file.close()
    #assignment_supervisor_file.close()