import sqlite3
from langchain.tools import Tool

# create db connection
conn = sqlite3.connect("db.sqlite")

def list_tables():
    c = conn.cursor()
    c.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
            )
    rows = c.fetchall() # fetches all the results
    return "\n".join([row[0] for row in rows if row is not None]) 

def run_query(query):
    '''runs the passed query
    and returns the result.'''

    # create a connection cursor
    try:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()
    except Exception as e:
        return f"The following error occured: {str(err)}"
        

# create run_query_tool
# this is our first tool that we'll be using 
# later with the "agents"
run_query_tool = Tool.from_function(
        name="run-sqlite-query",
        description="run a SQL query",
        func = run_query
        )


# if __name__ == '__main__':
#     print(list_tables())




