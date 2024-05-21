import time
from datetime import datetime

def main(code):
    api = str(time.time())
    api = api.replace(".", "aa")
    api = api.replace("1", "b116")
    api = api + str(datetime.now())
    api = api.replace("-", "Y7^")
    api = api.replace(":", "^Y*FS")
    api = api.replace(".", "a1a")
    api = api.replace(" ", "12*)FE")
    api = api + "yewhru2721" + code
    print(api)

code = "13819"
main(code)