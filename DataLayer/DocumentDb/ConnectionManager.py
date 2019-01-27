import configparser
import pydocumentdb.document_client as document_client
from DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager import documentDbConnectionDetails
import  os

_Session = None
#
# config = configparser.ConfigParser()
# configFile = config.read('Config.ini')
# documentDbConnectionDetails.documentdkey = config['DocumentDbConnectionDetails']['key']
# documentDbConnectionDetails.documentdburi = config['DocumentDbConnectionDetails']['uri']
# documentDbConnectionDetails.collectionname = config['DocumentDbConnectionDetails']['CollectionName']
# documentDbConnectionDetails.dbname = config['DocumentDbConnectionDetails']['DbName']
_Session = document_client.DocumentClient \
        (os.environ['db_uri'], {'masterKey': os.environ['db_key']})


def get_session():
    return _Session
