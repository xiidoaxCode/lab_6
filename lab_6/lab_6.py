#Myhailiv Ivan TR - 15

class Task:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    def calculate_estimation(self):
        E = (self.a + 4 * self.m + self.b) / 6
        SD = (self.b - self.a) / 6
        return E, SD


class Project:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def calculate_estimation(self):
        total_E = 0
        total_SE = 0

        for task in self.tasks:
            E, SD = task.calculate_estimation()
            total_E += E
            total_SE += SD

        project_E = total_E
        project_SE = total_SE

        project_CI_min = project_E - 2 * project_SE
        project_CI_max = project_E + 2 * project_SE

        return project_CI_min, project_CI_max


num_tasks = int(input("Enter the number of tasks: "))

project = Project()

for i in range(num_tasks):
    a = float(input("Enter the value for a in task {}: ".format(i+1)))
    m = float(input("Enter the value for m in task {}: ".format(i+1)))
    b = float(input("Enter the value for b in task {}: ".format(i+1)))
    task = Task(a, m, b)
    project.add_task(task)


project_CI_min, project_CI_max = project.calculate_estimation()


print("Project's 95% confidence interval: {} ... {} points".format(project_CI_min, project_CI_max))

