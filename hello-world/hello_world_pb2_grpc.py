# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hello_world_pb2 as hello__world__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/Greeter/SayHello',
        request_serializer=hello__world__pb2.HelloRequest.SerializeToString,
        response_deserializer=hello__world__pb2.HelloReply.FromString,
        )
    self.SendUserData = channel.unary_unary(
        '/Greeter/SendUserData',
        request_serializer=hello__world__pb2.UserDataRequest.SerializeToString,
        response_deserializer=hello__world__pb2.UserDataReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendUserData(self, request, context):
    """provide your information
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=hello__world__pb2.HelloRequest.FromString,
          response_serializer=hello__world__pb2.HelloReply.SerializeToString,
      ),
      'SendUserData': grpc.unary_unary_rpc_method_handler(
          servicer.SendUserData,
          request_deserializer=hello__world__pb2.UserDataRequest.FromString,
          response_serializer=hello__world__pb2.UserDataReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
