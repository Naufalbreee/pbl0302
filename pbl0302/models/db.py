import os

db = DAL('sqlite://carsweb.db', folder=os.path.join(request.folder, 'databases'), migrate=False)

db.define_table('tbcars',
    Field('carname', 'string'),
    Field('carbrand', 'string'),
    Field('carmodel', 'string'),
    Field('carprice', 'string'),
    migrate=False
)