import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",   # change this
        database="your_database"    #change this
    )

    if mydb.is_connected():
        print("Connection Ok")

    mycursor = mydb.cursor()

    # Create table
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS fee (
        roll INT PRIMARY KEY,
        name VARCHAR(100),
        amount INT,
        branch VARCHAR(20),
        phone BIGINT
    )
    """)

    while True:
        print("\n===== MENU =====")
        print("1. Insert Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. View Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # INSERT
        if choice == '1':
            try:
                r = int(input("Enter roll number: "))
                n = input("Enter name: ")
                m = int(input("Enter amount: "))
                b = input("Enter branch: ")
                p = int(input("Enter phone: "))

                sql = "INSERT INTO fee VALUES (%s, %s, %s, %s, %s)"
                mycursor.execute(sql, (r, n, m, b, p))
                mydb.commit()

                print("Record Inserted")
            except Exception as e:
                print("Error:", e)

        # UPDATE
        elif choice == '2':
            try:
                r = int(input("Enter roll number to update: "))
                print("What do you want to update?")
                print("1. Name\n2. Amount\n3. Branch\n4. Phone")

                field_choice = input("Enter choice: ")

                if field_choice == '1':
                    new_val = input("Enter new name: ")
                    sql = "UPDATE fee SET name=%s WHERE roll=%s"

                elif field_choice == '2':
                    new_val = int(input("Enter new amount: "))
                    sql = "UPDATE fee SET amount=%s WHERE roll=%s"

                elif field_choice == '3':
                    new_val = input("Enter new branch: ")
                    sql = "UPDATE fee SET branch=%s WHERE roll=%s"

                elif field_choice == '4':
                    new_val = int(input("Enter new phone: "))
                    sql = "UPDATE fee SET phone=%s WHERE roll=%s"

                else:
                    print("Invalid choice")
                    continue

                mycursor.execute(sql, (new_val, r))
                mydb.commit()

                if mycursor.rowcount > 0:
                    print("Record Updated")
                else:
                    print("Roll number not found")

            except Exception as e:
                print("Error:", e)

        # DELETE
        elif choice == '3':
            try:
                r = int(input("Enter roll number to delete: "))
                sql = "DELETE FROM fee WHERE roll=%s"

                mycursor.execute(sql, (r,))
                mydb.commit()

                if mycursor.rowcount > 0:
                    print("Record Deleted")
                else:
                    print("Roll number not found")

            except Exception as e:
                print("Error:", e)

        # VIEW
        elif choice == '4':
            try:
                mycursor.execute("SELECT * FROM fee")
                records = mycursor.fetchall()

                print("\n--- Records ---")
                for row in records:
                    print(row)

            except Exception as e:
                print("Error:", e)

        # EXIT
        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

except mysql.connector.Error as err:
    print("Database Error:", err)

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("Connection Closed")