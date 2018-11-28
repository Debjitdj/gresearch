import webhandler

operator = ["+", "-", "*", "/"]
brackets = ["(", ")"]

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
        
        check = (e in operator) and a.isdigit() and b.isdigit()
        return check

    def eval_expression3(self, query):
        arr = query.split(" ")
        a = int(arr[0])
        if arr[2] == "(":
        b = " ".join(arr[3:]) if arr[2] == "(" else int(arr[2])
        e = arr[1]
        res = 0
        if e == "+":
            res = b + a
        if e == "-":
            res = a - b
        if e == "*":
            res = a * b
        if e == "/":
            res = b // a
        return res 

    def check2_expression(self, query):
        arr = query.split(" ")
        q = []
        for e in arr:
            q.append(e)
        a = q[0]
        b = q[2]
        c = q[4]
        e1 = q[1]
        e2 = q[3]

        operator = ["+", "-", "*", "/"]
        check = (e1 in operator) and (e1 in operator) and a.isdigit() and b.isigit() and c.isdigit()
        return check

    def eval2_expression(self, query):
        arr = query.split(" ")
        first = arr[0] + arr[1] + arr[2]
        if self.check_expression(first):
            firstEval = self.eval_expression(first)
        second = str(firstEval + arr[3] + arr[4])
        if self.check_expression(second):
            return self.eval_expression(second)

    def is_expression(self, query):
        arr = query.split(" ")
        return [e for e in arr if not (e.isdigit() or e in brackets or e in operator)] is False

    def eval_expression(self, query):
        

    def answer_query(self, query):
        if "in" in query:
            return self.unit_conversion(query)
        if self.check_expression(query):
            return self.eval_expression(query)
        if self.check2_expression(query):
            return self.eval2_expression(query)
        return 85
