## Installing UV
* **Installation location** https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2
### Windows
```bash 
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" 
```

### Mac/Linux
* **Using Curl**
```
curl -LsSf https://astral.sh/uv/install.sh | sh # curl
```
* **Specific uv version**
```
curl -LsSf https://astral.sh/uv/0.7.9/install.sh | sh # Specific version with curl
```
* **Using Wget**
```
wget -qO- https://astral.sh/uv/install.sh | sh # wget
```

* **Applying to other Drives** Please restart any open environments/IDEs to allow changes to propegate. 

## Creating Servers

### sh script
* **Inside VS code / git bash** Use the existing ```setup_uv.sh``` script and pass in the server you wnat to create
```bash
./setup_uv.sh <server_name>
```

### Python script
* **This python script is for the MCP server use** Since running an sh script in windows is not typical. The LLM will utilize the py version