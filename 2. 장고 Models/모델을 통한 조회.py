#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'askcompany.settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()


# In[2]:


from instagram.models import Post


# In[6]:


qs = Post.objects.all()
print(type(qs))
print(qs.query)
qs


# In[8]:


qs = Post.objects.all().order_by('-id')
print(qs.query)
qs


# In[10]:


qs = Post.objects.all().order_by('-id')[:1]
print(qs.query)
qs


# In[11]:


qs = Post.objects.all().order_by('-id')
print(qs.query)
qs


# In[13]:


for post in qs : 
    print(post.id, post.message, post.created_at)


# In[14]:


for post in qs : 
    print("{id}, {message}, {created_at}".format(**post.__dict__))


# In[23]:


query = '메세지' #검색어
qs = Post.objects.all().filter(message__icontains=query).order_by('-id')
print(qs.query)
qs


# In[28]:


print(qs[2])
print(qs[3])


# In[31]:


qs = Post.objects.all()
qs.get(id=1)


# In[32]:


qs.get()


# In[36]:


qs.get(id__lte=1) #less than equal 작거나 같음


# In[37]:


qs.first()


# In[38]:


qs.last()


# In[40]:


print(qs.first())
print(qs.last())
print(qs.none().first())


# In[ ]:





# In[41]:


from django.db.models import Q


# In[47]:


qs = Post.objects.all()
qs = qs.filter(id__gte = 2, message__icontains=query)
print(qs.query)
qs


# In[50]:


from django.db.models import Q
qs = Post.objects.all()
qs = qs.filter(Q(id__gte = 2) | Q(message__icontains=query))
print(qs.query)
qs


# In[ ]:




