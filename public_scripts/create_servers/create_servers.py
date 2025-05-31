from typing import Any
from mcp.server.fastmcp import FastMCP
import os
import subprocess

mcp = FastMCP("create_servers")

# Add your @mcp.tool async functions here 

def setup_server(server_name: str) -> str:
    """ Create a new MCP server with the input name

        Args:
            Single MCP server name with the following rules:
            - No spaces in name
            - No special Characters in the name

        Return:
            Returns a string with the result of the script running
    """
    # run the setup_uv.sh file with the input server name

    subprocess.run(["bash", "../setup_uv.sh", "testing"], shell=True, check=True)
    # check if the server folder and server.py file is created in the current directory
    # Check if the directory exists
    if not os.path.exists(server_name):
        return "Folder was not created."
    else:
        if not os.path.exists(f"{server_name}.py"):
            return "Server folder was created, but the python script for the server was not"
        else:
            return "Folder and python script created successfully!"
        

if __name__ == "__main__":
    # Initialize and run the server
    setup_server("testing")
    #mcp.run(transport='stdio')
