from tasks import selenium_open_page
import time

if __name__ == '__main__':
    tasks = []

    for i in range(4):
        res = selenium_open_page.delay(i)
        tasks.append(res)

    for task in tasks:
        while not task.ready():
            pass
        print(task.get())
