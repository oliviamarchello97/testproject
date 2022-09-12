from datetime import datetime, timedelta
from enum import Enum

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 3, 16),
    "email": ["ops@partnerstack.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

class schedule(Enum):
    daily_1pm_UTC = "0 13 * * *"