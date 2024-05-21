from django.shortcuts import render

from pascal.backend.service.pascal_service import PascalService
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.http import HttpResponse
import json


class PascalViewSet(ViewSet):
    pascal_service = PascalService()

    @action(detail=True, url_path='matrix/<int:size>')
    def get_matrix(self, request, size: int):
        result = self.pascal_service.get_matrix(size)
        beauty_result = []
        for i in result:
            beauty_result.append([])
            for j in i:
                beauty_result[-1].append(str(j))
        response = {
            'data': beauty_result
        }
        return HttpResponse(json.dumps(response), content_type='application/json')

    @action(detail=False, url_path='line/<int:number>')
    def get_line(self, request, number: int):
        result = self.pascal_service.get_line(number)
        beauty_result = []
        for i in result:
                beauty_result.append(str(i))
        response = {
            'data': beauty_result
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
