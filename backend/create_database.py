from sqlalchemy import create_engine

# Define the SQLite URL
sqlite_url = "sqlite:///artdatabase.db"

# Create an engine
engine = create_engine(sqlite_url)

# Read SQL from the file and split into individual statements
with open('create_schema.sql') as file:
    sql_commands = file.read().split(';')

# Execute each SQL statement individually
for command in sql_commands:
    if command.strip() != '':
        engine.execute(command)

print("Database and tables created successfully.")