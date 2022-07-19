from logging import PlaceHolder
import streamlit as st
import auth.user as us
import auth.role as ro

def get_all_role_list():
    all_roles = ro.get_all_roles()
    all_roles_list=[]
    for i in range(len(all_roles)):
        all_roles_list.append(all_roles[i][1])
    return all_roles_list


def display_user_admin_page():

    with st.expander("Create new user"):
        name =st.text_input("","",placeholder="Nom",key = "create_name")
        password =st.text_input("","",placeholder="Mot de passe")
        all_roles_list=get_all_role_list()
        role =st.selectbox("role",all_roles_list,key='select1')
        role = ro.get_role_by_name(role)
        id_role = role[0]
        save = st.button("Enregistrer",on_click=us.create_new_user, args=(name,password,id_role),key='save')
        if save:
            st.success("success")
  

    with st.expander("display all users"):
        all_users = us.view_all_users()
        for i in range(len(all_users)):
            st.write("user n°",i+1)
            st.write("-> name: ", all_users[i][1])
            st.write("-> password: ", all_users[i][2])
            role = ro.get_role_by_id(all_users[i][3])
            st.write("-> role: ", role[1])
          

    with st.expander("update a user"):
        old_username = st.text_input("","",placeholder="Name du user à modifier",key ="old_username")
        new_username = st.text_input("","",placeholder="nouveau nom",key ="new_username")
        new_password = st.text_input("","",placeholder="nouveau mdp",key ="new_password")
        all_roles_list=get_all_role_list()
        new_role_name =st.selectbox("role",all_roles_list,key='select2')
        new_role = ro.get_role_by_name(new_role_name)
        new_id_role = new_role[0]
        submit = st.button("Enregistrer",on_click=us.update_old_user, args=(new_username,new_password,new_id_role,old_username),key='update')
        if submit:
            us.view_all_users()
            st.success("user modifié")

    with st.expander("delete a user"):
        username = st.text_input("","",placeholder="Name du user à supprimer",key ="username_todelete")
        password = st.text_input("","",placeholder="password du user à supprimer",key ="password_todelete")
        if username and password:
            user = us.db_get_user(username,password)
            if user:
                delete = st.button("supprimer",on_click=us.delete_user, args=(username,password), key='delete')
                if delete:
                    us.view_all_users()
                    st.success("user supprimé")
            else:
                st.error("ce user n'existe pas")


def display_role_admin_page():

    with st.expander("Create new role"):
        name =st.text_input("","",placeholder="Nom")
        save = st.button("Enregistrer",on_click=ro.create_new_role, args=(name,),key='save')
        if save:
            st.success("success")
  

    with st.expander("display all roles"):
        all_roles = ro.get_all_roles()
        for i in range(len(all_roles)):
            st.write("-> id: ",all_roles[i][0]) 
            st.write("-> name: ", all_roles[i][1])
          

    with st.expander("delete a role"):
        roleName = st.text_input("","",placeholder="Name du role à supprimer",key ="roleName_todelete")
        if roleName:
            role = ro.get_role_by_name(roleName)
            if role:
                delete = st.button("supprimer",on_click=ro.delete_role, args=(roleName,), key='delete')
                if delete:
                    ro.get_all_roles()
                    st.success("role supprimé")
            else:
                st.error("ce role n'existe pas")