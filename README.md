# web socket demo

a demo of web sockets (bi-directional)

- [web socket demo](#web-socket-demo)
  - [References](#references)
  - [Initial Setup](#initial-setup)
  - [Set your port](#set-your-port)
  - [Run WebSocket Server](#run-websocket-server)
  - [Stop web server](#stop-web-server)
  - [Play with app](#play-with-app)

## References

- See [betterstack fastapi-websockets](https://betterstack.com/community/guides/scaling-python/fastapi-websockets/)
- See [FastAPI](https://fastapi.tiangolo.com/)

## Initial Setup

```powershell
.\.venv\Scripts\Activate.ps1
```

## Set your port

```powershell
# Replace 8888 with whatever port you want
[System.Environment]::SetEnvironmentVariable("PORT", 8888, "User")
# Refresh your environment variables
```

## Run WebSocket Server

```powershell
uv run main.py
```

Yields:

```text
Port:  8888
INFO:     Will watch for changes in these directories: ['C:\\code\\websocketdemo']
INFO:     Uvicorn running on http://127.0.0.1:8888 (Press CTRL+C to quit)
INFO:     Started reloader process [7128] using WatchFiles
INFO:     Started server process [26148]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Stop web server

```powershell
^c # Control+C
```

Yields:

```powershell
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [26148]
INFO:     Stopping reloader process [7128]
```

## Play with app

```powershell
# Use whatever port you specified
start http://127.0.0.1:8888
```
