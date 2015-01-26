#!/bin/bash
#Created By: Ravi Tandon
#This is the harness file for running experiment 6 (In this experiment we vary the size of the cache in order to find out the faults due to the marking threads when the cache is hit in-core).
for cType in openjdk baseline
do
nKeys=10000000
for i in `seq 1 5`;
do
   stap -o /home/tandon/data/stap.out mark-$cType.stp &
   bash runCacheTests.sh $cType $nKeys
   nKeyValue=$(($nKeys/1000000))
   mv /home/tandon/data/stap.out /home/tandon/data/markPData/$cType/stap-$nKeyValue.out
   mv /home/tandon/data/threads.txt /home/tandon/data/markPData/$cType/threads-$nKeyValue.txt
   nKeys=$(($nKeys + 1000000))
done
done 
