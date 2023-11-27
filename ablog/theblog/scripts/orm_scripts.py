from django.db.models import Q

from ablog.theblog.models import Post

quereset = Post.objects.filter(Q(category__startswith='c') & Q(title_tag__startswith='P'))
print(quereset)