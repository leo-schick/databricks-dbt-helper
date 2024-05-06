# Databricks notebook source
# MAGIC %md
# MAGIC Prepare a cluster to run DBT scripts
# MAGIC
# MAGIC #### Required environment variables
# MAGIC - `DBT_PROJECT_DIR` - the path where the dbt project shall be saved locally. Suggestion: `DBT_PROJECT_DIR=/tmp/dbt_project`
# MAGIC - `DBT_PROJECT_GIT_REPOSITORY` - the git repository containing the dbt project to be cloned.
# MAGIC
# MAGIC #### Optional environment variables
# MAGIC - `DBT_REPOSITORY_REF` - the git reference to be cloned. If not set, `prod` is taken as production branch name.
# MAGIC - `DBT_GITHUB_SSH_PRIVATE_KEY` - the raw code of a SSH key. If set, the SSH key will be placed at `~/.ssh/github_id` and the ssh config will be created for host github.com.
# MAGIC - `DBT_CORE_VERSION` - the package version of `dbt-core` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.7.10 is taken.
# MAGIC - `DBT_DATABRICKS_VERSION` - the package version of `dbt-databricks` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.7.9 is taken.

# COMMAND ----------

# MAGIC %sh -e
# MAGIC if ! command -v dbt &> /dev/null
# MAGIC then
# MAGIC   echo "Install dbt-databricks ${DBT_DATABRICKS_VERSION:-1.7.9} with dbt core ${DBT_CORE_VERSION:-1.7.10}"
# MAGIC   /databricks/python/bin/pip install "dbt-databricks==${DBT_DATABRICKS_VERSION:-1.7.9}" "dbt-core==${DBT_CORE_VERSION:-1.7.10}"
# MAGIC else
# MAGIC   echo "dbt is already installed"
# MAGIC fi

# COMMAND ----------

# MAGIC %sh -e
# MAGIC if [ -z "${DBT_GITHUB_SSH_PRIVATE_KEY}" ]
# MAGIC then
# MAGIC         echo "Note: No ssh config is created for github.com. Private git repositories cannot be accessed. You can activate this feature with environment variable DBT_GITHUB_SSH_PRIVATE_KEY"
# MAGIC else
# MAGIC
# MAGIC         mkdir -p ~/.ssh
# MAGIC         echo "Host github.com
# MAGIC                 HostName github.com
# MAGIC                 User git
# MAGIC                 IdentityFile ~/.ssh/github_id
# MAGIC         " > ~/.ssh/config
# MAGIC
# MAGIC         echo -e "${DBT_GITHUB_SSH_PRIVATE_KEY}" > ~/.ssh/github_id
# MAGIC
# MAGIC         chmod 0600 ~/.ssh/github_id
# MAGIC
# MAGIC         ssh-keyscan -H github.com >> ~/.ssh/known_hosts
# MAGIC fi

# COMMAND ----------

# MAGIC %sh -e
# MAGIC #######################################
# MAGIC ## Clone git repository
# MAGIC if [ -z "${DBT_PROJECT_DIR}" ]
# MAGIC then
# MAGIC   echo 'You must provide environment variable DBT_PROJECT_DIR in your cluster configuration when using this lib. Please add "DBT_PROJECT_DIR=/tmp/dbt_project" to your cluster configuration.'
# MAGIC   exit 1
# MAGIC fi
# MAGIC if [ -z "${DBT_PROJECT_GIT_REPOSITORY}" ]
# MAGIC then
# MAGIC   echo 'You must provide environment variable DBT_PROJECT_GIT_REPOSITORY in your cluster configuration when using this lib.'
# MAGIC   exit 1
# MAGIC fi
# MAGIC [ -d $DBT_PROJECT_DIR ] || git clone $DBT_PROJECT_GIT_REPOSITORY $DBT_PROJECT_DIR
# MAGIC cd $DBT_PROJECT_DIR
# MAGIC git fetch
# MAGIC git reset --hard origin/${DBT_REPOSITORY_REF:-prod}
