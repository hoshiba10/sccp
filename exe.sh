#!/bin/bash
hour='+%H%m'

while true
do

if [ `date '%H%M' = "0400"` ] || [ `date '+%H%M'` = "1200" ]  || [ `date` '+%H%M' = "2000" ]; then

	hour='+%H%m'

	sudo python script.py 22 24

	sleep 5

	. ./result.txt

	ttytter -ssl -status="Temperature is ${TEST}  Humidity is ${TEST}"

	sleep 27000

fi

sleep 3 


done