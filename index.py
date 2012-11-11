#encoding=utf-8

import web
#import sae
from web.template import render

#urls
urls=(
		'/','index',
		'/categories','catego',
		'/admin','admin'
)


#templates
render = web.template.render('index/')
admin_render=web.template.render('admin/')

#静态页返回
class index:
    def GET(self):
        return render.index()

class catego:
	def GET(self):
		return render.categories()

class admin:
	def GET(self):
		return admin_render.admin()

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
