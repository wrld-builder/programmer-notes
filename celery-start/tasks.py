from celery import Celery


app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://localhost:6379/0')

@app.task
def upload_data():
    with open('new.txt', mode='a+') as f:
        f.write('Hello!\n')
