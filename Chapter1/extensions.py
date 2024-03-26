def main():
    user_input = input("Write the name of your file: ").lower().strip().split(".")
    extension = user_input[-1]
    mime = return_mime(extension)
    if not mime:
        print("application/octet-stream")
    else:
        print(mime)


def return_mime(extension):
    dictionary = {
        "gif": "*image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }
    for file_type in dictionary:
        if extension == file_type:
            return dictionary[file_type]


if __name__ == "__main__":
    main()
