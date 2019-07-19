import pytest

class String_calculator:

    def add(self, a):
        if not a:
            return 0
        else:
            if ',' in a:
                a = a.split(',')
            sum = 0
            for i in a:
                sum += int(i)
            return sum



