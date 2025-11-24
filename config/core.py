from pydantic import BaseModel


class UCConfig(BaseModel):
    catalog_name: str = "nbp"
    source_schema: str = "source"
    bronze_schema: str = "bronze"
    silver_schema: str = "silver"
    gold_schema: str = "gold"
    gold_table: str = "gold_table"


class NBPConfig(BaseModel):
    table_a: str = "table_a"
    table_b: str = "table_b"
    rate_type_a: str = "A"
    rate_type_b: str = "B"
    update_frequency_a: str = "DAILY"
    update_frequency_b: str = "WEEKLY"


class GitHub(BaseModel):
    repo: str = "Life_ETL"
    owner: str = "Jan-Dyndor"


class Config(BaseModel):
    catalog: UCConfig = UCConfig()
    nbp: NBPConfig = NBPConfig()
    github: GitHub = GitHub()


config = Config()
