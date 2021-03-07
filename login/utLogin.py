from .models import Person
def CheckUserExist(**kwargs):
    return Person.exist(**kwargs)
def CheckUserLogin(request):
    user=CheckUserExistReq(request)
    if user:
        if user[0].pk==request.session['has_login']['pkUser']:
            return user[0].userType
        del request.session['has_login']
    return False
def CheckUserExistReq(request):
    if 'has_login' in request.session:
        flag= CheckUserExist(**request.session['has_login'])
        if not flag:
            del request.session['has_login']
        return flag
    return False


