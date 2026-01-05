# Database Schema Documentation

## Entity-Relationship Description
* **ENTITY: customers**
  - **Purpose:** Stores customer identity and contact details.
  - **Attributes:** `customer_id` (PK), `first_name`, `last_name`, `email` (Unique).
  - **Relationships:** One customer can have MANY orders.

* **ENTITY: products**
  - **Purpose:** Stores product inventory data.
  - **Attributes:** `product_id` (PK), `product_name`, `category`, `price`, `stock`.

## Normalization (3NF)
This design is in Third Normal Form (3NF) because:
1. All columns contain atomic values (1NF).
2. All non-key attributes depend on the full primary key (2NF).
3. No transitive dependencies exist (e.g., Customer City depends on Customer, not Order) (3NF).