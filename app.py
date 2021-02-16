import dbcreds
import mariadb
import sys

def connect():
    return mariadb.connect(
        user = dbcreds.user,
        password = dbcreds.password,
        host = dbcreds.host,
        port = dbcreds.port,
        database = dbcreds.database    
)
def view_blogs():
    try:
        conn = connect()                                   
        cursor = conn.cursor()                            
        cursor.execute("SELECT * FROM blog_post")      
        result = cursor.fetchall()   
        row_count = cursor.rowcount
                           
        print("Returned " + str(row_count) + " results")
      
        for row in result:
            print(row)

    except:
        print("DB Error")
        sys.exit    
    finally:
        if (cursor != None):
            cursor.close()
        if (conn != None):
            conn.rollback()
            
# view_blogs()

def add_blog():
    username = input("blogger name: ")
    content = input("blog: ")
    

    conn = connect()                       
    cursor = conn.cursor()                 
    cursor.execute(                         
        "INSERT INTO blog_post (username, content) VALUES (?, ?)",
        [username, content]        
    ) 
    conn.commit()  
    if (cursor.rowcount == 1):
      
        print("New blog added successfully!!!")
    else:
       
        print("There was an error")

    cursor.close()                       
    conn.close()  
# add_blog()    


conn = None
cursor = None       

while True:
  
    print("1. Add new blog")
    print("2. View all blogs")
    print("3. Exit")
 
    choice = int(input("Choice: "))
    if choice == 1:
        add_blog()
    elif choice == 2:
        view_blogs()
    elif choice == 3:
     
        print("Goodbye!")
        break



