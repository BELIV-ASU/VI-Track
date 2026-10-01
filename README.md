VI-Track is an end-to-end vehicle-infrastructure cooperative 3D multi-object tracking framework that improves tracking robustness under temporal asynchrony through query-level fusion and temporal tracking query buffering.

## Data Preparation
Please prepare and download the V2X-SIM dataset from the official website.

The folder structure should be organized as follows before our processing.

```
mmdetection3d
├── mmdet3d
├── tools
├── configs
├── extra_tools
├── projects
├── ckpts
│   ├── model_val
│   ├── pretrain
├── data
│   ├── V2X-Sim
│   │   ├── maps
│   │   ├── samples
│   │   ├── sweeps
│   │   ├── v1.0-trainval
│   ├── infos
│   │   ├── track_cat_10_infos_train.pkl
│   │   ├── track_cat_10_infos_val.pkl
│   │   ├── track_test_cat_10_infos_test.pkl
│   │   ├── mmdet3d_nuscenes_30f_infos_train.pkl
│   │   ├── mmdet3d_nuscenes_30f_infos_val.pkl
│   │   ├── mmdet3d_nuscenes_30f_infos_test.pkl
```


## Training
You can train the model following [the instructions](https://github.com/open-mmlab/mmdetection3d/blob/v1.0.0rc3/docs/en/datasets/nuscenes_det.md).
If you want to train the detector and tracker in an end-to-end manner from scratch, please turn the parameter `train_track_only` in config file to `False`.

one should execute:
```bash
cd /path/to/mmdetection3d
bash extra_tools/dist_train.sh ${CFG_FILE} ${NUM_GPUS}
```
or train with a single GPU:
```bash
python3 extra_tools/train.py ${CFG_FILE}
```

## Evaluation

ATTENTION: Because the sequential property of data, only the single GPU evaluation manner is supported:
```bash
python3 extra_tools/test.py ${CFG_FILE} ${CKPT} --eval=bbox
```

## Checkpoint
You can find the checkpoint here: https://drive.google.com/drive/folders/1c427hV40tS1P0Y7XySyYJMtM1aNkoyAT?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto
