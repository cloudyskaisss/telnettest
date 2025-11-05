import asyncio
import telnetlib3

async def shell(reader, writer):
    writer.write("\r\nWelcome to Skai's Telnet Server!\r\n")
    writer.write('Type "exit" to disconnect.\r\n')
    while True:
        command = ""
        writer.write('>> ')
        while True:
            inp = await reader.read(1)
            if not inp:
                return

            writer.write(inp)

            if inp in ("\r", "\n"):
                break
            else:
                command += inp.lower()

        command = command.strip()
        if command == 'exit':
            writer.write('\r\nGoodbye!\r\n')
            break
        elif command == 'hello':
            writer.write('\r\nHello there!\r\n')
        else:
            writer.write(f'\r\nUnknown command: {command}\r\n')

        print(inp)
        print(command)

    writer.close()

async def main():
    server = await telnetlib3.create_server(
        host='31.97.209.167',
        port=23,
        shell=shell
    )
    print(f"Telnet server listening on {server.sockets[0].getsockname()}")
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
