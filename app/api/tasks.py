from celery import shared_task
# from time import sleep

# @shared_task(bind=True)
# def example_task(self):
#     print(self.request.id)
#     for i in range(1,101):
#         print(i)
#         self.update_state(state='PROGRESS', meta={'current': i, 'total': 100})
#         sleep(1)
        
#     return "Done"