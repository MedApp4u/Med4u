# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=100)
	password = serializers.CharField()