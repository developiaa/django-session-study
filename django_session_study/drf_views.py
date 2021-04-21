from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DjangoRestView(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]

	# permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		content = {
			'user': str(request.user),  # `django.contrib.auth.User` instance.
			'auth': str(request.auth),  # None
		}
		request.session.set_expiry(60 * 5)
		request.session['user'] = request.user.username
		return Response(content)


class SessionCheckView(APIView):
	def get(self, request):
		content = {
			'user': str(request.session.session_key)
		}
		return Response(content)
