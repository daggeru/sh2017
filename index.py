from wsgiref.simple_server import make_server

import falcon


class GeneratorPiosenki:
    def on_get(self, req, resp):
        tekst = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = tekst


api = falcon.API()
api.add_route('/', GeneratorPiosenki())

if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, api)
    print("Serving on port %s..." % port)
    httpd.serve_forever()