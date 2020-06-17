for i in range(int(input())):
    n = int(input())
    gest = list(input())
    if "Y" in gest:
        print("NOT INDIAN")
    elif "N" in gest and "I" not in gest:
        print("NOT SURE")
    elif "I" in gest:
        print("INDIAN")
