#!/bin/bash
# This is the base directory for the jar file of the Cache Directory
baseDir="/home/tandon/Projects/CacheBenchmark/dist"
jarFile="cacheBenchmark.jar"
gcOptions="-XX:+PrintGC -XX:+UseConcMarkSweepGC -XX:+PrintGCDetails"
javaPath=""
extraOptions=""
case "$1" in 

"openjdk")
javaPath="/home/tandon/Projects/NVJVM/build/linux-amd64/bin/java"
;;

"baseline")
javaPath="/home/tandon/Projects/JVM_Baseline/NVJVM/build/linux-amd64/bin/java"
;;

*)
esac

cd $baseDir

$javaPath $gcOptions $extraOptions -jar $jarFile

