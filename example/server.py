
import asyncio
import logging

import grpc
import example_pb2 as example_pb2
import example_pb2_grpc as example_pb2_grpc

async def get_fruit_name(fruit: example_pb2.FruitType) -> str:
    prefix = "FRUIT_TYPE_"
    caps_name = example_pb2.FruitType.Name(fruit).lstrip(prefix)
    return caps_name.title()

async def decide_tastiness(fruit: str) -> int:
        hash_value = abs(hash(fruit))
        return (hash_value % 10) + 1

class TastyServicer(example_pb2_grpc.TastyServicer):
    async def Eat(
        self,
        request: example_pb2.Fruit,
        context: grpc.aio.ServicerContext,
    ) -> example_pb2.TastyResponse:
        if request.fruit == example_pb2.FRUIT_TYPE_UNSPECIFIED:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("You must specify a fruit")
            return
        fruit = await get_fruit_name(request.fruit)
        logging.info("Tasting %s", fruit)
        tasty = await decide_tastiness(fruit)
        return example_pb2.TastyResponse(fruit=request.fruit, tastiness=tasty)



async def serve() -> None:
    server = grpc.aio.server()
    example_pb2_grpc.add_TastyServicer_to_server(TastyServicer(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.debug("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
if __name__ == "__main__":
    main()
