import numpy as np
import matplotlib.pyplot as plt
import os
import re

def parse_file(signal_file):
    lines = signal_file.readlines()
    return np.fromiter(map(float, lines), dtype=np.int)

def segment_data(data: np.ndarray, steps: int, dim: int) -> np.ndarray:
    return data.reshape([steps, dim])

def read_file(file_path):#, timesteps, data_dim, data_length):
    with open(file_path) as f:
        return parse_file(f)

# https://stackoverflow.com/a/4602224/11449725
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

##############################################################################

classes = {
    "HEALTHY"      :  0,
    "SEIZURE_FREE" :  1,
    "SEIZURE"      :  2
}

# TODO
sets = {
    "A": {"class": classes["HEALTHY"],      "letter": "Z"},
    "B": {"class": classes["HEALTHY"],      "letter": "O"},
    "C": {"class": classes["SEIZURE_FREE"], "letter": "N"},
    "D": {"class": classes["SEIZURE_FREE"], "letter": "F"},
    "E": {"class": classes["SEIZURE"],      "letter": "S"}
}

# ubonn = {
#     "healthy" : [
#         {"signal": [],
#          "letter": "Z",
#           "type" : "original",
#            "id"  : 1}
#            ]
#     }

signaltypes = {
    "MUSC" : "muscles",
    "EYES" : "eyes",
    "WHIT" : "white"
}

def signal_dict(signal, letter, filetype, signal_id):
    return {"signal": signal,
            "letter": letter,
            "type"  : filetype,
            "id"    : signal_id}

def get_metadata(filename):
    regex = r'[FNOSZ](-(?P<type>MUSC|EYES|WHIT))?(?P<Id>[0-9]{3})\.[txtTXT]'
    _type = re.search(regex, filename)
    return (_type.group("type"), _type.group("Id"))

def get_signalid(filename):
    return get_metadata(filename)[1]

def get_filetype(filename):
    filetype = get_metadata(filename)[0]
    if filetype: 
        return filetype 
    else: 
        return "original"

# TODO
def load_ubonn_dict():
    ubonn = {
        0 : {"signals": [], "type" : "healthy" },
        1 : {"signals": [], "type" : "seizure_free" },
        2 : {"signals": [], "type" : "seizure" }
    }

    base_path = "data"
    
    for key, dset in sets.items():
        letter = dset["letter"]
        clazz = dset["class"]
        directory = f'{base_path}/{letter}'
        for filename in os.listdir(directory):
            print(f"Read {filename}")
            signal = read_file(os.path.join(directory, filename))
            filetype = get_filetype(filename)
            signal_id = get_signalid(filename)
            as_dict = signal_dict(signal, letter, filetype, signal_id)
            ubonn[clazz]["signals"].append(as_dict)
    
    return ubonn

# TODO
def load_ubonn():
    '''
        Returns
         data   -   ndarray containing the raw signals
         labels -   ndarray containing the labels, using the following mapping
                    "HEALTHY"      :  0,
                    "SEIZURE_FREE" :  1,
                    "SEIZURE"      :  2
    '''
    return dataset_to_array(load_ubonn_dict())

def dataset_to_array(dset):
    data = []
    labels = []
    for key, class_content in dset.items():
        for signal_dict in class_content["signals"]:
            data.append(signal_dict["signal"])
            labels.append(key)
    return np.array(data), np.array(labels)

##############################################################################

if __name__ == "__main__":
    x, y = load_ubonn()
    x_shuffled, y_shuffled = unison_shuffled_copies(x, y)
    print(x_shuffled,y_shuffled)
    print(x.shape)
    print(y.shape)
