from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"  # Adjust if needed
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    with engine.connect() as conn:
        print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", e)