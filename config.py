class config:
    ROOT_DIR = './'
    SRC_DIR = ROOT_DIR + 'src/'
    IMAGE_PATH = SRC_DIR + 'image'

    BATCH_SIZE = 32
    N_EPOCHS = 30
    LR = 3e-4
    SEED = 77

if __name__ == '__main__':
    print('This is config module')