from movementDirection.movements.Direction import DirectionAbstract
from ..config.GpioConfigHelper import GpioConfiHelper
class Stop(DirectionAbstract):

   def direction(self):
       helper = GpioConfiHelper()
       helper.all_off()
       return "ENGINE STOPED"
