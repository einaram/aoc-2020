import numpy as np

def read_rulesfile(datatype='test'):
    with open(f"input/11.{datatype}.in") as infile:
        data = infile.read().split("\n")
        data = [[float(x.replace("L", '0').replace(".", 'nan'))
                 for x in row] for row in data]
        return np.array(data)


layout = read_rulesfile('data')

def subset_slice(idx, xy_max):

    x,y = idx
    xmin = x-1 if x-1 > 0 else 0
    xmax = x+2 if x < xy_max[0] else xy_max[0]
    ymin = y-1 if y > 0 else 0
    ymax = y+2 if y < xy_max[1] else xy_max[1]
    
    return np.s_[xmin:xmax, ymin:ymax]

while True:
    new_layout = np.copy(layout)
    for idx, x in np.ndenumerate(layout):
        s=subset_slice(idx, layout.shape)
        if x == 0 and np.nansum(layout[s])==0:
            new_layout[idx] = 1
        elif x == 1 and np.nansum(layout[s]) > 4:
            new_layout[idx] = 0
        
    # print(new_layout)
    # print("__________________________________________")
    if (np.nan_to_num(new_layout) == np.nan_to_num(layout)).all():
        print(np.nansum(layout))
        break
    layout = new_layout




