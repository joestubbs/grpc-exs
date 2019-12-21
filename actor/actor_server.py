"""Implementation of the GRPC actor wrapper server."""

from concurrent import futures
import logging

import grpc

import actor_pb2
import actor_pb2_grpc


class StrStrActorServer(actor_pb2_grpc.StrStrActorServicer):

    def send_message(self, request, context):
        # in the future, we would parse context for JWT metadata, add additional details, etc., and send to actor.

        # invoke the actual actor, get message
        result = self.execute_actor(request.msg)

        # return the result as a formated message
        return actor_pb2.strReply(reply=result)

    def execute_actor(self, message):
        msg = f"execution complte! I got: {message}"
        return '{ "status": "success", "message": ' +  f'"{msg}"' + '}'


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    actor_pb2_grpc.add_StrStrActorServicer_to_server(StrStrActorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

