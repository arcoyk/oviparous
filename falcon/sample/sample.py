import falcon
import json
class Index:
  def on_get(self, req, resp):
    x = read_req(req)
    default = {
      'title': 'helloこんにちは hello',
      'result': f(x)
      }
    resp.body = json.dumps(default, ensure_ascii=False)
    resp.status = falcon.HTTP_200

class Article(object):
  def on_get(self, req, resp, text):
    article = {
      'title': 'hello',
      'result': f(text)
    }
    resp.body = json.dumps(article, ensure_ascii=False)
    resp.status = falcon.HTTP_200

def f(x):
  x = int(x)
  return x * 5

def read_req(req, default=0):
  rst = req.stream.read()
  if rst != b'':
    return rst
  else:
    return default

api = falcon.API()
api.add_route('/', Index())
api.add_route('/article/{text}', Article())
