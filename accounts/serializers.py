from django.contrib.auth import User,get_user_model
from rest_framework.serializers import Serializer


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		modal = get_user_model()

		fields = ('id','username')
