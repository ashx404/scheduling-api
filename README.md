# scheduling-api

> A Task Scheduling API which can be used to schedule GET requests to a specific URL passed.
> Parameters:
> 1)date 'd' which takes date input in the format as specified [dd-mm-yyyy] Example- d=22-12-2019
> 2)time 't' which takes time input in the 24 hour format as specified [hh:mm](IST) Example- t=20:41
> 3)url 'url' API route which we want to GET whenever the date-time matches. Example- url=http://localhost:9999/mock

> Routes :

1. /ping : which returns the 'OK' status.
2. /schedule : actual route used to schedule
   Call as '/schedule?t=22:00&d=22-12-2019&url=http://localhost:9999/mock'

## Setup

```bash
# install dependencies
pip3 install -r requirements.txt

# start server
python manage.py runserver

```
