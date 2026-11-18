records = {}

def read_int(text):
    
    try:
        return int(text.strip())
    except ValueError:
        return None
    
    
def valid_marks(marks):
    return marks is not None and 0 <= marks <= 100

def format_record(roll, data):
    name, course, marks = data
    return f"{roll} | {name} | {course} | {marks}"


def add_record(roll, name, course, marks):
    
    if roll is None:
        return "roll number must be a number."
    if roll in records:
        return f"Roll number {roll} already exists."
    if not valid_marks(marks):
        return "marks must be between 0 and 100."
    if not name or not course:
        return "Name and course cannot be empty."
    records[roll] = (name,course,marks)
    return "Record added: " + format_record(roll,records[roll])

def view_records():
    if not records:
        return "No records found."
    rows = sorted(records.items())
    line = "+---------+------------------------+-------------+---------+"
    out = [line,
           f"| {'Roll':<6} | {'Name':<20} | {'Course':<10} | {'Marks':<5} |",
           line]
    for roll, (name, course, marks) in rows:
        out.append(f"|{roll:<6} | {name:<20} | {course:<10} | {marks:<5} | ")
    out.append(line)
    return "\n".join(out)

def search_record(roll):
    if roll is None or roll not in records:
        return f"Roll number {roll} not found."
    return format_record(roll, records[roll])


def uodate_record(roll, new_marks):
    if roll is None or roll not in records:
        return f"Roll number {roll} not found."
    if not valid_marks(new_marks):
        return "Marks must be between 0 and 100."
    name, course, _ = records[roll]
    records[roll] = (name,course,new_marks)
    return f"Marks updated: {new_marks}"

def delete_record(roll):
    if roll is None or roll not in records:
        return f"Roll number {roll} not found."
    del records[roll]
    return f"Record deleted: {roll}"

MENU = """
===== Student Record Management System =====
1. Add record
2. View all records
3. Search record
4. Update marks
5. Delete record
6. Exit"""


def main():
    while True:
        print(MENU)
        choice = input("Enter option: ").strip()
        
        if choice == "1":
            line = input("Enter roll no,name,course,marks (comma separated):")
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 4:
                print("please enter exactly 4 values: roll, name, course, marks.")
                continue
            roll, name, course, marks = parts
            print(add_record(read_int(roll),name,course,read_int(marks)))
            
        elif choice =="2":
            print(view_records())
            
        elif choice =="3":
            roll = read_int(input("Enter roll number to search: "))
            print(search_record(roll))
            
        elif choice == "4":
            roll = read_int(input("Enter roll number: "))
            marks = read_int(input("Enter new marks: "))
            print(uodate_record(roll, marks))

        elif choice == "5":
            roll = read_int(input("Enter roll number to delete: "))
            print(delete_record(roll))
            
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. please choose 1-6. ")
            
            
if __name__=="__main__":
    main()  
