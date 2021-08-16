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
#This file finds all events and mapping nodes for each of binary and non-binary node.
#
#
#
###############################

#from cStringIO import StringIO
import unittest
import glob
import sys

from collections import Counter
import os,sys



numberofallpossible = 100

#get file name to write on it
listofinput = ["0"]
listofinput = sys.argv

Inputfilename =  listofinput[1]
outputfilename = listofinput[2]
tmpdir = listofinput[3]

f1 = open('./binarymapping.txt', 'a')
f2 = open('./binaryevent.txt', 'a')
f3 = open("./nonbinarymapping.txt", 'a')
f4 = open("./nonbinaryevent.txt", 'a')
outputfilenamtemp = str(outputfilename)
outputfilenamtemp = outputfilenamtemp.replace(".txt","")
outputfilenamtemp = str(outputfilenamtemp)+".log"

f5 = open(outputfilenamtemp, 'a')



#vector for binary nodes that keep name ,mapping and event
binarynodesname = ["0"]
binarynodemapping = ["0"]
binarynodeevent = ["0"]
tempbinarynode = []
allbinarynodeinfo = allsubtreenodes = [["00","00","00"]]

#vector for non-binary nodes that keep name ,mapping and event
nonbinarynodesname = ["0"]
nonbinarynodemapping = ["0"]
nonbinarynodeevent = ["0"]
allnonbinarynodeinfo = [["00","00","00"]]


#Read input file line by line and add each line to listofinputlines
listofinputlines=[]
with open(Inputfilename, "r") as ins:

  for line in ins:
    if (str(line) != "**") :

      listofinputlines.append(line)




#add information of binary and non-binary node to allbinarynodeinfo and allnonbinarynodeinfo
for x in range(0, len(listofinputlines)):

  #find a type of node,binary or non-binary
  typeofnode = listofinputlines[x].split(',')[0]

  #add information of binary  node to allbinarynodeinfo
  if typeofnode == "binary" or  typeofnode == "nonbinary"  :
    c= 0
    Recipient = "-1"
    if "Recipient -->" in listofinputlines[x]:
      Recipient = listofinputlines[x].split("Recipient --> ")[1]
      Recipient = str(Recipient.replace("\n",''))

    tempname1 = str(listofinputlines[x].split(',')[1:-1])
    tempname2 = str(listofinputlines[x].split(',')[1:-1][-1])

    tempname3 = str(listofinputlines[x].split(',')[1:-1][-2])

    tempname1 = str(tempname1.split(']')[0])
    tempname1 = str(tempname1.split('[')[2])
    tempname1 = str(tempname1.replace('\"',''))
    tempbinarynode = []
    tempbinarynode1 = []

    tempbinarynode = []
    tempbinarynode.append(tempname1)

    tempbinarynode1.append(tempname2)
    tempbinarynode1.append(tempname3)
    tempbinarynode1.append(typeofnode)
    if  Recipient != "-1":
      tempbinarynode1.append(str(Recipient))



    tempbinarynode.append(tempbinarynode1)
    tempvectname = []
    tempvectname = tempname1.split(',')
    for xz in range(0, len(allnonbinarynodeinfo)):


      tempvectname11 = []
      tempvectname1 = []
      tempvectname11 = allnonbinarynodeinfo[xz][0]
      tempvectname1 = tempvectname11.split(',')
      tempint = 0
      for x in range(0,len(tempvectname1)):
        for xy in range(0,len(tempvectname)):

          if(tempvectname1[x] == tempvectname[xy] ):
            tempint = tempint+1



      if(tempint == len(tempvectname1) and tempint == len(tempvectname)):
        allnonbinarynodeinfo[xz].append(tempbinarynode1)

        break

      if(tempint != len(tempvectname) and xz == len(allnonbinarynodeinfo)-1):
        allnonbinarynodeinfo.append(tempbinarynode)

for xz in range(1, len(allnonbinarynodeinfo)):


  if len(allnonbinarynodeinfo[xz])>0:
    dupnum = 0
    spenum =0
    transnum = 0
    muxnum = 0
    sumnum = 0
    listmapping = []
    listrecipient= []

    #Find percenage of event and mapping for each node

    for xt in range(1,len(allnonbinarynodeinfo[xz])):

      if allnonbinarynodeinfo[xz][xt][1] == " Duplication":
        dupnum = dupnum + 1
      if allnonbinarynodeinfo[xz][xt][1] == " Speciation":
        spenum = spenum + 1
      if allnonbinarynodeinfo[xz][xt][1] == " Transfer":
        transnum = transnum + 1
      listmapping.append(allnonbinarynodeinfo[xz][xt][0])
      if(len(allnonbinarynodeinfo[xz][xt]) == 4):
        listrecipient.append(allnonbinarynodeinfo[xz][xt][3])
    count = Counter(listmapping)

    countmax = count.most_common(1)

    maxnum = max(dupnum,spenum,transnum)
    sumnum = dupnum+spenum+transnum

    if allnonbinarynodeinfo[xz][1][2] == "binary":


      f1.write(str((countmax[0][1]*100)/len(listmapping))+"\n");
      f2.write(str((maxnum*100)/sumnum)+"\n");
      f5.write("binary: "   )
      f5.write(allnonbinarynodeinfo[xz][0]+",     ")
      f5.write("Event:[  " )
      if(dupnum >0):
        f5.write("Duplications :"  +str((dupnum*100)/sumnum)+"% , " )
      if(spenum >0):
        f5.write("Speciations :"  +str((spenum*100)/sumnum)+"% , " )
      if(transnum >0):
        f5.write("Transfers :"  +str((transnum*100)/sumnum)+"% , " )
      f5.write("  ]  ," )
      f5.write("  Mapping [  " )
      for x in set(listmapping):
        f5.write( x+ " : "+ str((listmapping.count(x)*100)/len(listmapping))+"% , ")
      f5.write(" ]" )
      if len(listrecipient)>0:
        f5.write(" ,Recipient [" )
        for x in set(listrecipient):
          f5.write( x+ " : "+ str((listrecipient.count(x)*100)/len(listrecipient))+"% , ")
        f5.write(" ]" )


      f5.write("\n" )

    if allnonbinarynodeinfo[xz][1][2] == "nonbinary":

      f3.write(str((countmax[0][1]*100)/len(listmapping))+"\n");
      f4.write(str((maxnum*100)/sumnum)+"\n");
      f5.write("nonbinary: "   )
      f5.write(allnonbinarynodeinfo[xz][0]+",   ")
      f5.write("Event: [ " )
      if(dupnum >0):
        f5.write("Duplications :"  +str((dupnum*100)/sumnum)+"% , " )
      if(spenum >0):
        f5.write("Speciations :"  +str((spenum*100)/sumnum)+"% , " )
      if(transnum >0):
        f5.write("Transfers :"  +str((transnum*100)/sumnum)+"% , " )
      f5.write("  ]  ," )
      f5.write("  Mapping [  " )
      for x in set(listmapping):
        f5.write( x+ " : "+ str((listmapping.count(x)*100)/len(listmapping))+"% , ")
      f5.write(" ]" )
      if len(listrecipient)>0:
        f5.write(" ,Recipient [" )
        for x in set(listrecipient):
          f5.write( x+ " : "+ str((listrecipient.count(x)*100)/len(listrecipient))+"% , ")
        f5.write(" ]" )

      f5.write("\n" )

    if allnonbinarynodeinfo[xz][1][2] == "bad binary":


      f5.write("bad binary :"   )
      f5.write(allnonbinarynodeinfo[xz][0]+"\n\n")

f5.write("\n*********\n")



