from django.shortcuts import render


def index(request):
	print(request.session.session_key)
	request.session['test'] = "hahaha"
	return render(request, './index.html')


def result(request):
	session_id = request.session.session_key
	test = request.session['test']

	contents = {
		'session_id': session_id,
		'test': test
	}
	return render(request, './result.html', contents)
