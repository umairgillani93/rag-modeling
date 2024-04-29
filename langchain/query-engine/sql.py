import sqlite3
from langchain.tools import Tool

# create db connection
conn = sqlite3.connect("db.sqlite")

def run_query(query):
    '''runs the passed query
    and returns the result.'''

    # create a connection cursor
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

# create run_query_tool
# this is our first tool that we'll be using 
# later with the "agents"
run_query_tool = Tool.from_function(
        name="run-sqlite-query",
        description="run a SQL query",
        func = run_query
        )





