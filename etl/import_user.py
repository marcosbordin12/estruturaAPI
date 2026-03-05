import csv
from app.database import SessionLocal
from app.services import register_user

db = SessionLocal()

with open("etl/users.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        register_user(db, row["name"], row["email"], row["password"])