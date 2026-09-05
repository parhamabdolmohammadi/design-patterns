

class CloudStream:
    def write(self, data: str):
        print(f"Storing {data}")


class EncryptedCloudStream(CloudStream):

    def write(self, data: str):
        encrypted = self.__encrypt(data)
        super().write(encrypted)

    def __encrypt(self, data: str):
        return "393h23095#$@#^@"


class CompressedCloudStream(CloudStream):

    def write(self, data: str):
        compressed = self.__compressed(data)
        super().write(compressed)

    def __compressed(self, data: str):
        return data.sub_string[0:5]


if __name__ == "__main__":
    cloudStream = CloudStream()
    cloudStream.write("Here is some data")

    cloudStream = EncryptedCloudStream()
    cloudStream.write("Here is some data")
