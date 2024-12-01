Endpoints for locations:
GET http://localhost:8000/api/v1/locations -> return all locations ---Works
GET http://localhost:8000/api/v1/locations/{id} -> return specific location ---Works
POST http://localhost:8000/api/v1/locations -> add location ---Works
PUT http://localhost:8000/api/v1/locations/{id} -> update existing location ---Works
DELETE http://localhost:8000/api/v1/locations/{id} -> remove existing location ---Works


###
Endpoints for items:
GET http://localhost:8000/api/v1/items -> return all items ---Works
GET http://localhost:8000/api/v1/items/{id} -> return specific item ---Works
GET http://localhost:8000/api/v1/items/{id}/inventory -> return specific item inventories of locations ---Does not work?
GET http://localhost:8000/api/v1/items/{id}/inventory/totals -> return total stats of specific item ---Does not work?
POST http://localhost:8000/api/v1/items -> add item ---Does not work ---tries to add an integer to a string because the current data has a string as an uid, only works if case is empty
PUT http://localhost:8000/api/v1/items/{id} -> update existing item ---Works
DELETE http://localhost:8000/api/v1/items/{id} -> remove existing item ---Works
###

Endpoints for orders:
GET http://localhost:8000/api/v1/orders -> return all orders ---Works
GET http://localhost:8000/api/v1/orders/{id} -> return specific order ---Works
GET http://localhost:8000/api/v1/orders/{id}/items -> return all items of a specific order ---Works
POST http://localhost:8000/api/v1/orders -> add order ---Works
PUT http://localhost:8000/api/v1/orders/{id} -> update existing order ---Works
PUT http://localhost:8000/api/v1/orders/{id}/items -> update items of a specific order ---Does not work
DELETE http://localhost:8000/api/v1/orders/{id} -> remove existing order ---Works
