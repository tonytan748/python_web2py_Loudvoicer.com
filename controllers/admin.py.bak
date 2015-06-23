# -*- coding: utf-8 -*-
from PIL import Image
import os
import StringIO

MENULIST={'网站系统管理':
                          {'管理员管理':'user',
                           '网站信息管理':'webadmin',
                           },
                     '栏目管理':'categories',
                     '颜色管理':'colors',
                     '新闻管理':{
                            '新闻列表':'newslist',
                            '新增新闻':'addnews',
                            },
                     '图片管理':{
                            '图片列表':'piclist',
                            '新增图片':'addpic'},
                     }

PER_PAGE=20

IMG_PATH="https://www.pythonanywhere.com/user/tonytan/files/home/tonytan/web2py/applications/new_loudvoicer/uploads"

#@auth.requires_membership('managers')
def index(): 
    menulist=MENULIST
    whatpage=None
    return locals()

#@auth.requires_membership('managers')
def webadmin():
    menulist=MENULIST
    whatpage="webadmin"
    try:
        record=db.webadmin[1]
        if record:
            form=SQLFORM(db.webadmin,record,deletable=True,submit_button='更新',showid=False)
        else:
            form=SQLFORM(db.webadmin,submit_button='提交')
    except:
         return redirect(URL('admin','index'))
    if form.process(keepvalues=True).accepted:
        response.flash='信息更新完成'
    elif form.errors:
        response.flash='错误，请重试'
    return locals()

def webinfo():
    menulist=MENULIST
    whatpage="webadmin"
    info=db().select(db.webadmin.ALL)
    return locals()

#@auth.requires_membership('managers')
def categories():
    menulist=MENULIST
    whatpage="categories"
    form=SQLFORM(db.categories,formstyle='table2cols').process()
    categories=db(db.categories).select()
    return locals()

#@auth.requires_membership('managers')
def categorie_define():
    menulist=MENULIST
    whatpage="categories"
    record=db.categories(request.args(0,cast=int)) or redirect(URL('colors'))
    form=SQLFORM(db.categories,record,submit_button='更新',formstyle='table2cols',showid=False)
#    form.add_button('返回',URL('categories'))
    if form.process().accepted:
        session.flash="标签修改完成"
        redirect(URL('categories'))
    elif form.errors:
        response.flash="标签修改出现错误，请重试"
    return locals()

#@auth.requires_membership('managers')
def categorie_delete():
    record=db.categories(request.args(0,cast=int)) or redirect(URL('admin','categories'))
    db(db.categories.id==record.id).delete()
    session.flash="删除成功"
    return redirect(URL('admin','categories'))

#@auth.requires_membership('managers')
def colors():
    menulist=MENULIST
    whatpage="colors"
    form=SQLFORM(db.colors).process()
    colors=db(db.colors).select()
    return locals()

#@auth.requires_membership('managers')
def color_define():
    menulist=MENULIST
    whatpage="colors"
    record=db.colors(request.args(0,cast=int)) or redirect(URL('admin','colors'))
    form=SQLFORM(db.colors,record,submit_button='更新')
    if form.process().accepted:
        session.flash="修改完成"
        redirect(URL('colors'))
    elif form.errors:
        response.flash="出现错误，请重试"
    return locals()

def download():
    return response.download(request,db)

#@auth.requires_membership('managers')
def color_delete():
    record=db.colors(request.args(0,cast=int)) or redirect(URL('colors'))
    db(db.colors.id==record.id).delete()
    session.flash="删除成功"
    return redirect(URL('colors'))

#@auth.requires_membership('managers')
def newslist():
    menulist=MENULIST
    whatpage="newslist"
    news=db(db.news).select() or None
    return locals()

#@auth.requires_membership('managers')
def addnews():
    menulist=MENULIST
    whatpage="addnews"
    form=SQLFORM(db.news)
    if form.process().accepted:
        session.flash="新增新闻完成"
        redirect(URL('news'))
    elif form.errors:
        response.flash="新增错误，请重试"
    return locals()

#@auth.requires_membership('managers')
def piclist():
    menulist=MENULIST
    whatpage="piclist"
    imgpath=IMG_PATH
    #os.path.join(request.folder,'uploads')
    page=request.args(0,cast=int,default=0)
    start=page*PER_PAGE
    stop=start+PER_PAGE
    rows=db(db.images).select(orderby=~db.images.created_on,limitby=(start,stop)) or None

    cat=db(db.categories).select()
    catlist={}
    for i in cat:
        catlist[i.id]=i.name
    return locals()

#@auth.requires_membership('managers')
def addpic():
    menulist=MENULIST
    whatpage="addpic"
    form=SQLFORM(db.images,submit_button='增加')
                 #,fields=['categories','title','picattribute','picfrom','picauthor','linkurl','pickeywords','picdescription','piccontent','picurl','camera','checkinfo','hits','zan'])
    #my_extra_element = TR(LABEL('颜色选择',_class='col'))
    #form[0].insert(1,my_extra_element)
    #m=0
    #for color in db(db.colors).select():
#        tr=SELECT(OPTION(color.name,_value=color_name))
        #tr=LABEL(INPUT(_name='color_name',_type='checkbox',_value=color.name),color.name,_bgcolor='color.image',_class='colors')
        #form[0].insert(2,tr)
        #m+=1
    if form.process().accepted:
    #(onvalidation=resize_pic).accepted:
        resize_img(form)
        get_new_size_img(form,500,375,'smallpic')
        get_new_size_img(form,860,683,'mainpic')
        response.flash="新增图片成功"
    elif form.errors:
        response.flash="有错误，请重试"
    return locals()

def pic_define():
    menulist=MENULIST
    whatpage="piclist"
    imgpath=IMG_PATH
    record=db.images(request.args(0,cast=int)) or redirect(URL('piclist'))
    form=SQLFORM(db.images,record,deletable=True,upload=URL('uploads'),showid=False,submit_button='更新')
    if form.process().accepted:
        session.flash="图片修改完成"
        redirect(URL('piclist'))
    elif form.errors:
        response.flash='错误请重试'
    return locals()

def pic_delete():
    record=db.images(request.args(0,cast=int)) or redirect(URL('piclist'))
    name=record.picurl
    filepath=os.path.join(request.folder,'uploads')
    try:
        os.remove(os.path.join(filepath,'resizepic',name))
        os.remove(os.path.join(filepath,'resizepic',name))
    except:
        pass
    db(db.images.id==record.id).delete()
    session.flash="删除成功"
    return redirect(URL('piclist'))

def resize_img(form):
    filepath=os.path.join(request.folder,'uploads')
    origina_img_name=form.vars.picurl
    im=Image.open(os.path.join(filepath,origina_img_name))
    xsize,ysize=im.size
    resolution="{} x {}".format(xsize,ysize)

    stream=open(os.path.join(filepath,origina_img_name),'rb')
    size=str(os.path.getsize(os.path.join(filepath,origina_img_name)))

    x=2048
    y=1536
    if xsize>ysize and xsize>x:
        xs=x
        ys=xsize*y/x
        newsize=im.resize((xs,ys),Image.BILINEAR)
    elif ysize>xsize and ysize>y:
        ys=y
        xs=ysize*x/y
        newsize=im.resize((xs,ys),Image.BILINEAR)
    else:
        newsize=im
    picurl=newsize.save(os.path.join(filepath,origina_img_name))
    picresize=newsize.save(os.path.join(filepath,'resizepic',origina_img_name))

    #save_to_new_file=os.path.join(filepath,'smallpic',origina_img_name)
    #picsmallsize=get_new_size_img(picresize,save_to_new_file)
    db(db.images.title==form.vars.id).update(picresolution=resolution,picsize=size)#,picresize=picresize)

def get_new_size_img(form,width,height,filename):
    h=int(height)
    w=int(width)
    filepath=os.path.join(request.folder,'uploads')
    origina_img_name=form.vars.picurl
    try:
        im=Image.open(os.path.join(filepath,origina_img_name))
        new_x_size,new_y_size=im.size
        if int(new_x_size)*h>int(new_y_size)*w:
            bottom=int(new_y_size)
            ccwidth=(bottom*w/h)/2
            left=int(new_x_size)/2-ccwidth
            top=0
            right=int(new_x_size)/2+ccwidth
        elif int(new_x_size)*h<int(new_y_size)*w:
            right=int(new_x_size)
            left=0
            ccheight=(right*h/w)/2
            bottom=int(new_y_size)/2+ccheight
            top=int(new_y_size)/2-ccheight
        else:
            left=0
            top=0
            right=int(new_x_size)
            bottom=int(new_y_size)

        box = (int(left), int(top),int(right),int(bottom))
        region = im.crop(box)
        region.save(os.path.join(filepath,filename,origina_img_name))
        #db(db.images.title==form.vars.id).update(picsmallsize=region)
    except Exception as e:
        session.flash=str(e)
        return False

    
def img_by_datetime():
    return locals()

def img_by_zan():
    return locals()

def img_by_clicks():
    return locals()
