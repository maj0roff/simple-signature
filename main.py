from sign import Signature

clRequestPart1="user:maj0r"
clRequestPart2="pass:123"
clRequestPart3="type:create-module"
clRequestSign="328b3e746dd4100274e48002a02818ac"

def main():
    if Signature.validate(clRequestPart1, clRequestPart2, clRequestPart3, clientSignature=clRequestSign):
	    print("Correct request")
    else:
        print("Bad signature")

if __name__ == "__main__":
	main()