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
                for i in a:
                    try:
                        if int(i) >= 0:
                            summary += int(i)
                        else:
                            raise Exception("negatives not allowed: {}".format(int(i)))
                    except ValueError:
                        pass
                return summary
            else:
                return int(a)


