#!/bin/bash
#Created By: Ravi Tandon
#This is the harness file for running experiment 2 (In this experiment we vary the number of threads).
nKeys=13000000
for i in `seq 1 2`;
do
   echo "number of keys = $nKeys"
   bash runCacheTests.sh $1 $nKeys
   nKeys=$(($nKeys + 1000000))
done    
