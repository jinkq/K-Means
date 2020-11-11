#!/bin/bash
for k in {2..8};do
    for iternum in {2..10};do
        cd /workspace/K-Means
        hdfs dfs -rm -r output
        hadoop jar /workspace/K-Means/target/K-Means-1.0-SNAPSHOT.jar $k $iternum input output
        rm -rf output
        hdfs dfs -get output output
        cd src/main/python
        python plot.py $k $iternum
    done
done
exit