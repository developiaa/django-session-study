from django.shortcuts import render
from django.contrib.auth import logout as auth_logout


def index(request):
	print(request.session.session_key)
	# 세션 만료 시간
	# ex) 60 * 5 = 300일 경우 5분
	# 현재 30초
	request.session.set_expiry(60 * 5)
	request.session['test'] = "session test value"
	return render(request, './index.html')


def result(request):
	session_id = request.session.session_key
	test = request.session['test']

	contents = {
		'session_id': session_id,
		'test': test
	}
	return render(request, './result.html', contents)


def delete_session(request):
	print(request.session.session_key)
	auth_logout(request)
	return render(request, './result2.html')
