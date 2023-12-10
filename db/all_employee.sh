#!/bin/bash

# Path to the SQLite database file
db_path="/Users/nednik/PycharmProjects/502IT-cw2/db/Bookstore.db"

# SQL query to update the role
sql_query="UPDATE Users SET role = 'employee';"

# Execute the SQL query using the sqlite3 command
sqlite3 "$db_path" "$sql_query"
