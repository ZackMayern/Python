import math

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    ac = math.sqrt(ab**2+bc**2)
    h = ac/2
    adj = bc/2
    angle = int(round(math.degrees(math.acos(adj/h))))

    print(str(angle)+chr(176))