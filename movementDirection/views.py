from rest_framework.decorators import detail_route
from rest_framework.response import  Response
from rest_framework.viewsets import ViewSet
from movementDirection.movements import Start, Stop, Forward


#movement/
class MovementDirection(ViewSet):
    @detail_route(methods=['get'])
    def on(self):
        start = Start()
        return Response(start.direction())

    @detail_route(methods=['get'])
    def off(self):
        stop = Stop()
        return Response(stop.direction())

    def forward(self):
        forward = Forward()
        return Response(forward.direction())