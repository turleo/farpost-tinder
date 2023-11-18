from rest_framework import serializers

from profiles.models import UserProfile, Interests


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interests
        fields = ['id', 'name']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    interests = serializers.StringRelatedField(many=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'profile_picture',
                'first_name', 'last_name',
                'bio', 'interests']
