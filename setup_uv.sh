#!/bin/bash

# Create an alias for uv
# Check if the user provided a project name
if [ -z "$1" ]; then
  echo "Please provide a project name"
  exit 1
fi

# Initialize variables
# Get the directory the script resides in
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use absolute path for the target directory
PROJECT_NAME="$1"

PROJ_PATH=$SCRIPT_DIR/servers/$PROJECT_NAME

# Change into the output directory
uv init $PROJ_PATH
cd $PROJ_PATH

# Activate the virtual environment
uv venv
venv=$(pwd)/.venv
source $venv/Scripts/activate

# Initialize the uv project and install dependencies
uv add "mcp[cli]"

# Create a Python file (using `touch` and then editing it with `echo`)
if [ -f "main.py" ]; then
  mv main.py ${PROJECT_NAME}.py # rename the main/py file
else
  touch ${PROJECT_NAME}.py # create the new file if it doesn't exist
fi

# add the default mcp imports, mcp name, and main func
echo "from typing import Any" > ${PROJECT_NAME}.py # <-- Replaces all current content in file with this line
echo "from mcp.server.fastmcp import FastMCP" >> ${PROJECT_NAME}.py
echo "mcp = FastMCP(\"${PROJECT_NAME}\")" >> ${PROJECT_NAME}.py
echo "# Add your tools here" >> ${PROJECT_NAME}.py  # empty line to separate the code blocks
echo "@mcp.tool()" >> ${PROJECT_NAME}.py  # empty line to separate the code blocks
echo "#    async def add(x: float, y: float) -> float:" >> ${PROJECT_NAME}.py  # empty line to separate the code blocks
echo "        return x + y" >> ${PROJECT_NAME}.py  # empty line to separate the
echo "if __name__ == \"__main__\":" >> ${PROJECT_NAME}.py
echo "    # Initialize and run the server" >> ${PROJECT_NAME}.py
echo "    mcp.run(transport='stdio')" >> ${PROJECT_NAME}.py