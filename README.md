initialize a directory
```bash
uv init sse_server
```
create venv and activate
```bash
uv venv
#for windows
.venv\Scripts\activate
```
install libraries
```bash
uv pip install -r requirements.txt
```
build the docker image
```bash
docker build -t terminal_sse_server .
```
run the docker image
```bash
docker run --rm -p 8081:8081 -v <PATH_TO_WORKSPACE_DIRECTORY_Required_FOR_COMMAND_LINE_TOOL>:/root/mcp/workspace terminal_sse_server
