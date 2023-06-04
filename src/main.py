class TodoList():

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return f'{self.__class__.__name__}({self.task})'

    def __str__(self):
        return '\n'.join(self.task)

    def __add__(self, oth):
        oth = self.task + oth.task
        obj = TodoList(oth)
        return obj


tasks = ['Task1', 'Task2']
list1 = TodoList(tasks)

print(repr(list1))
# TodoList(list[str])

print(list1)
# task1
# task2

list2 = TodoList(['task3', 'task4'])

list3 = list1 + list2

print(list3)
# task1
# task2
# task3
# task4
