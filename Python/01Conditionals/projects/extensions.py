ext = input("What is the name of your file? ").strip().lower()

match ext:
    case ext.endswith(".gif"):
        print("image/gif")
    case ext.endswith(".jpg"):
        print("image/jpg")
    case ext.endswith(".jpeg"):
        print("image/jpeg")
    case ext.endswith(".png"):
        print("image/png")
    case ext.endswith(".pdf"):
        print("application/pdf")
    case ext.endswith(".txt"):
        print("text/plain")
    case _:
        print("application/octet-stream")