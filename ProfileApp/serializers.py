# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'dob', 'address', 'mobile')
