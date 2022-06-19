printjson(db.people.insert([{
    "sex" : "Male",
    "first_name" : "Bartlomiej",
    "last_name" : "Lasocha",
    "job" : "IT Analyst",
    "email" : "testowymailbartka@test.pl",
    "location" : {
        "city" : "Warszawa",
        "address" : {
            "streetname" : "Woronicza",
            "streetnumber" : "17"
        }
    },
    "description" : "tutaj jest opis Bartka",
    "height" : "186",
    "weight" : "100",
    "birth_date" : "1997-09-22T15:21:28Z",
    "nationality" : "Poland",
    "credit" : [
        {
            "type" : "instapayment",
            "number" : "2482609562781172",
            "currency" : "PLN",
            "balance" : "98645.20"
        },
        {
            "type" : "mastercard-electron",
            "number" : "5649756312348409",
            "currency" : "PLN",
            "balance" : "8888.88"
        },
        {
            "type" : "bank account",
            "number" : "3539512340312345",
            "currency" : "GBR",
            "balance" : "22401.33"
        }
        
    ]
}]))