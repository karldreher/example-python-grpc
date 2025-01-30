import random
import grpc
import logging

import example_pb2
import example_pb2_grpc

logging.basicConfig(level=logging.INFO)
def run_client():
    # Create a gRPC channel to connect to the server
    channel = grpc.insecure_channel('localhost:50051')

    # Create a stub for the gRPC service
    stub = example_pb2_grpc.TastyStub(channel)
    # randomly pick a fruit from the enum
    fruit = random.choice(example_pb2.FruitType.keys())
    # print("requesting", fruit)
    # Make a request to the server
    request = example_pb2.Fruit(fruit=fruit)
    try:
        response = stub.Eat(request)
        # Print the response from the server
        logging.info("Tasted %s, tastiness: %d", example_pb2.FruitType.Name(response.fruit), response.tastiness)
    except grpc.RpcError as e:
        logging.error(e.details())
        logging.error(e.code())
        logging.error("")


def main():
    for _ in range(100):
        run_client()

if __name__ == '__main__':
    main()

