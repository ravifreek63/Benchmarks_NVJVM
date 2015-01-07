#!/bin/bash

#This is the top level file for running all the tests

#The first argument is for the type of collector to be run 

case "$1" in
"openjdk")
sudo bash ~/change.sh openjdk
bash runSearchTests.sh 20 200
;; 

*)
sudo bash ~/change.sh 
;;

esac
