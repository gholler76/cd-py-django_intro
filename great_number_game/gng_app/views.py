from django.shortcuts import HttpResponse, redirect, render
import random


def index(request):
    new_game = "<WSGIRequest: GET '/'>"
    guess_number = 0
    sub_btn = '<input type="text" name="guess" class="guess-form" placeholder="Enter your guess here"></input><br class="space"><button type="submit" class="btn btn-primary btn-block mt-2"><h3>Submit</h3></button>'
    play_btn = '<div class="btn-box"><a href = "http://localhost:8000/"><h3>Play Again!</h3></a></div>'
    too_high = 'Nope! \n Too high!'
    too_low = 'Nope! \n Too low!'
    good_luck = 'Good luck!'
    correct = "Well done! \n That was the number!"

    if request.method == 'GET':
        rand_number = random.randint(1, 100)
        print('**********RANDOM NUMBER************')
        print(rand_number)
        request.session['random'] = rand_number
        print('**********SESSION NUMBER************')
        print(request.session['random'])

        context = {
            'message': good_luck,
            'color': "color0",
            'submit': sub_btn
        }

        return render(request, "index.html", context)

    else:
        guess_number = int(request.POST['guess'])
        print('**********GUESSED NUMBER************')
        print(guess_number)
        print('**********SESSION NUMBER************')
        print(request.session['random'])

        if guess_number > request.session['random']:
            print("**********too high*******")

            context = {
                'message': too_high,
                'color': "color1",
                'submit': sub_btn
            }
            print("****************too high return********")
            return render(request, "index.html", context)

        elif guess_number < request.session['random']:
            print("**********too low*******")
            context = {
                'message': too_low,
                'color': "color1",
                'submit': sub_btn
            }
            print("****************too high return********")
            return render(request, "index.html", context)

        else:
            guess_number = request.session['random']
            print("**********CORRECT!!!*******")
            context = {
                'message': correct,
                'color': "color2",
                'submit': play_btn
            }
            print("****************CORRECT return********")
            del request.session['random']
            return render(request, "index.html", context)


def reset(request):
    return redirect('reset.html')
