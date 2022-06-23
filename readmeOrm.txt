>>> from ormcalls.models import Blog
>>> b = Blog(name='Best NEtflix Movies', tagline='This is th eblog related to netflix', totalviewers=2000)  
>>> b.save()
>>> Blog.objects.all()
<QuerySet [<Blog: Best Food HAbbits>, <Blog: Best time to excercise>, <Blog: Best Games to play>, <Blog: Best NEtflix Movies>]>
>>> Blog.objects.filter(name='Best time to excercise')
<QuerySet [<Blog: Best time to excercise>]>
>>> Blog.objects.filter(tagline__startswith ='This')  
<QuerySet [<Blog: Best time to excercise>, <Blog: Best Games to play>, <Blog: Best NEtflix Movies>]>
>>> Blog.objects.filter(tagline__endswith ='netflix') 
<QuerySet [<Blog: Best NEtflix Movies>]>
>>>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> Blog.objects.filter(tagline__iexact ='This is a blog related to games') 
<QuerySet [<Blog: Best Games to play>]>
>>> Blog.objects.filter(tagline__iexact ='This is a blog related to GAMES') 
<QuerySet [<Blog: Best Games to play>]>
>>> Blog.objects.filter(tagline__contains ='blog')                            
<QuerySet [<Blog: Best Food HAbbits>, <Blog: Best time to excercise>, <Blog: Best Games to play>, <Blog: Best NEtflix Movies>]>
