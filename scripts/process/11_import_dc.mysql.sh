#!/usr/bin/env bash

ROOT=$(realpath $(dirname $0)/../..)
source $ROOT/configuration.cnf
source $ROOT/scripts/set-mysql-vars.sh

php $ROOT/scripts/csv2sql.php ${OUTPUT_DIR}/dc.csv issue

mysql $MYSQL_EXTRA_PARAMETERS $MY_DB -e "SELECT COUNT(*) as 'before deleting DC' FROM issue"

mysql $MYSQL_EXTRA_PARAMETERS $MY_DB -e "DELETE FROM issue
WHERE recordId IN 
(SELECT recordId 
   FROM file_record AS fr 
   JOIN file AS f USING(file) 
   WHERE metadata_schema = 'DDB-DC');"

mysql $MYSQL_EXTRA_PARAMETERS $MY_DB -e "SELECT COUNT(*) AS 'after deleting DC' FROM issue"

mysql $MYSQL_EXTRA_PARAMETERS $MY_DB < ${OUTPUT_DIR}/dc.sql

mysql $MYSQL_EXTRA_PARAMETERS $MY_DB -e "SELECT COUNT(*) AS 'after importing DC' FROM issue"
