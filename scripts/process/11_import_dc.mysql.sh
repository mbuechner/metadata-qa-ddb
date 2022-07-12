#!/usr/bin/env bash

ROOT=$(realpath $(dirname $0)/../..)
source $ROOT/configuration.cnf

php $ROOT/scripts/csv2sql.php ${OUTPUT_DIR}/dc.csv issue

mysql --defaults-extra-file=$ROOT/mysql-config.cnf $MY_DB -e "SELECT COUNT(*) as 'before deleting DC' FROM issue"

mysql --defaults-extra-file=$ROOT/mysql-config.cnf $MY_DB -e "DELETE FROM issue 
WHERE recordId IN 
(SELECT recordId 
   FROM file_record AS fr 
   JOIN file AS f USING(file) 
   WHERE metadata_schema = 'DDB-DC');"

mysql --defaults-extra-file=$ROOT/mysql-config.cnf $MY_DB -e "SELECT COUNT(*) AS 'after deleting DC' FROM issue"

mysql --defaults-extra-file=$ROOT/mysql-config.cnf $MY_DB < ${OUTPUT_DIR}/dc.sql

mysql --defaults-extra-file=$ROOT/mysql-config.cnf $MY_DB -e "SELECT COUNT(*) AS 'after importing DC' FROM issue"
