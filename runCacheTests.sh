#!/bin/bash
# This is the base directory for the jar file of the Cache Directory
baseDir="/home/tandon/Projects/CacheBenchmark/dist"
jarFile="cacheBenchmark.jar"
javaPath=""
extraOptions=""
#numberKeys="10000000"
numberKeys="$2"
fanout="16"
numberThreads="9"
numberSamplesPerThread="1000"
percentageCacheHit="100"
runningTime="30" #in_seconds
getsPerPut="20"
numberCollections="1"
collectorType="$1"
cacheParameters="$numberKeys $fanout $numberThreads $numberSamplesPerThread $percentageCacheHit $runningTime $getsPerPut $collectorType"
gcOptions="-XX:-PrintGC -XX:+UseConcMarkSweepGC -XX:-PrintGCDetails -Xms30g -XX:NewRatio=300 -XX:NumberCollections=$numberCollections"
nConcThreads=""

case "$1" in 

"openjdk")
javaPath="/home/tandon/Projects/NVJVM/build/linux-amd64/bin/java"
extraOptions="-XX:NumberPartitions=1000 -XX:ConcGCThreads=5"
;;

"baseline")
javaPath="/home/tandon/Projects/JVM_Baseline/NVJVM/build/linux-amd64/bin/java"
extraOptions="-XX:ConcGCThreads=4"
;;

*)
esac

cd $baseDir
cmd="$javaPath $gcOptions $extraOptions -jar $jarFile $cacheParameters"
echo $cmd
echo 3 > /proc/sys/vm/drop_caches
$cmd
