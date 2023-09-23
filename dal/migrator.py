from alembic.config import Config
from typing import NoReturn
from sqlalchemy_utils import database_exists, create_database
from alembic import command


class Migrator(object):

    @staticmethod
    def start_migration() -> NoReturn:
        alembic_cfg = Config("././alembic.ini")
        url = alembic_cfg.get_section_option('alembic', 'sqlalchemy.url')

        if not database_exists(url):
            create_database(url)

        command.upgrade(alembic_cfg, "head")
