import os


def clear_screen():
    command = {
        'posix': 'clear',
        'nt': 'cls'
    }.get(os.name)

    os.system(command)