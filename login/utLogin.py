from .models import Person
def CheckUserExist(**kwargs):
    return Person.exist(**kwargs)
def CheckUserLogin(request):
    if 'has_login' in request.session:
        user=CheckUserExist(**request.session['has_login'])
        if user:
            if user[0].pk==request.session['has_login']['pkUser']:
                return user[0].userType
        del request.session['has_login']
    return False


