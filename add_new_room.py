__author__ = 'aclement'

import os


def addRoom(newRoomNumber):
    rooms = RoomSlot.objects.filter(room=" 8")
    for r in rooms:
        RoomSlot.objects.get_or_create(period=r.period, start_time = r.start_time, end_time = r.end_time, date = r.date, room = newRoomNumber, reserved=False, day_type=r.day_type)


if __name__ == "__main__":
    from django.conf import settings
    newRoomName = "9"
    newRoomNumber = " 12"
    print "Adding Room " + newRoomName +" Collab Slots.........."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KentCollabCheckout.settings")
    from CollabCheckout.models import RoomSlot

    addRoom(newRoomNumber)