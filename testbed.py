import os
from collections import OrderedDict
from datetime import date, time, datetime, timedelta


__author__ = 'Alex Clement'


def remove_duplicates(list):
    new_list = []
    seen = set()
    for e in list:
        value = e.class_title
        if value not in seen:
            new_list.append(e)
            seen.add(value)

    return new_list

def print_list(list):
    for e in list:
        print e

def format_time(time):
    if len(time) > 3:
        mins = time[2:4]
        hours = time[:2]
    else:
        mins = time[1:3]
        hours = "0"+time[0:1]
    return hours +":"+mins

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCollabCheckout.settings")
from CollabCheckout.models import RoomSlot
from CollabCheckout.views import get_periods, get_room_name, get_period_name

# temp = Calendar.objects.filter(period = 2, class_title__istartswith="AP")
#
# temp = temp[0]
#
# print temp.class_title
#
# print views.get_teachers(temp.class_title, period = 2)
#
# temp_list = Calendar.objects.filter(period=1)
#
# print_list(temp_list)
#
# print '__________________________________________'
# print_list(remove_duplicates(temp_list))

# print Calendar.objects.all()
#
# print Calendar.objects.filter(period = 6, school__in=[7,8])
#
# print_list(Calendar.objects.filter(school=6))
#
# print Calendar.objects.filter(school = 6, class_title__in=["6th Latin Language Arts", "6th Physical Education", "6th Writing Skills", "6th Arts Rotation", "6th Latin"], period=1)
#
# print Calendar.objects.filter(school="ELEC")
#
# class_name = "6th Science"
#
# print class_name.split("6th ")[1].lower()
#
# print Calendar.objects.filter(period=10, class_title="KDS Letter Days")


# print_list(RoomSlot.objects.all())
#
# periods=RoomSlot.objects.values_list('period').distinct()
# new_periods = []
# for period in periods:
#     if period[0] == 0:
#         temp = (0, "Before school")
#     elif period[0] == 8:
#         temp = (8, "After school: 3:30-4:30")
#     elif period[0] == 9:
#         temp = (9, "After school: 4:30-5:30")
#     elif period[0] == 10:
#         temp = (10, "First Half of Lunch")
#     elif period[0] == 11:
#         temp = (11, "Second Half og Lunch")
#     else:
#         temp = (period[0], period[0])
#     new_periods.append(temp)
#
# print new_periods
#
# print_list(Calendar.objects.filter(period=1))
#
# dateText = "8/20/2014"
# period = 1
# email = "aclement@kentdenver.org"
#
# rooms = []
# date_array = str(dateText).split("/")
# d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
# rooms = RoomSlot.objects.filter(period=period, date=d, reserved=False)
# new_rooms=[]
# for r in rooms:
#     number = int(r.room)
#     if number == 1:
#         roomString = "Collaboration Studio 1"
#     elif number ==  2:
#         roomString = "Collaboration Studio 2"
#     elif number == 3:
#         roomString = "Collaboration Studio 3"
#     elif number == 4:
#         roomString = "Collaboration Studio 4"
#     elif number == 5:
#         roomString = "Collaboration Studio 5"
#     elif number == 6:
#         roomString = "Collaboration Studio 6"
#     elif number == 7:
#         roomString = "Collaboration Studio 7"
#     elif number == 8:
#         roomString = "Collaboration Studio 8"
#     elif number == 9 and str(email).find("1") == -1:
#         roomString = "Duncan Center 3"
#     elif number == 10 and str(email).find("1") == -1:
#         roomString = "Duncan Center 4"
#     elif number == 11 and str(email).find("1") == -1:
#         roomString = "Global Teleconferencing Center"
#     temp = dict(number=number, text=roomString)
#     new_rooms.append(temp)
#
# print_list(new_rooms)



date_source = datetime.now()
time = date_source.time()
end_time = date_source - timedelta(minutes=5)
d = date_source.date()

print time
print end_time
print date_source.date()

current_period = RoomSlot.objects.filter(start_time__lte = time, end_time__gte = end_time, date = d)[0]
print current_period

period_usage = []
all_meetings = RoomSlot.objects.all()
for i in range(1,13):
    room_meetings = RoomSlot.objects.filter(room=i)
    for j in room_meetings:
        if j.reserved:
            print j.period



