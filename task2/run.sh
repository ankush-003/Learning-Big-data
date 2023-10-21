#!/usr/bin/env bash

# upload all file to hdfs
hdfs dfs -rm -r /task2
hdfs dfs -mkdir /task2
hdfs dfs -put dataset_large.txt /task2/

# Clean up the intermediate HDFS directories which could have been created as a part of a previous run
hdfs dfs -ls /Intermediate-1
if [[ $? == 0 ]]
then
	echo "Deleteing Intermediate-1 HDFS directory before starting job.."
	hdfs dfs -rm -r /Intermediate-1
fi

hdfs dfs -ls /Intermediate-2
if [[ $? == 0 ]]
then
	echo "Deleting Intermediate-2 HDFS directory before starting job.."
	hdfs dfs -rm -r /Intermediate-2
fi

echo "Initiating stage-1"
echo "==========================================================="

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files "mapper1.py","reducer1.py" \
-mapper "mapper1.py" \
-reducer "reducer1.py" \
-input /task2/dataset_large.txt \
-output /Intermediate-1

echo "==========================================================="
echo "Stage-1 done"
hdfs dfs -cat /Intermediate-1/part-00000
echo "Initiating stage-2"
echo "==========================================================="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files "$PWD/mapper2.py","$PWD/reducer2.py" \
-mapper "$PWD/mapper2.py" \
-reducer "$PWD/reducer2.py" \
-input /Intermediate-1/part-00000 \
-output /Intermediate-2
echo "==========================================================="
echo "Stage-2 done"
hdfs dfs -cat /Intermediate-2/part-00000
echo "Initializing stage-3"
echo "==========================================================="

hdfs dfs -rm -r /task2/output

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files "$PWD/mapper3.py","$PWD/reducer3.py" \
-mapper "$PWD/mapper3.py" \
-reducer "$PWD/reducer3.py" \
-input /Intermediate-2/part-00000 \
-output /task2/output

echo "==========================================================="
echo "Stage-3 done"
rm out_final.txt
hdfs dfs -cat /task2/output/part-00000 > out_final.txt
diff -y expected_output_dataset_large.txt out_final.txt
