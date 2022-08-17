from os import environ 

class Config(object):
   API_ID = int(environ['API_ID'])
   API_HASH = environ['API_HASH'])
   OWNER_ID = int(environ['OWNER_ID']))
   BOT_TOKEN = environ.get('BOT_TOKEN', None)
   SESSION_STRING = environ.get('SESSION_STRING', None)
   FILTERS = environ.get('FILTERS', None) #None for forward all type messages
