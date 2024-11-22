import todo_list

def test_get_tasks_size():
    tasks_size = todo_list.get_tasks_size()

    # do assertion
    assert tasks_size == 0

def test_add_task():
    todo_list.add_task('taskname here')

    size = todo_list.get_tasks_size()

    assert size == 1