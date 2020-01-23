import subprocess

def getProcs():
    #Get all processes
    rawOutput = subprocess.check_output(['tasklist'])

    #Start formatting--------------------------------------
    outputSplitSpace = str(rawOutput).split(" ")

    #Get all lines with a .exe in them
    exeList = []
    for item in outputSplitSpace:
        if ".exe" in item:
            exeList.append(item)

    #Remove formatting
    exeFormatList = []
    for item in exeList:
        stringTmp = item.split("K\\r\\n")
        if len(stringTmp) == 2:
            exeFormatList.append(stringTmp[1])
        else:
            exeFormatList.append(stringTmp[0])
    #------------------------------------------------------
    return exeFormatList;

#Monitor created processes and list them all
def monitorProcs(runTimes):
    created = []
    tempList = []
    for i in range(0,runTimes):
        procs = getProcs()
        if i != 0:
            for item in procs:
                if not item in tempList:
                    created.append(item)
        tempList = procs
    return created;