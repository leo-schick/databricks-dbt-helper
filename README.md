# Databricks dbt helper

This repository holds helper Databricks Notebooks to run dbt on a Databricks cluster.

Read my story on Medium: [How to run dbt on Databricks job cluster](https://medium.com/@leo-schick/how-to-run-dbt-on-databricks-job-cluster-d12e8cfdcc6d).

&nbsp;

## Running dbt on a Job cluster

*Note:* Does not work with Python models, see [databricks/dbt-databricks#586](https://github.com/databricks/dbt-databricks/issues/586)

Add the following environment variables to your job cluster configuration:

#### Required environment variables
- `DBT_PROJECT_NAME` - the project name of the project
- `DBT_PROJECT_DIR` - the path where the dbt project shall be saved locally. Suggestion: `DBT_PROJECT_DIR=/tmp/dbt_project`
- `DBT_PROJECT_GIT_REPOSITORY` - the git repository containing the dbt project to be cloned.

#### Optional environment variables
- `DBT_REPOSITORY_REF` - the git reference to be cloned. If not set, `prod` is taken as production branch name.
- `DBT_GITHUB_SSH_PRIVATE_KEY` - the raw code of a SSH key. If set, the SSH key will be placed at `~/.ssh/github_id` and the ssh config will be created for host github.com.
- `DBT_CORE_VERSION` - the package version of `dbt-core` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.7.10 is taken.
- `DBT_DATABRICKS_VERSION` - the package version of `dbt-databricks` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.7.9 is taken.

#### Set up Workflow and Notebook

To know how to set up the workflow and Notebook where the cluster runs, read [my story on Medium](https://medium.com/@leo-schick/how-to-run-dbt-on-databricks-job-cluster-d12e8cfdcc6d)


## Running dbt on All-purpose cluster

Add the following environment variables to your cluster configuration:

### Required environment variables
- `DBT_PROJECT_DIR` - the path where the dbt project shall be saved locally. Suggestion: `DBT_PROJECT_DIR=/tmp/dbt_project`
- `DBT_PROJECT_GIT_REPOSITORY` - the git repository containing the dbt project to be cloned.

### Optional environment variables
- `DBT_REPOSITORY_REF` - the git reference to be cloned. If not set, `prod` is taken as production branch name.
- `DBT_GITHUB_SSH_PRIVATE_KEY` - the raw code of a SSH key. If set, the SSH key will be placed at `~/.ssh/github_id` and the ssh config will be created for host github.com.
- `DBT_CORE_VERSION` - the package version of `dbt-core` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.7.10 is taken.
- `DBT_DATABRICKS_VERSION` - the package version of `dbt-databricks` to be installed when not already installed (e.g. via dependencies in a workflow task). If not set, 1.7.9 is taken.

### Include lib/dbt

Load as first task in your Notebook the `lib/dbt.py` package:
```
%run /path_to_this_repository/lib/dbt.py
```

Now you can call dbt commands this:
```
%sh -e
dbt run -s tag:nightly
```
