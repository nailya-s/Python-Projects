from .models import PrivacyPolicy

def getting_privacy_privacy(request):

    privacy_policy = PrivacyPolicy.objects.filter(is_active=True).last()

    return locals()