from .models import Person
def CheckUserExist(**kwargs):
    return Person.exist(**kwargs)
def CheckUserLogin(request):
    if 'has_login' in request.session:
        user=CheckUserLogin(request.session['has_login'])
        if user:
            if user[0].pk==request.session['has_login']['pkUser']:
                return True 
        del request.session['has_login']
    return False


