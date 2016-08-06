echo $(date) "| stop-cluster | " $(curl -X POST -H "Content-Type: application/json" -u username:password \
https://seekasia.cloud.databricks.com/api/2.0/clusters/delete \
-d "@default-cluster-stop.json") $(cat default-cluster-stop.json) >> \
/Users/nicholedean/Documents/GitHub/python-batch/databricks/automated-spark-cluster-creation/cluster-status.log