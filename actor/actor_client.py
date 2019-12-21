"""Python implementation of the GRPC hello_world.Greeter client."""

from __future__ import print_function
import logging

import grpc

import actor_pb2
import actor_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        # here, we would need to have a function that took the actor id and returned a connection/stub.
        stub = actor_pb2_grpc.StrStrActorStub(channel)
        response = stub.send_message(actor_pb2.sendStrMsg(msg='a test message'))

    print("Actor client received: " + response.reply)


if __name__ == '__main__':
    logging.basicConfig()
    run()
