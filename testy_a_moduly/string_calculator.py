class StringCalculator:

    counting = 0

    def add(self, a):
        self.counting += 1
        if not a:
            return 0
        else:
            if a[0] == "/":
                delimiter_1 = a[3]
                delimiter_2 = a[6]
            else:
                delimiter = ","
            if "\n" in a:
                a = a.replace("\n", delimiter)
            if delimiter in a:
                a = a.split(delimiter)
                summary = 0
                numbers = ""
                for i in a:
                    try:
                        i = int(i)
                    except ValueError:
                        pass
                    if type(i) == int:
                        if i > 0 and i <= 1000:
                            summary += i
                        elif i < 0:
                            numbers += str(i) + " "
                if numbers:
                    raise Exception("negatives not allowed: {}".format(numbers))
                else:
                    return summary
            else:
                return int(a)

    def get_called_count(self):
        return self.counting
