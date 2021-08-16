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


############################
#
#
#
#This file processes the output from DTLR and randomly selects some optimal resolutions.
#
#
#
############################


#from cStringIO import StringIO
import unittest
import glob

import random
import sys
import sys
import os
from shutil import copyfile
import shutil

numberofsampling = 100
listofinput = ["0"]
listofinput = sys.argv
tmpdir  =  listofinput[2]

copyfile("./temp.txt",tmpdir+"/temp.txt")
copyfile("./Ranger-DTL.linux",tmpdir+"/Ranger-DTL.linux")
numberofsampling = int(listofinput[3])
outputfile = listofinput[4]
tempinputfilename = listofinput[5]
ffselectedresolution = open("./allselectedresolution.txt", 'a')

Inputfilename =  listofinput[1]
listofinputlines=[]

#Reading output of DTLRF1 file#
with open(Inputfilename, "r") as ins:

  for line in ins:
      listofinputlines.append(line)

indexofspeciestree =listofinputlines.index("Species Tree:\n")
speciesetree =  listofinputlines[indexofspeciestree+1]

#index of start line of optimalresolution
indexofoptimalresolutions =listofinputlines.index("---------------- Optimal resolutions ----------------\n")

#index of end line of optimalresolution
numberofoptimalresolution = len(listofinputlines)-7 - indexofoptimalresolutions



# Randomely select optimal resolution from output of DTLRF1
if(numberofoptimalresolution > numberofsampling):

	randomoptimalresolutions = random.sample(range(1, numberofoptimalresolution+1),numberofsampling)
	for i in range(numberofsampling):


		f1 = open(tmpdir+"/"+str(tempinputfilename)+"_R"+str(i), 'w+')
		f1.write(speciesetree)
		tempgenetree = listofinputlines[randomoptimalresolutions[i]+ indexofoptimalresolutions]
		tempgenetree = tempgenetree.replace(".","")
		f1.write(tempgenetree)
		ffselectedresolution.write(tempgenetree)


else:
	for i in range(0,numberofoptimalresolution):

		f1 = open(tmpdir+"/"+str(tempinputfilename)+"_R"+str(i+1), 'w+')
		f1.write(speciesetree)
		tempgenetree = listofinputlines[indexofoptimalresolutions+i+1]
		tempgenetree = tempgenetree.replace(".","")
		f1.write(tempgenetree)
		ffselectedresolution.write(tempgenetree)







