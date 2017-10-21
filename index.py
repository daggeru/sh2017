from wsgiref.simple_server import make_server

import falcon


class Index:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:
            resp.body = f.read()


class GeneratorPiosenki:
    def on_get(self, req, resp):
        tekst = {
            'zwrotki': [
                ['pierwsza linijka1', 'druga linijka1', 'trzecia linijka1', 'czwarta linijka1'],
                ['pierwsza linijka2', 'druga linijka2', 'trzecia linijka2', 'czwarta linijka2'],
                ['pierwsza linijka3', 'druga linijka3', 'trzecia linijka3', 'czwarta linijka3'],
            ],
            'refren': [
                ['pierwsza linijka refrenu', 'druga linijka refrenu', 'trzecia linijka refrenu', 'czwarta linijka refrenu'],
            ]
        }

        resp.media = tekst


api = falcon.API()
api.add_route('/', Index())
api.add_route('/generuj', GeneratorPiosenki())

if __name__ == '__main__':
    port = 8000
    httpd = make_server('', port, api)
    print("Serving on port %s..." % port)
    httpd.serve_forever()
