import dagshub
dagshub.init(repo_owner='bhasin888', repo_name='lmm_proj', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)