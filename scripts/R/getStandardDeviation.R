#This is a file which is gets the standard deviation of the latencies of get requests for mark phase. 
list.Ct<-c("baseline","openjdk")
for (cType in list.Ct){
for (i in 10:14){
fileName=sprintf("/home/tandon/latency_%s_%d.txt",cType, i)
data=read.table(fileName)
sDev=mean(data$V1)
cat(sprintf("%s, %f\n", fileName, sDev))
}
}
