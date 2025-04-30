from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_async_engine(os.getenv('DATABASE'))
new_session = async_sessionmaker(engine, expire_on_commit=False)
