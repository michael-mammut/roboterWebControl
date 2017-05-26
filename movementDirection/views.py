from rest_framework.decorators import detail_route
from rest_framework.response import  Response
from rest_framework.viewsets import ViewSet
from movementDirection.movements.Start import Start
from movementDirection.movements.Stop import Stop
from movementDirection.movements.Forward import Forward


#movement/
class MovementDirection(ViewSet):
    @detail_route(methods=['get'])
    def on(self, request):
        start = Start()
        return Response(start.direction())

    @detail_route(methods=['get'])
    def off(self, request):
        stop = Stop()
        return Response(stop.direction())

    def forward(self, request):
        forward = Forward()
        return Response(forward.direction())