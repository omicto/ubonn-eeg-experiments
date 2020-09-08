from reading import *
from preprocessing import eyes, muscles, white_noise
import numpy as np

def write_signal_to_file(f, signal):
    for sample in signal:
        f.write(str(sample))
        f.write('\n')

def save_signal(signal, path, identifier=""):
    # base_path = "data/extended"
    # directory = f'{base_path}/{label}/{label}{identifier}.txt'
    path = f'{path}.txt'
    with open(path,'w+') as f:
        write_signal_to_file(f, signal)

def extend_ubonn():
    base_path = "data"
    data = []
    labels = []
    for key, dset in sets.items():
        letter = dset["letter"]
        directory = f'{base_path}/{letter}'
        count = 0
        for filename in os.listdir(directory):
            signal = read_file(os.path.join(directory, filename))
            e = np.floor(eyes(signal))
            Id = get_signalid(filename)
            save_signal(e, f'{directory}/{letter}-EYES{Id}')
            m = np.floor(muscles(signal))
            save_signal(m, f'{directory}/{letter}-MUSC{Id}')
            w = np.floor(white_noise(signal))
            save_signal(w, f'{directory}/{letter}-WHIT{Id}')
            count += 1
            print(f'Extended file {filename}')

if __name__ == "__main__":
    extend_ubonn()
