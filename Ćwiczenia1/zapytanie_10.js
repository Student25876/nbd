printjson(db.people.update({"job":"Editor"},{$unset: {"email":true}}, {multi:true}))
