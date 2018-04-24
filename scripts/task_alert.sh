#!/bin/bash
. /root/env.sh
python /cron/task_alert.py  >> /var/log/test.log 2>&1
