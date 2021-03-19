from django.shortcuts import HttpResponse, redirect, render
import random
import re
from time import gmtime, strftime


def index(request):
    print('***********GET***********')
    # on first page load (GET) 'activity' and 'gold' session keys are created
    request.session['activity'] = []
    request.session['gold'] = 0
    request.session['log'] = []
    print('********NEW SESSION**********')
    print(request.session)
    return render(request, 'index.html')


def process(request):
    print('*******POST DATA ADDED********')
    print('v v v v v v v v v v v v v v v v')
    # adds activity value to the session
    request.session['activity'].append(request.POST['activity'])

    # creates string of 'activity' value
    activity = str(request.POST['activity'])
    print(activity)
    # sets current activity gold to 0
    activity_gold = 0

    #  if statement to assign gold to previous activity
    if activity == 'farm':
        activity_gold = random.randint(10, 20)
    elif activity == 'cave':
        activity_gold = random.randint(5, 10)
    elif activity == 'house':
        activity_gold = random.randint(2, 5)
    elif activity == 'casino':
        activity_gold = random.randint(-50, 50)
    print(activity_gold)

    # adds gold to session 'gold" total
    request.session['gold'] += activity_gold
    print(request.session['gold'])

    # set values for log string going back to activity log
    result = ''
    ending = '!'
    date = strftime("%Y-%m-%d %H:%M %p", gmtime())
    color = "color-pos"
    # bad_chars = ['[', ' ,', ']', '']

    # sets 'lost" or 'earned' flag depending on value of coin for the current activity
    if activity_gold >= 0:
        result = 'earned'
    else:
        activity_gold < 0
        result = 'gambled away'
        ending = "... Ouch."
        color = "color-neg"

    # creates string for activity log and appends to session key 'log' with a line break
    str_log = f'<h4 class="{color}">You visited the {activity} and {result} {activity_gold} gold{ending} ~~~ ({date})</h4><br >'
    print('********************session log template*******************')
    print(str_log)
    session_log = request.session['log']
    session_log.insert(0, str_log)
    request.session['log'] = session_log
    print(request.session['log'])

    # context dict for data passing into HTML
    context = {
        "activity_gold": activity_gold,
        "total_gold": request.session['gold'],
        "log": request.session['log']
    }

    return render(request, 'index.html', context)
