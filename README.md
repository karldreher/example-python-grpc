# example-python-grpc

This repo contains an example GRPC client/server with Python.  
The only files written by hand are the `protos/example.proto`, the `example/server.py`, `example/client.py` and the "shim" `example/generate.py` which is used as a build tool.  

By running `poetry run generate`, the server and client code are automatically generated from `protos/example.proto`.  When this file is updated, the generated `pb2` files should be regenerated.

This follows the example from https://grpc.io/docs/languages/python/quickstart/.  

## Running the server and client
Install dependencies and generate protobufs:
```
poetry install
poetry run generate

```
Run the client and server (in separate consoles)
```
poetry run server
poetry run client
```