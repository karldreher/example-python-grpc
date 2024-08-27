# example-python-grpc

This repo contains an example GRPC client/server with Python.  
The only files written by hand are the `protos/example.proto`, and the "shim" `example/generate.py` which is used as a build tool.  

By running `poetry run generate`, the server and client code are automatically generated from `protos/example.proto`.  

This follows the example from https://grpc.io/docs/languages/python/quickstart/.  