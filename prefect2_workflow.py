from prefect import flow, task
from prefect_shell import ShellOperation

@task(name="scripts/create_database.mysql.sh", 
      description="create the database tables")
def createdb_task():
    with ShellOperation(
        commands=[
            "scripts/create_database.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/ingest/01_download_from_ftp.sh", 
      description="download files from FTP server")
def download_task():
    with ShellOperation(
        commands=[
            "scripts/ingest/01_download_from_ftp.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/ingest/02_extract_downloaded_files.sh", 
      description="unzip the downloaded zip files")
def unzip_task():
    with ShellOperation(
        commands=[
            "scripts/ingest/02_extract_downloaded_files.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/ingest/03_extract_basic_info_from_downloaded_files.sh", 
      description="extract file info (path")
def extract_basic_info_task():
    with ShellOperation(
        commands=[
            "scripts/ingest/03_extract_basic_info_from_downloaded_files.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/ingest/04_import_basic_info.mysql.sh", 
      description="import file info into MySQL (it first transforms CSV to SQL)")
def import_basic_info_task():
    with ShellOperation(
        commands=[
            "scripts/ingest/04_import_basic_info.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/ingest/05_harvest_edm.mysql.sh", 
      description="(optional) harvest Europeana-EDM records for each data sets")
def harvest_edm_task():
    with ShellOperation(
        commands=[
            "scripts/ingest/05_harvest_edm.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/index/01_index_ddb-edm.sh", 
      description="index DDB-EDM records")
def index_ddb_edm_task():
    with ShellOperation(
        commands=[
            "scripts/index/01_index_ddb-edm.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/index/02_index_marc.sh", 
      description="index MARC records")
def index_marc_task():
    with ShellOperation(
        commands=[
            "scripts/index/02_index_marc.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/index/03_index_ddb-dc.sh", 
      description="index DDB-DC records")
def index_ddb_dc_task():
    with ShellOperation(
        commands=[
            "scripts/index/03_index_ddb-dc.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/index/04_index_lido.sh", 
      description="index LIDO records")
def index_lido_task():
    with ShellOperation(
        commands=[
            "scripts/index/04_index_lido.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/index/05_index_mets-mods.sh", 
      description="index METS-MODS records")
def index_mets_mods_task():
    with ShellOperation(
        commands=[
            "scripts/index/05_index_mets-mods.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/01_process_ddb-edm.sh", 
      description="quality assessment of DDB-EDM records")
def measure_ddb_edm_task():
    with ShellOperation(
        commands=[
            "scripts/process/01_process_ddb-edm.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/02_process_marc.sh", 
      description="quality assessment of MARC")
def measure_marc_task():
    with ShellOperation(
        commands=[
            "scripts/process/02_process_marc.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/03_process_ddb-dc.sh", 
      description="quality assessment of DDB-DC")
def measure_ddb_dc_task():
    with ShellOperation(
        commands=[
            "scripts/process/03_process_ddb-dc.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/04_process_lido.sh", 
      description="quality assessment of LIDO")
def measure_lido_task():
    with ShellOperation(
        commands=[
            "scripts/process/04_process_lido.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/05_process_mets-mods.sh", 
      description="quality assessment of METS-MODS")
def measure_mets_mods_task():
    with ShellOperation(
        commands=[
            "scripts/process/05_process_mets-mods.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/11_import_ddb-edm.mysql.sh", 
      description="import DDB-EDM")
def import_ddb_edm_task():
    with ShellOperation(
        commands=[
            "scripts/process/11_import_ddb-edm.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/11_import_marc.mysql.sh", 
      description="import MARC")
def import_marc_task():
    with ShellOperation(
        commands=[
            "scripts/process/11_import_marc.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/11_import_dc.mysql.sh", 
      description="import DDB-DC")
def import_dc_task():
    with ShellOperation(
        commands=[
            "scripts/process/11_import_dc.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/11_import_lido.mysql.sh", 
      description="import LIDO")
def import_lido_task():
    with ShellOperation(
        commands=[
            "scripts/process/11_import_lido.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/11_import_mets-mods.mysql.sh", 
      description="import METS-MODS")
def import_mets_mods_task():
    with ShellOperation(
        commands=[
            "scripts/process/11_import_mets-mods.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@task(name="scripts/process/12_calculate_aggregations.mysql.sh", 
      description="calculate aggregated results")
def calculate_aggregations_task():
    with ShellOperation(
        commands=[
            "scripts/process/12_calculate_aggregations.mysql.sh"
        ],
        working_dir=f".",
        return_all=True,
        log_stderr=True
    ) as my_script:
        my_script_process = my_script.trigger()
        my_script_process.wait_for_completion()


@flow
def ingest_flow():
    download_task()
    unzip_task()
    extract_basic_info_task()
    import_basic_info_task()
    harvest_edm_task()


@flow
def index_flow():
    index_ddb_edm_task()
    index_marc_task()
    index_ddb_dc_task()
    # index_lido_task()
    # index_mets_mods_task()


@flow
def measure_flow():
    measure_ddb_edm_task()
    measure_marc_task()
    measure_ddb_dc_task()
    # measure_lido_task()
    # measure_mets_mods_task()


@flow
def import_flow():
    import_ddb_edm_task()
    import_marc_task()
    import_dc_task()
    # import_lido_task()
    # import_mets_mods_task()


@flow
def main_flow():
    createdb_task()
    ingest_flow()
    index_flow()
    measure_flow()
    import_flow()
    calculate_aggregations_task()


if __name__ == "main":
    main_flow()
