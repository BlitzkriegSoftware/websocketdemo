# web socket demo

a demo of web sockets (bi-directional)

- See [betterstack fastapi-websockets](https://betterstack.com/community/guides/scaling-python/fastapi-websockets/)

## Initial Setup

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run WebSocket Server

```powershell
 fastapi dev main.py
```

Yields:

```text
   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from C:\code\websocketdemo

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories: ['C:\\code\\websocketdemo']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [12684] using WatchFiles
      INFO   Started server process [16132]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```
