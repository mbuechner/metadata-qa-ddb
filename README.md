# metadata-qa-ddb
A metadata quality assessment tool customized for the requirements of the Deutsche Digitale Bibliothek

Log in tinto MySQL, create a database and a dedicated user:

```
CREATE DATABASE ddb;

CREATE USER '<user name>'@'localhost' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON ddb.* TO '<user name>'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

# Installation

Set the configuration file.

1. Create a configuration file:
```
cp configuration.cnf.template configuration.cnf
```
2. Edit the configuration file

```
INPUT_DIR=<path to input directory>
OUTPUT_DIR=<path to output directory>
FTP_USER=<FTP user name>
FTP_PW=<FTP password>
MY_DB=<MySQL database name>
MY_USER=<MySQL user name>
MY_PASSWORD=<MySQL password>
```

# Running the software

## Download files and import file information into the database

create the database tables
```
scripts/database.mysql.sql
```

download files from FTP server
```
scripts/ingest/01_download_from_ftp.sh
```

unzip the downloaded zip files
```
scripts/ingest/02_extract_downloaded_files.sh
```

extract file info (path, size etc.) from the directory. The file paths contain semantic information about the data providers. The following data elements are extracted: file path, metadata schema, provider identifier, provider name, data set identifier, data set name, last modification date, file size. These data are saved into $OUTPUT_DIR/files.csv file.
```
scripts/ingest/03_extract_basic_info_from_downloaded_files.sh
```

import file info into MySQL (it first transforms CSV to SQL)
```
scripts/ingest/04_import_basic_info.mysql.sh
```

harvest EDM records for each data sets
```
scripts/ingest/05_harvest_edm.mysql.sh
```

## Index and store raw information
index DDB-EDM records
```
scripts/index/01_index_ddb-edm.sh
```

index MARC records
```
scripts/index/02_index_marc.sh
```

index DDB-DC records
```
scripts/index/03_index_ddb-dc.sh
```

index LIDO records
```
scripts/index/04_index_lido.sh
```

index METS-MODS records
```
scripts/index/05_index_mets-mods.sh
```

## Measurement

measure DDB-EDM
```
scripts/process/01_process_ddb-edm.sh
```

measure MARC
```
scripts/process/02_process_marc.sh
```

measure DDB-DC
```
scripts/process/03_process_ddb-dc.sh
```

measure LIDO
```
scripts/process/04_process_lido.sh
```

measure METS-MODS
```
scripts/process/05_process_mets-mods.sh
```

## Importing measurement results to database


import DDB-EDM
```
scripts/process/11_import_ddb-edm.mysql.sh
```

import MARC
```
scripts/process/11_import_marc.mysql.sh
```

import DDB-DC
```
scripts/process/11_import_dc.mysql.sh
```

import LIDO
```
scripts/process/11_import_lido.mysql.sh
```

import METS-MODS
```
scripts/process/11_import_mets-mods.mysql.sh
```

calculate aggregated results
```
scripts/process/12_calculate_aggregations.mysql.sh
```
