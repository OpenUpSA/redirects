from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404
import newrelic.agent


class RedirectsMiddleware(object):
    redirects = {
        # domain (without www.) -> full new URL

        # TO: livingwage.code4sa.org
        'living-wage.code4sa.org': 'http://livingwage.code4sa.org/',
        'livingwagestory.code4sa.org': 'http://livingwage.code4sa.org/',
        'maps.code4sa.org': 'http://mapit.code4sa.org/',
    }

    def process_request(self, request):
        host = request.get_host()
        if host.startswith("www."):
            host = host[4:]

        if host in self.redirects:
            return HttpResponsePermanentRedirect(self.redirects[host])

        if request.path == '/ping':
            newrelic.agent.ignore_transaction()
            return HttpResponse('pong')

        raise Http404()
