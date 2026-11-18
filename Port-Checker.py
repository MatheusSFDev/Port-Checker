#by MatheusSFDev
import socket, concurrent.futures

program = True

# * Program Functions
def checkPorts(host):
    ports = []
    
    print("The Ports are being Checked, please wait...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as exec:
        futures = [exec.submit(checkPort, host, port) for port in range(1, 65535)]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                ports.append(future.result())
    
    print(F"These are the Open Ports for '{host}':")
    for port in ports:
        print(F"[{port}]", end=" ")
        
    print("")

def checkPort(host, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    conn.settimeout(0.5)
    
    success = True
    
    try:
        conn.connect((host, port))
        print(F"The Port [{port}] is Open")
    except socket.timeout:
        success = False
    except ConnectionRefusedError:
        success = False
    except Exception as ex:
        print("Unknown Error has Ocurred, Mode Details:")
        print(ex)
        success = False
    finally:
        conn.close()
    
    return port if success else False

def validateHost(host):
    numbers = host.rsplit(".")
    
    if len(numbers) == 4:
        for num in numbers:
            if int(num) < 0 or int(num) > 255:
                return False
        
        return True
    else:
        print("Incorrect Format, Please Insert an Valid IP, Ex: 192.168.1.1")
        return False

print("-------------------------------------------------------")
print("- Port Checker -")
print("#by MatheusSFDev")
print("-------------------------------------------------------")

# * Main Program
while program:
    print("Enter a Host to Test the Ports (Press Enter to leave)")
    host = input("-> ")
    
    match host:
        case "":
            program = False
        case _:
            if validateHost(host):
                checkPorts(host)
    
    print("-------------------------------------------------------")

print("Thanks for Using!")
print("-------------------------------------------------------")

input("Press Enter to Close...")