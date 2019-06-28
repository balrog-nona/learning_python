class StringCalculator:

    def add(self, a):
        if not a:
            return 0
        else:
            if a[0] == "/":
                delimiter = a[2]
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
                        if i > 0:
                            summary += i
                        else:
                            numbers += str(i) + " "
                if numbers:
                    raise Exception("negatives not allowed: {}".format(numbers))
                else:
                    return summary
            else:
                return int(a)
