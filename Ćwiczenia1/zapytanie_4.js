printjson(db.people.find({$and:[{"weight":{$gt:68}},{"weight":{$lt:71.5}}]},{"nazwisko":1,"weight":1}).toArray())

