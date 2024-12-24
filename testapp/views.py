from django.shortcuts import render
import random
from faker import Faker
fake=Faker()
def pwd():
    ra=fake.random_int(min=8,max=15)
    return ra
# Create your views here.
def pwd_view(request ):
    a='ABCDEFGIJKLMNOPQRSTUVWXYZ'
    b='abcdefgihjklmnopqrstuvwxyz'
    c='0123456789'
    d='!@#$%^&*_+">~'
    length=pwd()
    all=a+b+c+d
    password=(''.join(random.sample(all,length)))
    my_dict={'password':password}
    return render (request,'testapp/pwd.html',my_dict)