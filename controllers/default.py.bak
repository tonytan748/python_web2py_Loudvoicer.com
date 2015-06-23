# -*- coding: utf-8 -*-
import os

IMG_PATH="https://www.pythonanywhere.com/user/tonytan/files/home/tonytan/web2py/applications/new_loudvoicer/uploads"

PER_PAGE=9
def index():
    imgpath=IMG_PATH
    newpiclis=db(db.images).select(orderby=~db.images.created_on)
    page=request.args(0,cast=int,default=0)
    start=page*PER_PAGE
    stop=start+PER_PAGE
    rows=db(db.images).select(orderby=~db.images.created_on,limitby=(start,stop)) or None
    listcount=db(db.images).count()
    return locals()

def categorie():
    imgpath=IMG_PATH
    catid=request.args(0,cast=int,default=0)
    catname=db(db.categories.id==catid).select().first()

    page=request.args(1,cast=int,default=1)
    start=(page-1)*PER_PAGE
    stop=start+PER_PAGE
    listcount=db(db.images.categories==catname.id).count()
    rows=db(db.images.categories==catname.id).select(orderby=~db.images.created_on,limitby=(start,stop)) or None
    return locals()

def color():
    imgpath=IMG_PATH
    colid=request.args(0,cast=int,default=0)
    colname=db(db.colors.id==colid).select().first()

    page=request.args(1,cast=int,default=1)
    start=(page-1)*PER_PAGE
    stop=start+PER_PAGE
    listcount=db(db.images.colors==catname.id).count()
    rows=db(db.images.colors==colname.id).select(orderby=~db.images.created_on,limitby=(start,stop)) or None
    return locals()

def show():
    picid=request.args(0,cast=int,default=0)
    pic=db.images[picid]
    imgpath=IMG_PATH
    imgs=db(db.images.categories==pic.categories).select(orderby=~db.images.created_on)[:3]
    return locals()

def g4():
    return dict(name=T("mobile"))


def getzanqty():
    item = db.images[request.vars.zanid]
    new_votes = int(item.zan) + 1
    item.update_record(zan=new_votes)
    response.falsh=str(new_votes)
    return str(new_votes)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
