class Time:
    # constructor
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour  # attribute: hour
        self._minute = minute  # attribute: minute
        self._second = second  # attribute: second

    @property  # read
    def hour(self):
        return self._hour

    @hour.setter  # write
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f"Hour ({hour}) must be between 0-23")
        self._hour = hour

    @property  # read
    def minute(self):
        return self._minute

    @minute.setter  # write
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f"Minute ({minute}) must be between 0-59")
        self._minute = minute

    @property  # read-only property
    def second(self):
        return self._second

    def __str__(self):
        return f'{self._hour}h:{self._minute}m:{self._second}s'