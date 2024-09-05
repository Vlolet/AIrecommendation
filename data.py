import config
CONFIG = config.config
class customDataset:
    def hello(self):
        print('OK')

class dataloader:
    def loadData(self, path):
        path = CONFIG.IMAGE_PATH
        print()

if __name__ == '__main__':
    print('This is customdata module')