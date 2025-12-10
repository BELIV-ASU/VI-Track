import pickle
with open('/home/jingxiong/DQTrack-main/mmdetection3d/data/V2X-SIM/track_cat_10_infos_val.pkl', 'rb') as f:
    data = pickle.load(f)
print(data.keys())