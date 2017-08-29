import falcon
import json
class Index:
  def on_get(self, req, resp):
    default = {
      'title': 'こんにちは',
      'numbers': [3, 1, 2]
      }
    resp.body = json.dumps(default, ensure_ascii=False)
api = falcon.API()
api.add_route('/', Index())
