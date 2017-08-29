import falcon
import json

class ItemsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        items = {
            'title': 'Python+FalconでWebAPI',
            'tags': [
                {
                    'name': 'Python','versions':[]
                },
                {
                    'name': 'Falcon','vresions':[]
                }
            ]
        }

        resp.body = json.dumps(items,ensure_ascii=False)

api = falcon.API()
api.add_route('/items', ItemsResource())
