### How to use:

- Run <code>sh /path/to/this/scripts/databricks-start.sh</code> to start a spark cluster based on the setting we had in <code>default-cluster-start.json</code>
- Then the cluster id of the newly created spark cluster will be return and we will store in <code>default-cluster-stop.json</code>
- Then, run <code>sh /path/to/this/scripts/databricks-stop.sh</code> to stop the spark cluster
- You will need to put both bash script commands above into a crontab, so that can automate the process
- Remember to put your Databricks credentials into environment variables so that the scripts can read the value

That's it, you got the automation~ :)
