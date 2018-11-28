import webhandler

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""
        arr = rpn.split(" ")
        q = []
        operator = ["+", "-", "*", "/"]
        for e in arr:
            if e not in operator:
                q.append(e)
            else:
                a = int(q.pop())
                b = int(q.pop())
                res = 0
                if e == "+":
                    res = b + a
                if e == "-":
                    res = b - a
                if e == "*":
                    res = b * a
                if e == "/":
                    res = b // a
                q.append(res)
        return q.pop()
