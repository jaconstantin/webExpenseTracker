from etrack.models import User1, User2
from django.utils import timezone

q = User2.objects.get(pk=1)
q.description

timezone.now().date()
timezone.now().time()

##try adding db entry through the API
r = User2(entrydate=timezone.now().date(),entrytime=timezone.now().time(),prcurrency="Php",prvalue=5000,description="heavy lunch")
r.save()