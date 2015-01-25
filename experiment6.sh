#!/bin/bash
#Created By: Ravi Tandon
#This is the harness file for running experiment 6 (In this experiment we vary the size of the cache in order to find out the faults due to the marking threads when the cache is hit in-core).
nKeys=10000000
for i in `seq 1 5`;
do
   echo "number of keys = $nKeys"
   bash runCacheTests.sh $1 $nKeys 
   nKeys=$(($nKeys + 1000000))
done
