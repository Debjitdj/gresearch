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

    def answer_query(self, query):
        if "in" in query:
            return self.unit_conversion(query)
        return 85
