#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    pass
    n = 0
    while wall_is_beneath():
        if cell_is_filled():
            n += 1
        elif wall_is_above():
            fill_cell()

        while not wall_is_above():
            move_up()
            if cell_is_filled():
                n += 1
            else:
                fill_cell()

        while not wall_is_beneath():
            move_down()

        move_right()

    mov('ax', n)

if __name__ == '__main__':
    run_tasks()
