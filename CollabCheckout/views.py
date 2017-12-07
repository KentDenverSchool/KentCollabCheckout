from datetime import date, datetime, timedelta
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import commit
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from CollabCheckout.forms import RoomSlotForm, ManyRoomSlotForm
from CollabCheckout.models import RoomSlot


def index(request):
    context = RequestContext(request)
    return render_to_response('CollabCheckout/index.html', context);

def get_periods(dateText = ""):
    periods = [dict(number="None", text="None")]
    if str(dateText).find("-") > -1:
        d = dateText
    else:
        date_array = str(dateText).split("/")
        d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
    day_type = RoomSlot.objects.filter(date=d)[0].day_type
    period_0 = dict(number=0, text="Before school")
    period_1 = dict(number=1, text="Period 1")
    period_2 = dict(number=2, text="Period 2")
    period_3 = dict(number=3, text="Period 3")
    period_4 = dict(number=4, text="Period 4")
    period_5 = dict(number=5, text="Period 5")
    period_6 = dict(number=6, text="Period 6")
    period_7 = dict(number=7, text="Period 7")
    period_8 = dict(number=8, text="After school: 3:30-4:30")
    period_9 = dict(number=9, text="After school: 4:30-5:30")
    period_10 = dict(number=10, text="First half of lunch")
    period_11 = dict(number=11, text="Second half of lunch")
    if day_type == "A":
        periods = [period_0, period_1, period_3, period_4, period_6, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "B":
        periods = [period_0, period_1, period_2, period_4, period_5, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "C":
        periods = [period_0, period_1, period_2, period_3, period_5, period_6, period_8, period_9, period_10, period_11]
    elif day_type == "D":
        periods = [period_0, period_2, period_3, period_4, period_6, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "E":
        periods = [period_0, period_1, period_3, period_4, period_5, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "F":
        periods = [period_0, period_1, period_2, period_4, period_5, period_6, period_8, period_9, period_10, period_11]
    elif day_type == "G":
        periods = [period_0, period_2, period_3, period_5, period_6, period_7, period_8, period_9, period_10, period_11]
    return periods

def period_list(request):
    context = RequestContext(request)
    if request.method == "GET":
        dateText = request.GET.get('dateText')
    periods = get_periods(dateText)
    context_list = dict(options = periods)
    return render_to_response('CollabCheckout/option_list.html', context_list, context)


def checkout(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = RoomSlotForm(request.POST)

        if form.is_valid():

            email = request.POST.get('email');
            period =  request.POST.get('period');
            room =  request.POST.get('room');
            room = " " + str(room)
            dateText =  request.POST.get('date');
            date_array = str(dateText).split("/")
            d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
            print ("Period: " + period + " Room: " +room + " Date: " + d)
            try:
                room = RoomSlot.objects.get(period=period, room=room, date=d, reserved=False)
            except ObjectDoesNotExist:
                extra_error = "That room is already taken, please select another"
                return render_to_response('CollabCheckout/checkout.html', {'form': form, "extra_error": extra_error}, context)
            form = RoomSlotForm(request.POST, instance=room)
            room.reserved = True;
            room.checkout_email = email;
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            extra_message = "Checkout successful!"
            return render_to_response('CollabCheckout/checkout.html', {'form': form, "extra_message": extra_message}, context)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = RoomSlotForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('CollabCheckout/checkout.html', {'form': form}, context)

def get_room_list(period, dateText, email):
    rooms = []
    date_array = str(dateText).split("/")
    d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
    rooms = RoomSlot.objects.filter(period=period, date=d, reserved=False)
    new_rooms=[]
    for r in rooms:
        number = int(r.room)
        if number == 1:
            roomString = "Collaboration Studio 1"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number ==  2:
            roomString = "Collaboration Studio 2"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 3:
            roomString = "Collaboration Studio 3"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 4:
            roomString = "Collaboration Studio 4"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 5:
            roomString = "Collaboration Studio 5"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 6:
            roomString = "Collaboration Studio 6"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 7:
            roomString = "Collaboration Studio 7"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 8:
            roomString = "Collaboration Studio 8"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 12:
            roomString = "Collaboration Studio 9"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        elif number == 9 and str(email).find("1") == -1 and str(email) != "":
            roomString = "Balcony Conference Table"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
        # elif number == 10 and str(email).find("1") == -1 and str(email) != "":
        #     roomString = "Duncan Center 4"
        #     temp = dict(number=number, text=roomString)
        #     new_rooms.append(temp)
        elif number == 11 and str(email).find("1") == -1 and str(email) != "":
            roomString = "Idea Lab"
            temp = dict(number=number, text=roomString)
            new_rooms.append(temp)
    i = -1;
    for n in new_rooms:
        if n['text'] == "Collaboration Studio 9":
            i = new_rooms.index(n)
        if n['text'] == "Collaboration Studio 8":
            i2 = new_rooms.index(n)
    if i > 0:
        temp = new_rooms[i]
        new_rooms.remove(new_rooms[i])
        new_rooms.insert(i2+1, temp)

    return new_rooms


def room_list(request):
    context = RequestContext(request)
    if request.method == "GET":
        dateText = request.GET.get('dateText')
        period = request.GET.get('period')
        email = request.GET.get('email')
    rooms = get_room_list(period, dateText, email)
    context_list = dict(options = rooms)
    return render_to_response('CollabCheckout/option_list.html', context_list, context)


def active_rooms(request):
    context = RequestContext(request)
    date_source = datetime.now()
    time = date_source.time()
    end_time = date_source - timedelta(minutes=5)
    d = date_source.date()
    try:
        current_period = RoomSlot.objects.filter(start_time__lte = time, end_time__gte = end_time, date = d)[0]
    except IndexError:
        return render_to_response('CollabCheckout/current_usage.html', {'current_period':"None", 'next_period':"None", 'list' : []}, context)
    periods = RoomSlot.objects.filter(date=d, room=current_period.room).order_by('start_time')
    i = 0
    for p in periods:
        i = i + 1
        if p.period == current_period.period:
            break
    try:
        next_period = periods[i].period
    except IndexError:
        next_period = -1;
    current_period_value = current_period.period
    context_list = dict(current_period=get_period_name(current_period_value))
    context_list['next_period'] = get_period_name(next_period)
    curr_list = RoomSlot.objects.filter(period=current_period.period, date=current_period.date)
    next_list = []
    if next_period != -1:
        next_list = RoomSlot.objects.filter(period=next_period, date=current_period.date)
    list = []
    for item in curr_list:
        if item.reserved:
            userString = item.checkout_email
        else:
            userString = ""
        list.append(dict(room=get_room_name(item.room), current_user=userString, next_user=""))
    for item in list:
        for n in next_list:
            if item['room'] == get_room_name(n.room) and n.reserved:
                item['next_user'] = n.checkout_email

    # temp = list[11]
    # list[11] = list[10]
    # list[10] = list[9]
    # list[9] = list[8]
    # list[8] = temp

    context_list['list'] = list

    return render_to_response('CollabCheckout/current_usage.html', context_list, context)

def get_room_name(number):
    number = int(number)
    if number == 1:
        roomString = "Collaboration Studio 1"
    elif number ==  2:
        roomString = "Collaboration Studio 2"
    elif number == 3:
        roomString = "Collaboration Studio 3"
    elif number == 4:
        roomString = "Collaboration Studio 4"
    elif number == 5:
        roomString = "Collaboration Studio 5"
    elif number == 6:
        roomString = "Collaboration Studio 6"
    elif number == 7:
        roomString = "Collaboration Studio 7"
    elif number == 8:
        roomString = "Collaboration Studio 8"
    elif number == 9:
        roomString = "Balcony Conference Table"
    elif number == 10:
        roomString = "Duncan Center 4"
    elif number == 11:
        roomString = "Idea Lab"
    return roomString

def get_period_name(number):
        number = int(number)
        if number == 0:
            periodString = "Before school"
        elif number == 1:
            periodString = "Period 1"
        elif number ==  2:
            periodString = "Period 2"
        elif number == 3:
            periodString = "Period 3"
        elif number == 4:
            periodString = "Period 4"
        elif number == 5:
            periodString = "Period 5"
        elif number == 6:
            periodString = "Period 6"
        elif number == 7:
            periodString = "Period 7"
        elif number == 8:
            periodString = "After school: 3:30-4:30"
        elif number == 9:
            periodString = "After school: 4:30-5:30"
        elif number == 10:
            periodString = "First half of lunch"
        elif number == 11:
            periodString = "Second half of lunch"
        elif number == -1:
            periodString = "None"
        return periodString

@login_required
def checkout_many_rooms(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = ManyRoomSlotForm(request.POST)

        if form.is_valid():

            email = request.POST.get('email');
            period =  request.POST.get('period');
            room =  request.POST.get('room');
            room = " " + str(room)
            rooms = RoomSlot.objects.filter(period=period, room=room)
            for r in rooms:
                r.checkout_email = email
                r.reserved = True
                r.save()
            print rooms;
            # Now call the index() view.
            # The user will be shown the homepage.
            extra_message = str(len(rooms)) + " Checkout(s) successful!"
            return render_to_response('CollabCheckout/manycheckout.html', {'form': form, "extra_message": extra_message}, context)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ManyRoomSlotForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('CollabCheckout/manycheckout.html', {'form': form}, context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)


    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        print user
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/collabcheckout/manycheckouts/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('CollabCheckout/login.html', {}, context)


def colab_stats(request):
    context = RequestContext(request)
    context_list = dict()
    return render_to_response('CollabCheckout/collab_stats.html', context_list, context)
