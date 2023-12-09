from sqlalchemy import create_engine, text

# Define the SQLite URL
sqlite_url = "sqlite:///artdatabase.db"

# Create an engine
engine = create_engine(sqlite_url)

# Read SQL from the file and split into individual statements
with open('create_schema.sql') as file:
    sql_commands = file.read().split(';')

# Execute each SQL statement individually
with engine.connect() as connection:
    for command in sql_commands:
        if command.strip() != '':
            connection.execute(text(command))

print("Database and tables created successfully.")
