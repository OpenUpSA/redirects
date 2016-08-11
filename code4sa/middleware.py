from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404
import newrelic.agent


class RedirectsMiddleware(object):
    redirects = {
        # domain (without www.) -> full new URL

        'living-wage.code4sa.org': 'http://livingwage.code4sa.org/',
        'livingwagestory.code4sa.org': 'http://livingwage.code4sa.org/',
        'maps.code4sa.org': 'http://mapit.code4sa.org/',

        'compliancetracker.org.za': 'http://muni.compliancetracker.org.za/',

        'wazimap.org': 'http://wazimap.co.za',
        'wazimap.com': 'http://wazimap.co.za',
        'wazimap.info': 'http://wazimap.co.za',

        'info.speakupmzansi.org.za': 'http://speakupmzansi.org.za',
        'speakupmzansi.co.za': 'http://speakupmzansi.org.za',
        'speakupmzansi.org': 'http://speakupmzansi.org.za',
        'speakup.org.za': 'http://speakupmzansi.org.za',

        'hackforwater.org.za': 'http://www.hack4water.org.za',

        # this redirects www -> non-www
        'vote4thebudget.org': 'http://vote4thebudget.org',
        'municipalmoney.gov.za': 'https://municipalmoney.gov.za',
        'municipaldata.treasury.gov.za': 'https://municipaldata.treasury.gov.za',
        'youthexplorer.org.za': 'http://youthexplorer.org.za',

        # this redirects non-www -> www
        'hack4water.org.za': 'http://www.hack4water.org.za',
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
