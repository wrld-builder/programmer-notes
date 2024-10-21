from tasks import upload_data


result = upload_data.delay()
print(result)
