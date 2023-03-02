{ \
        echo "JAR=$(echo $MQA_JAR)"; \
        echo "INPUT_DIR=$(echo $MQA_INPUT_DIR)"; \
        echo "OUTPUT_DIR=$(echo $MQA_OUTPUT_DIR)"; \
        echo "FTP_USER=$(echo $MQA_FTP_USER)"; \
        echo "FTP_PW=$(echo $MQA_FTP_PW)"; \
        echo "MY_HOST=$(echo $MQA_MY_HOST)"; \
        echo "MY_PORT=$(echo $MQA_)"; \
        echo "MY_DB=$(echo $MQA_MY_PORT)"; \
        echo "MY_USER=$(echo $MQA_MY_USER)"; \
        echo "MY_PASSWORD=$(echo $MQA_MY_PASSWORD)"; \
        echo "SOLR_HOST=$(echo $MQA_SOLR_HOST)"; \
	echo "SOLR_PORT=$(echo $MQA_SOLR_PORT)"; \
} > configuration.cnf

tail -f /dev/null
