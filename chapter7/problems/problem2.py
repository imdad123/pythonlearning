l = ["Harry", "Ron", "Hermione","shoail","shoaib"]
user_post = input("Enter the name: ")
for i in l:
    # if i[0].lower() == "s" and user_post[0].lower() == "s":
    #     print(f"Welcome {i}")
    if i.startswith("s") and user_post.startswith("s"):
        print(f"Welcome {i}")