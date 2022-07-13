from auth.role_db_mgt import *


def init_role_db():
    db_create_roletable()
    role = db_get_role_by_name("admin")
    if not role:
        db_add_role("admin")
        db_add_role("user")


def create_new_role(name: str) -> bool:
    role = db_get_role_by_name(name)
    if not role:
        db_add_role(name)
        return True
    else:
        return False


def get_role_by_id(id:int):
    role = db_get_role_by_id(id)
    return role


def get_role_by_name(name:str):
    role = db_get_role_by_name(name)
    return role


def get_all_roles():
    all_roles = db_get_all_roles()
    return all_roles


def delete_role(name:str):
    role = get_role_by_name(name)
    if not role:
        return False
    else:
        db_delete_role(name)
        return True

