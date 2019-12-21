# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import actor_pb2 as actor__pb2


class StrStrActorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_message = channel.unary_unary(
        '/StrStrActor/send_message',
        request_serializer=actor__pb2.sendStrMsg.SerializeToString,
        response_deserializer=actor__pb2.strReply.FromString,
        )


class StrStrActorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_message(self, request, context):
    """send a message
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StrStrActorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_message': grpc.unary_unary_rpc_method_handler(
          servicer.send_message,
          request_deserializer=actor__pb2.sendStrMsg.FromString,
          response_serializer=actor__pb2.strReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'StrStrActor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ByteByteActorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_message = channel.unary_unary(
        '/ByteByteActor/send_message',
        request_serializer=actor__pb2.sendByteMsg.SerializeToString,
        response_deserializer=actor__pb2.byteReply.FromString,
        )


class ByteByteActorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_message(self, request, context):
    """send a message
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ByteByteActorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_message': grpc.unary_unary_rpc_method_handler(
          servicer.send_message,
          request_deserializer=actor__pb2.sendByteMsg.FromString,
          response_serializer=actor__pb2.byteReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ByteByteActor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
