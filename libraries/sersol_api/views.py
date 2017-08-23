from django.http import JsonResponse
import requests
import xmltodict


# proxy for the Serials Solutions XML API
# used by the library catalog to show KB holdings alongside print
def sersol(request):
    # we require an ISSN in the query string
    issn = request.GET.get('issn', None)

    if issn is None:
        return JsonResponse({'error': 'No ISSN parameter provided'})
    else:
        # grab XML data from Sersol
        response = requests.get('http://ey7mr5fu9x.openurl.xml.serialssolutions.com/openurlxml?version=1.0&url_ver=Z39.88-2004&issn=%s' % issn)
        namespaces = { 'http://xml.serialssolutions.com/ns/openurl/v1.0': None }
        # convert XML to python dict which will be in turn converted to JSON
        data = xmltodict.parse(
            response.text,
            process_namespaces=True,
            namespaces=namespaces,
        )['openURLResponse']
        return JsonResponse(data)
