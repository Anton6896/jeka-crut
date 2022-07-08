import logging
import psycopg2

from src.settings import settings

logger = logging.getLogger(__name__)


class DBConnector:
    def __init__(self) -> None:
        self.connection = None
        self.ensure_tables()

    def get_connection(self):
        logger.info('getting connection')
        try:
            if self.connection:
                return self.connection
            self.connection = psycopg2.connect(**settings.db_params())
            return self.connection
        except Exception as e:
            logger.exception(f'unable to connect to db : \n{e}')

    def ensure_tables(self):
        logger.info('ensuring tables')
        name = 'user_table'
        try:
            with self.get_connection().cursor() as cur:
                cur.execute(
                    f"CREATE TABLE IF NOT EXISTS {name} ("
                    "id serial PRIMARY KEY, "
                    "username VARCHAR(255) NOT NULL, "
                    "data varchar,"
                    "timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW());"
                )
                logger.info(f'table ok {name}')
                self.get_connection().commit()

        except Exception as e:
            logger.exception(f'unable to ensure db : \n{e}')

    def table_insert(self, data: dict, table_name: str) -> bool:
        logger.info(f'inserting to table : {table_name}')
        try:
            with self.get_connection().cursor() as cur:
                keys_items = []
                values_items = []
                for key, value in data.items():
                    if key and value:
                        keys_items.append(key)
                        values_items.append(value)

                columns = ','.join(keys_items)

                q = f"INSERT INTO {table_name} ({columns}) values ("
                for item in values_items:
                    if item == values_items[-1]:
                        q += f"'{value}');"
                    else:
                        q += f"'{value}',"

                logger.info(f'query \n - {q}')

                cur.execute(q)
                cur.execute('SELECT LASTVAL()')
                lastid = cur.fetchone()[0]
                self.get_connection().commit()
                logger.info(f'inserting to table : {table_name} OK')
                return lastid

        except Exception as e:
            logger.exception(f'unable to wright to db : \n{e}')

        return False

    def __del__(self):
        if self.connection:
            logger.info('closing unclosed connection')
            self.connection.close()
