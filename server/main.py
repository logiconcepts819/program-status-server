import sys
from exit_code_server import ExitCodeServer
from command_line_parser import parse_command_line

def main(argv):
    led_pairs = parse_command_line(argv)
    if led_pairs is None:
        return 1
    
    server = ExitCodeServer(led_pairs)
    try:
        server.loop()
    except KeyboardInterrupt:
        pass
    server.shutdown()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
