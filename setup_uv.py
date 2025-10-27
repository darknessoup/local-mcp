import os
import sys
import subprocess
from pathlib import Path
import shutil

def main():
    if len(sys.argv) < 2:
        print("Please provide a project name")
        sys.exit(1)

    project_name = sys.argv[1]

    # Get the directory this script resides in
    script_dir = Path(__file__).resolve().parent
    proj_path = script_dir / "servers" / project_name
    pub_path = script_dir / "public_scripts"

    # Run `uv init`
    subprocess.run(["uv", "init", str(proj_path)], check=True)

    # Change into the project directory
    os.chdir(proj_path)

    # Create and activate the virtual environment
    subprocess.run(["uv", "venv"], check=True)
    venv_path = proj_path / ".venv"

    activate_script = venv_path / "Scripts" / "activate"

    # Activate venv in a subprocess and run uv add
    os.system(f"{venv_path}/Scripts/activate")
    subprocess.run(["uv", "add", "mcp[cli]"])
    os.system("deactivate")

    py_file = proj_path / f"{project_name}.py"
    main_py = proj_path / "main.py"

    if main_py.exists():
        main_py.rename(py_file)
    else:
        py_file.touch()

    public_project_path = pub_path / project_name / f"{project_name}.py"
    if public_project_path.exists():
        print("Copying existing public_script to project directory...")
        shutil.copy(public_project_path, py_file)
        if py_file.exists():
            print("File copied successfully.")
        else:
            print("File not found in public_scripts directory.")
    else:
        print("Creating default Python file content...")
        py_file.write_text(
            "from typing import Any\n"
            "from mcp.server.fastmcp import FastMCP\n"
            f"mcp = FastMCP(\"{project_name}\")\n"
            "# Add your tools here\n"
            "#@mcp.tool()\n"
            "#    async def add(x: float, y: float) -> float:\n"
            "#    return x + y\n"
            "if __name__ == \"__main__\":\n"
            "    # Initialize and run the server\n"
            "    mcp.run(transport='stdio')\n"
        )

if __name__ == "__main__":
    main()
