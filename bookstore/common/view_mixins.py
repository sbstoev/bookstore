from django.shortcuts import redirect


# This redirects you to the dashboard if some is logged in, else it will send you to home page
class RedirectToDashboard:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)