from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

import Category.models  # noqa: F401
import Customer.models  # noqa: F401
import Order.models  # noqa: F401
import Product.models  # noqa: F401
from alembic import context
from config import DATABASE_URL
from db import Base

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_sync_database_url() -> str:
    if DATABASE_URL.startswith("sqlite+aiosqlite"):
        return DATABASE_URL.replace("sqlite+aiosqlite", "sqlite")
    return DATABASE_URL.replace("+asyncpg", "")


def run_migrations_offline():
    context.configure(
        url=get_sync_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        {
            "sqlalchemy.url": get_sync_database_url(),
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
