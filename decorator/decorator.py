from django.shortcuts import redirect,render

def auto_session(func):
    def check_session(request,*args,**kwargs):
        flag = request.session.get("loginflag")
        if not flag:
            return render(request, "index.html")

        request.session. set_expiry(30)
        request.session.clear_expired()
        return func(request,*args,**kwargs)

    return check_session