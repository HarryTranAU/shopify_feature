# When you import a directory but you havent given a specific file name then it will import __init__.py by default


from controllers.user_controller import user                 # Importing the user blueprint
from controllers.store_controller import store          

registerable_controllers = [
    user,
    store
]
