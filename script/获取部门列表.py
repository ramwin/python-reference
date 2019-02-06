#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-12-25 13:29:49


import re


class Dept(models.Model):
    title = models.CharField("部门名称", max_length=10)
    path = models.CharField("部门路径", max_length=100)


class DeptSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Dept
        fields = ["id", "title", "children"]

    def get_children_qs(self, obj):
        qs = Dept.objects.filter(path__startswith=obj.path)
        results = []
        for i in qs:
            if re.match(r'^{}\.\d+$'.format(qs.path), i.path):
                results.append(i)
        return results

    def get_children(self, obj):
        qs = self.get_children_qs(obj)
        return DeptSerializer(qs, many=True).data
