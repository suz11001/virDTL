#!/usr/bin/python

"""
*   Copyright (C) 2017 Soumya Kundu and Mukul S. Bansal (mukul.bansal@uconn.edu).
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

from __future__ import division
from random import randint
from itertools import islice
import subprocess, shutil, os, sys, getopt

#------------------------------------------------------------------------------

# Defines the global variables:

os_name = sys.platform
input_file = ""
output_file = ""
duplication = ""
transfer = ""
loss = ""
seed = ""
seed_input = False
quiet = False
summary = False
dated = False
sample = 100
sample_input = False
input_args = []
directory = ""
dir_addr = ""
OptRoot_output = ""
num_optrootings = 0

#------------------------------------------------------------------------------

# Defines the main function:

def main(argv):

    try:
        arg_parsing(argv)
        run_OptRoot(argv)
        run_RangerDTL()
        run_AggregateRanger()
        conserved_clusters()
        summary_data()
        generate_output()

    finally:
        if directory != "":
            shutil.rmtree(directory)

#------------------------------------------------------------------------------

# Handles the input from the user:

def arg_parsing(argv):

    # Identifies all global variables updated in argument handling:

    global input_file
    global output_file
    global duplication
    global transfer
    global loss
    global seed
    global seed_input
    global quiet
    global summary
    global dated
    global sample
    global sample_input

    # Calls the help function of Ranger-DTL:

    help_call = ""
    if os_name.startswith("linux"):
        help_call = subprocess.Popen("./Ranger-DTL.linux -h".split(),
                    stdout=subprocess.PIPE)

    elif os_name.startswith("win32"):
        help_call = subprocess.Popen("./Ranger-DTL.win -h".split(),
                    stdout=subprocess.PIPE)

    elif os_name.startswith("darwin"):
        help_call = subprocess.Popen("./Ranger-DTL.mac -h".split(),
                    stdout=subprocess.PIPE)

    else:
        print("ERROR: Operating System Not Supported")
        sys.exit(2)
    help_output = help_call.communicate()[0]

    # Constructs the final output of the help function:

    help_final = ""
    if os_name.startswith("win32"):
        help_final = (help_output.decode("utf8").split("Usage:")[0] +
                      "Usage: SummarizeOptRootings.py [ARGUMENT]" +
                      help_output.decode("utf8").split("[ARGUMENT]")[1] +
                      "  -d, --dated                 use dated version of Ranger-DTL" +
                      "\n" +
                      "  -n, --sample                set the number of sampled optimal reconciliations for each rooting (default value 100)")

    else:
        help_final = (help_output.decode("utf8").split("Usage:")[0] +
                      "Usage: ./SummarizeOptRootings.py [ARGUMENT]" +
                      help_output.decode("utf8").split("[ARGUMENT]")[1] +
                      "  -d, --dated                 use dated version of Ranger-DTL" +
                      "\n" +
                      "  -n, --sample                set the number of sampled optimal reconciliations for each rooting (default value 100)")

    # Parses the arguments provided by the user:

    try:
        opts, args = getopt.getopt(argv,
                                   "i:o:D:T:L:qsvdn:h",
                                   ["input=",
                                    "output=",
                                    "type=",
                                    "thr=",
                                    "add=",
                                    "seed=",
                                    "quiet",
                                    "summary",
                                    "version",
                                    "dated",
                                    "sample=",
                                    "help"])

    # Handles invalid arguments:

    except getopt.GetoptError as err:
        print(err)
        if os_name.startswith("win32"):
            print("Try SummarizeOptRootings.py --help for a list of arguments")
        else:
            print("Try ./SummarizeOptRootings.py --help for a list of arguments")
        sys.exit(2)

    # Handles help and version, assigns user-specified values to variables:

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help_final)
            sys.exit()
        elif opt in ("-v", "--version"):
            if os_name.startswith("linux"):
                subprocess.call(["./Ranger-DTL.linux", "-v"])
            elif os_name.startswith("win32"):
                subprocess.call(["./Ranger-DTL.win", "-v"])
            else:
                subprocess.call(["./Ranger-DTL.mac", "-v"])
            sys.exit()

        elif opt in ("-i", "--input"):
            input_file = arg
        if opt in ("-o", "--output"):
            output_file = arg
        if opt == "-D":
            duplication = arg
        if opt == "-T":
            transfer = arg
        if opt == "-L":
            loss = arg
        if opt == "--seed":
            seed = arg
            seed_input = True
        if opt in ("-q", "--quiet"):
            quiet = True
        if opt in ("-s", "--summary"):
            summary = True
        if opt in ("-d", "--dated"):
            dated = True
        if opt in ("-n", "--sample"):
            sample = int(arg)
            sample_input = True

    # Checks for missing input file:

    if input_file == "":
        print("ERROR: Missing input file")
        if os_name.startswith("win32"):
            print("Try SummarizeOptRootings.py --help for a list of arguments")
        else:
            print("Try ./SummarizeOptRootings.py --help for a list of arguments")
        sys.exit(2)

    # If reconciliation costs not provided, uses default costs from Ranger-DTL:

    if duplication == "":
        duplication = help_final.split("Duplication cost: ")[1]
        duplication = duplication.split(",")[0]

    if transfer == "":
        transfer = help_final.split("Transfer cost: ")[1]
        transfer = transfer.split(",")[0]

    if loss == "":
        loss = help_final.split("Loss cost: ")[1]
        loss = loss.split("Random seed:")[0]
        if os_name.startswith("win32"):
            loss = loss.strip("\r\n")
        else:
            loss = loss.strip("\n")

#------------------------------------------------------------------------------

# Prepares arguments and runs OptRoot:

def run_OptRoot(argv):

    global input_args
    global output_file

    # Prepares the list of arguments to be passed to OptRoot:

    input_args = argv
    if output_file == "":
        output_file = "SummarizeOptRootings_output"
        input_args += ["-o", output_file]

    if summary:
        if "-s" in input_args:
            input_args.remove("-s")
        else:
            input_args.remove("--summary")

    if sample_input:
        input_args.remove(str(sample))
        if "-n" in input_args:
            input_args.remove("-n")
        else:
            input_args.remove("--sample")

    # Determines and runs the appropriate version of OptRoot:

    if not quiet:
        print("Generating All Optimal Rootings...")

    if dated:
        if "-d" in input_args:
            input_args.remove("-d")
        else:
            input_args.remove("--dated")
        if os_name.startswith("linux"):
            input_args = ["./OptRoot-Dated.linux"] + input_args
        elif os_name.startswith("win32"):
            input_args = ["./OptRoot-Dated.win"] + input_args
        else:
            input_args = ["./OptRoot-Dated.mac"] + input_args
        subprocess.call(input_args)

    else:
        if os_name.startswith("linux"):
            input_args = ["./OptRoot.linux"] + input_args
        elif os_name.startswith("win32"):
            input_args = ["./OptRoot.win"] + input_args
        else:
            input_args = ["./OptRoot.mac"] + input_args
        subprocess.call(input_args)

#------------------------------------------------------------------------------

# Prepares input files and arguments for Ranger-DTL, and then runs Ranger-DTL:

def run_RangerDTL():

    global input_args
    global directory
    global dir_addr
    global OptRoot_output
    global num_optrootings

    # Prepares the input files for Ranger-DTL:

    x = randint(1, 99999)
    y = randint(1, 99999)
    directory = "DTL_output_" + str(x) + "_" + str(y)
    dir_addr = directory + os.path.sep
    os.mkdir(directory)
    OptRoot_output = dir_addr + "OptRoot_output"
    shutil.move(output_file, OptRoot_output)
    all_optimal_rootings = dir_addr + "all_optimal_rootings"

    with open(OptRoot_output) as infile, \
         open(all_optimal_rootings, "w") as outfile:
        copy = False
        for line in infile:
            if line.startswith(" -"):
                copy = True
            elif not line.strip():
                copy = False
            elif copy:
                outfile.write(line)

    with open(OptRoot_output) as infile:
        for line in infile:
            if "The total number of optimal rootings is:" in line:
                num_optrootings = int(line.split(" ")[7])

    for i in range(1, num_optrootings + 1):
        name = "input"
        filename = name + str(i)
        filepath = dir_addr + filename

        with open(input_file) as infile, open(filepath, "w") as outfile:
            for line in islice(infile, 0, 1):
                outfile.write(line)

        with open(all_optimal_rootings) as infile, \
             open(filepath, "a") as outfile:
            for line in islice(infile, i - 1, i):
                outfile.write(line)

    # Prepares the list of arguments to be passed to Ranger-DTL:

    input_args.remove(input_args[0])
    input_args.remove(input_file)

    if "-i" in input_args:
        input_args.remove("-i")
    else:
        input_args.remove("--input")
    input_args.remove(output_file)

    if "-o" in input_args:
        input_args.remove("-o")
    else:
        input_args.remove("--output")

    if seed_input:
        input_args.remove("--seed")
        input_args.remove(seed)

    if quiet:
        if "-q" in input_args:
            input_args.remove("-q")
        else:
            input_args.remove("--quiet")

    # Determines and runs the appropriate version of Ranger-DTL:

    if not quiet:
        print("Computing Reconciliation Data...")

    var = 1
    for entry in sorted(os.listdir(directory)):
        if entry.startswith("input"):
            dirname = dir_addr + "output" + str(var)
            os.mkdir(dirname)
            for i in range(1, sample + 1):

                if dated:
                    input_args2 = []

                    if os_name.startswith("linux"):
                        input_args2 = (["./Ranger-DTL-Dated.linux",
                                        "-i",
                                        dir_addr + entry,
                                        "-o",
                                        dirname + os.path.sep + "out" + str(i),
                                        "--seed",
                                        str(i),
                                        "-q"] +
                                       input_args)

                    elif os_name.startswith("win32"):
                        input_args2 = (["./Ranger-DTL-Dated.win",
                                        "-i",
                                        dir_addr + entry,
                                        "-o",
                                        dirname + os.path.sep + "out" + str(i),
                                        "--seed",
                                        str(i),
                                        "-q"] +
                                       input_args)

                    else:
                        input_args2 = (["./Ranger-DTL-Dated.mac",
                                        "-i",
                                        dir_addr + entry,
                                        "-o",
                                        dirname + os.path.sep + "out" + str(i),
                                        "--seed",
                                        str(i),
                                        "-q"] +
                                       input_args)
                    subprocess.call(input_args2)

                else:
                    input_args2 = []

                    if os_name.startswith("linux"):
                        input_args2 = (["./Ranger-DTL.linux",
                                        "-i",
                                        dir_addr + entry,
                                        "-o",
                                        dirname + os.path.sep + "out" + str(i),
                                        "--seed",
                                        str(i),
                                        "-q"] +
                                       input_args)

                    elif os_name.startswith("win32"):
                        input_args2 = (["./Ranger-DTL.win",
                                        "-i",
                                        dir_addr + entry,
                                        "-o",
                                        dirname + os.path.sep + "out" + str(i),
                                        "--seed",
                                        str(i),
                                        "-q"] +
                                       input_args)

                    else:
                        input_args2 = (["./Ranger-DTL.mac",
                                        "-i",
                                        dir_addr + entry,
                                        "-o",
                                        dirname + os.path.sep + "out" + str(i),
                                        "--seed",
                                        str(i),
                                        "-q"] +
                                       input_args)
                    subprocess.call(input_args2)
            var += 1

#------------------------------------------------------------------------------

# Runs AggregateRanger:

def run_AggregateRanger():

    for item in sorted(os.listdir(directory)):
        if item.startswith("output"):
            os.chdir(dir_addr + item)
            aggr = ""

            if os_name.startswith("linux"):
                aggr = subprocess.Popen("../../AggregateRanger.linux out".split(),
                       stdout=subprocess.PIPE)

            elif os_name.startswith("win32"):
                aggr = subprocess.Popen("../../AggregateRanger.win out".split(),
                       stdout=subprocess.PIPE)

            else:
                aggr = subprocess.Popen("../../AggregateRanger.mac out".split(),
                       stdout=subprocess.PIPE)
            output = aggr.communicate()[0]

            with open("aggr.out", "wb") as outfile:
                outfile.write(output)
            os.chdir("../..")

#------------------------------------------------------------------------------

# Parses output from AggregrateRanger to determine conserved clusters:

def conserved_clusters():

    # Obtains all the internal node entries from the AggregateRanger output:

    for item in sorted(os.listdir(directory)):
        if item.startswith("output"):

            with open(dir_addr + item + os.path.sep + "aggr.out") as infile, \
                 open(dir_addr + "internal_nodes_" + item, "a") as outfile:
                for line in infile:
                    if "Speciations" in line:
                        if "m1 = " not in line:
                            text = line.split("LCA")[1]
                            text = "LCA" + text
                            outfile.write(text)

    # Catches error where the input file does not contain valid information:

    if not os.path.isfile(dir_addr + "internal_nodes_output1"):
        print("ERROR: Invalid input file")
        sys.exit(2)

    # Identifies all the clusters from the internal node entries:

    for item in sorted(os.listdir(directory)):
        if item.startswith("internal"):

            with open(dir_addr + item) as infile, \
                 open(dir_addr + "clusters_" + item, "a") as outfile:
                for line in infile:
                    cluster = line.split(":")[0]
                    outfile.write(cluster + "\n")

    # Determines the clusters that are conserved across all optimal rootings:

    shutil.copyfile(dir_addr + "clusters_internal_nodes_output1",
                    dir_addr + "conserved_clusters")
    for item in sorted(os.listdir(directory)):
        if item.startswith("clusters"):

            with open(dir_addr + item) as file1, \
                 open(dir_addr + "conserved_clusters", "r+") as file2:
                lines1 = file1.readlines()
                lines2 = file2.readlines()
                intersection = []
                for i in lines1:
                    for j in lines2:
                        if i == j:
                            intersection.append(i)
                file2.seek(0)
                file2.truncate()
                file2.writelines(intersection)

#------------------------------------------------------------------------------

# Prepares summary data for the reconciliation across multiple roots:

def summary_data():

    with open(dir_addr + "conserved_clusters") as infile:
        for line in infile:
            node = line.split("]")[0]
            speciation_total = 0
            duplication_total = 0
            transfer_total = 0
            mapping_string = ""

            with open(dir_addr + "mapping_nodes", "a+") as mapfile:
                for item in sorted(os.listdir(directory)):
                    if item.startswith("internal"):

                        with open(dir_addr + item) as infile2, \
                             open(dir_addr + "long_output", "a") as outfile:
                            for x in infile2:
                                if node in x:

                                    # Writes full reconciliation data to long output file:

                                    outfile.write(x)

                                    # Prepares summary data for short output file:

                                    grep1 = x.split("=")[1]
                                    grep2 = grep1.split(",")[0]
                                    speciations = grep2.split(" ")[1]
                                    grep1 = x.split("=")[2]
                                    grep2 = grep1.split(",")[0]
                                    duplications = grep2.split(" ")[1]
                                    grep1 = x.split("=")[3]
                                    grep2 = grep1.split("]")[0]
                                    transfers = grep2.split(" ")[1]
                                    grep1 = x.split(" ")[15]
                                    mapping = grep1.split(",")[0]
                                    multiple = ""
                                    mapfile.seek(0)

                                    for y in mapfile:
                                        if mapping + "*"  == y.strip():
                                            multiple = y
                                    mapfile.seek(2)

                                    if multiple == "":
                                        mapfile.write(mapping + "*" + "\n")
                                    speciation_total += int(speciations)
                                    duplication_total += int(duplications)
                                    transfer_total += int(transfers)

                mapfile.seek(0)
                for z in mapfile:
                    map_string = z.split("*")[0]
                    if mapping_string == "":
                        mapping_string = map_string
                    else:
                        mapping_string = mapping_string + ", " + map_string
                mapfile.seek(0)
                mapfile.truncate()

            event_total = num_optrootings * sample
            speciation_total = speciation_total * 100
            duplication_total = duplication_total * 100
            transfer_total = transfer_total * 100
            speciation_ratio = speciation_total / event_total
            duplication_ratio = duplication_total / event_total
            transfer_ratio = transfer_total / event_total

            string = (node +
                      "]: [Speciations = " +
                      str(speciation_ratio) +
                      "%, Duplications = " +
                      str(duplication_ratio) +
                      "%, Transfers = " +
                      str(transfer_ratio) +
                      "%], [Most Frequent mapping(s) --> " +
                      str(mapping_string) +
                      "]." +
                      "\n")

            with open(dir_addr + "short_output", "a") as short_output:
                short_output.write(string)

    # Catches the case where there are no conserved clusters:

    long_file = open(dir_addr + "long_output", "a")
    long_file.close()
    short_file = open(dir_addr + "short_output", "a")
    short_file.close()

#------------------------------------------------------------------------------

# Prepares final output files:

def generate_output():

    # Creates final output files:

    with open(OptRoot_output) as infile, \
         open(dir_addr + "final_output", "a") as outfile:
        outfile.write(("Input file: " +
                       input_file +
                       "\n" +
                       "Duplication cost: " +
                       duplication +
                       ", Transfer cost: " +
                       transfer +
                       ", Loss cost: " +
                       loss +
                       "\n" +
                       "Sample Size for each Optimal Rooting: " +
                       str(sample) +
                       "\n"))
        with open(dir_addr + os.path.sep + "output1" + os.path.sep + "out1") as out1:
            outfile.write("\n" + "\n")
            copy = False
            for line in out1:
                if line.startswith(" -"):
                    copy = True
                elif not line.strip():
                    copy = False
                elif copy:
                    if line.startswith("Species"):
                        outfile.write(line.strip())
                        outfile.write("\n" + "\n")
                    else:
                        outfile.write(line)
        for line in infile:
            outfile.write(line)
        outfile.write(("\n" +
                       "\n" +
                       "Reconciliation Data for Conserved Subtrees:" +
                       "\n" +
                       "\n" ))
    shutil.copyfile(dir_addr + "final_output",
                    dir_addr + "final_output2")

    # Adds reconciliation data from conserved clusters to final output files:

    with open(dir_addr + "long_output") as infile, \
         open(dir_addr + "final_output", "a") as outfile:
        for line in infile:
            outfile.write(line)

    with open(dir_addr + "short_output") as infile, \
         open(dir_addr + "final_output2", "a") as outfile:
        for line in infile:
            outfile.write(line)

    # Obtains reconciliation data for the root node from each optimal rooting:

    for item in sorted(os.listdir(directory)):
        if item.startswith("output"):

            with open(dir_addr + item + os.path.sep + "aggr.out") as infile, \
                 open(dir_addr + "root_nodes", "a") as outfile:
                for line in infile:
                    if "m1 = " in line:
                        root = line.split("LCA")[1]
                        root = "LCA" + root
                        outfile.write(root)

    with open(dir_addr + "root_nodes", "r+") as infile:
        lines = infile.readlines()
        lines.sort()
        infile.seek(0)
        infile.writelines(lines)

    with open(dir_addr + "root_nodes") as infile, \
         open(dir_addr + "root_nodes2", "a") as outfile:

        with open(dir_addr + "mapping_roots", "a+") as mapfile:
            root_speciation = 0
            root_duplication = 0
            root_transfer = 0
            mapping_string = ""

            for x in infile:
                grep1 = x.split("=")[1]
                grep2 = grep1.split(",")[0]
                speciations = grep2.split(" ")[1]
                grep1 = x.split("=")[2]
                grep2 = grep1.split(",")[0]
                duplications = grep2.split(" ")[1]
                grep1 = x.split("=")[3]
                grep2 = grep1.split("]")[0]
                transfers = grep2.split(" ")[1]
                grep1 = x.split(" ")[15]
                mapping = grep1.split(",")[0]
                multiple = ""
                mapfile.seek(0)

                for y in mapfile:
                    if mapping + "*" == y.strip():
                        multiple = y
                mapfile.seek(2)

                if multiple == "":
                    mapfile.write(mapping + "*" + "\n")
                root_speciation += int(speciations)
                root_duplication += int(duplications)
                root_transfer += int(transfers)

            mapfile.seek(0)
            for z in mapfile:
                map_string = z.split("*")[0]
                if mapping_string == "":
                    mapping_string = map_string
                else:
                    mapping_string = mapping_string + ", " + map_string
            mapfile.seek(0)
            mapfile.truncate()

            root_total = num_optrootings * sample
            root_speciation = root_speciation * 100
            root_duplication = root_duplication * 100
            root_transfer = root_transfer * 100
            speciation_ratio = root_speciation / root_total
            duplication_ratio = root_duplication / root_total
            transfer_ratio = root_transfer / root_total

            string = ("[Root Cluster]: [Speciations = " +
                      str(speciation_ratio) +
                      "%, Duplications = " +
                      str(duplication_ratio) +
                      "%, Transfers = " +
                      str(transfer_ratio) +
                      "%], [Most Frequent mapping(s) --> " +
                      str(mapping_string) + "]." +
                      "\n")
            outfile.write(string)

    # Adds reconciliation data from the root nodes to the final output files:

    with open(dir_addr + "root_nodes") as infile1, \
         open(dir_addr + "root_nodes2") as infile2, \
         open(dir_addr + "final_output", "a") as outfile1, \
         open(dir_addr + "final_output2", "a") as outfile2:
        outfile1.write(("\n" +
                        "\n" +
                        "Reconciliation Data for Root Cluster:" +
                        "\n" +
                        "\n"))
        outfile2.write(("\n" +
                        "\n" +
                        "Reconciliation Data for Root Cluster:" +
                        "\n" +
                        "\n"))
        for line in infile1:
            outfile1.write(line)
        for line in infile2:
            outfile2.write(line)

    shutil.copyfile(dir_addr + "final_output2",
                    output_file + "_short")
    if not summary:
        shutil.copyfile(dir_addr + "final_output",
                        output_file + "_long")

#------------------------------------------------------------------------------

if __name__ == "__main__":
    main(sys.argv[1:])
