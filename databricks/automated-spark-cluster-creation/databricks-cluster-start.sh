#!/bin/sh

startCluster="$(curl -X POST -H "Content-Type: application/json" \
-u username:password https://seekasia.cloud.databricks.com/api/2.0/clusters/create -d "@default-cluster-start.json")"

# Put into log for logging purpose
echo $(date) " | start-cluster | " $startCluster >> /Users/nicholedean/Documents/GitHub/python-batch/databricks/automated-spark-cluster-creation/cluster-status.log

# Put into default-cluster-stop.json to use by databricks-cluster-stop.sh
echo $startCluster > /Users/nicholedean/Documents/GitHub/python-batch/databricks/automated-spark-cluster-creation/default-cluster-stop.json
