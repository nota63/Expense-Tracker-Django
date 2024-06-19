from django.shortcuts import render

categoryExpense = []
moneyEntry = []
total_money = 0


def home(request):
    return render(request, 'home.html')


def penny(request):
    global total_money, categoryExpense, moneyEntry  # Use global variables

    if 'total_money' not in request.session:
        request.session['total_money'] = 0

    inr = ''
    if request.method == 'POST':
        penny = int(request.POST.get('money', 0))
        category = request.POST.get('category', '')
        categoryExpense.append(category)
        moneyEntry.append(penny)
        inr = f"INR {penny} for {category} Expense Added"
        request.session['total_money'] += penny

    context = {
        'total_money': request.session['total_money'],
        'inr': inr,
        'categoryExpense': categoryExpense,
        'moneyEntry': moneyEntry
    }

    return render(request, 'penny.html', context)
