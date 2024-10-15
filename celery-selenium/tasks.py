import time
from selenium import webdriver
from celery import Celery
from selenium.webdriver.common.by import By

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://localhost:6379/0')


@app.task
def selenium_open_page(index: int):
    with open('./pages.txt', mode='r') as file:
        urls = [i[:-1] for i in file.readlines()]
    print(urls)

    driver = webdriver.Chrome()
    driver.get('https://' + urls[index])
    time.sleep(3)
    title = driver.title
    driver.quit()

    return title

