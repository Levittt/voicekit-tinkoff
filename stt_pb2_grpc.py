# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import longrunning_pb2 as tinkoff_dot_cloud_dot_longrunning_dot_v1_dot_longrunning__pb2
import stt_pb2 as tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2


class SpeechToTextStub(object):
    """Speech recognition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recognize = channel.unary_unary(
                '/tinkoff.cloud.stt.v1.SpeechToText/Recognize',
                request_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeRequest.SerializeToString,
                response_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeResponse.FromString,
                )
        self.StreamingRecognize = channel.stream_stream(
                '/tinkoff.cloud.stt.v1.SpeechToText/StreamingRecognize',
                request_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingRecognizeRequest.SerializeToString,
                response_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingRecognizeResponse.FromString,
                )
        self.LongRunningRecognize = channel.unary_unary(
                '/tinkoff.cloud.stt.v1.SpeechToText/LongRunningRecognize',
                request_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.LongRunningRecognizeRequest.SerializeToString,
                response_deserializer=tinkoff_dot_cloud_dot_longrunning_dot_v1_dot_longrunning__pb2.Operation.FromString,
                )
        self.StreamingUnaryRecognize = channel.stream_unary(
                '/tinkoff.cloud.stt.v1.SpeechToText/StreamingUnaryRecognize',
                request_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingUnaryRecognizeRequest.SerializeToString,
                response_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeResponse.FromString,
                )


class SpeechToTextServicer(object):
    """Speech recognition.
    """

    def Recognize(self, request, context):
        """Method to recognize whole audio at once: sending complete audio, getting complete recognition result.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingRecognize(self, request_iterator, context):
        """Method for streaming recognition.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LongRunningRecognize(self, request, context):
        """Method to create longrunning recognition operation. Created operation will persist for a limited time and will be deleted after that time has expired.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingUnaryRecognize(self, request_iterator, context):
        """Method to synchronous recognize audio stream. Returns recognition result after all audio has been sent and processed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeechToTextServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recognize': grpc.unary_unary_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeRequest.FromString,
                    response_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeResponse.SerializeToString,
            ),
            'StreamingRecognize': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingRecognize,
                    request_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingRecognizeRequest.FromString,
                    response_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingRecognizeResponse.SerializeToString,
            ),
            'LongRunningRecognize': grpc.unary_unary_rpc_method_handler(
                    servicer.LongRunningRecognize,
                    request_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.LongRunningRecognizeRequest.FromString,
                    response_serializer=tinkoff_dot_cloud_dot_longrunning_dot_v1_dot_longrunning__pb2.Operation.SerializeToString,
            ),
            'StreamingUnaryRecognize': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamingUnaryRecognize,
                    request_deserializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingUnaryRecognizeRequest.FromString,
                    response_serializer=tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.cloud.stt.v1.SpeechToText', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpeechToText(object):
    """Speech recognition.
    """

    @staticmethod
    def Recognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.cloud.stt.v1.SpeechToText/Recognize',
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeRequest.SerializeToString,
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tinkoff.cloud.stt.v1.SpeechToText/StreamingRecognize',
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingRecognizeRequest.SerializeToString,
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingRecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LongRunningRecognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.cloud.stt.v1.SpeechToText/LongRunningRecognize',
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.LongRunningRecognizeRequest.SerializeToString,
            tinkoff_dot_cloud_dot_longrunning_dot_v1_dot_longrunning__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingUnaryRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/tinkoff.cloud.stt.v1.SpeechToText/StreamingUnaryRecognize',
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.StreamingUnaryRecognizeRequest.SerializeToString,
            tinkoff_dot_cloud_dot_stt_dot_v1_dot_stt__pb2.RecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
