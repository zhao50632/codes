# Define a function to execute SQL queries and compare results from Oracle and PostgreSQL databases
def execute_and_compare_queries(sql_queries):
    for sql_query in sql_queries:
        # Connect to Oracle database
        oracle_connection = cx_Oracle.connect("username", "password", "host:port/service_name")
        oracle_cursor = oracle_connection.cursor()

        # Execute the SQL query on Oracle database
        oracle_cursor.execute(sql_query)

        # Fetch the results from Oracle database
        oracle_results = oracle_cursor.fetchall()

        # Close the Oracle connection
        oracle_cursor.close()
        oracle_connection.close()

        # Connect to PostgreSQL database
        postgres_connection = psycopg2.connect("dbname=your_db_name user=your_username password=your_password host=your_host port=your_port")
        postgres_cursor = postgres_connection.cursor()

        # Execute the SQL query on PostgreSQL database
        postgres_cursor.execute(sql_query)

        # Fetch the results from PostgreSQL database
        postgres_results = postgres_cursor.fetchall()

        # Close the PostgreSQL connection
        postgres_cursor.close()
        postgres_connection.close()

        # Export the query results to separate txt files
        with open("oracle_query_results.txt", "a") as oracle_output_file:
            # Write the header (column names) to the txt file
            header = [desc[0] for desc in oracle_cursor.description]
            oracle_output_file.write("\t".join(header) + "\n")

            # Write the Oracle results to the txt file
            for row in oracle_results:
                oracle_output_file.write("\t".join(map(str, row)) + "\n")

        with open("postgres_query_results.txt", "a") as postgres_output_file:
            # Write the header (column names) to the txt file
            header = [desc[0] for desc in postgres_cursor.description]
            postgres_output_file.write("\t".join(header) + "\n")

            # Write the PostgreSQL results to the txt file
            for row in postgres_results:
                postgres_output_file.write("\t".join(map(str, row)) + "\n")

        # Compare the results from Oracle and PostgreSQL
        if oracle_results != postgres_results:
            # If the results are different, write the SQL query to a txt file
            with open("different_results.txt", "a") as diff_file:
                diff_file.write(sql_query + "\n")

# Define a list of SQL queries
sql_queries = ["SELECT * FROM your_table_name1;", "SELECT * FROM your_table_name2;", "SELECT * FROM your_table_name3;"]

# Call the function with the list of SQL queries
execute_and_compare_queries(sql_queries)
