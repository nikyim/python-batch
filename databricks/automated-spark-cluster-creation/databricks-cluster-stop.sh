#!/bin/sh

databricks_username=$(echo "$DATABRICKS_USERNAME")
databricks_passwd=$(echo "$DATABRICKS_PASSWD")

echo $(date) "| stop-cluster | " $(curl -X POST -H "Content-Type: application/json" \
-u $databricks_username:$databricks_passwd \
https://seekasia.cloud.databricks.com/api/2.0/clusters/delete \
-d "@default-cluster-stop.json") $(cat default-cluster-stop.json) >> \
/Users/nicholedean/Documents/GitHub/python-batch/databricks/automated-spark-cluster-creation/cluster-status.log