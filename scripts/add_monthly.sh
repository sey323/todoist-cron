#!/bin/bash
. /root/env.sh
python /cron/add_monthly.py  >> /var/log/test.log 2>&1
