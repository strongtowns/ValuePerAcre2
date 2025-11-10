class QueryConstructor:
    def __init__(self):
        self.url = ''

    def construct_query(self):
        self.url += "query"

    def return_constructed_query(self):
        return self.url