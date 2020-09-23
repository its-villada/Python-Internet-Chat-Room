import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Localhost
host=socket.gethostname()
port=54545

s.bind((host,port))

s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got connection from',addr)
    conn.send((r"""\

        Que la fuerza de telecomunicaciones 2 te acompañe 


                        _--~~| |~~--_
                       /     | |   \ \
                      |      |      | |
                     |       | |       |
                     |       |         |
                    /__----_ | | _----__\
                   |/_-~~~-_\| |/_-~~~-_\|
                   //    #  \===/    #  \\
                  //        |===|        \\
                 / |________|/~\|________| \
                /  \        |___|        /  \
               /   ^\      /| | |\      /^   \
              /     ^\   /| | | | |\   /^     \
             /       ^\/| | | | | | |\/^       \
            <          O|_|_|_|_|_|_|O          >
             ~\        \   -------   /        /~
               ~\       ~\ \_____/ /~       /~
                 ~\       ^-_____-^       /~
           _________>                   <__________
/~~~~~~~~~~                                        ~~~~~~~~~~~\

                    """).encode('utf-8'))
    conn.close()

s.close()