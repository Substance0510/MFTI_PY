#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    pass
    if wall_is_above() == False:
        move_up()
    elif wall_is_beneath() == False:
        move_down()
    elif wall_is_on_the_left() == False:
        move_left()
    elif wall_is_on_the_right() == False:
        move_right()
    else:
        print('ALARM!!!')

if __name__ == '__main__':
    run_tasks()
