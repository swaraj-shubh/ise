import os
from sqlalchemy import create_engine

db_url = "postgresql://neondb_owner:npg_cL1zbWxnrg7p@ep-still-night-aoni83q8-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
if "?sslmode=require" in db_url:
    db_url = db_url.replace("?sslmode=require", "")

try:
    engine = create_engine(db_url, connect_args={"sslmode": "require"})
    engine.connect()
    print("Success")
except Exception as e:
    print("Error:", e)
