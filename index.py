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
            'zwr1': {
                '1': 'pierwsza linijka',
                '2': 'druga linijka',
                '3': 'trzecia linijka',
                '4': 'czwarta linijka'
            },
            'ref': {
                '1': 'pierwsza linijka refrenu',
                '2': 'druga linijka refrenu',
                '3': 'trzecia linijka refrenu',
                '4': 'czwarta linijka refrenu'
            },
            'zwr2': {
                '1': 'pierwsza linijka 2 zwrotki',
                '2': 'druga linijka 2 zwrotki',
                '3': 'trzecia linijka 2 zwrotki',
                '4': 'czwarta linijka 2 zwrotki'
            },
            'prz': {
                '1': 'pierwsza linijka przejscia',
                '2': 'druga linijka przejscia',
            }
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
