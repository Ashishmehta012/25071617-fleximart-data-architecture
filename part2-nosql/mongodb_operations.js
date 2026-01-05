// 1. Insert Data
db.products.insertMany([
  { "product_id": "P001", "name": "Laptop", "category": "Electronics", "price": 1200 },
  { "product_id": "P002", "name": "T-Shirt", "category": "Clothing", "price": 25 }
]);

// 2. Query High Value Items
db.products.find({ "price": { $gt: 1000 } });

// 3. Update Review
db.products.updateOne(
  { "product_id": "P001" },
  { $set: { "reviews": [] } }
);