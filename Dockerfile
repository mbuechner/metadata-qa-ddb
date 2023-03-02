FROM ubuntu:jammy
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

# Install Ubuntu requirements
RUN sed -i 's|http://|http://de.|g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y openjdk-11-jdk wget gnupg curl jq maven lsof php php-http-request2 php-mysql php-sqlite3 mysql-client

# SQLite 
RUN apt-get install sqlite3

# Java
RUN apt-get install openjdk-11-jdk

# R
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | gpg --dearmor -o /usr/share/keyrings/r-project.gpg && \
	echo "deb [signed-by=/usr/share/keyrings/r-project.gpg] https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/" | tee -a /etc/apt/sources.list.d/r-project.list && \
	apt-get update && \
	apt-get install -y --no-install-recommends r-base r-cran-tidyverse r-cran-stringr r-cran-gridextra


# Installing software
COPY . /opt/metadata-qa-ddb
WORKDIR /opt/metadata-qa-ddb

RUN export MQA_VERSION=1.0.0 && \
	mvn package -DskipTests && \
	mv target/metadata-qa-ddb-${MQA_VERSION}-jar-with-dependencies.jar target/metadata-qa-ddb.jar && \
	mkdir data/ data/input data/output

ENV MQA_JAR=/opt/metadata-qa-ddb/target/metadata-qa-ddb.jar

ENTRYPOINT ["tail", "-f", "/dev/null"]
