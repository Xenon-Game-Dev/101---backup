import howdoi
import dropbox
# access key sl.A2b1IVR3Jx8FruSrNX4p2MhziI1dgx3wsOwDeozecU1rBLJgl0WOjjDo28QnpF86EPoe91upxjH7AMz8PFaznja-L1SfWciiFOaSLJWgcI11n1D3M00yEpIpMewi1aFgdhwFotQ

class backupData :
    def __init__ (self, accessKey):
        self.accessKey = accessKey

    def backup(self, fileFrom, fileTo):
        
        DropBox1 = dropbox.Dropbox(self.accessKey)

        with open(fileFrom, 'rb') as file:
            DropBox1.files_upload(file.read(), fileTo)

def initiateBackup(fileInput, fileDestination):
    accessKey = "sl.A2b1IVR3Jx8FruSrNX4p2MhziI1dgx3wsOwDeozecU1rBLJgl0WOjjDo28QnpF86EPoe91upxjH7AMz8PFaznja-L1SfWciiFOaSLJWgcI11n1D3M00yEpIpMewi1aFgdhwFotQ"
    backUpData = backupData(accessKey)
    fileFrom = fileInput
    fileTo = fileDestination
    backUpData.backup(fileFrom=fileFrom, fileTo=fileTo)

initiateBackup('example.txt', '/Backups/exampleBACKUP.txt')    
print("FILE-SUCCESSFULLY-BACKED-UP")








