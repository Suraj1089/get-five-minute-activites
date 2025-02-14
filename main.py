from datetime import date

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# for demo purpose. due to time constraints not using any database
# another format I could have use that storing all the result with
# date as a key but if user input date is not match it will return
# empty response. hence sending all the response regardless of key

DAILY_DATA = [
    {
        "id": 1,
        "title": "Stimulus Explosion",
        "tag": "G 2x/Week",
        "is_completed": False
    },
    {
        "id": 2,
        "title": "Advanced Mobility",
        "tag": "G Maximize",
        "is_completed": False
    },
    {
        "id": 3,
        "title": "Auditory Memory 2",
        "tag": "G 1x/Day",
        "is_completed": False
    },
    {
        "id": 4,
        "title": "Auditory Magic",
        "tag": "G 2 sounds/Day",
        "is_completed": False
    },
    {
        "id": 5,
        "title": "Knowledge Boosters",
        "tag": "G 2x/Day",
        "is_completed": False
    },
    {
        "id": 6,
        "title": "Talk To Listen",
        "tag": "G 1x/Day",
        "is_completed": False
    },
    {
        "id": 7,
        "title": "Energy Ball",
        "tag": "Maximize",
        "is_completed": False
    },
    {
        "id": 8,
        "title": "Visual Solfege",
        "tag": "G 1x/Day",
        "is_completed": False
    }
]


class DailyDataUpdate(BaseModel):
    user_id: int | None
    request_date: date | None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/per_day_plan')
def get_per_day_plan(
    request_date: date | None = None
):
    if request_date is None:
        request_date = date.today()
    # not using this data
    # but in real word application we can query the database
    # and get the result accordingly for the given date
    remaining_activites = len(
        list(filter(lambda i: not i['is_completed'], DAILY_DATA)))
    # fastapi will handle this and return 200 status code with this data
    return {'remaining_activites': remaining_activites, 'data': DAILY_DATA}


@app.patch('/per_day_plan/{task_id}')
def update_per_day_plan(
    task_id: int,
    # in real world we could have Authorization token in header to identify user.
    task: DailyDataUpdate
):
    request_date = task.request_date
    if request_date is None:
        # here we can use localization if we want.
        # send simple error message
        return {'user_message': 'Invalid date. please select a date'}
    # get the data for user id and request_date combination
    # from database
    # for now I will just update the data in DAILY_DATA
    for item in DAILY_DATA:
        if item['id'] == task_id:
            item['is_completed'] = not item['is_completed']
    remaining_activites = len(
        list(filter(lambda i: not i['is_completed'], DAILY_DATA)))
    return {'remaining_activites': remaining_activites, 'data': DAILY_DATA}
