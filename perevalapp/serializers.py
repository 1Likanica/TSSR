from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Pereval, Authors, Coords, Images, Level


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['user_email', 'user_phone', 'user_fam', 'user_name', 'user_otc']

    def save(self, **kwargs):
        self.is_valid()
        user = Authors.objects.filter(user_email=self.validated_data.get('user_email'))
        if user.exists():
            return user.first()
        else:
            new_user = Authors.objects.create(
                user_email=self.validated_data.get('user_email'),
                user_phone=self.validated_data.get('user_phone'),
                user_fam=self.validated_data.get('user_fam'),
                user_name=self.validated_data.get('user_name'),
                user_otc=self.validated_data.get('user_otc'),
            )
        return new_user


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height', ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['data', 'title']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class PerevalSerializer(WritableNestedModelSerializer):
    user_id = AuthorsSerializer()
    coord_id = CoordSerializer()
    level_id = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user_id
            data_user = data.get('user_id')
            user_fields_for_validation = [
                instance_user.user_email != data_user['user_email'],
                instance_user.user_phone != data_user['user_phone'],
                instance_user.user_fam != data_user['user_fam'],
                instance_user.user_name != data_user['user_name'],
                instance_user.user_otc != data_user['user_otc'],
            ]
            if data_user is not None and any(user_fields_for_validation):
                raise serializers.ValidationError(
                    {
                        'Ошибка': 'Данные пользователя заменить нельзя',
                    }
                )
        return data

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'level_id', 'user_id', 'coord_id', 'images', 'status']
