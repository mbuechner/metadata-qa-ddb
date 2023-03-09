#!/bin/bash
echo "Environment variables";
echo "---------------------";
echo "\$MQA_DATA=$MQA_DATA";
echo "\$MQA_FTP_USER=$MQA_FTP_USER";
echo "\$MQA_FTP_PW=$MQA_FTP_PW";
echo "\$MQA_MY_HOST=$MQA_MY_HOST";
echo "\$MQA_MY_PORT=$MQA_MY_PORT";
echo "\$MQA_MY_DB=$MQA_MY_DB";
echo "\$MQA_MY_USER=$MQA_MY_USER";
echo "\$MQA_MY_PASSWORD=$MQA_MY_PASSWORD";
echo "\$MQA_SOLR_HOST=$MQA_SOLR_HOST";
echo "\$MQA_SOLR_PORT=$MQA_SOLR_PORT";

echo "Create folder ${MQA_DATA}/input and ${MQA_DATA}/output ...";
mkdir -p ${MQA_DATA}/input ${MQA_DATA}/output

echo "Add Prefect deployment in background ..."
prefect deployment build prefect2_workflow.py:main_flow -a -n metadata-qa

echo "Start Supervisor ..."
supervisord -c /etc/supervisor/conf.d/supervisord.conf
