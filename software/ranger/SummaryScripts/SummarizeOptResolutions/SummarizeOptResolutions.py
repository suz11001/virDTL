#!/usr/bin/python

"""
*   Copyright (C) 2017 Misagh Kordi, Soumya Kundu, and Mukul S. Bansal (mukul.bansal@uconn.edu).
*
*   This program is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

###################################
#
#
#
#This file parses the input command and calls DTLR and Ranger-DTL to find optimal resolutions and optimal reconciliations.
#It then finds the mapping and event assignment for each of binary and non-binary node.
#Finally, it prepares the output file.
#
#
#
####################################

from __future__ import print_function
import subprocess
#from cStringIO import StringIO
import unittest
import glob
import sys
import os
from shutil import copyfile
import shutil
import tempfile
import time
from datetime import datetime

start_time = datetime.now()

#write line by line on listoflines
def find_nth_character(str1, substr, n):
    pos = -1
    for x in range(n):
        pos = str1.find(substr, pos+1)
        if pos == -1:
            return None
    return pos

############

#prepare output file
def printfile(inputfile ,outputfileaddress ):

	listofinputlines=[]

	with open(inputfile, "r") as ins:
		for line in ins:
			listofinputlines.append(line)

	indexofspeciestree =listofinputlines.index("Species Tree:\n")
	speciesetree =  listofinputlines[indexofspeciestree+1]
	indexofgenetree =listofinputlines.index("Original Gene Tree:\n")
	genetree =  listofinputlines[indexofgenetree+1]

	f2 = open(outputfileaddress, 'w+')
	f2.write("Input file: "+inputgenetree+"\n")
	f2.write("Output file:  "+finaloutputfile+"\n")
	f2.write("Duplication cost: "+str(duplicationvalue)+"\t\t")
	f2.write("Loss cost: "+str(lossvalue)+"\t\t")
	f2.write("Transfer cost: "+str(transfervalue)+"\n")
	f2.write("Bootstrap cutoff value: "+str(bootsraptvalue)+"\n")

	f2.write("Number of random optimal resolutions chosen: "+str(numberofdiferrentoptimalresolution)+"\n")
	f2.write("Number of random optimal DTL reconciliations chosen per resolution: "+str(numberofdiferentreconciliation)+"\n")
	f2.write("\n\n------------ Reconciliation for Gene Tree 1 (rooted) -------------\n\n")

	f2.write("Species Tree:\n")
	f2.write(speciesetree+"\n")

	global typeofDTLInput
	typeofDTLInput = listofinputlines[len(listofinputlines)-1][0]

	genetreecopy = str(genetree)
	genetreec1 = str(genetree)

	numberofinternalnodes =  genetree.count(')')
	ind = -1
	for x in range(1,numberofinternalnodes+1):

		startpoint = find_nth_character(genetree,")",x)
		endpoint = startpoint+1
		genetree = genetree[:startpoint]+ ")m"+ str(x) +  genetree[endpoint:]

	f2.write("Gene Tree1:\n")
	f2.write(genetree+"\n")

	typeofDTLInput = "2"

	if int(typeofDTLInput) == 0 :
		numberofinternalnodes =  genetree.count('_')
		for x in range(1,numberofinternalnodes+1):
			startpoint = find_nth_character(genetree,"_",1)
			endpoint = find_nth_character(genetree,".",1)
			genetree = genetree[:startpoint]+  ""+  genetree[endpoint+1:]


	genetree = genetree.replace('.',"")
	f2.write("Gene Tree:\n")
	f2.write(genetree+"\n")

	listofinputlines[indexofgenetree+4] = listofinputlines[indexofgenetree+4].replace("Gene tree", "Gene Tree")
	f2.write(listofinputlines[indexofgenetree+2])
	f2.write(listofinputlines[indexofgenetree+3])
	f2.write(listofinputlines[indexofgenetree+4])
	f2.write(listofinputlines[indexofgenetree+5])
	f2.write(listofinputlines[indexofgenetree+6])
	f2.write(listofinputlines[indexofgenetree+7])
	listofinputlines[indexofgenetree+8] = listofinputlines[indexofgenetree+8].replace("Gene tree", "Gene Tree")
	f2.write(listofinputlines[indexofgenetree+8])
	f2.write(listofinputlines[indexofgenetree+9])

	f2.write("\n\n-------------------------------------------------------------------")

	return;

############


listofinput = ["0"]
listofinput = sys.argv
typeofDTLInput = 0

numberofdiferrentoptimalresolution = 100
numberofdiferentreconciliation = 100

callDTLResolutionsoftware = listofinput[1]
typeofcalling = 0
cleanup = 0


error = False
hel = False

#control input
if "-h" in listofinput or "--help" in listofinput:
	error = True
	hel = True
	print("-i, --input","       input file.\n")
	print("-o, --output","      output file.\n")
	print("-D","                Duplication cost [whole number only, defult value 2].\n")
	print("-T","                Transfer cost [whole number only, defult value 3].\n")
	print("-L","                Loss cost [whole number only, defult value 1].\n")

	print("--numSol","          Number of random optimal DTL reconciliations chosen per resolution [default value 100].\n")
	print("--numRes","          Number of random optimal resolutions to be chosen [default value 100].\n")
	print("-B","                Bootstrap cutoff value [whole number between 0 and 100 only,\n                   default value 80].\n")
	#print "-c, --cleanup","      remove all temporary files.\n"
	print("-h","                brief help message.\n")
	print("-q, --quiet","       no process output.\n")

if(hel != True):
	if "-R" in listofinput:
		typeofcalling = 1
	if "-c" in listofinput or "--cleanup" in listofinput:
		cleanup = 1
#	if "-q" in listofinput or "--quiet" in listofinput:
		#error = True

	#-i read input
	if "-i" in listofinput or "--input" in listofinput:

		if "--input" in listofinput:
			inputfilesign = listofinput.index("--input")
		else:
			inputfilesign = listofinput.index("-i")

		inputgenetree = listofinput[inputfilesign+1]
		tempinputfilename = inputgenetree

		#print "inputgenetree",inputgenetree
		if not(os.path.isfile(inputgenetree)):
			print("Can not find "+str(inputgenetree)+" file.")
			error = True

		with open(inputgenetree) as infile:
			lines = infile.readlines()

		invalid_input = False
		for i in range(1, len(lines)):
			if invalid_input:
				break
			tree = lines[i].split(")")
			for j in range(1, len(tree) - 1):
				if len(tree[j]) == 0:
					print("Invalid input file: Missing bootstrap support values on the gene tree")
					invalid_input = True
					error = True
					break
				elif tree[j][0].isdigit():
					pass
				else:
					print("Invalid input file: Missing bootstrap support values on the gene tree")
					invalid_input = True
					error = True
					break

	else:
		print("Please enter gene tree name after -i")
		error = True

	#-o
	if "-o" in listofinput or "--output" in listofinput:

		if "--output" in listofinput:
			finaloutputfilesign = listofinput.index("--output")
		else:
			finaloutputfilesign = listofinput.index("-o")

		finaloutputfile = listofinput[finaloutputfilesign+1]
	else:
		print("Please enter final output file after -o")
		error = True


	#-B
	if "-B" in listofinput:
		bootsraptvaluesign = listofinput.index(str("-B"))

		bootsraptvalue = listofinput[bootsraptvaluesign+1]
	else:

		bootsraptvalue = 80

	#-L
	if "-L"  in listofinput:
		lossvaluesign = listofinput.index(str("-L"))

		lossvalue = listofinput[lossvaluesign+1]
	else:

		lossvalue = 1

		#-D
	if "-D" in listofinput:
		duplicationvaluesign = listofinput.index(str("-D"))

		duplicationvalue = listofinput[duplicationvaluesign+1]
	else:

		duplicationvalue = 2

	#-T
	if "-T" in listofinput:
		transfervaluesign = listofinput.index(str("-T"))

		transfervalue = listofinput[transfervaluesign+1]
	else:

		transfervalue = 3

	#-N
	if "-N" in listofinput:
		printoptimalresolutionsign = listofinput.index(str("-N"))

		printoptimalresolutionvalue = listofinput[printoptimalresolutionsign+1]
	else:

		printoptimalresolutionvalue = 2147483647

	#number of diferrent optimal resolutions
	if "--numRes" in listofinput:
		numberofdiferrentoptimalresolutionindex = listofinput.index(str("--numRes"))

		numberofdiferrentoptimalresolution = listofinput[numberofdiferrentoptimalresolutionindex+1]

	#number of diferent reconciliation
	if "--numSol" in listofinput:
		numberofdiferentreconciliationindex = listofinput.index(str("--numSol"))

		numberofdiferentreconciliation = int(listofinput[numberofdiferentreconciliationindex+1])
############


	#Create tempfile and tempfolder
	if error == False:

		dirname, basename = os.path.split("./run.py")

		TempfileoutputforDTL = tempfile.NamedTemporaryFile( dir="./", delete = False)
		nameofTempfileoutputforDTL =  TempfileoutputforDTL.name

		Tempfileinput = tempfile.NamedTemporaryFile( dir="./", delete = False)
		nameofTempfileinput =  Tempfileinput.name

		tmpdir = tempfile.mkdtemp(prefix=str(finaloutputfile+"."), dir = "./")

		if os.path.isfile(finaloutputfile):
			os.remove(finaloutputfile)

		#Find optimal resolution by calling DTLRF1
		if typeofcalling > -1:

			subprocess.call([ "./DTLR" , '-i', str(inputgenetree), '-o',str(finaloutputfile), '-B',str(bootsraptvalue), '-L',str(lossvalue), '-D',str(duplicationvalue), '-T',str(transfervalue),  '-N',str(numberofdiferrentoptimalresolution)])
			os.rename(finaloutputfile,str(nameofTempfileoutputforDTL) )
		#Choose randon optilal resolution and random reconciliation

		try:
			subprocess.call(['python', "selectoptimalresolutions.py" ,str(nameofTempfileoutputforDTL),tmpdir,str(numberofdiferrentoptimalresolution),finaloutputfile, tempinputfilename])
			subprocess.call([ "./Ranger-DTL.linux" ,'-i', str(inputgenetree), '-o',nameofTempfileinput, '-q'])
			printfile(str(nameofTempfileoutputforDTL),finaloutputfile)

			for file in os.listdir(tmpdir):
				if "_R" in file:

					for ii in range(numberofdiferentreconciliation):

						rangerinput = str(tmpdir+"/"+file)
						rangeroutput = str(tmpdir+"/"+file+"_r"+str(ii)+'.txt')

						#Choose  random reconciliation

						subprocess.call([ "./Ranger-DTL.linux" ,'-i', rangerinput, '-o',rangeroutput, "--seed", str(ii+1) , "-q"])

						#Choose  binary and nonbinary nodes

						subprocess.call([ 'python',"./analys.py" ,rangeroutput,tmpdir+"/temp.txt",tmpdir+'/result0.txt' ,tmpdir])


			#Find event and mapping for binary and non-binary nodes

			subprocess.call([ 'python',"./distribution.py" ,tmpdir+'/result0.txt',finaloutputfile ,tmpdir])

			subprocess.call([ 'python',"./output.py" ,finaloutputfile ,'./binaryevent.txt','./binarymapping.txt','./nonbinaryevent.txt','./nonbinarymapping.txt',tmpdir,nameofTempfileinput,str(inputgenetree),nameofTempfileoutputforDTL,typeofDTLInput])

			end_time = datetime.now()
			listofinputlinesforgenetree = []
			listofinputlinesforgenetree1 = []
			with open(finaloutputfile, "r") as ins:
				for line in ins:
					listofinputlinesforgenetree.append(line)

				for x in range(1,len(listofinputlinesforgenetree)):
					line = listofinputlinesforgenetree[x]

					while line.find("_fa37JncCHryDsbzayy4cBWDxS22Jjz",0) != -1:
						pos1 = line.find("_fa37JncCHryDsbzayy4cBWDxS22Jjz",0)
						pos2 = line.find(",",pos1)
						pos3 = line.find(")",pos1)
						pos4 = line.find("]",pos1)
						if pos2 == -1:
							pos2 = len(line)+1
						if pos3 == -1:
							pos3 = len(line)+1
						if pos4 == -1:
							pos4 = len(line)+1
						minimum = min(pos4, pos2 , pos3)

						line = line.replace(line[pos1:minimum],"")

					listofinputlinesforgenetree1.append(line)
			f = open(finaloutputfile, 'w')
			for x in range(1,len(listofinputlinesforgenetree1)):
				f.write(listofinputlinesforgenetree1[x])

		except Exception as inst:
			print("Can not continue")
			#os.remove(finaloutputfile)
		finally:
			#Clean up temporary files and folders
			if os.path.isfile("./binaryeventnumber.txt"):
				os.rename("./binaryeventnumber.txt",tmpdir+"/binaryenentnumber.txt")
				os.rename("./binaryevent.txt",tmpdir+"/binaryevent.txt")
				os.rename("./binarymapping.txt",tmpdir+"/binarymapping.txt")
				os.rename("./binarymappingnumber.txt",tmpdir+"/binarymappingnumber.txt")
				os.rename("./binaryRecipientnumber.txt",tmpdir+"/binaryRecipientnumber.txt")
				os.rename("./nonbinaryevent.txt",tmpdir+"/nonbinaryenent.txt")
				os.rename("./nonbinaryeventnumber.txt",tmpdir+"/nonbinaryenentnumber.txt")
				os.rename("./nonbinarymapping.txt",tmpdir+"/nonbinarymapping.txt")
				os.rename("./nonbinarymappingnumber.txt",tmpdir+"/nonbinarymappingnumber.txt")
				os.rename("./nonbinaryRecipientnumber.txt",tmpdir+"/nonbinaryRecipientnumber.txt")
			os.remove("./allselectedresolution.txt")
			os.remove(nameofTempfileoutputforDTL)
			os.remove(Tempfileinput.name)
			outputfilenamtemp = finaloutputfile.replace(".txt","")
			outputfilenamtemp = str(outputfilenamtemp)+".log"
			if os.path.isfile(outputfilenamtemp):
				os.remove(outputfilenamtemp)
			os.remove("./temp.txt")
			shutil.rmtree(tmpdir)

