import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJzN61lymG72058uvxeSOwP01whrYzdQgdN9lJZCBsp4gS8PzsUL3kxslHaFqb9mLsSpv0s9t6FSh44-q57YWRS1igk8ikQ1C9XEVyWqkX7-VZ9ozV6cSyEVcvJBpA9qlxYqemHFWH8-'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('successfully uploaded')

main()
