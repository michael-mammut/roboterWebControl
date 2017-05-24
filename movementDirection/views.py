from rest_framework.decorators import detail_route
from rest_framework.response import  Response
from rest_framework.viewsets import ViewSet


#movement/
class MovementDirection(ViewSet):
    @detail_route(methods=['get'])
    def on(self, request):
        print("ON XXX")
        return Response("ON XXX")

    @detail_route(methods=['get'])
    def off(self, request):
        print("OFF XXX")
        return Response("OFF XXX")
