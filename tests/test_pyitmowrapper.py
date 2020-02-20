from pyitmowrapper import ItmoAPI


def test_itmo_group_schedule():
    """Tests itmo group schedule"""
    provider = ItmoAPI()
    lessons_list = provider.scheduleApi.get_group_schedule('P3114')
    assert isinstance(lessons_list, dict)
    assert lessons_list['label'] == 'P3114'


def test_itmo_room_list():
    """Tests itmo room list"""
    provider = ItmoAPI()
    room_list = provider.scheduleApi.get_room_list()
    assert isinstance(room_list, list)
    assert 'room' in room_list[0].keys()


def test_get_teachers_list_by_offset():
    """Tests itmo teachers list by offset"""
    provider = ItmoAPI()
    teachers_list = provider.scheduleApi.get_teachers_list_by_offset(0)
    assert isinstance(teachers_list, dict)
    assert isinstance(teachers_list['list'], list)


def test_get_teachers_list_by_lastname():
    """Tests itmo teachers list by lastname"""
    provider = ItmoAPI()
    teachers_list = provider.scheduleApi.get_teachers_list_by_lastname('')
    assert isinstance(teachers_list, dict)
    assert isinstance(teachers_list['list'], list)


def test_lessons_schedule_by_teacher_id():
    """Tests itmo teachers schedule by pid"""
    provider = ItmoAPI()
    pid = 110103
    teachers_schedule = provider.scheduleApi. \
        lessons_schedule_by_teacher_id(pid)
    assert isinstance(teachers_schedule, dict)
    assert isinstance(teachers_schedule['schedule'], list)
    assert teachers_schedule['pid'] == pid
