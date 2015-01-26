import fileinput
baseDirectory='/home/tandon/data/markPData/'
cTypeArray =['baseline', 'openjdk']
def average(array):
   sum = 0
   n_sum = 0
   for num in array:
     sum = sum + num
     n_sum = n_sum + 1
   if n_sum == 0:
     return 0
   return sum/n_sum

def sumF(array):
   sum = 0
   n_sum = 0
   for num in array:
     sum = sum + num
     n_sum = n_sum + 1
   if n_sum == 0:
     return 0
   return sum

def printRuntime(dir, a1, a2, a3, a4, collType, numKeys):
	runTimeFileName=dir+'/analysis/runtime.txt'
	with open(runTimeFileName, "a") as rTFile:
		rTFile.write(collType+'\n')
		rTFile.write(numKeys+'\n')
		rTFile.write(str(average(a1))+'\n')
		rTFile.write(str(average(a2))+'\n')
		rTFile.write(str(average(a3))+'\n')
		rTFile.write(str(average(a4))+'\n')
	rTFile.close()

def printWaitTime(dir, a1, a2, a3, a4, collType, numKeys):
        waitTimeFileName=dir+'/analysis/waitingTime.txt'
        with open(waitTimeFileName, "a") as wTFile:
                wTFile.write(collType+'\n')
                wTFile.write(numKeys+'\n')
                wTFile.write(str(average(a1))+'\n')
                wTFile.write(str(average(a2))+'\n')
                wTFile.write(str(average(a3))+'\n')
                wTFile.write(str(average(a4))+'\n')
        wTFile.close()

def printTotalFaults(dir, a1, a2, a3, a4, collType, numKeys):
        faultFileName=dir+'/analysis/totalFaults.txt'
        with open(faultFileName, "a") as fFile:
                fFile.write(collType+'\n')
                fFile.write(numKeys+'\n')
                fFile.write(str(sumF(a1))+'\n')
                fFile.write(str(sumF(a2))+'\n')
                fFile.write(str(sumF(a3))+'\n')
                fFile.write(str(sumF(a4))+'\n')
        fFile.close()	


def printFaultRate(dir, a1, a2, a3, a4, collType, numKeys):
        faultFileName=dir+'/analysis/FaultRate.txt'
        with open(faultFileName, "a") as fFile:
                fFile.write(collType+'\n')
                fFile.write(numKeys+'\n')
                fFile.write(str(sumF(a1))+'\n')
                fFile.write(str(sumF(a2))+'\n')
                fFile.write(str(sumF(a3))+'\n')
                fFile.write(str(sumF(a4))+'\n')
        fFile.close()


def printWaitPerFault(dir, a1, a2, a3, a4, collType, numKeys):
        waitPerFaultFileName=dir+'/analysis/WaitPerFault.txt'
        with open(waitPerFaultFileName, "a") as fFile:
                fFile.write(collType+'\n')
                fFile.write(numKeys+'\n')
                fFile.write(str(sumF(a1))+'\n')
                fFile.write(str(sumF(a2))+'\n')
                fFile.write(str(sumF(a3))+'\n')
                fFile.write(str(sumF(a4))+'\n')
        fFile.close()

for cType in cTypeArray:
	directory=baseDirectory+cType
	for nKeys in range(10, 14):
		thread_file_name=directory+'/threads-'+ str(nKeys)+'.txt'
                thread_file=open(thread_file_name)
		# This is the declaration of container for arrays
		vmT=[]
		vmgcT=[]
		cgcT=[]
		javaT=[]
		#This is for parsing the file and getting the thread ids
		count=0
		threadId=0
		for line in thread_file:
			ar = line.split(',')
			if count == 0:
				for tid in ar:
					vmT.append(tid.strip(' \t\n\r'))
			elif count == 1:
				for tid in ar:
					vmgcT.append(tid.strip(' \t\n\r'))
			elif count == 2:
				for tid in ar:
					cgcT.append(tid.strip(' \t\n\r'))
			elif count == 3:
				for tid in ar:
					javaT.append(tid.strip(' \t\n\r'))
			count = count + 1

		lineCount=0
		#Scanning the stap file now 
		stap_file_name=directory+'/stap-'+str(nKeys)+'.out'
		stap_file=open(stap_file_name)
		#We start with getting the runtime for the different threads 
		vmTRuntime=[];vmgcTRuntime=[];cgcTRuntime=[];javaTRuntime=[]
                vmTWaittime=[];vmgcTWaittime=[];cgcTWaittime=[];javaTWaittime=[] 
		vmTFaults=[];vmgcTFaults=[];cgcTFaults=[];javaTFaults=[]
		vmTFaultRate=[];vmgcTFaultRate=[];cgcTFaultRate=[];javaTFaultRate=[]
		vmTWaitPerFault=[];vmgcTWaitPerFault=[];cgcTWaitPerFault=[];javaTWaitPerFault=[]

		for line in stap_file:
			sp_array = line.split()
			threadId = sp_array[0]
			waitTime = int(sp_array[1])
			faults   = int(sp_array[2])
			runningTime = int(sp_array[3])
			if threadId in vmT:
				if(runningTime>0):
					vmTRuntime.append(runningTime)
					if(faults>0):
						vmTFaultRate.append(float(faults)/float(runningTime)*1000) #Faults/millisecond				
				if(waitTime>0):
					vmTWaittime.append(waitTime)	
				if(faults>0):
					vmTFaults.append(faults)
					if(waitTime>0):
						vmTWaitPerFault.append(float(waitTime)/float(faults))
				
			elif threadId in vmgcT:
				if(runningTime>0):
					vmgcTRuntime.append(runningTime)
                                        if(faults>0):
                                                vmgcTFaultRate.append(float(faults)/float(runningTime)*1000)
				if(waitTime>0):
					vmgcTWaittime.append(waitTime)
                                if(faults>0):
                                        vmgcTFaults.append(faults)
					if(waitTime>0):
						vmgcTWaitPerFault.append(float(waitTime)/float(faults))

			elif threadId in cgcT:
				if(runningTime>0):
					cgcTRuntime.append(runningTime)
                                        if(faults>0):
                                                cgcTFaultRate.append(float(faults)/float(runningTime)*1000)
				if(waitTime>0):
					cgcTWaittime.append(waitTime)
                                if(faults>0):
                                        cgcTFaults.append(faults)
					if(waitTime>0):
						cgcTWaitPerFault.append(float(waitTime)/float(faults))

			elif threadId in javaT:
				if(runningTime>0):
					javaTRuntime.append(runningTime)
                                        if(faults>0):
                                                javaTFaultRate.append(float(faults)/float(runningTime)*1000)
				if(waitTime>0):
					javaTWaittime.append(waitTime)
                                if(faults>0):
                                        javaTFaults.append(faults)
					if(waitTime>0):
						javaTWaitPerFault.append(float(waitTime)/float(faults))

		#printRuntime(baseDirectory, vmTRuntime, vmgcTRuntime, cgcTRuntime, javaTRuntime, cType, str(nKeys))
		#printWaitTime(baseDirectory, vmTWaittime, vmgcTWaittime, cgcTWaittime, javaTWaittime, cType, str(nKeys))
		#printTotalFaults(baseDirectory, vmTFaults, vmgcTFaults, cgcTFaults, javaTFaults, cType, str(nKeys))
		#printFaultRate(baseDirectory, vmTFaultRate, vmgcTFaultRate, cgcTFaultRate, javaTFaultRate, cType, str(nKeys))
		printWaitPerFault(baseDirectory, vmTWaitPerFault, vmgcTWaitPerFault, cgcTWaitPerFault, javaTWaitPerFault, cType, str(nKeys))
		#endForScanningTheStapFile		
	#endForKeyRangeIteration
#endForCollectorType
