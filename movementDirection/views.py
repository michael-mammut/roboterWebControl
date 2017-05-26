from rest_framework.decorators import detail_route
from rest_framework.response import  Response
from rest_framework.viewsets import ViewSet
from movementDirection.movements.Start import Start
from movementDirection.movements.Stop import Stop
from movementDirection.movements.Forward import Forward
from movementDirection.movements.Backwards import Backwards
from movementDirection.movements.Left import Left
from movementDirection.movements.Right import Right



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

    @detail_route(methods=['get'])
    def forward(self, request):
        forward = Forward()
        return Response(forward.direction())

    @detail_route(methods=['get'])
    def backwards(self, request):
        backwards = Backwards()
        return Response(backwards.direction())

    @detail_route(methods=['get'])
    def left (self, request):
        left = Left()
        return Response(left.direction())

    @detail_route(methods=['get'])
    def right(self, request):
        right = Right()
        return Response(right.direction())