import random
import grpc
import example_pb2
import example_pb2_grpc
# Import the generated gRPC module

def run_client():
    # Create a gRPC channel to connect to the server
    channel = grpc.insecure_channel('localhost:50051')

    # Create a stub for the gRPC service
    stub = example_pb2_grpc.TastyStub(channel)
    # randomly pick a fruit from the enum
    fruit = random.choice(example_pb2.FruitType.keys())
    print("requesting", fruit)
    # Make a request to the server
    request = example_pb2.Fruit(name=fruit)
    response = stub.Eat(request)

    # Print the response from the server
    # feels wrong to use the enum like this, did i screw it up?
    print(example_pb2.FruitType.Name(response.name), "tastiness", response.tastiness)

def main():
    for _ in range(100):
        run_client()

if __name__ == '__main__':
    main()