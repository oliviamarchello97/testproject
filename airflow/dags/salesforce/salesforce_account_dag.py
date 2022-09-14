from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash_operator import BashOperator
from util.constants import (
    default_args,
    schedule,
)

DBT_MODEL = "/testproject/airflow/dbt_test/models/salesforce/salesforce_account.sql"

with DAG(
    dag_id='salesforce_account_dag',
    default_args=default_args,
    catchup=False,
    schedule_interval=schedule.daily_1pm_UTC.value,
) as dag:


    sync_source_destination = AirbyteTriggerSyncOperator(
        task_id='airbyte_sync_sfdc_bq',
        connection_id="88c3900d-1257-4381-b3e7-92b6e23ce378",
        trigger_rule="none_failed",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --{DBT_MODEL}",
        trigger_rule="none_failed",
    )


    sync_source_destination >> dbt_run