# Shopify - Advance Abandoned Cart Feature

##### Harry Tran (T3A3)

## Scope

---

#### **What is Shopify?**

Shopify is a commerce platform that allows anyone to set up an online store and sell their products. Merchants can also sell their products in person with Shopify POS(Point of Sale).

---

#### **What is an Abandoned Cart?**

Abandonment is an ecommerce term used to describe a visitor on a web page who leaves that page before completing the desired action. Examples of abandonment include shopping cart abandonment, referring to visitors who add items to their online shopping cart, but exit without completing the purchase.

---

#### **Structure**

Note: This is my personal interpretation of the structure using personal experience and public information, this is by no means a representation of Shopify's actually data structure.

- The Merchant/Seller would create a `user`
- A `user` can create one `store` (one-to-one)
- A `store` can have many `products`, `customers`, and `orders` (one-to-many)
- An `order` can have many `products` and `products` can belong to many `orders` (many-to-many)
- `orders` and `products` are associated through a join table `orders_products`

---

#### **Abandoned Cart Implementation**

The Abandoned Cart will be implemented through an additional property to the order table called `order_placed`. Using database joins, the abandoned cart customers can be targeted through joining customer details with orders that have not been placed(`order_placed`set to `False`).

---

#### **ERD**

[External DBDigram.io Link](https://dbdiagram.io/d/5feec11d80d742080a34b954)

![Entity Relationship Diagram](docs/shopify_feature_erd.png)

---

## Requirement R2

**Discuss how the application will handle the privacy of user data within the system, and how security features of the frameworks you are utilising will assist to mitigate security concerns.**

**Bcrypt**

In this application, Bcrypt will be used to hash the passwords registered to the database. In the event, the database is breached the password are still unusable without the original hashing password.

Hashing is preferred over encryption because encryption is a two-way function, where the encrypted password can be decrypted. Whereas, hashing is a one-way function. With a properly designed algorithm, there is no way to reverse the hashing process.

**JWT**

JWT is used for authorization and authentication purposes in this application. The use of JWT can allow a user to create, read, update, and delete resource from their own stores, but not other user's stores.

**Marshmallow**

Marshmallow is used for object serialization and deserialization in this application. When configured properly, marshmallow is able to validate data as it is being received. Example: data type validators such as Integers and Strings provide marshmallow with information about what type of data is being expected.

**SQLAlchemy**

SQLAlchemy is a object-relational mapper (ORM) that bridges database relations into objects. This allows the application to communicate with the database without using raw SQL queries, preventing possible avenues for SQL injections. A specific example has been found that using the filter method is susceptible to SQL injections. However, in combination with input validation this SQL injection line of attack can be prevented.

**AWS (specifically Private Subnets)**

Hosting the database on a private subnet on AWS is another way to secure the data of the application. The structure of this application will require the database to be hosted on a private subnet that isn't associated with a route table that directs traffic to an internet gateway. We will be accessing the the private subnet by using a bastion host on a public subnet. EC2 instances hosted on the same VPC are able to communicate with one another. Allowing the bastion host to communicate with the database on the private subnet.

---

## Installation (Linux)

Install Python and git

```
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3
```

Git clone and Open Folder

```
git clone https://github.com/HarryTranAU/shopify_feature.git
cd shopify_feature
```

Optional: Virtual Environment (Recommended)

```
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```

Install Pip/requirements

```
sudo apt-get install python3-pip
pip install -r requirements.txt
```

Program Start

```
export FLASK_APP=src/main.py
export FLASK_ENV=development
flask run
```

---

## OpenAPI

Endpoints documented using OpenAPI 3.0.3.

[Interactive UI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/HarryTranAU/shopify_feature/master/docs/endpoints.yml)

---