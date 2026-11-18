#by MatheusSFDev

program = True

# * Program Functions
def checkPorts(host):
    pass

def checkPort(host, port):
    pass

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