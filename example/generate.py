import subprocess
def main():
    subprocess.run(["python", "-m", "grpc_tools.protoc", "-Iprotos", "--python_out=example/", "--pyi_out=example/", "--grpc_python_out=example/", "protos/example.proto"])