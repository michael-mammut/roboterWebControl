
class DirectionAbstract:
    _engineA = False
    _engineB = False
    _speed = 0

    def drive(self):
        pass

    def direction(self):
        pass

    def getEngineA(self):
        return self._engineA

    def getEngineB(self):
        return self._engineB

    def setEngineA(self, boolean):
        self._engineA = boolean

    def setEngineB(self, boolean):
        self._engineB = boolean

    def getSpeed(self):
        return self._speed

    def setSpeed(self, int):
        self._speed = int

