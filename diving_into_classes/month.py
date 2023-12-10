from dataclasses import dataclass

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

dec99 = Month(1999, 12)
print(dec99)
