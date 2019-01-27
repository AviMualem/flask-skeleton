import  DataLayer.DocumentDb.ConnectionManager

class AlertsRepository(object):
    def __init__(self, dbSession):
        self.dbSession=1

    def get_all_alerts():
        #session = DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager.StaticSessionProvider.session
        query = {'query': 'SELECT * FROM server s'}
        options = {}
        options['enableCrossPartitionQuery'] = True
        options['maxItemCount'] = 1
        options['continuation'] = True
        #a =session.QueryDocuments("dbs/I0ZgAA==/colls/I0ZgAK08JQA=/", query, options)
        a=  DataLayer.DocumentDb.ConnectionManager.get_session().QueryDocuments("dbs/I0ZgAA==/colls/I0ZgAK08JQA=/", query, options)
        df = list(a.fetch_next_block())
        return df

