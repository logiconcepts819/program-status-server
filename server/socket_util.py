def recvall(sock, n):
    """
    Helper function to recv n bytes, or return None if EOF is HIT. This
    function should not be used directly outside this module.
    """
    data = ''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data