import time 

def test():
    print("app is running")
    time.sleep(5)
    return test()

if __name__ == "__main__":
    test()
