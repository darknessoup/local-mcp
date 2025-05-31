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