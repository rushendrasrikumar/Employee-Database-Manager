from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(uri)
db = client["employee_db"]
collection = db["employees"]

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    collection.insert_one({"name": name, "age": age, "department": department})
    print("✅ Employee added.")

def view_employees():
    print("\n📋 Employee List:")
    for emp in collection.find():
        print(f"ID: {emp['_id']} | Name: {emp['name']} | Age: {emp['age']} | Department: {emp['department']}")

def update_employee():
    emp_id = input("Enter employee _id to update: ")
    field = input("Field to update (name, age, department): ")
    new_value = input(f"Enter new value for {field}: ")
    if field == "age":
        new_value = int(new_value)
    collection.update_one({"_id": eval(emp_id)}, {"$set": {field: new_value}})
    print("🔄 Employee updated.")

def delete_employee():
    emp_id = input("Enter employee _id to delete: ")
    collection.delete_one({"_id": eval(emp_id)})
    print("🗑️ Employee deleted.")

def main():
    while True:
        print("\nEmployee Database Manager")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

