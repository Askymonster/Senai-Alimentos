import sqlite3
import pandas as pd
import streamlit as st

con = sqlite3.connect("Alimentos.db")

con.execute("PRAGMA foreign_keys = ON;")

##############################
#INSERTS
##############################


def insert_user(name,email):
    con.execute(f'''
    INSERT INTO user (name, email)
    VALUES (?,?)
    ''',(name, email))
    con.commit()
    
def insert_task(desc_task,sector_n,priority,cad_data,status):
    con.execute(f'''
    INSERT INTO task (desc_task,sector_n,priority,cad_data,status)
    VALUES (?,?,?,?,?)
    ''',(desc_task,sector_n,priority,cad_data,status))
    con.commit()
    
##############################
#UPDATES
##############################

def update_user(id_user, new_name="", new_email=""):
    if new_name != "" and new_email != "":
        con.execute("UPDATE user SET name = ?, email = ? WHERE id_user = ?",
                    (new_name, new_email, id_user))

    elif new_name != "":
        con.execute("UPDATE user SET name = ? WHERE id_user = ?",
                    (new_name, id_user))

    elif new_email != "":
        con.execute("UPDATE user SET email = ? WHERE id_user = ?",
                    (new_email, id_user))

    con.commit()
    
def update_task(id_task,id_user,new_desc,new_sector_n,new_priority,new_cad_data,new_status):
    con.execute(f'''
    UPDATE user
    SET id_user = ?, desc_task = ?, sector_n = ?, priority = ?, cad_data = ?, status = ?
    WHERE id_task = ?
    ''',(id_task,id_user,new_desc,new_sector_n,new_priority,new_cad_data,new_status))
    con.commit()
    
##########################
#REMOVES
##########################
    
def remove_user(plan,ID):
    con.execute(f'DELETE FROM {plan} WHERE id_user = ?',(ID,))
    con.commit()
    
def remove_task(plan,ID):
    con.execute(f'DELETE FROM {plan} WHERE id_task = ?',(ID,))
    con.commit()

######################
#SEARCHER
#####################


def searcher(plan,column,name):
    resp = f'''
        SELECT * FROM {plan}
        WHERE {column} LIKE ?
        '''
    output = pd.read_sql_query(resp, con, params=(f"%{name}%",))
    return output


def le_plan(Name):
    if Name == 'Users':
        data = pd.read_sql_query('''
        SELECT * FROM user
        ''', con)
    if Name == 'Task':
        data = pd.read_sql_query('''
        SELECT * FROM task
        ''', con)
    return data



##########################
#STREAMLIT CODE
##########################

st.title('Mole Alimentos S/A')
tab1, tab2, tab3 = st.tabs(['Intro','UserTab','Tasks'])


#Initial TAB
with tab1:
    st.title('Welcome to Mole Alimentos S/A')
    st.image('LogoMole.png')
  
    
#USER TAB
with tab2:
    login,add,edit,remov = st.tabs(['Login','New User', 'Edit','Remove'])
    with login:
        st.title('Login')
        email = st.text_input('Email')
        search = st.button('Login')
        if search:
            output = searcher('user','email',email)
            st.write(output)
    with add:
        st.title('New User')
        with st.form('Sign In', clear_on_submit = True):
            name = st.text_input('Name')
            email = st.text_input('E-mail')
            INS = st.form_submit_button('Insert')
            if INS:
                insert_user(name, email)
    with edit:
        st.title('Update user data')
        with st.form('Registration update', clear_on_submit = True):
            User_id = st.number_input('User ID', min_value=0)
            N_Name = st.text_input('Update Name')
            N_Email = st.text_input('Update Email')
            UPT = st.form_submit_button('Update')
            if UPT:
                if N_Name == "" and N_Email == "":
                    st.warning("Fill in at least one field.")
                else:
                    update_user(User_id, N_Name, N_Email)
                    st.success("Updated!")
    with remov:
        st.title('Remove user')
        with st.form('Remove user registration', clear_on_submit = True):
            ID_remove = st.number_input('User id removed', min_value=0)
            REM = st.form_submit_button('Remove')
            if REM:
                remove_user(user,ID_remove)
 
                
# TASKS TAB
with tab3:
    st.title('Task Manager')
    todo, doing, done = st.coluns(3)
    
    

con.commit()
con.close()