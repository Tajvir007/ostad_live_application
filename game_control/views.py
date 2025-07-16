from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Game, GameCategory, GameQuestion, QuestionAnswer,Tournament
# Create your views here.
def bet_control(request):
    if request.user.is_superuser:
        context = {
            'game_category' : GameCategory.objects.all(),
            'tournament' : Tournament.objects.all(),
            'games' : Game.objects.filter(status = 'Active', game_status = 'Live')
        }
        return render(request, 'superadmin/game_control/bet-control.html',context = context)
    else:
        return redirect('/account/login/') 

def game_category(request):
    return render(request, 'superadmin/game_control/game_category.html')

def tournament(request):
    return render(request, 'superadmin/game_control/tournament.html')








def add_game(request):
    if request.method=='POST':
        if request.user.is_superuser:
            fields = ['game_category','tournament','name','team1','team2','start']
            data = request.POST
            for i in fields:
                if data[i] == "" or data[i] == None:
                    messages.error(request,f"Please Enter {i}")
                    return redirect('/game-control/bet-control/')
                
            game = Game.objects.create(tournament = data['tournament'],
                                       game_category = data['game_category'],
                                       name = data['name'],
                                       team1 = data['team1'],
                                       team2 = data['team2'],
                                       start = data['start']
                                       )
            if not data['game_status'] == "" or data['game_status']== None:
                game.game_status = data['game_status']
            if not data['status'] == "" or data['status'] == None:
                game.status = data['status']
            game.save()
            return redirect('/game-control/bet-control/')
        else:
            return redirect('/account/login/')
    else:
        return redirect('/game-control/bet-control/')
    


def add_question(request,pk):
    if request.method=='POST':
        if request.user.is_superuser:
            data = request.POST
            fields = ['question','end']
            for i in fields:
                if i not in data:
                    return redirect('/game-control/bet-control/')
            try:
                game = Game.objects.get(id=pk)
            except:
                return redirect('/game-control/bet-control/')
            question = GameQuestion.objects.create(game = game, question = data['question'], end = data['end'])
            return redirect('/game-control/bet-control/')
        else:
            return redirect('/')
        
    else:
        return redirect('/game-control/bet-control/')
    
        


def add_answer(request, pk):
    if request.method == 'POST':
        if request.user.is_superuser:
            data = request.POST
            fields = ['answer','rate','possible_return','bets','multi']
            for i in fields:
                if i not in data:
                    return redirect('/game-control/bet-control/')
            try:
                question = GameQuestion.objects.get(id=pk)
            except:
                return redirect('/game-control/bet-control/')
            answer = QuestionAnswer.objects.create(question = question, answer = data['answer'])

            if not data['rate'] == "" or data['rate'] == None:
                answer.rate = data['rate']
            if not data['bets'] == "" or data['bets'] == None:
                answer.bets = data['bets']
            if not data['multi'] == "" or data['multi'] == None:
                answer.multi = data['multi']
            if not data['possible_return'] == "" or data['possible_return'] == None:
                answer.possible_return = data['possible_return']
            answer.save()
            return redirect('/game-control/bet-control/')
        else:
            return redirect('/')
    else:
        return redirect('/game-control/bet-control/')
            

