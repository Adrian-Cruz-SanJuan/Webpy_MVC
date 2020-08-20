import web

urls = (
    '/', 'application.controllers.alumnos.index.Index',
    '/insert', 'application.controllers.alumnos.insert.Insert',
    '/delete', 'application.controllers.alumnos.delete.Delete',
    '/update', 'application.controllers.alumnos.update.Update',
    '/view', 'application.controllers.alumnos.view.View',
     '/list', 'application.controllers.alumnos.list.List',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()