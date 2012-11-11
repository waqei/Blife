#encoding=utf-8

import web
import sae
from web.template import render

#urls
urls=(
		'/','index'
		'categories','catego'
)


#templates
render = web.template.render('index/')
#admin = web.template.frender('admin/admin.html')

class index:
    def GET(self):
        return render.index()
class catego:
	def GET(self):
		return render.categories()

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
