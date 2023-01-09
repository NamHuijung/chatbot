import socket

class BotServer:
    # 1.
    def __init__(self, srv_port, listen_num):
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None


    # 2. sock 생성
    def create_sorck(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock


    # 3. client 대기
    def ready_for_client(self):
        return self.mySock.accept() # 반환 (conn, address) 튜플
    # conn : 연결된 챗봇 클라이언트와 데이터를 송수신할 수 있는 클라이언트 소켓
    # address : 연결된 챗봇 클라이언트 소켓의 바인드된 주소

    # 4. sock 반환
    def get_sock(self):
        return self.mySock