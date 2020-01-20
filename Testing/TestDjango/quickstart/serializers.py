from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Serialization - convert the state of an object into a form that can be persisted or transported.
# Basically, we're saving the state as some format, e.g. JSON, XML, that we can then throw around.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
