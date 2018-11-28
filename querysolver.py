import webhandler

class QuerySolver(object):
    def __init__(self):
        pass

    def unit_conversion(self, query):
        factor = {"days": 86400, "hours": 3600, "minutes": 60, "seconds": 1, "feet": 0.3048, "metres": 1, "yards": 0.9144, "inches": 0.0254, "miles": 1609.34, "years": 31536000}
        arr = query.split(" ")
        num = float(arr[0])
        if arr[1] in factor:
            num *= factor[arr[1]]
        if arr[3] in factor:
            num /= factor[arr[3]]
        return str(num) + " " + arr[3]

    def check_expression(self, query):
        arr = query.split(" ")
        a = arr[0]
        b = arr[2]
        e = arr[1]
        operator = ["+", "-", "*", "/"]
        check = (e in operator) and a.isdigit() and b.isdigit()
        return check

    def eval_expression(self, query):
        arr = query.split(" ")
        a = int(arr[0])
        b = int(arr[2])
        e = arr[1]
        res = 0
        if e == "+":
            res = b + a
        if e == "-":
            res = a - b
        if e == "*":
            res = a * b
        if e == "/":
            res = a // b
        return res

    def answer_query(self, query):
        if "in" in query:
            return self.unit_conversion(query)
        if self.check_expression(query):
            return self.eval_expression(query)
        return 85
