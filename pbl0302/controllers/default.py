def index():
    keyword = request.vars.keyword or ''
    if keyword:
        query = (db.tbcars.carname.contains(keyword)) | \
                (db.tbcars.carbrand.contains(keyword)) | \
                (db.tbcars.carmodel.contains(keyword)) | \
                (db.tbcars.carprice.contains(keyword))
        cars = db(query).select()
    else:
        cars = db(db.tbcars).select()
    return dict(cars=cars, keyword=keyword)

def create():
    form = SQLFORM(db.tbcars)
    if form.process().accepted:
        session.flash = 'Data mobil berhasil ditambahkan!'
        redirect(URL('index'))
    return dict(form=form)

def update():
    car_id = request.args(0, cast=int)
    record = db.tbcars(car_id) or redirect(URL('index'))
    form = SQLFORM(db.tbcars, record)
    if form.process().accepted:
        session.flash = 'Data mobil berhasil diperbarui!'
        redirect(URL('index'))
    return dict(form=form)

def delete():
    car_id = request.args(0, cast=int)
    db(db.tbcars.id == car_id).delete()
    session.flash = 'Data mobil berhasil dihapus!'
    redirect(URL('index'))