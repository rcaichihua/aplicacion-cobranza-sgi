from datetime import time

class TimeFormat(fields.Raw):
    def format(self, value):
        return time.strftime(value, "%d/%m/%Y, %H:%M:%S")