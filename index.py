#encoding=utf-8
import web

#urls
from web.template import render

urls=(
		'/','index'
)

#application
#app = web.application(urls, globals())

#templates
index = web.template.frender('index/index.html')
#admin = web.template.frender('admin/admin.html')
name="hello"

class index:
    def GET(self):
        return render.index(None)


if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
