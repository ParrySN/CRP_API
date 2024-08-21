import db

system = db.getCollection('system')

print(system[0]['branches'])
