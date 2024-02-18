ext = input("What is the name of your file? ").strip().lower()


match ext:
    case _ if ext.endswith(".gif"):
        print("image/gif")
    case _ if ext.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    case _ if ext.endswith(".png"):
        print("image/png")
    case _ if ext.endswith(".pdf"):
        print("application/pdf")
    case _ if ext.endswith(".txt"):
        print("text/plain")
    case _:
        print("application/octet-stream")