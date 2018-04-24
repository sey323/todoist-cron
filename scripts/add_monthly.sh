#!/bin/bash
. /root/env.sh
python /cron/add_weekly.py  >> /var/log/test.log 2>&1
