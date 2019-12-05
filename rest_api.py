import json


class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        data = json.loads(payload) if payload else None
        if url == '/users':
            if payload is None:
                result = self.database
            else:
                result = { 'users' :
                    [self._select_username(data['users'])] }
        return json.dumps(result)

    def post(self, url, payload=None):
        data = json.loads(payload)
        result = {}

        if url == '/add':
            result = {
                'name': data['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0}
            self.database[data['user']] = result
        elif url == '/iou':
            result = self.lend(data['borrower'], data['lender'], data['amount'])

        return json.dumps(result)


    def lend(selfself, amount, borrower, lender):
        pass