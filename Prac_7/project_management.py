from project import Project
from datetime import datetime


def main():
    file_name = 'projects.txt'
    projects = load_projects(file_name)
    print_menu()
    choice = input(">>>").lower()
    while choice != "q":
        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(file_name, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y")
            filtered_projects = filter_projects_by_date(projects, date)
            for project in filtered_projects:
                print(project)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid option, please try again.")
        print_menu()
        choice = input(">>> ").lower()


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        project_choice = int(input("Project choice: "))
        selected_project = projects[project_choice]
        print(selected_project)

        new_completion_percentage = input("New Percentage: ")
        if new_completion_percentage:
            selected_project.update_completion(new_completion_percentage)

        new_priority = input("New Priority: ")
        if new_priority:
            selected_project.update_priority(new_priority)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def load_projects(file_name):
    projects = []
    with open(file_name, 'r') as file:
        file.readline()
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            project_data = [project.name,
                            project.start_date.strftime('%d/%m/%Y'),
                            str(project.priority),
                            str(project.cost_estimate),
                            str(project.completion_percentage)]
            file.write("\t".join(project_data) + "\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects: ")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects: ")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    return filtered_projects


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)

    projects.append(new_project)

def print_menu():
    """Print the main menu for the application"""
    print("- (L)oad projects from file")
    print("- (S)ave projects to file")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

main()