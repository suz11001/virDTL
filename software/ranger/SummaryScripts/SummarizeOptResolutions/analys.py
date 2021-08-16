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
#This file finds binary and non-binary nodes of any optimal resolution.
#Any node on the path of non-binary node to its children is called bad binary and will not be considered as a binary node.
#
#
###############################

#from cStringIO import StringIO
import subprocess
import unittest
import glob
import sys


#get file name to write on it
listofinput = ["0"]
listofinput = sys.argv

Inputfilename =  listofinput[1]
DTLpostordersoftwareoutput = listofinput[2]
outputfilename = listofinput[3]
tmpdir = listofinput[4]

childofnonbinarynode = []
allchildofnonbinarynodes = [[]]
childofnonbinarynode1 = []
allchildofnonbinarynodes1 = [[]]



#find post order of number from DTL out put

listoflinesDTL=[]
nonbinarynodesDTL=[]
binarynodesDTL=[]
childrenofnonbinarynode = []
childrenofnonbinarynode1 = []

subtreenodesDTL = []
allsubtreenodesDTL = [[]]

subtreenodesDTLb = []
allsubtreenodesDTLb = [[]]
badbinary = []
allbadbinary = [[]]
with open(DTLpostordersoftwareoutput, "r") as ins:

    for line in ins:
        listoflinesDTL.append(line)


#find all child of non-binary nodes from output of DTLRF1
listoflinesDTLnonbinarytemp1 = listoflinesDTL.index('non-binary-nodes:\n')
listoflinesDTLbinarytemp1 = listoflinesDTL.index('all internal nodes of non-binary nodes:\n')
for tu in range(listoflinesDTLnonbinarytemp1+1, listoflinesDTLbinarytemp1-1):
  tempstring = listoflinesDTL[tu]
  tempstring= tempstring.replace("\n","")
  nonbinarynodesDTL.append(tempstring)

for tu in range(listoflinesDTLbinarytemp1+1, len(listoflinesDTL)):

  tempstring = listoflinesDTL[tu]
  tempstring= tempstring.replace("\n","")

  if(tempstring == "*"):
    childrenofnonbinarynode.append("new node")
    childrenofnonbinarynode1.append("new node")

  else:

    childrenofnonbinarynode.append(tempstring)
    childrenofnonbinarynode1.append(tempstring)

for x in range(0,len(childrenofnonbinarynode1)):
  st = str(childrenofnonbinarynode1[x])
  if(st != "new node"):
    badbinary.append(st)
  else:
    allbadbinary.append(badbinary)
    badbinary = []

badbinary = []

for x in range(len(nonbinarynodesDTL)-2,-1,-1):

  stemp1 =  nonbinarynodesDTL[x]
  for xy in range(x+1,len(nonbinarynodesDTL)):

    stemp2 =  nonbinarynodesDTL[xy]
    if(stemp1 in stemp2):

      temp1vector = []
      temp2vector = []
      index = 0
      for xz in range(0,len(childrenofnonbinarynode)):

        if (index == x):

          if childrenofnonbinarynode[xz] !="new node":
            temp1vector.append(str(childrenofnonbinarynode[xz]))
        if (index == x+1):
          break
        if (childrenofnonbinarynode[xz] == "new node"):
          index = index+1

      index = 0
      befor =""
      after = ""
      for xz in range(0,len(childrenofnonbinarynode)):

        if (index == xy):

          if childrenofnonbinarynode[xz] !="new node":

            temp2vector.append(str(childrenofnonbinarynode[xz]))
            if(stemp1 in str(childrenofnonbinarynode[xz])):
              befor , after = str(childrenofnonbinarynode[xz]).split(stemp1)

              del childrenofnonbinarynode[xz]
              if(befor!=""):
                childrenofnonbinarynode.insert(xz,befor)


              for q in range(0,len(temp1vector)):

                childrenofnonbinarynode.insert(q+xz,temp1vector[q])
              if(after != ""):
                childrenofnonbinarynode.insert(xz+len(temp1vector),after)


        if (index == xy+1):
          break
        if (childrenofnonbinarynode[xz] == "new node"):
          index = index+1


tempvec = []
allnodes = [[]]
for x in range(0,len(childrenofnonbinarynode)):
  if(childrenofnonbinarynode[x] != "new node"):
    tempvec.append(childrenofnonbinarynode[x])
  if(childrenofnonbinarynode[x] == "new node"):
    allnodes.append(tempvec)
    tempvec = []


f1 = open(outputfilename, 'a')

#find all child of non-binary nodes from output of DTLRF1 regaurdless of resolution and order
with open(Inputfilename, "r") as ins:
    listoflines = ["0"]
    for line in ins:
        listoflines.append(line)
del listoflines[0];

nodename = ["0"]
nodeevent = ["0"]
nodemapping = ["0"]
noderecipient = ["0"]


#find all child of non-binary nodes from output of DTLRF1
linetemp = listoflines.index('Gene Tree: \n')
linetempcopy = linetemp


originalinorder = listoflines[linetemp+1]

allpart = originalinorder.split(')')[0:-1]
postordernumberofonternalnodes = 2
length = 0

for x in range(0, len(allpart)):

  length = length + len(allpart[x])+1
  #print 'index :   ', originalinorder[length]
  allpart1 = allpart[x].split(',')[0:-1]
  t=len(allpart1)+postordernumberofonternalnodes
  #print t
  postordernumberofonternalnodes = t +1


#Find start line of file
linetemp = listoflines.index('Reconciliation:\n')
allnodesname = ["0"]
subtreenodes = ["0"]
allsubtreenodes = [["00","00"]]


correctpostorder = 0
for x in range(linetemp+1, len(listoflines)-3):


  Recipient = "-1"
  if("Recipient" in str(listoflines[x]) ):

    Recipient = "Recipient"+listoflines[x].split('Recipient')[1]
    #print Recipient
  if(':' in str(listoflines[x]) and listoflines[x].split(':')[1]  == " Leaf Node\n"):
    allnodesname.append(listoflines[x].split(':')[0])
  if(len(listoflines[x].split('=')) >1):
    #Find a node name  in post order
    pstordername = listoflines[x].split('=')[0]
    lcatemp1 =  listoflines[x].split('=')[1]

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
      nameplusdot = allnodesname[xy]+"."
      subtreenodes.append(nameplusdot)
    allsubtreenodes.append(subtreenodes)

    for xz1 in range(0,len(allnodes)):

      if (len(subtreenodes) > 0):

        numberofmathching = 0
        numberofmathching1 = 0
        vectorin = []
        vectorin1 = []
        if(len(allnodes[xz1]) > 0 ):
          for asd in range(0,len(allnodes[xz1])):
            vectorin.append(0)
            vectorin1.append(0)


        for xz3 in range(0,len(subtreenodes)):
          for xz2 in range(0,len(allnodes[xz1])):
            if subtreenodes[xz3] in allnodes[xz1][xz2] :
              vectorin[xz2] = vectorin[xz2] + 1
              numberofmathching1 = numberofmathching1+1
              break

        for xq in range(0,len(vectorin)):


          if vectorin[xq]+1 == len(str(allnodes[xz1][xq]).split('.')):
            numberofmathching = numberofmathching+1

        tempfindnonbinary=0

        vectorin1 = []
        if (numberofmathching >1 and numberofmathching < len(allnodes[xz1])):
          for xz3 in range(0,len(subtreenodes)):
            for xz2 in range(0,len(allbadbinary[xz1])):


              if subtreenodes[xz3] in allbadbinary[xz1][xz2] :
                vectorin1.append(xz2)

          if(len(set(vectorin1))>1):
            typeofnode = "bad binary"

        elif (numberofmathching ==1 and numberofmathching < len(allnodes[xz1])):
          for xm in range(0,len(vectorin)):
            if vectorin[xm]>0:
              tempfindnonbinary = tempfindnonbinary+1
          if(tempfindnonbinary>=2):
            typeofnode = "bad binary"

        if (numberofmathching == len(allnodes[xz1]) and numberofmathching>0 and numberofmathching1 == len(subtreenodes)):
          typeofnode = "nonbinary"

          break

    if typeofnode != "badddd binary":

      strings = ""

      #f1.write(typeofnode+",");
      #f1.write(str(subtreenodes)+",");

      event1 = listoflines[x].split(':')[1]
      event2 = event1.split(',')[0]
      #f1.write(event2+',')
      nodeevent.append(event2)


      mapping1 = listoflines[x].split('Mapping -->')[1]
      mapping2 = mapping1.split(',')[0]
      if (len(mapping2.split('\n')) >1):
        mapping2 = mapping2.split('\n')[0]
      #f1.write(mapping2+',')
      nodemapping.append(mapping2)
    strings = strings+ typeofnode+","+ str(subtreenodes)+","+event2+','+mapping2+','
    if Recipient != "-1":
        #f1.write(Recipient)
        strings = strings +Recipient
    #f1.write("\n")
    strings = strings +"\n"
    f1.write(strings)

del allnodesname[0];
#f1.write("**\n")
f1.write("**\n")

