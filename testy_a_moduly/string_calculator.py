class StringCalculator:
    """
    The class is created according to the test exercise here:
    https://static1.squarespace.com/static/5c741968bfba3e13975e33a6/t/5ca6614d971a1877cadc4f8a/1554407757512/String+
    Calculator+Kata+v1.pdf
    """

    counting_add = 0

    def add(self, a):
        self.counting_add += 1
        if not a:
            return 0
        else:
            if a[0] == '/':
                delimiter = a[3]
            else:
                delimiter = ","
            if "\n" in a:
                a = a.replace("\n", delimiter)
            if delimiter in a:
                a = a.split(delimiter)
                sum = 0
                numbers = ""
                for i in a:
                    try:
                        i = int(i)
                    except ValueError:
                        pass
                    if type(i) == int:
                        if i >= 0 and i <= 1000:
                            sum += i
                        elif i < 0:
                            numbers += str(i) + ", "
                if numbers:
                    raise Exception("negatives not allowed: {}".format(numbers))
                else:
                    return sum
            else:
                return int(a)


    def get_called_count(self):
        return self.counting_add

