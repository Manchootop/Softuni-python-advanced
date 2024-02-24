from exam.profiles.models import Profile

def has_profile_nav(request):
    profile = Profile.objects.first()
    return {'has_profile_nav': profile is None}