from controllers.user_controller import user
from controllers.store_controller import store
from controllers.product_controller import product
from controllers.customer_controller import customer
from controllers.order_controller import order
from controllers.admin_controller import admin

registerable_controllers = [
    user,
    store,
    product,
    customer,
    order,
    admin
]
