import mysql.connector

try:
    # Establish connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="menagerie"  # Replace with your database name
    )

    # Create a cursor
    mycursor = mydb.cursor()

    # SQL query to retrieve name, birth date, and month of birth
    sql_query = "SELECT name, birth, MONTH(birth) FROM pet"

    # Execute the query
    mycursor.execute(sql_query)

    # Fetch all the rows from the query result
    pet_birth_info = mycursor.fetchall()

    # Display the name, birth date, and month of birth
    for name, birth_date, month_birth in pet_birth_info:
        print(f"Name: {name}, Birth Date: {birth_date}, Month of Birth: {month_birth}")

except mysql.connector.Error as error:
    print("Error:", error)
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
