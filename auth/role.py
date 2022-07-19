from auth.role_db_mgt import *


def init_role_db():
    """
    It creates a role table if it doesn't exist, then it checks if the admin role exists, and if it
    doesn't, it creates it
    """
    db_create_roletable()
    role = db_get_role_by_name("admin")
    if not role:
        db_add_role("admin")
        db_add_role("user")


def create_new_role(name: str) -> bool:
    """
    > This function creates a new role if it doesn't already exist
    
    :param name: str - The name of the role to create
    :type name: str
    :return: A boolean value.
    """
    role = db_get_role_by_name(name)
    if not role:
        db_add_role(name)
        return True
    else:
        return False


def get_role_by_id(id:int):
    """
    This function gets a role by id
    
    :param id: The id of the role you want to get
    :type id: int
    :return: A role object
    """
    role = db_get_role_by_id(id)
    return role


def get_role_by_name(name:str):
    """
    This function gets a role by name
    
    :param name: The name of the role you want to get
    :type name: str
    :return: A role object
    """
    role = db_get_role_by_name(name)
    return role


def get_all_roles():
    """
    This function gets all the roles from the database and returns them
    :return: A list of dictionaries.
    """
    all_roles = db_get_all_roles()
    return all_roles



def delete_role(name:str):
    """
    "If the role exists, delete it and return True, otherwise return False."
    :param name: The name of the role to delete
    :type name: str
    :return: The return value is a boolean value.
    """
    role = get_role_by_name(name)
    if not role:
        return False
    else:
        db_delete_role(name)
        return True

