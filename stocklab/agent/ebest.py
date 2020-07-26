class XASession:
    """로그인 상태를 확인하기 위한 클래스 변수."""

    login_state = 0

    def on_login(self, code, msg):
        """
        로그인 시도 후 호출되는 이벤트.
        Code 가 0000이면 로그인 성공.

        :param code:
        :param msg:
        :return:
        """

        if code == "0000":
            print(code, msg)
            XASession.login_state = 1
        else:
            print(code, msg)

    def on_disconnect(self):
        """
        서버와 연결이 끊어지면 발생하는 이벤트.
        :return:
        """

        print("Session disconnected")
        XASession.login_state = 0


class EBest:
    def __init__(self, mode=None):
        """
        config.ini 파일을
        :param mode:
        """
