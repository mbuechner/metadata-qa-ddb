#!/bin/bash
echo "Environment variables";
echo "---------------------";
echo "\$MQA_JAR=${MQA_DATA}/target/metadata-qa-ddb.jar";
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

echo "Unpacking /opt/metadata-qa-ddb.tar.gz into $MQA_DATA ...";
mkdir -p $MQA_DATA
tar --overwrite -xzvf /opt/metadata-qa-ddb.tar.gz -C $MQA_DATA

echo "Create folder ${MQA_DATA}/data, ${MQA_DATA}/data/input and ${MQA_DATA}/data/output";
mkdir ${MQA_DATA}/data ${MQA_DATA}/data/input ${MQA_DATA}/data/output

echo "Start Prefect workflow in background ..."
cd $MQA_DATA
python3 prefect2_workflow.py &

echo "Start Prefect server ..."
prefect server start --host 0.0.0.0
