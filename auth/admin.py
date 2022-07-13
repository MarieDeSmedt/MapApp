from logging import PlaceHolder
import streamlit as st
import auth.user as us

def display_admin_page():
    with st.expander("Create new user"):
        name =st.text_input("","",placeholder="Nom")
        password =st.text_input("","",placeholder="Mot de passe")
        role =st.selectbox("role",("admin","user"))
        save = st.button("Enregistrer",on_click=us.create_new_user, args=(name,password,role),key='save')
        if save:
            st.success("success")
  

    with st.expander("display all users"):
        all_users = us.view_all_users()
        for i in range(len(all_users)):
            st.write("user n°",i)
            st.write("-> name: ", all_users[i][0])
            st.write("-> password: ", all_users[i][1])
            st.write("-> role: ", all_users[i][2])
          


    with st.expander("update a user"):
        old_userName = st.text_input("","",placeholder="Name du user à modifier",key ="old_userName")
        new_userName = st.text_input("","",placeholder="nouveau nom",key ="new_userName")
        new_password = st.text_input("","",placeholder="nouveau mdp",key ="new_password")
        new_role =st.selectbox("role",("admin","user"),key='new_role')
        submit = st.button("Enregistrer",on_click=us.update_old_user, args=(new_userName,new_password,new_role,old_userName),key='update')
        if submit:
            us.view_all_users()
            st.success("user modifié")

    with st.expander("delete a user"):
        userName = st.text_input("","",placeholder="Name du user à supprimer",key ="userName_todelete")
        password = st.text_input("","",placeholder="password du user à supprimer",key ="password_todelete")
        if userName and password:
            user = us.db_get_user(userName,password)
            if user:
                delete = st.button("supprimer",on_click=us.delete_user, args=(userName,password), key='delete')
                if delete:
                    us.view_all_users()
                    st.success("user supprimé")
            else:
                st.error("ce user n'existe pas")