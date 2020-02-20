from pyitmowrapper import ItmoAPI

provider = ItmoAPI()

"""get schedule of group P3114"""
lessons_list = provider.scheduleApi.get_group_schedule('P3114')

"""get all rooms"""
room_list = provider.scheduleApi.get_room_list()

"""Get first 100 teachers from alphabet order list"""
teachers_list = provider.scheduleApi.get_teachers_list_by_offset(0)

"""get teachers with lastname starts with Афанас"""
teachers_list = provider.scheduleApi.get_teachers_list_by_lastname('Афанас')

"""get Afanas's schedule"""
teachers_schedule = provider.scheduleApi.lessons_schedule_by_teacher_id(110103)
