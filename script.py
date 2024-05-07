#!/usr/bin/env python3

import mysql.connector
from datetime import datetime, timedelta
import os

# Get database credentials from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

other_db_user = os.getenv('OTHER_DB_USER')
other_db_password = os.getenv('OTHER_DB_PASSWORD')
other_db_host = os.getenv('OTHER_DB_HOST')
other_db_name = os.getenv('OTHER_DB_NAME')

# Define the time range for the entire last day
start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
end_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

try:
    # Establish the connection to the first database
    with mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name) as cnx:
        # Create a cursor object
        with cnx.cursor() as cursor:
            # Query for successful tasks
            query_success = ("SELECT COUNT(*) FROM MEDIA WHERE processing_state = 'success' "
                             "AND Last_updated BETWEEN %s AND %s")

            # Query for unsuccessful tasks
            query_unsuccess = ("SELECT COUNT(*) FROM MEDIA WHERE processing_state != 'success' "
                               "AND Last_updated BETWEEN %s AND %s")

            # Execute the query for successful tasks
            cursor.execute(query_success, (start_time, end_time))

            # Fetch the result for successful tasks
            result_success = cursor.fetchone()
            print(f"Number of tasks succeeded last night: {result_success[0]}")

            # Execute the query for unsuccessful tasks
            cursor.execute(query_unsuccess, (start_time, end_time))

            # Fetch the result for unsuccessful tasks
            result_unsuccess = cursor.fetchone()
            print(f"Number of tasks failed last night: {result_unsuccess[0]}")

    # Establish the connection to the other database
    with mysql.connector.connect(user=other_db_user, password=other_db_password, host=other_db_host, database=other_db_name) as cnx2:
        # Create a cursor object for the other database
        with cnx2.cursor() as cursor2:
            # Create the task_summary table if it doesn't exist
            cursor2.execute("""
                CREATE TABLE IF NOT EXISTS task_summary (
                    date DATE,
                    successful_tasks INT,
                    unsuccessful_tasks INT
                )
            """)

            # Insert the result into the task_summary table
            insert_query = "INSERT INTO task_summary (date, successful_tasks, unsuccessful_tasks) VALUES (%s, %s, %s)"
            cursor2.execute(insert_query, (start_time.date(), result_success[0], result_unsuccess[0]))

            # Commit the changes to the other database
            cnx2.commit()

except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")