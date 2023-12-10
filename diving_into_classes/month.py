from dataclasses import dataclass
import datetime
import calendar

@dataclass
class Month:
    
    year: int
    month: int

    def __str__(self):
        return f"{self.year}-{self.month:02d}"

    def __lt__(self, other):
        if not isinstance(other, Month):
            return NotImplemented
        return (self.year, self.month) < (other.year, other.month)

    def __le__(self, other):
        if not isinstance(other, Month):
            return NotImplemented
        return (self.year, self.month) <= (other.year, other.month)
    
    @property
    def first_day(self):
        return datetime.date(self.year, self.month, 1)

    @property
    def last_day(self):
        number_of_month_days = calendar.monthrange(self.year, self.month)[1]
        return datetime.date(self.year, self.month, number_of_month_days)    

    @classmethod
    def from_date(cls, date):
        if not isinstance(date, datetime.date):
            return NotImplemented
        return cls(date.year, date.month)

    def strftime(self, format):
        return datetime.date(self.year, self.month, 1).strftime(format)

dec99 = Month(1999, 12)
print(dec99)
print(dec99.first_day)
print(dec99.last_day)

nye2000 = datetime.date(2000, 12, 31)
dec2000 = Month.from_date(nye2000)
print(dec2000)
print(dec2000.strftime('%b %Y'))
