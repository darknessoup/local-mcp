from typing import Any
from mcp.server.fastmcp import FastMCP
import subprocess
import os
mcp = FastMCP("python_help")
# Add your tools here

@mcp.tool()
async def run_python(script_path: str, python_exe: str = "python") -> str:
    """ Run the target python script from a specific location using a specified Python interpreter and return the output from the script.
        Args: 
            The path to the Python script to be executed.
            Optional: The path to the Python executable to use (default is 'python')
    
        Returns:
            stdout of the subprocess, if it exits normally; stderr otherwise.
    """
    # Check if the script exists
    if not os.path.exists(script_path):
        return "Script does not exist."
        
    try:
        # Run the Python script using subprocess with the specified Python executable
        result = subprocess.run([python_exe, script_path], capture_output=True, text=True)
    except FileNotFoundError:
        return f"Python interpreter '{python_exe}' not found."
    
    # If the process exited normally, return stdout; otherwise stderr
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
    
@mcp.tool()
async def get_python_location(script_name: str) -> str:
    """ gets the location of a Python script to be executed

    Args:
       script_name (str): The name of the Python script to get the location for.

    returns:
        The path to the Python script.
    """
    # From the current directory or the workspace root directory, search all sub directories for the python script
    script_path = None
    # the root directory is the top level of the git repo -> run git command to get top level
    root_dir = os.getcwd()

    for root, dirs, files in os.walk(root_dir):
        if script_name in files:
            script_path = os.path.join(root, script_name)
            break
    return script_path

    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
