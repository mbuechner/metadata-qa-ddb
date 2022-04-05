#!/usr/bin/env bash

ROOT=$(realpath $(dirname $0)/../..)
source $ROOT/configuration.cnf

MVN_REPO=/home/kiru/.m2/repository
CLASSPATH="$MVN_REPO/ch/qos/logback/logback-core/1.2.11/logback-core-1.2.11.jar"
CLASSPATH="$CLASSPATH:/$MVN_REPO/org/slf4j/slf4j-api/1.7.38/slf4j-api-1.7.38.jar"
CLASSPATH="$CLASSPATH:/$MVN_REPO/ch/qos/logback/logback-classic/1.2.11/logback-classic-1.2.11.jar"

java -Xmx4g -DlogDir="$ROOT/logs" -cp $CLASSPATH:$ROOT/$JAR de.gwdg.metadataqa.ddb.App \
  --format csv \
  --path solr/qa_ddb_mets_mods \
  --recursive \
  --sqlitePath $OUTPUT_DIR/ddb.sqlite \
  --rootDirectory $INPUT_DIR \
  --directory $INPUT_DIR/METS-MODS \
  --schema $ROOT/src/main/resources/mets-mods-schema.yaml \
  --output $OUTPUT_DIR/mets-mods.csv \
  --record-address '//mets:mets'
