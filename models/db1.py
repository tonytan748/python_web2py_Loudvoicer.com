# -*- coding: utf-8 -*-
import os
#from plugin_color_widget import color_widget
from plugin_multiselect_widget import hmultiselect_widget

db.define_table('webadmin',
                Field('webname',notnull=True,requires=IS_NOT_EMPTY(),label="网站名称",comment='必填'),    # 网站名称
                Field('weburl',label="网站地址"),    #网站地址
                Field('logo','upload',label="网站LOGO"),    #网站LOGO
                Field('pic','upload',label="网站大图片"),    #网站大图片
                Field('author',label="作者"),    #作者
                Field('seotitle',label="seo标签"),    #seo标签
                Field('keyword',label="关键字"),    #关键字
                Field('description','text',label="描述"),    #描述
                Field('copyright','text',label="版权信息"),    #版权信息
                Field('hotline',label="客服热线"),    #客服热线
                Field('icp',label="icp备案号"),    #icp备案号
                format='%(webname)s')

db.define_table('categories',
                Field('name',unique=True,notnull=True,requires=(IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'categories.name')),label="标签名",comment='必填'),    #标签名
                Field('description','string',label='描述'),    #标签描述
                Field('sort_num','integer',default=1,label='排序'),    #标签排序
                auth.signature,
                format='%(name)s')

db.define_table('news',
                Field('title',unique=True,requires=(IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'news.title')),label='标题',comment='必填'),    #新闻标题
                Field('contents','text',label='新闻内容'),
                Field('views','integer',default=+1,writable=False,readable=False),    #浏览量
                auth.signature,
                format='%(title)s')

db.define_table('colors',
                Field('name',requires=(IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'colors.name')),label='颜色名称',comment='必填'),    #颜色名称
                Field('description','string',label='颜色描述'),    #颜色描述
                Field('engname',requires=(IS_NOT_EMPTY()),label='颜色英文名',comment='必填'),
                #Field('image',widget=color_widget,label='颜色选择'),    #颜色图片
                auth.signature,
                format='%(name)s')
#db.colors.image.widget = color_widget

db.define_table('images',         #图片管理表
                Field('categories','reference categories',requires=(IS_IN_DB(db,'categories.id','%(name)s')),label='栏目',comment='必填'),    #分类
                #Field('colors','list:integer',label='颜色',requires=(IS_NOT_EMPTY(),IS_IN_SET([(color.id,color.name) for color in db(db.colors).select()], multiple=True)),comment='必填'),    #颜色
                Field('colors','reference colors',requires=(IS_NOT_EMPTY(),IS_IN_DB(db,'colors.id','%(name)s')),label='颜色',comment='必填, 单选'),    #颜色
                Field('title','string',requires=(IS_NOT_EMPTY(),IS_NOT_IN_DB(db, 'images.title')),label='标题',comment='必填'),   #标题
                Field('picattribute',label='属性'),       #属性
                Field('picfrom',label='图片来源'),     #图片来源
                Field('picauthor',label='作者'),     #作者
                Field('linkurl',label='跳转链接'),    #跳转链接
                Field('pickeywords',label='关键词'),   #关键词
                Field('picdescription','string',label='摘要',comment='显示在列表左上角'),    #摘要
                Field('piccontent','text',label='详细内容'),    #详细内容
                Field('picurl','upload',uploadseparate=False,autodelete=True,requires=[IS_NOT_EMPTY(),IS_IMAGE()],label='图片',comment='必填'),    #图片
                #Field('picresize','upload',readable=False,writable=False,autodelete=True),    #改变图片体积后保存
                #Field('picsmallsize',readable=False,writable=False,autodelete=True),     #截图用于前台展示
                Field('picresolution',readable=False,writable=False,label='图片大小',comment='图片大小　4896x3264 PX (X-LARGE)'), #图片大小　4896x3264 PX (X-LARGE)
                Field('picsize',readable=False,writable=False,label='图片尺寸',comment='图片尺寸　4 MB'),    #图片尺寸　4 MB
                Field('camera',label='相机型号',comment='相机型号　如：FUJIFILM X-E2'),    #相机型号　FUJIFILM , X-E2
                Field('checkinfo','boolean',default=True,label='审核状态'),    #审核状态
                Field('hits','integer',default=+1),    #点击次数
                Field('zan','integer',default=+1),    #赞
                auth.signature,
                format='%(title)s')

db.images.colors.widget = hmultiselect_widget
