

from django.shortcuts import render
import random

def main_menu(request):
    return render(request, 'menu.html')

# 1. لعبة حجر ورقة مقص
def rps_game(request):
    user_choice = request.GET.get('choice')
    comp_choice = None
    result = None

    if user_choice:
        choices = ['Rock', 'Paper', 'Scissors']
        comp_choice = random.choice(choices)

        if user_choice == comp_choice:
            result = "It's a Tie! (تعادل)"
        elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
             (user_choice == 'Paper' and comp_choice == 'Rock') or \
             (user_choice == 'Scissors' and comp_choice == 'Paper'):
            result = "You Win! (أنت كسبت 🎉)"
        else:
            result = "You Lose! (الكمبيوتر كسب 🤖)"

    context = {
        'user': user_choice,
        'comp': comp_choice,
        'result': result
    }
    return render(request, 'pages/rps.html', context)

# 2. لعبة تخمين الرقم
def guess_game(request):
    if 'secret_number' not in request.session:
        request.session['secret_number'] = random.randint(1, 10)

    secret = request.session['secret_number']
    user_guess = request.GET.get('guess')
    message = "Take a guess from 1 to 10!"

    if user_guess:
        guess = int(user_guess)
        if guess == secret:
            message = "Correct! You guessed it 🎉"
            del request.session['secret_number']
        elif guess < secret:
            message = "Too Low! Try a higher number ⬆️"
        else:
            message = "Too High! Try a lower number ⬇️"

    return render(request, 'pages/guess.html', {'message': message})

# 3. لعبة حظك اليوم
def lucky_game(request):
    fortunes = [
        "Today is your lucky day! You will write bug-free code 🖥️",
        "A major breakthrough in your project is coming soon 🚀",
        "Take a break, coffee is calling your name ☕",
        "You will find the missing semicolon in less than 5 minutes 🎯",
        "Do not push to production on Friday! 🛑"
    ]
    
    current_fortune = None
    if request.GET.get('get_fortune'):
        current_fortune = random.choice(fortunes)

    return render(request, 'pages/lucky.html', {'fortune': current_fortune})

