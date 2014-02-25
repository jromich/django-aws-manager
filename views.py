from django.http import HttpResponse
from django.contrib import messages
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.views import generic
from models import AWSServer
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def get_rdp(request, public_dns,username):
    # send a remote desktop file to user    
    rdp_content = "auto connect:i:1\nfull address:s:%s\nusername:s:%s" % (public_dns, username)
    response = HttpResponse(rdp_content, mimetype='application/x-rdp')
    response['Content-Disposition'] = 'attachment; filename="ph_server_connect.rdp"'
    return response

# def start(request, pk):
#     # start an ec2 server
#     #server = .get_object(self, pk)
#     #server.start()

# def stop(request, pk):
#     # start an ec2 server
#     server = self.get_object(self, pk)
#     server.stop()



# class ControlServerView(LoginRequiredMixin, StaffuserRequiredMixin, generic.UpdateView):
#     print "hi2"    
#     model = AWSServer
#     #opts = model._meta
# #    form_class = ProcessTransactionForm
#     success_url = '../'

#     def get(self, request, *args, **kwargs):
#         #self.object = self.get_object(queryset=Transaction.objects.all())
#         super(ControlServerView, self).get(request, *args, **kwargs)
#         print "testing"
#         server = self.get_object()
#         #return redirect("/")#
#         return HttpResponseRedirect(self.object.get_absolute_url())
