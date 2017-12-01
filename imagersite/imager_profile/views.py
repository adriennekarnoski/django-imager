from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from imager_profile.models import ImagerProfile
from imager_images.models import Photo



def profile_view(request, username=None):
    if username is None and request.user.is_authenticated:
        request_user = User.objects.filter(username=request.user)
        profile = ImagerProfile.objects.get(user=request_user)
        image_query = Photo.objects.filter(user=profile)
        image_count = image_query.count()
        return render(request, 'imager_profile/profiles.html', context={'profile': profile, 'image_count': image_count})
    else:
        request_user = User.objects.filter(username=username)
        profile = ImagerProfile.objects.get(user=request_user)
        return render(request, 'imager_profile/profiles.html', context={'profile': profile})