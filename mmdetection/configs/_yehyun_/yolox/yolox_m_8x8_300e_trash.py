_base_ = './yolox_s_8x8_300e_trash.py'

# model settings
model = dict(
    backbone=dict(deepen_factor=0.67, widen_factor=0.75),
    neck=dict(in_channels=[192, 384, 768], out_channels=192, num_csp_blocks=2),
    bbox_head=dict(in_channels=192, feat_channels=192),
)
