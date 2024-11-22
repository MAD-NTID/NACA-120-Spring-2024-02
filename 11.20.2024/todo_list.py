# A list of dictionary values
# [] is a list
# {} is a dictionary
# When you put it together
# [{}, {}, {}]

tasks = []

def get_tasks_size():
    return len(tasks)

def add_task(name, status='todo'):
    tasks.append({
        'taskname': name,
        'taskstatus': status
    })