import requests


class ScheduleAPI:
    ApiUrl = ''

    def get_teachers_list_by_offset(self, offset: int):
        req = self.ApiUrl + '/schedule_person?offset={}'.format(offset)
        return requests.get(req).json()

    def get_teachers_list_by_lastname(self, lastname: str):
        req = self.ApiUrl + '/schedule_person?lastname={}'.format(lastname)
        return requests.get(req).json()

    def get_group_schedule(self, group_name: str):
        req = self.ApiUrl + '/schedule_lesson_group/{}'.format(group_name)
        return requests.get(req).json()

    def lessons_schedule_by_teacher_id(self, teacher_id: int):
        req = self.ApiUrl + '/schedule_lesson_person/{}'.format(teacher_id)
        return requests.get(req).json()

    def get_room_list(self):
        req = self.ApiUrl + '/schedule_lesson_room'
        return requests.get(req).json()

    def __init__(self, url):
        self.ApiUrl = url


class ItmoAPI:
    ApiUrl = "https://mountain.ifmo.ru/api.ifmo.ru/public/v1"
    scheduleApi = None

    def __init__(self):
        self.scheduleApi = ScheduleAPI(self.ApiUrl)
