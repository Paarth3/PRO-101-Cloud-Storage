import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def uploadData(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        with open(fileFrom,'wb') as f:
            dbx.files_upload(f.read(), fileTo)


def main():
    accessToken = ""
    transferData = TransferData(accessToken)

    fileFrom = input("Please Enter the path of file to be uploaded : ")
    fileTo = input("Please Enter the path of file where it is suupposed to be uploaded : ")

    TransferData.uploadData(fileFrom,fileTo)