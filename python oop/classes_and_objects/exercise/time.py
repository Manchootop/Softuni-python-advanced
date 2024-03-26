class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        super().__init__(hours, minutes, seconds)

    def get_time(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


    def next_second(self):
        self.seconds += 1
        # seconds reach 60
        if self.seconds > self.max_seconds:
            self.minutes += 1
            self.seconds = 0

            # minutes reach 60
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours = 0

                # hours reach 24
                if self.hours > self.max_hours:
                    self.hours = 0

        return self.get_time()




time1 = Time(9, 30, 59)
print(time1.next_second())
time2 = Time(10, 59, 59)
print(time2.next_second())
time3 = Time(23, 59, 59)
print(time3.next_second())

