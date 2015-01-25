#!/bin/bash
#Created By: Ravi Tandon
#This is the harness file for running experiment 6 (In this experiment we vary the size of the cache in order to find out the faults due to the marking threads when the cache is hit in-core).
nKeys=15000000
for i in `seq 1 8`;
do
   echo "number of keys = $nKeys"
   bash runCacheTests.sh openjdk $nKeys
   nKeys=$(($nKeys + 3000000))
done
