# -*- coding: utf-8 -*-

from model import User, Blog, Comment
import orm 


def test():
    yield from orm.create_pool( user='root', password='123456', database='awesome')
    
    u = User(id='testid', name='Test', email='test@example.com', passwd='12345678', image='about:blank')
    
    yield from u.save()
    
for x in test():
    pass    
    