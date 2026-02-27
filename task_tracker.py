from datetime import datetime
# ---------------------------------
# Stage Class
# ---------------------------------
class Stage:
    def __init__(self, name):
        self.name = name
        self.status = "Pending"
        
# --------------------------------
# Task Class
# ---------------------------------
class Task:
    def __init__(self, task_id, lesson_name, assigned_to, due_date):
        self.task_id = task_id
        self.lesson_name = lesson_name
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.status = "Pending"

        # 5 Fixed Workflow Stages
        self.stages = [
            Stage("AI Image Creation"),
            Stage("Image Voice-over"),
            Stage("Screen Recording"),
            Stage("Screen Recording Voice-over"),
            Stage("Video Editing")
        ]
    # ---------------------------------
    # function to check task status
    # ---------------------------------
    def check_status(self):
        today = datetime.today().date()
        delay_days = (today - self.due_date).days

        print("\n---------------------------------------------------------")
        print(f"Task ID      : {self.task_id}")
        print(f"Lesson Name  : {self.lesson_name}")
        print(f"Assigned To  : {self.assigned_to}")
        print(f"Due Date     : {self.due_date}")
        print(f"Task Status  : {self.status}")

        # Display All Stages
        print("\nWorkflow Stages:")
        for stage in self.stages:
            print(f"  - {stage.name} : {stage.status}")

        # Overdue & Reminder Logic
        if delay_days > 0 and self.status == "Pending":
            print("\n Task is OVERDUE!")
            print("→ Send Email Reminder")

            if delay_days > 2:
                print("→ Send WhatsApp Reminder")

            if delay_days > 5:
                print("→ Trigger IVR Call")
        else:
            print("\n Task is On Time")

        print("----------------------------------------------------\n")


# ---------------------------------
# Safe Date Input Function
# ---------------------------------
def get_valid_date():
    while True:
        date_input = input("Enter Due Date (YYYY-MM-DD): ")
        try:
            return datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print(" Invalid date format! Please use YYYY-MM-DD.")


# ---------------------------------
# Safe Integer Input
# ---------------------------------
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# ---------------------------------
# Main Program
# ---------------------------------
def main():
    print("\n-------------Workflow Task Tracker -----------------------\n")

    tasks = []

    total_tasks = get_valid_int("How many tasks do you want to enter? ")

    for i in range(total_tasks):
        print(f"\nEnter details for Task {i+1}")

        task_id = get_valid_int("Enter Task ID: ")
        lesson_name = input("Enter Lesson Name: ")
        assigned_to = input("Enter Assigned To: ")
        due_date = get_valid_date()

        task = Task(task_id, lesson_name, assigned_to, due_date)
        tasks.append(task)

    print("\n\n-------------------Checking All Tasks ------------------------")

    for task in tasks:
        task.check_status()


if __name__ == "__main__":
    main()