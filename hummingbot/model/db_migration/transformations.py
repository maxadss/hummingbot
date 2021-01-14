from hummingbot.model.db_migration.base_transformation import DatabaseTransformation
from hummingbot.model.sql_connection_manager import SQLConnectionManager
from sqlalchemy import (
    Column,
    Text,
)


class AddExchangeTradeIdColumnToOrders(DatabaseTransformation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def apply(self, db_handle: SQLConnectionManager) -> SQLConnectionManager:
        exchange_trade_id_column = Column("exchange_trade_id", Text, nullable=True)
        self.add_column(db_handle.engine, "Order", exchange_trade_id_column, dry_run=False)
        return db_handle

    @property
    def name(self):
        return "AddExchangeTradeIdColumnToOrders"

    @property
    def from_version(self):
        return 20190614

    @property
    def to_version(self):
        return 20210114
