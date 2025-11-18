from pydantic import BaseModel


class UCConfig(BaseModel):
    catalog_name: str = "nbp"
    source_schema: str = "source"
    bronze_schema: str = "bronze"
    silver_schema: str = "silver"
    gold_schema: str = "gold"


class NBPConfig(BaseModel):
    table_a: str = "table_a"
    table_b: str = "table_b"


class Config(BaseModel):
    catalog: UCConfig = UCConfig()
    nbp: NBPConfig = NBPConfig()


config = Config()
