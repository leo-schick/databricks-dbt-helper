# Databricks notebook source
# MAGIC %md
# MAGIC Install and configure requirements for a DBT job cluster.
# MAGIC
# MAGIC #### Required environment variables
# MAGIC - `DBT_PROJECT_NAME` - the project name of the project

# COMMAND ----------

# MAGIC %run ./dbt

# COMMAND ----------

# MAGIC %sh
# MAGIC if [ -z "${DBT_PROJECT_NAME}" ]
# MAGIC then
# MAGIC   echo 'You must provide environment variable DBT_PROJECT_NAME in your cluster configuration when using this lib.'
# MAGIC   exit 1
# MAGIC fi
# MAGIC mkdir -p /root/.dbt
# MAGIC echo "$DBT_PROJECT_NAME:
# MAGIC   target: default
# MAGIC   outputs:
# MAGIC     default:
# MAGIC       type: spark
# MAGIC       method: session
# MAGIC       schema: dbt
# MAGIC       host: NA
# MAGIC       threads: 14
# MAGIC
# MAGIC elementary:
# MAGIC   target: default
# MAGIC   outputs:
# MAGIC     default:
# MAGIC       type: spark
# MAGIC       method: session
# MAGIC       schema: dbt_elementary
# MAGIC       host: NA
# MAGIC       threads: 14" > /root/.dbt/profiles.yml
