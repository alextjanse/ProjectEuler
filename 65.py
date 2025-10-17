from lib.rationals import Rational

class InfiniteContinuedFraction:
    def __init__(self, head: int, tail: list[int]) -> None:
        self.head = head
        self.tail = tail
    
    def value(self, n):
        value = self.head
        yield value

        tail = Rational
        for a in self.tail:


