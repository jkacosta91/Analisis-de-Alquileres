import os
import logging
import pandas as pd
from modules import DataConn
from dotenv import load_dotenv

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s :: MainModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()


def main():
    user_credentials = {
        "REDSHIFT_USERNAME": os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD": os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST": os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT": os.getenv('REDSHIFT_PORT', '5439'),
        "REDSHIFT_DBNAME": os.getenv('REDSHIFT_DBNAME')
    }

    schema: str = "jkacosta91_coderhouse"
    table: str = "idealista"

    data_conn = DataConn(user_credentials, schema)

    # Carga de datos desde el CSV de Idealista
    try:
        file_path = "idealista.csv"
        data_df = pd.read_csv(file_path)
    except FileNotFoundError:
        logging.error(f"Idealista data file not found: {file_path}")
        return

    try:
        data_conn.upload_data(data_df, table)
        logging.info(f"Data uploaded to -> {schema}.{table}")
    except Exception as e:
        logging.error(f"Not able to upload data\n{e}")

    finally:
        data_conn.close_conn()


if __name__ == "__main__":
    main()