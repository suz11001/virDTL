"""
*   Copyright (C) 2017 Misagh Kordi and Mukul S. Bansal (mukul.bansal@uconn.edu).
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



##############################
#
#
#
#This file prepares the output.
#
#
#
###############################


#from cStringIO import StringIO
import subprocess
import unittest
import glob
import sys
import os


def find_nth_character(str1, substr, n):
    pos = -1
    for x in range(n):
        pos = str1.find(substr, pos+1)
        if pos == -1:
            return None
    return pos


#get file name to write on it
listofinput = ["0"]
listofinput = sys.argv

outputfilenam =  listofinput[1]
binaryeventfile = listofinput[2]
binarymappingfile = listofinput[3]
nonbinaryeventfile = listofinput[4]
nonbinarymappingfile = listofinput[5]
tmpdir = listofinput[6]
inputfile = listofinput[7]
DTLRoutput = listofinput[9]
typeofDTLInput = listofinput[10]

ffnoneventnum = open("./nonbinaryeventnumber.txt", 'a')
ffnonmapnum = open("./nonbinarymappingnumber.txt", 'a')
ffbieventnum = open("./binaryeventnumber.txt", 'a')
ffbimapnum = open("./binarymappingnumber.txt", 'a')
ffnonrecnum = open("./nonbinaryRecipientnumber.txt", 'a')
ffbirectnum = open("./binaryRecipientnumber.txt", 'a')

selectedresolution=""

with open("./allselectedresolution.txt", "r") as ins:
  	for line in ins:
	    selectedresolution = selectedresolution+line


outputfilename = open(outputfilenam, 'a')
listofinputlines=[]


with open(inputfile, "r") as ins:
  	for line in ins:
	    listofinputlines.append(line)


linetemp = listofinputlines.index('Reconciliation:\n')
allnodesname = ["0"]
subtreenodes = ["0"]
allsubtreenodes = [["00","00"]]
postordern = []
for x in range(linetemp+1, len(listofinputlines)-3):


	if ':' in str(listofinputlines[x]) and listofinputlines[x].split(':')[1]  == " Leaf Node\n":
		allnodesname.append(listofinputlines[x].split(':')[0])


	if len(listofinputlines[x].split('=')) >1 :

		pstordername=listofinputlines[x].split('=')[0]
		postordern.append(pstordername)

		lcatemp1 =  listofinputlines[x].split('=')[1]

		lcatemp1 = lcatemp1.split(']')[0]

		lcatemp1 =  lcatemp1.split('[')[1]

		leftest =  lcatemp1.split(',')[0]

		rightest =  lcatemp1.split(',')[1]
		rightest = rightest.replace(" ","")


		startnode = allnodesname.index(leftest)
		endnode = allnodesname.index(rightest)

		subtreenodes = []
		typeofnode = "binary"
		for xy in range(startnode,endnode+1):
	  		nameplusdot = allnodesname[xy]
	  		subtreenodes.append(nameplusdot)
		allsubtreenodes.append(subtreenodes)

# Find percenage of event and mappign from tempfiles
listofinputlinesforgenetree = []
with open(outputfilenam, "r") as ins:
	for line in ins:
		listofinputlinesforgenetree.append(line)


indexofgenetree =listofinputlinesforgenetree.index("Gene Tree1:\n")
genetreee=  listofinputlinesforgenetree[indexofgenetree+1]

listofinputlines = []
outputfilenamtemp = outputfilenam.replace(".txt","")
outputfilenamtemp = str(outputfilenamtemp)+".log"
with open(outputfilenamtemp, "r") as ins:
	for line in ins:
		listofinputlines.append(line)


outputfilename.write("\n\n")
for x in range(0,len(listofinputlines)-1):
	if(len(listofinputlines[x])>2):
		typeofN=listofinputlines[x].split(':')[0]
		tem1 = listofinputlines[x].split(':')[1:2]
		tem1 = tem1[0].split("Event")[0]
		otherinfo = str("Event " +listofinputlines[x].split("Event")[1])

		tem1 = tem1.replace(".","")

		tem2 = tem1.split(',')[0:-1]

		for xz in range(0,len(tem2)):
			tem2[xz] = tem2[xz].replace(" ","")
			tem2[xz] = tem2[xz].replace(" ","")
		orderingenetree = []
		for xc in range(0,len(tem2)):
			tem2[xc] = tem2[xc].strip("'")
			indexofnode = genetreee.find(str(tem2[xc]))
			orderingenetree.append(indexofnode)


		substring1 =  genetreee[min(orderingenetree)-1: genetreee.find(')',max(orderingenetree))+1]
		indexminus = 1


		while genetreee[min(orderingenetree)-1-indexminus] == '(':
			indexminus = indexminus+1
		substring =  genetreee[min(orderingenetree)-1: ]
		indexminus = indexminus-1
		substring4 =  genetreee[min(orderingenetree)-1- indexminus: ]

		numberofopenprantesis = genetreee[min(orderingenetree)-1- indexminus: genetreee.find(')',max(orderingenetree))+1 ].count('(')
		numberofopenprantesis = genetreee[min(orderingenetree)-1- indexminus: genetreee.find(')',max(orderingenetree))+1 ].count('(')

		tempppp = substring4.find(':',find_nth_character(substring4,')',numberofopenprantesis))
		tempp0 = substring4[min(orderingenetree)-1- indexminus:tempppp]

		tempp1 = genetreee[max(orderingenetree): genetreee.find(')',max(orderingenetree))]
		tempp11 = genetreee[min(orderingenetree): genetreee.find(',',min(orderingenetree))]

		temp2 = tempp0[tempp0.find(tempp1):]
		if(temp2.find(',') != -1):
			temp3 = temp2[:temp2.find(',')+1]

		else:
			temp3 = temp2
		lastparantesis1 = temp3.count(')')
		temp4 = temp3[find_nth_character(temp3,')',lastparantesis1)+1:]


		if(temp4.find(':') != -1):
			temp4 = temp4[:temp4.find(':')]

		temp4 = substring4[find_nth_character(substring4,')',len(orderingenetree)-1)+1: find_nth_character(substring4,')',len(orderingenetree))]
		temp45 = substring4[find_nth_character(substring4,')',len(orderingenetree)-1)+1: substring4.find(',', find_nth_character(substring4,')',len(orderingenetree)-1))]


		if len(temp45) <len(temp4):
			temp4 = temp45
		temp4 = temp4.replace(';','')
		otherinfo1 = str(otherinfo[otherinfo.find("[")+1:otherinfo.find("]")])
		otherinfo10 =[]
		otherinfo10 = otherinfo1.split(',')[0:-1]
		maxnum = -1
		indexmaxnum  = "-1"
		differenteventtype = len(otherinfo10)
		numSpeciations = 0
		numDuplications = 0
		numTransfers = 0
		for x1 in range(0,len(otherinfo10)):
			xw1 = str(otherinfo10[x1])[str(otherinfo10[x1]).find(":")+1 :str(otherinfo10[x1]).find("%")]
			xw2 = str(otherinfo10[x1])[:str(otherinfo10[x1]).find(":") ]
			xw2 = 	xw2.replace(" ","")
			xw2 = 	xw2.replace(" ","")
			xw2 = 	xw2.replace(" ","")
			xw2 = 	xw2.replace(" ","")

			xw1 = str(int(float(xw1)))

			if xw2 == "Speciations":
				numSpeciations = xw1
			if xw2 == "Transfers":
				numTransfers = xw1
			if xw2 == "Duplications":
				numDuplications = xw1

			if(int(xw1) > int(maxnum)):
				maxnum = xw1
				indexmaxnum = xw2


		otherinfo = str(otherinfo)[otherinfo.find("]")+1:]
		otherinfo1 = str(otherinfo[otherinfo.find("[")+1:otherinfo.find("]")])
		otherinfo10 =[]
		otherinfo10 = otherinfo1.split(',')[0:-1]
		maxnum1 = -1
		indexmaxnum1 = "-1"
		for x1 in range(0,len(otherinfo10)):
			xw1 = str(otherinfo10[x1])[str(otherinfo10[x1]).find(":")+1 :str(otherinfo10[x1]).find("%")]
			xw2 = str(otherinfo10[x1])[:str(otherinfo10[x1]).find(":") ]
			xw1 = str(int(float(xw1)))
			if(int(xw1) > int(maxnum1)):
				maxnum1 = xw1
				indexmaxnum1 = xw2
		otherinfoR = str(otherinfo)[otherinfo.find("]")+1:]
		otherinfo1R = str(otherinfoR[otherinfoR.find("[")+1:otherinfoR.find("]")])
		otherinfo10R =[]
		otherinfo10R = otherinfo1R.split(',')[0:-1]
		numberofrecipe = len(otherinfo10R)
		maxnum1R = -1
		indexmaxnum1R = "-1"
		for x1 in range(0,len(otherinfo10R)):
			xw1 = str(otherinfo10R[x1])[str(otherinfo10R[x1]).find(":")+1 :str(otherinfo10R[x1]).find("%")]
			xw2 = str(otherinfo10R[x1])[:str(otherinfo10R[x1]).find(":") ]
			xw1 = str(int(float(xw1)))
			if(int(xw1) > int(maxnum1R)):
				maxnum1R = xw1
				indexmaxnum1R = xw2

		# For each node print event and mapping information
		indexmaxnum1R = indexmaxnum1R.replace(" ","")
		maxnum1R = str(maxnum1R).replace(" ","")
		indexmaxnum1 = indexmaxnum1.replace(" ","")
		maxnum1= maxnum1.replace(" ","")
		indexmaxnum = indexmaxnum.replace(" ","")
		tempp11 = tempp11.replace(".","")
		tempp1 = tempp1.replace(".","")
		typeofNN = "Binary"
		if typeofN == "nonbinary" :
			typeofNN = "Non-binary"
		outputfilename.write(temp4+" = LCA["+tempp11+", "+tempp1+"]: "+typeofNN+", [Speciations = "+str(numSpeciations) +"% "+ ", Duplications = "+ str(numDuplications)+"% "+ ", Transfers = " +str(numTransfers)+"%"+"], ")
		outputfilename.write(" [Most Frequent mapping --> "+indexmaxnum1+" ("+maxnum1+"%)")
		if maxnum1R != "-1" and indexmaxnum =="Transfers" :
			outputfilename.write(", Recipient --> "+indexmaxnum1R+" ("+maxnum1R+"%)]")
		else:
			outputfilename.write("]")

		if maxnum1R != "-1" and indexmaxnum =="transfer" :
			outputfilename.write(" ,Numberofdifferenrecipient-->"+str(numberofrecipe))
		outputfilename.write("\n")
		if typeofN == "binary":
			ffbimapnum.write(str(len(otherinfo10))+"\n")
			ffbieventnum.write(str(differenteventtype)+"\n")
			if(numberofrecipe > 0):
				ffbirectnum.write(str(numberofrecipe)+"\n")
		if typeofN == "nonbinary":
			ffnonmapnum.write(str(len(otherinfo10))+"\n")
			ffnoneventnum.write(str(differenteventtype)+"\n")
			if(numberofrecipe > 0):
				ffnonrecnum.write(str(numberofrecipe)+"\n")
		count = 0

		for i in range(0,len(tem2)):
			z = 0

			for xy in range(1,len(allsubtreenodes)):

				for xz in range(0,len(allsubtreenodes[xy])):
					if(str(allsubtreenodes[xy][xz]) in str(tem2[i])):
						count = count + 1
						z = 1
						break
				if z==1:
					break

binaryeventline=[]
binarymappingline=[]
nonbinaryeventline=[]
nonbinarymappingline=[]

with open(binaryeventfile, "r") as ins:

	for line in ins:
		line= line.replace("\n","")
		binaryeventline.append(line)

with open(binarymappingfile, "r") as ins:

	for line in ins:
		line= line.replace("\n","")
		binarymappingline.append(line)


with open(nonbinaryeventfile, "r") as ins:

	for line in ins:
		line= line.replace("\n","")
		nonbinaryeventline.append(line)

with open(nonbinarymappingfile, "r") as ins:

	for line in ins:
		line= line.replace("\n","")
		nonbinarymappingline.append(line)

sumtbinaryevent = 0

outputfilename.write("\n\n")


# print percentage of consistency for binary and non-binary nodes
count = 0
for x in range(0,len(binaryeventline)):
	if(str(int(float(binaryeventline[x]))) == str(100)):
		sumtbinaryevent = sumtbinaryevent + int(float(binaryeventline[x]))
		count = count +1
if(count>-1):
	outputfilename.write("Percentage of binary nodes with 100% percent events consistency = ")
	outputfilename.write((str(int((count*100)/len(binaryeventline))))+"\n")

sumtbinaryevent = 0
count = 0
for x in range(0,len(binarymappingline)):
	if(str(int(float(binarymappingline[x]))) == str(100)):
		sumtbinaryevent = sumtbinaryevent + int(float(binarymappingline[x]))
		count = count +1
if(count>-1):
	outputfilename.write("Percentage of binary nodes with 100% mapping consistency = ")
	outputfilename.write(str(int((count*100)/(len(binarymappingline))))+"\n")


sumtbinaryevent = 0
count = 0
for x in range(0,len(nonbinaryeventline)):
	if(str(int(float(nonbinaryeventline[x]))) == str(100)):
		sumtbinaryevent = sumtbinaryevent + int(float(nonbinaryeventline[x]))
		count = count +1
if(count>-1):
	outputfilename.write("Percentage of non-binary nodes with 100% event consistency = ")
	outputfilename.write(str(int((count*100)/(len(nonbinaryeventline))))+"\n")

sumtbinaryevent = 0
count = 0
for x in range(0,len(nonbinarymappingline)):
	if(str(int(float(nonbinarymappingline[x]))) == str(100)):
		sumtbinaryevent = sumtbinaryevent + int(float(nonbinarymappingline[x]))
		count = count +1
if(count>-1):
	outputfilename.write("Percentage of non-binary nodes with 100% mapping consistency = ")
	outputfilename.write(str(int((count*100)/(len(nonbinarymappingline))))+"\n")



outputfilename.write("\n\n----------------------Chosen optimal resolutions--------------------\n\n")


if int(typeofDTLInput )==0 :
	numberofinternalnodes =  selectedresolution.count('_')
	for x in range(1,numberofinternalnodes+1):
		startpoint = find_nth_character(selectedresolution,"_",1)
		endpoint1 = selectedresolution.find(',',startpoint)
		endpoint2 = selectedresolution.find(')',startpoint)
		if endpoint2 < endpoint1 and endpoint2!= -1:
			endpoint1 = endpoint2
		if endpoint1 < endpoint2 and endpoint2!= -1 and endpoint1== -1:
			endpoint1 = endpoint2
		#print  endpoint1,endpoint2,startpoint,selectedresolution[:startpoint]+  ""+  selectedresolution[endpoint1+1:]
		selectedresolution = selectedresolution[:startpoint]+  ""+  selectedresolution[endpoint1:]

outputfilename.write(selectedresolution)




listofinputlinesforgenetree = []
with open(outputfilenam, "r") as ins:
	for line in ins:
		listofinputlinesforgenetree.append(line)


indexofgenetree =listofinputlinesforgenetree.index("Gene Tree1:\n")
genetreee=  listofinputlinesforgenetree[indexofgenetree+1]

#os.remove(outputfilename.name)
f2 = open(outputfilename.name, 'w+')
for x in range(1,indexofgenetree-1):
	f2.write(listofinputlinesforgenetree[x])
for x in range(indexofgenetree+2, len(listofinputlinesforgenetree)):
	f2.write(listofinputlinesforgenetree[x])

f2.truncate()
