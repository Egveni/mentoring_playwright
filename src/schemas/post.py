POST_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname": {type: 'string'},
        "lastname": {type: 'string'},
        "totalprice": {type: 'integer'},
        "depositpaid": {type: 'boolean'},
        "bookingdates": {
            "type": 'object',
            "properties": {
                "checkin": {type: 'string', format: 'date'},
                "checkout": {type: 'string', format: 'date'},
        "additionalneeds": {type: 'string'}
        },
        }
    }
}



#{'bookingid': 998}
#{'firstname': 'Josh', 'lastname': 'Allen', 'totalprice': 111, 
#'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 
#'checkout': '2019-01-01'}, 'additionalneeds': 'super bowls'}