from django.utils.http import urlquote
from django.http import HttpResponsePermanentRedirect, Http404


class RedirectsMiddleware(object):
    redirects = {
        # domain (without www.) -> full new URL
        'living-wage.co.za': 'http://living-wage.news24.com/wageCalc.html',
    }

    def process_request(self, request):
        host = request.get_host()
        if host.startswith("www."):
            host = host[4:]

        if host in self.redirects:
            return HttpResponsePermanentRedirect(self.redirects[host])

        raise Http404()
