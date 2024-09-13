import grpc
from concurrent import futures
import greet_pb2_grpc
import greet_pb2


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greet_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')  # Puerto 50051
    server.start()
    print("Servidor gRPC corriendo en el puerto 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
