#!/bin/bash

# Create an alias for uv
# Check if the user provided a project name
if [ -z "$1" ]; then
  echo "Please provide a project name"
  exit 1
fi

# Initialize variables
PROJECT_NAME=$1

# Create the output directory
mkdir -p $OUTPUT_DIR

# Change into the output directory
uv init $PROJECT_NAME
cd $PROJECT_NAME

# Initialize the uv project and install dependencies
uv add "mcp[cli]"

# Activate the virtual environment

uv venv
venv=$(pwd)/.venv
source $venv/Scripts/activate

# Create a Python file (using `touch` and then editing it with `echo`)
if [ -f "main.py" ]; then
  mv main.py ${PROJECT_NAME}.py # rename the main/py file
else
  touch ${PROJECT_NAME}.py # create the new file if it doesn't exist
fi

# add the default mcp imports, mcp name, and main func
echo "from typing import Any" > ${PROJECT_NAME}.py # <-- Replaces all current content in file with this line
echo "from mcp.server.fastmcp import FastMCP" >> ${PROJECT_NAME}.py
echo "" >> ${PROJECT_NAME}.py  # empty line to separate the code blocks
echo "mcp = FastMCP(\"${PROJECT_NAME}\")" >> ${PROJECT_NAME}.py
echo "if __name__ == \"__main__\":" >> ${PROJECT_NAME}.py
echo "    # Initialize and run the server" >> ${PROJECT_NAME}.py
echo "    mcp.run(transport='stdio')" >> ${PROJECT_NAME}.py