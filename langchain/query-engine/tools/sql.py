import sqlite3
from typing import List
from langchain.tools import Tool
from pydantic.v1 import BaseModel
from langchain.agents import tool

# create db connection
conn = sqlite3.connect("db.sqlite")

class RunQueryArgsSchema(BaseModel):
    query: str

class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]

def list_tables():
    c = conn.cursor()
    c.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
            )
    rows = c.fetchall() # fetches all the results
    return "\n".join([row[0] for row in rows if row is not None]) 

@tool
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

def describe_tables(table_names):
    c = conn.cursor()
    tables = ', '.join("'" + table + "'" for table in table_nams)
    rows = c.execute(
            f"SELECT sql FROM sqlite_master WHERE type='table' AND name in {table_names};"
            )
    return '\n'.join(row[0] for row in rows if row[0] is not None)
        

# create run_query_tool
# this is our first tool that we'll be using 
# later with the "agents"
run_query_tool = Tool.from_function(
        name="run-sqlite-query",
        description="run a SQL query",
        func = run_query,
        args_schema = RunQueryArgsSchema
        )

describe_tables_tool = Tool.from_function(
        name = "describe_tables",
        description = "Give a list of table names, returns the schema of those tables",
        func = describe_tables,
        args_schema = DescribeTablesArgsSchema
        )


# if __name__ == '__main__':
#     print(list_tables())




