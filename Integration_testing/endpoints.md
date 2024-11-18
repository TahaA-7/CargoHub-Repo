Endpoints for locations:
GET http://localhost:3000/api/v1/locations -> return all locations
GET http://localhost:3000/api/v1/locations/{id} -> return specific location
POST http://localhost:3000/api/v1/locations -> add location
PUT http://localhost:3000/api/v1/locations/{id} -> update existing location
DELETE http://localhost:3000/api/v1/locations/{id} -> remove existing location

Endpoints for items:
GET http://localhost:3000/api/v1/items -> return all items ---Works
GET http://localhost:3000/api/v1/items/{id} -> return specific item ---Works
GET http://localhost:3000/api/v1/items/{id}/inventory -> return specific item inventories of locations ---Does not work?
GET http://localhost:3000/api/v1/items/{id}/inventory/totals -> return total stats of specific item ---Does not work?
POST http://localhost:3000/api/v1/items -> add item ---Does not work
PUT http://localhost:3000/api/v1/items/{id} -> update existing item ---Works
DELETE http://localhost:3000/api/v1/items/{id} -> remove existing item ---Works

Endpoints for orders:
GET http://localhost:3000/api/v1/orders -> return all orders
GET http://localhost:3000/api/v1/orders/{id} -> return specific order
GET http://localhost:3000/api/v1/orders/{id}/items -> return all items of a specific order
POST http://localhost:3000/api/v1/orders -> add order
PUT http://localhost:3000/api/v1/orders/{id} -> update existing order
PUT http://localhost:3000/api/v1/orders/{id}/items -> update items of a specific order
DELETE http://localhost:3000/api/v1/orders/{id} -> remove existing order
