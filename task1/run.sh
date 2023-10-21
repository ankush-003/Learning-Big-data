#!/usr/bin/env bash

chmod a+x *.py

hdfs dfsadmin -safemode 
hdfs dfs -rm -r /task1
hdfs dfs -mkdir /task1
hdfs dfs -put "sample_data.json" /task1/

echo "Running mapper and reducer"
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /task1/sample_data.json \
-output /task1/out

echo "for output check /task1/out directory in hdfs"
echo "copying output to local directory"
rm out_task1.txt
hdfs dfs -cat /task1/out/part-00000 > out_task1.txt
diff -y expected_output_sample_data.txt out_task1.txt
