import subprocess
def main():
    subprocess.run(["python", "-m", "grpc_tools.protoc", "-Iprotos/example", "--python_out=.", "--pyi_out=.", "--grpc_python_out=.", "protos/example/example.proto"])