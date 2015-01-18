#!/bin/bash
#Created By: Ravi Tandon
#This is the harness file for running experiment 2 (In this experiment we vary the number of threads).
nThreads=2
for i in `seq 1 5`;
do
   nThreads=$(($nThreads + 1))
   echo "nThreads=$nThreads"
   bash runCacheTests.sh $1 $nThreads
done    

