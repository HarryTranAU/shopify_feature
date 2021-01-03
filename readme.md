# Shopify - Advance Abandoned Cart Feature

##### Harry Tran (T3A3)

## Scope

#### **What is Shopify?**

Shopify is a commerce platform that allows anyone to set up an online store and sell their products. Merchants can also sell their products in person with Shopify POS(Point of Sale).

#### **What is an Abandoned Cart?**

Abandonment is an ecommerce term used to describe a visitor on a web page who leaves that page before completing the desired action. Examples of abandonment include shopping cart abandonment, referring to visitors who add items to their online shopping cart, but exit without completing the purchase.

#### **Structure**

Note: This is my personal interpretation of the structure using personal experience and public information, this is by no means a representation of Shopify's actually data structure.

- The Merchant/Seller would create a `user`
- A `user` can create one `store` (one-to-one)
- A `store` can have many `products`, `customers`, and `orders` (one-to-many)
- An `order` can have many `products` and `products` can belong to many `orders` (many-to-many)
- `orders` and `products` are associated through a join table `orders_products`

#### **Abandoned Cart Implementation**

The Abandoned Cart will be implemented through an additional property to the order table called `order_placed`. Using database joins, the abandoned cart customers can be targeted through joining customer details with orders that have not been placed(`order_placed`set to `False`).

#### **ERD**

[External DBDigram.io Link](https://dbdiagram.io/d/5feec11d80d742080a34b954)

![Entity Relationship Diagram](docs/shopify_feature_erd.png)

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
# OpenAPI

Endpoints documented using OpenAPI 3.0.3.

[Interactive UI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/HarryTranAU/shopify_feature/master/docs/endpoints.yml)

