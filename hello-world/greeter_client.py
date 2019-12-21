"""Python implementation of the GRPC hello_world.Greeter client."""

from __future__ import print_function
import logging

import grpc

import hello_world_pb2
import hello_world_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_world_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloRequest(name='you'))

        response2 = stub.SendUserData(hello_world_pb2.UserDataRequest(name='Joe Stubbs', age=39, home_city='Houston'))
    print("Greeter client received: " + response.message)
    print("Greeter client received: " + response2.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
