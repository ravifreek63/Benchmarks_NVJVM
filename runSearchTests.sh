#!/bin/bash
#This is for running the SearchTests

#Arguments
#The first argument is the size of min size of the heap, the second argument is the maximum size of the heap


java -XX:+PrintGC -XX:+PrintGCDetails -Xms$1m -Xmx$2m -jar /home/tandon/Benchmarks/benchmark/java/benchmarks/dacapo.jar lusearch
