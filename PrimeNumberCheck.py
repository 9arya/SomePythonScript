#MIT License
#
#Copyright (c) 2026 9arya
import sys
def main():
    if len(sys.argv) < 2:
        try:
            Integer = int(input("Number to check:").strip())
            if Integer < 1:print("this script not support negatif and zero");return
            for n in range(2, Integer):
                a = Integer % n
                if a == 0:
                    print("False: not primes numbers")
                    break
            else:print("True: is prime numbers")
        except ValueError:
            print("ValueError: is not number")
            return
        except (KeyboardInterrupt, EOFError):return
    else:
        if int(sys.argv[1]) < 1:print("this script not support negatif and zero");return
        for n in range(2, int(sys.argv[1])):
            a = int(sys.argv[1]) % n
            if a == 0:
                print("False: not prime numbers")
                break
        else:print("True: is prime numbers")
if __name__=="__main__":main()
