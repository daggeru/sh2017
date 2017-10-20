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
            'zwrotki''tekst_disco.txt': [
                'pierwsza linijka#1\ndruga linijka#1\ntrzecia linijka#1\nczwarta linijka#1',
                'pierwsza linijka#2\ndruga linijka#2\ntrzecia linijka#2\nczwarta linijka#2',
                'pierwsza linijka#3\ndruga linijka#3\ntrzecia linijka#3\nczwarta linijka#3'
            ],
            'refreny': [
                'pierwsza linijkaREF#1\ndruga linijkaREF#1\ntrzecia linijkaREF#1\nczwarta linijkaREF#1',
                'pierwsza linijkaREF#2\ndruga linijkaREF#2\ntrzecia linijkaREF#2\nczwarta linijkaREF#2'
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
