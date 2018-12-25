#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-12-25 13:29:49


class Dept(models.Model):
    title = models.CharField("部门名称", max_length=10)
    path = models.CharField("部门路径", max_length=100)


class DeptSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        fields = ["id", "title", "children"]

    def get_children(self, obj):
        qs = Dept.objects.filter(path__endswith = ".{}".format(obj.id)).exclude(id=obj.id)
        return DeptSerializer(qs, many=True).data
