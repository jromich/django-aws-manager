from django.http import HttpResponse

def get_rdp(request, public_dns,username):
    # send a remote desktop file to user
    rdp_content = "auto connect:i:1\nfull address:s:%s\nusername:s:%s" % (public_dns, username)
    response = HttpResponse(rdp_content, mimetype='application/x-rdp')
    response['Content-Disposition'] = 'attachment; filename="ph_server_connect.rdp"'
    return response

