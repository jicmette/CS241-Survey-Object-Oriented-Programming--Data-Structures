class Time: 
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
        self._hours_simple = 0
        self.period1 = ""
        self.secondsSinceMidnight = 0

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def hours_simple(self):
        return self._hours_simple

    def period(self):
        return self._period1

    def set_hours(self, hours):
        if hours > 23:
            hours = 23
        elif hours < 0:
            hours = 0

        self._hours = hours

    def set_minutes(self, minutes):
        if minutes > 59:
            minutes = 59
        elif minutes < 0:
            minutes = 0

        self._minutes = minutes
    
    def set_seconds(self, seconds):
        if seconds > 59:
            seconds = 59
        elif seconds < 0:
            seconds = 0

        self._seconds = seconds
    
    def set_hours_simple(self, hours_simple):
        self._hours_simple = hours_simple

    def set_period(self, period1):
        self.period1 = period1
    
    hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)
    simple = property(hours_simple, period)

    @property
    def hours_simple(self):
        return self.hours_simple()

    @hours_simple.setter
    def hours_simple(self, hours_simple):
        return self.set_hours_simple(hours_simple)

    @property
    def period(self):
        return self.period()
    
    @period.setter
    def period(self, period1):
        return self.set_period(period1)

    @property
    def seconds_since_midnight(self):
        return self.secondsSinceMidnight

    @seconds_since_midnight.setter
    def seconds_since_midnight(self, secondsSinceMidnight):
        self.secondsSinceMidnight = secondsSinceMidnight

def main():

    time = Time()
    #hours = int(input("Enter an hour: "))
    #minutes = int(input("Enter minutes: "))
    #seconds = int(input("Enter the seconds: "))

    #time.hours = hours
    #time.minutes = minutes
    #time.seconds = seconds

    #print("The time is:")
    #print("Hours: {}".format(time.hours))
    #print("Minutes: {}".format(time.minutes))
    #print("Seconds: {}".format(time.seconds))

    sem = int(input("Enter seconds since midnight: "))
    time.secondsSinceMidnight = sem

    hours = int(sem % 60)
    minutes = int(hours % 60)
    seconds = int(minutes % 60)

    print("{}:{}:{}".format(hours, minutes, seconds))

if __name__ == "__main__":
    main()





