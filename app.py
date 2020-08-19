import web

urls = (
    '/', 'application.controllers.index.Index',
    '/insert', 'application.controllers.insert.Insert',
    '/delete', 'application.controllers.delete.Delete',
    '/update', 'application.controllers.update.Update',
    '/view', 'application.controllers.view.View',
     '/list', 'application.controllers.list.List',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()