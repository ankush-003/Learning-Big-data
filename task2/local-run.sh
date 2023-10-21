#!/usr/bin/env bash

rm out*.txt

if [ $2 -ge 1 ]
then
echo "Starting stage 1"
cat $1 | ./mapper1.py > out_map1.txt
echo "mapper 1 output"
cat out_map1.txt
cat out_map1.txt | sort -k 1,1 | ./reducer1.py > out_red1.txt
echo "reducer 1 output"
cat out_red1.txt
echo "Stage 1 ran successfully!"
fi
if [ $2 -ge 2 ]
then
echo "starting stage 2"
cat out_red1.txt | ./mapper2.py > out_map2.txt
echo "mapper 2 output"
cat out_map2.txt
cat out_map2.txt | sort -k 1,1 | ./reducer2.py > out_red2.txt
echo "reducer 2 output"
cat out_red2.txt
echo "stage 2 ran successfully!"
fi
if [ $2 -eq 3 ]
then
echo "starting stage 3"
cat out_red2.txt | ./mapper3.py > out_map3.txt
echo "mapper 3 output"
cat out_map3.txt
cat out_map3.txt | sort -k 1,1 | ./reducer3.py > out_red3.txt
echo "reducer 3 output"
cat out_red3.txt
cat "stage 3 ran successfully!"
echo "comparing outputs"
diff -y expected_output_dataset_sample.txt out_red3.txt
fi
