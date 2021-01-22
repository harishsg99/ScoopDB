import os
import time
import json
import hashlib

print("Hello", os.environ["TYPE"],os.getpid())

# *** Master Server ***

if os.environ['TYPE'] == "master":
    import plyvel
    db = plyvel.DB(os.environ['DB'], create_if_missing=True)

def master(env , start_response):
    key = env['REQUEST_URI'].encode('utf-8')
    metakey = db.get(key)

    if metakey is None:
        if env['REQUEST_METHOD'] in ['PUT']:
            # TODO : handle putting key
            pass

        start_response('404 not found', [('content-type','text/plain')])
        return [b'key not found']

    meta = json.loads(metakey)

    headers = [('location', 'http://%s%s' % (meta['volume'],key)) ,('expires','0')]
    start_response('302 Found' , headers)
    return [b""]

Class FileCache(object):
    def __init__(self,basedir):
        os.makedirs(basedir)
        self.basedir = basedir

    def keytopath(kself.key , mkdir_ok = False):
        path = basedir + "/" + key[0:1] +"/" +key[1:2] + "/" +key[2:]
        if not in os.path.isdir(path)
            os.makedirs(path)
        return os.path.join(path , key[2:]) 

    def exists(self , key):
        return os.path.isfile(self.keytopath(key))

    def delete(self , key):
        return os.path.unlink(self.keytopath(key))

    def get(self , key):
        return open(self.keytopath(key) , "rb").read()

    def put(self , key):
        with open(self.keytopath(key) ,"wb") as f:
            f.write(value)

        pass
    

if os.environ["TYPE"] == "volume":
    host = socket.gethostname()

    master = os.environ['MASTER']

    fc = FileCache(os.environ['VOLUME'])

def volume(env , start_response):
    key = env['REQUEST_URI'].encode('utf-8')
    hashedkey = hashlib.md5(key).hexdigest()

    if env['REQUEST_METHOD'] in ['GET']:
        if not fc.exists(key):
            start_response('404 not found', [('content-type','text/plain')])
            return [b'key not found']
        return[fc.get(key)]
    if env['REQUEST_METHOD'] in ['PUT']:  
        fc.put(key, env['wsgi.input'].read(env['CONTENT_LENGTH'])
              
