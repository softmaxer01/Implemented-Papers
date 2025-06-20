```text
==========================================================================================
Layer (type:depth-idx)                   Output Shape              Param #
==========================================================================================
GoogLeNet                                [1, 1000]                 --
├─conv_block: 1-1                        [1, 64, 112, 112]         --
│    └─conv.weight                                                 ├─9,408
│    └─conv.bias                                                   ├─64
│    └─batch_norm.weight                                           ├─64
│    └─batch_norm.bias                                             └─64
│    └─Conv2d: 2-1                       [1, 64, 112, 112]         9,472
│    │    └─weight                                                 ├─9,408
│    │    └─bias                                                   └─64
│    └─BatchNorm2d: 2-2                  [1, 64, 112, 112]         128
│    │    └─weight                                                 ├─64
│    │    └─bias                                                   └─64
│    └─ReLU: 2-3                         [1, 64, 112, 112]         --
├─MaxPool2d: 1-2                         [1, 64, 56, 56]           --
├─conv_block: 1-3                        [1, 192, 56, 56]          --
│    └─conv.weight                                                 ├─110,592
│    └─conv.bias                                                   ├─192
│    └─batch_norm.weight                                           ├─192
│    └─batch_norm.bias                                             └─192
│    └─Conv2d: 2-4                       [1, 192, 56, 56]          110,784
│    │    └─weight                                                 ├─110,592
│    │    └─bias                                                   └─192
│    └─BatchNorm2d: 2-5                  [1, 192, 56, 56]          384
│    │    └─weight                                                 ├─192
│    │    └─bias                                                   └─192
│    └─ReLU: 2-6                         [1, 192, 56, 56]          --
├─MaxPool2d: 1-4                         [1, 192, 28, 28]          --
├─inception_block: 1-5                   [1, 256, 28, 28]          --
│    └─branch1.conv.weight                                         ├─12,288
│    └─branch1.conv.bias                                           ├─64
│    └─branch1.batch_norm.weight                                   ├─64
│    └─branch1.batch_norm.bias                                     ├─64
│    └─branch2.0.conv.weight                                       ├─18,432
│    └─branch2.0.conv.bias                                         ├─96
│    └─branch2.0.batch_norm.weight                                 ├─96
│    └─branch2.0.batch_norm.bias                                   ├─96
│    └─branch2.1.conv.weight                                       ├─110,592
│    └─branch2.1.conv.bias                                         ├─128
│    └─branch2.1.batch_norm.weight                                 ├─128
│    └─branch2.1.batch_norm.bias                                   ├─128
│    └─branch3.0.conv.weight                                       ├─3,072
│    └─branch3.0.conv.bias                                         ├─16
│    └─branch3.0.batch_norm.weight                                 ├─16
│    └─branch3.0.batch_norm.bias                                   ├─16
│    └─branch3.1.conv.weight                                       ├─12,800
│    └─branch3.1.conv.bias                                         ├─32
│    └─branch3.1.batch_norm.weight                                 ├─32
│    └─branch3.1.batch_norm.bias                                   ├─32
│    └─branch4.1.conv.weight                                       ├─6,144
│    └─branch4.1.conv.bias                                         ├─32
│    └─branch4.1.batch_norm.weight                                 ├─32
│    └─branch4.1.batch_norm.bias                                   └─32
│    └─conv_block: 2-7                   [1, 64, 28, 28]           --
│    │    └─conv.weight                                            ├─12,288
│    │    └─conv.bias                                              ├─64
│    │    └─batch_norm.weight                                      ├─64
│    │    └─batch_norm.bias                                        └─64
│    │    └─Conv2d: 3-1                  [1, 64, 28, 28]           12,352
│    │    │    └─weight                                            ├─12,288
│    │    │    └─bias                                              └─64
│    │    └─BatchNorm2d: 3-2             [1, 64, 28, 28]           128
│    │    │    └─weight                                            ├─64
│    │    │    └─bias                                              └─64
│    │    └─ReLU: 3-3                    [1, 64, 28, 28]           --
│    └─Sequential: 2-8                   [1, 128, 28, 28]          --
│    │    └─0.conv.weight                                          ├─18,432
│    │    └─0.conv.bias                                            ├─96
│    │    └─0.batch_norm.weight                                    ├─96
│    │    └─0.batch_norm.bias                                      ├─96
│    │    └─1.conv.weight                                          ├─110,592
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─conv_block: 3-4              [1, 96, 28, 28]           18,720
│    │    │    └─conv.weight                                       ├─18,432
│    │    │    └─conv.bias                                         ├─96
│    │    │    └─batch_norm.weight                                 ├─96
│    │    │    └─batch_norm.bias                                   └─96
│    │    └─conv_block: 3-5              [1, 128, 28, 28]          110,976
│    │    │    └─conv.weight                                       ├─110,592
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
│    └─Sequential: 2-9                   [1, 32, 28, 28]           --
│    │    └─0.conv.weight                                          ├─3,072
│    │    └─0.conv.bias                                            ├─16
│    │    └─0.batch_norm.weight                                    ├─16
│    │    └─0.batch_norm.bias                                      ├─16
│    │    └─1.conv.weight                                          ├─12,800
│    │    └─1.conv.bias                                            ├─32
│    │    └─1.batch_norm.weight                                    ├─32
│    │    └─1.batch_norm.bias                                      └─32
│    │    └─conv_block: 3-6              [1, 16, 28, 28]           3,120
│    │    │    └─conv.weight                                       ├─3,072
│    │    │    └─conv.bias                                         ├─16
│    │    │    └─batch_norm.weight                                 ├─16
│    │    │    └─batch_norm.bias                                   └─16
│    │    └─conv_block: 3-7              [1, 32, 28, 28]           12,896
│    │    │    └─conv.weight                                       ├─12,800
│    │    │    └─conv.bias                                         ├─32
│    │    │    └─batch_norm.weight                                 ├─32
│    │    │    └─batch_norm.bias                                   └─32
│    └─Sequential: 2-10                  [1, 32, 28, 28]           --
│    │    └─1.conv.weight                                          ├─6,144
│    │    └─1.conv.bias                                            ├─32
│    │    └─1.batch_norm.weight                                    ├─32
│    │    └─1.batch_norm.bias                                      └─32
│    │    └─MaxPool2d: 3-8               [1, 192, 28, 28]          --
│    │    └─conv_block: 3-9              [1, 32, 28, 28]           6,240
│    │    │    └─conv.weight                                       ├─6,144
│    │    │    └─conv.bias                                         ├─32
│    │    │    └─batch_norm.weight                                 ├─32
│    │    │    └─batch_norm.bias                                   └─32
├─inception_block: 1-6                   [1, 480, 28, 28]          --
│    └─branch1.conv.weight                                         ├─32,768
│    └─branch1.conv.bias                                           ├─128
│    └─branch1.batch_norm.weight                                   ├─128
│    └─branch1.batch_norm.bias                                     ├─128
│    └─branch2.0.conv.weight                                       ├─32,768
│    └─branch2.0.conv.bias                                         ├─128
│    └─branch2.0.batch_norm.weight                                 ├─128
│    └─branch2.0.batch_norm.bias                                   ├─128
│    └─branch2.1.conv.weight                                       ├─221,184
│    └─branch2.1.conv.bias                                         ├─192
│    └─branch2.1.batch_norm.weight                                 ├─192
│    └─branch2.1.batch_norm.bias                                   ├─192
│    └─branch3.0.conv.weight                                       ├─8,192
│    └─branch3.0.conv.bias                                         ├─32
│    └─branch3.0.batch_norm.weight                                 ├─32
│    └─branch3.0.batch_norm.bias                                   ├─32
│    └─branch3.1.conv.weight                                       ├─76,800
│    └─branch3.1.conv.bias                                         ├─96
│    └─branch3.1.batch_norm.weight                                 ├─96
│    └─branch3.1.batch_norm.bias                                   ├─96
│    └─branch4.1.conv.weight                                       ├─16,384
│    └─branch4.1.conv.bias                                         ├─64
│    └─branch4.1.batch_norm.weight                                 ├─64
│    └─branch4.1.batch_norm.bias                                   └─64
│    └─conv_block: 2-11                  [1, 128, 28, 28]          --
│    │    └─conv.weight                                            ├─32,768
│    │    └─conv.bias                                              ├─128
│    │    └─batch_norm.weight                                      ├─128
│    │    └─batch_norm.bias                                        └─128
│    │    └─Conv2d: 3-10                 [1, 128, 28, 28]          32,896
│    │    │    └─weight                                            ├─32,768
│    │    │    └─bias                                              └─128
│    │    └─BatchNorm2d: 3-11            [1, 128, 28, 28]          256
│    │    │    └─weight                                            ├─128
│    │    │    └─bias                                              └─128
│    │    └─ReLU: 3-12                   [1, 128, 28, 28]          --
│    └─Sequential: 2-12                  [1, 192, 28, 28]          --
│    │    └─0.conv.weight                                          ├─32,768
│    │    └─0.conv.bias                                            ├─128
│    │    └─0.batch_norm.weight                                    ├─128
│    │    └─0.batch_norm.bias                                      ├─128
│    │    └─1.conv.weight                                          ├─221,184
│    │    └─1.conv.bias                                            ├─192
│    │    └─1.batch_norm.weight                                    ├─192
│    │    └─1.batch_norm.bias                                      └─192
│    │    └─conv_block: 3-13             [1, 128, 28, 28]          33,152
│    │    │    └─conv.weight                                       ├─32,768
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
│    │    └─conv_block: 3-14             [1, 192, 28, 28]          221,760
│    │    │    └─conv.weight                                       ├─221,184
│    │    │    └─conv.bias                                         ├─192
│    │    │    └─batch_norm.weight                                 ├─192
│    │    │    └─batch_norm.bias                                   └─192
│    └─Sequential: 2-13                  [1, 96, 28, 28]           --
│    │    └─0.conv.weight                                          ├─8,192
│    │    └─0.conv.bias                                            ├─32
│    │    └─0.batch_norm.weight                                    ├─32
│    │    └─0.batch_norm.bias                                      ├─32
│    │    └─1.conv.weight                                          ├─76,800
│    │    └─1.conv.bias                                            ├─96
│    │    └─1.batch_norm.weight                                    ├─96
│    │    └─1.batch_norm.bias                                      └─96
│    │    └─conv_block: 3-15             [1, 32, 28, 28]           8,288
│    │    │    └─conv.weight                                       ├─8,192
│    │    │    └─conv.bias                                         ├─32
│    │    │    └─batch_norm.weight                                 ├─32
│    │    │    └─batch_norm.bias                                   └─32
│    │    └─conv_block: 3-16             [1, 96, 28, 28]           77,088
│    │    │    └─conv.weight                                       ├─76,800
│    │    │    └─conv.bias                                         ├─96
│    │    │    └─batch_norm.weight                                 ├─96
│    │    │    └─batch_norm.bias                                   └─96
│    └─Sequential: 2-14                  [1, 64, 28, 28]           --
│    │    └─1.conv.weight                                          ├─16,384
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─MaxPool2d: 3-17              [1, 256, 28, 28]          --
│    │    └─conv_block: 3-18             [1, 64, 28, 28]           16,576
│    │    │    └─conv.weight                                       ├─16,384
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
├─MaxPool2d: 1-7                         [1, 480, 14, 14]          --
├─inception_block: 1-8                   [1, 512, 14, 14]          --
│    └─branch1.conv.weight                                         ├─92,160
│    └─branch1.conv.bias                                           ├─192
│    └─branch1.batch_norm.weight                                   ├─192
│    └─branch1.batch_norm.bias                                     ├─192
│    └─branch2.0.conv.weight                                       ├─46,080
│    └─branch2.0.conv.bias                                         ├─96
│    └─branch2.0.batch_norm.weight                                 ├─96
│    └─branch2.0.batch_norm.bias                                   ├─96
│    └─branch2.1.conv.weight                                       ├─179,712
│    └─branch2.1.conv.bias                                         ├─208
│    └─branch2.1.batch_norm.weight                                 ├─208
│    └─branch2.1.batch_norm.bias                                   ├─208
│    └─branch3.0.conv.weight                                       ├─7,680
│    └─branch3.0.conv.bias                                         ├─16
│    └─branch3.0.batch_norm.weight                                 ├─16
│    └─branch3.0.batch_norm.bias                                   ├─16
│    └─branch3.1.conv.weight                                       ├─19,200
│    └─branch3.1.conv.bias                                         ├─48
│    └─branch3.1.batch_norm.weight                                 ├─48
│    └─branch3.1.batch_norm.bias                                   ├─48
│    └─branch4.1.conv.weight                                       ├─30,720
│    └─branch4.1.conv.bias                                         ├─64
│    └─branch4.1.batch_norm.weight                                 ├─64
│    └─branch4.1.batch_norm.bias                                   └─64
│    └─conv_block: 2-15                  [1, 192, 14, 14]          --
│    │    └─conv.weight                                            ├─92,160
│    │    └─conv.bias                                              ├─192
│    │    └─batch_norm.weight                                      ├─192
│    │    └─batch_norm.bias                                        └─192
│    │    └─Conv2d: 3-19                 [1, 192, 14, 14]          92,352
│    │    │    └─weight                                            ├─92,160
│    │    │    └─bias                                              └─192
│    │    └─BatchNorm2d: 3-20            [1, 192, 14, 14]          384
│    │    │    └─weight                                            ├─192
│    │    │    └─bias                                              └─192
│    │    └─ReLU: 3-21                   [1, 192, 14, 14]          --
│    └─Sequential: 2-16                  [1, 208, 14, 14]          --
│    │    └─0.conv.weight                                          ├─46,080
│    │    └─0.conv.bias                                            ├─96
│    │    └─0.batch_norm.weight                                    ├─96
│    │    └─0.batch_norm.bias                                      ├─96
│    │    └─1.conv.weight                                          ├─179,712
│    │    └─1.conv.bias                                            ├─208
│    │    └─1.batch_norm.weight                                    ├─208
│    │    └─1.batch_norm.bias                                      └─208
│    │    └─conv_block: 3-22             [1, 96, 14, 14]           46,368
│    │    │    └─conv.weight                                       ├─46,080
│    │    │    └─conv.bias                                         ├─96
│    │    │    └─batch_norm.weight                                 ├─96
│    │    │    └─batch_norm.bias                                   └─96
│    │    └─conv_block: 3-23             [1, 208, 14, 14]          180,336
│    │    │    └─conv.weight                                       ├─179,712
│    │    │    └─conv.bias                                         ├─208
│    │    │    └─batch_norm.weight                                 ├─208
│    │    │    └─batch_norm.bias                                   └─208
│    └─Sequential: 2-17                  [1, 48, 14, 14]           --
│    │    └─0.conv.weight                                          ├─7,680
│    │    └─0.conv.bias                                            ├─16
│    │    └─0.batch_norm.weight                                    ├─16
│    │    └─0.batch_norm.bias                                      ├─16
│    │    └─1.conv.weight                                          ├─19,200
│    │    └─1.conv.bias                                            ├─48
│    │    └─1.batch_norm.weight                                    ├─48
│    │    └─1.batch_norm.bias                                      └─48
│    │    └─conv_block: 3-24             [1, 16, 14, 14]           7,728
│    │    │    └─conv.weight                                       ├─7,680
│    │    │    └─conv.bias                                         ├─16
│    │    │    └─batch_norm.weight                                 ├─16
│    │    │    └─batch_norm.bias                                   └─16
│    │    └─conv_block: 3-25             [1, 48, 14, 14]           19,344
│    │    │    └─conv.weight                                       ├─19,200
│    │    │    └─conv.bias                                         ├─48
│    │    │    └─batch_norm.weight                                 ├─48
│    │    │    └─batch_norm.bias                                   └─48
│    └─Sequential: 2-18                  [1, 64, 14, 14]           --
│    │    └─1.conv.weight                                          ├─30,720
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─MaxPool2d: 3-26              [1, 480, 14, 14]          --
│    │    └─conv_block: 3-27             [1, 64, 14, 14]           30,912
│    │    │    └─conv.weight                                       ├─30,720
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
├─inception_block: 1-9                   [1, 512, 14, 14]          --
│    └─branch1.conv.weight                                         ├─81,920
│    └─branch1.conv.bias                                           ├─160
│    └─branch1.batch_norm.weight                                   ├─160
│    └─branch1.batch_norm.bias                                     ├─160
│    └─branch2.0.conv.weight                                       ├─57,344
│    └─branch2.0.conv.bias                                         ├─112
│    └─branch2.0.batch_norm.weight                                 ├─112
│    └─branch2.0.batch_norm.bias                                   ├─112
│    └─branch2.1.conv.weight                                       ├─225,792
│    └─branch2.1.conv.bias                                         ├─224
│    └─branch2.1.batch_norm.weight                                 ├─224
│    └─branch2.1.batch_norm.bias                                   ├─224
│    └─branch3.0.conv.weight                                       ├─12,288
│    └─branch3.0.conv.bias                                         ├─24
│    └─branch3.0.batch_norm.weight                                 ├─24
│    └─branch3.0.batch_norm.bias                                   ├─24
│    └─branch3.1.conv.weight                                       ├─38,400
│    └─branch3.1.conv.bias                                         ├─64
│    └─branch3.1.batch_norm.weight                                 ├─64
│    └─branch3.1.batch_norm.bias                                   ├─64
│    └─branch4.1.conv.weight                                       ├─32,768
│    └─branch4.1.conv.bias                                         ├─64
│    └─branch4.1.batch_norm.weight                                 ├─64
│    └─branch4.1.batch_norm.bias                                   └─64
│    └─conv_block: 2-19                  [1, 160, 14, 14]          --
│    │    └─conv.weight                                            ├─81,920
│    │    └─conv.bias                                              ├─160
│    │    └─batch_norm.weight                                      ├─160
│    │    └─batch_norm.bias                                        └─160
│    │    └─Conv2d: 3-28                 [1, 160, 14, 14]          82,080
│    │    │    └─weight                                            ├─81,920
│    │    │    └─bias                                              └─160
│    │    └─BatchNorm2d: 3-29            [1, 160, 14, 14]          320
│    │    │    └─weight                                            ├─160
│    │    │    └─bias                                              └─160
│    │    └─ReLU: 3-30                   [1, 160, 14, 14]          --
│    └─Sequential: 2-20                  [1, 224, 14, 14]          --
│    │    └─0.conv.weight                                          ├─57,344
│    │    └─0.conv.bias                                            ├─112
│    │    └─0.batch_norm.weight                                    ├─112
│    │    └─0.batch_norm.bias                                      ├─112
│    │    └─1.conv.weight                                          ├─225,792
│    │    └─1.conv.bias                                            ├─224
│    │    └─1.batch_norm.weight                                    ├─224
│    │    └─1.batch_norm.bias                                      └─224
│    │    └─conv_block: 3-31             [1, 112, 14, 14]          57,680
│    │    │    └─conv.weight                                       ├─57,344
│    │    │    └─conv.bias                                         ├─112
│    │    │    └─batch_norm.weight                                 ├─112
│    │    │    └─batch_norm.bias                                   └─112
│    │    └─conv_block: 3-32             [1, 224, 14, 14]          226,464
│    │    │    └─conv.weight                                       ├─225,792
│    │    │    └─conv.bias                                         ├─224
│    │    │    └─batch_norm.weight                                 ├─224
│    │    │    └─batch_norm.bias                                   └─224
│    └─Sequential: 2-21                  [1, 64, 14, 14]           --
│    │    └─0.conv.weight                                          ├─12,288
│    │    └─0.conv.bias                                            ├─24
│    │    └─0.batch_norm.weight                                    ├─24
│    │    └─0.batch_norm.bias                                      ├─24
│    │    └─1.conv.weight                                          ├─38,400
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─conv_block: 3-33             [1, 24, 14, 14]           12,360
│    │    │    └─conv.weight                                       ├─12,288
│    │    │    └─conv.bias                                         ├─24
│    │    │    └─batch_norm.weight                                 ├─24
│    │    │    └─batch_norm.bias                                   └─24
│    │    └─conv_block: 3-34             [1, 64, 14, 14]           38,592
│    │    │    └─conv.weight                                       ├─38,400
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
│    └─Sequential: 2-22                  [1, 64, 14, 14]           --
│    │    └─1.conv.weight                                          ├─32,768
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─MaxPool2d: 3-35              [1, 512, 14, 14]          --
│    │    └─conv_block: 3-36             [1, 64, 14, 14]           32,960
│    │    │    └─conv.weight                                       ├─32,768
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
├─inception_block: 1-10                  [1, 512, 14, 14]          --
│    └─branch1.conv.weight                                         ├─65,536
│    └─branch1.conv.bias                                           ├─128
│    └─branch1.batch_norm.weight                                   ├─128
│    └─branch1.batch_norm.bias                                     ├─128
│    └─branch2.0.conv.weight                                       ├─65,536
│    └─branch2.0.conv.bias                                         ├─128
│    └─branch2.0.batch_norm.weight                                 ├─128
│    └─branch2.0.batch_norm.bias                                   ├─128
│    └─branch2.1.conv.weight                                       ├─294,912
│    └─branch2.1.conv.bias                                         ├─256
│    └─branch2.1.batch_norm.weight                                 ├─256
│    └─branch2.1.batch_norm.bias                                   ├─256
│    └─branch3.0.conv.weight                                       ├─12,288
│    └─branch3.0.conv.bias                                         ├─24
│    └─branch3.0.batch_norm.weight                                 ├─24
│    └─branch3.0.batch_norm.bias                                   ├─24
│    └─branch3.1.conv.weight                                       ├─38,400
│    └─branch3.1.conv.bias                                         ├─64
│    └─branch3.1.batch_norm.weight                                 ├─64
│    └─branch3.1.batch_norm.bias                                   ├─64
│    └─branch4.1.conv.weight                                       ├─32,768
│    └─branch4.1.conv.bias                                         ├─64
│    └─branch4.1.batch_norm.weight                                 ├─64
│    └─branch4.1.batch_norm.bias                                   └─64
│    └─conv_block: 2-23                  [1, 128, 14, 14]          --
│    │    └─conv.weight                                            ├─65,536
│    │    └─conv.bias                                              ├─128
│    │    └─batch_norm.weight                                      ├─128
│    │    └─batch_norm.bias                                        └─128
│    │    └─Conv2d: 3-37                 [1, 128, 14, 14]          65,664
│    │    │    └─weight                                            ├─65,536
│    │    │    └─bias                                              └─128
│    │    └─BatchNorm2d: 3-38            [1, 128, 14, 14]          256
│    │    │    └─weight                                            ├─128
│    │    │    └─bias                                              └─128
│    │    └─ReLU: 3-39                   [1, 128, 14, 14]          --
│    └─Sequential: 2-24                  [1, 256, 14, 14]          --
│    │    └─0.conv.weight                                          ├─65,536
│    │    └─0.conv.bias                                            ├─128
│    │    └─0.batch_norm.weight                                    ├─128
│    │    └─0.batch_norm.bias                                      ├─128
│    │    └─1.conv.weight                                          ├─294,912
│    │    └─1.conv.bias                                            ├─256
│    │    └─1.batch_norm.weight                                    ├─256
│    │    └─1.batch_norm.bias                                      └─256
│    │    └─conv_block: 3-40             [1, 128, 14, 14]          65,920
│    │    │    └─conv.weight                                       ├─65,536
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
│    │    └─conv_block: 3-41             [1, 256, 14, 14]          295,680
│    │    │    └─conv.weight                                       ├─294,912
│    │    │    └─conv.bias                                         ├─256
│    │    │    └─batch_norm.weight                                 ├─256
│    │    │    └─batch_norm.bias                                   └─256
│    └─Sequential: 2-25                  [1, 64, 14, 14]           --
│    │    └─0.conv.weight                                          ├─12,288
│    │    └─0.conv.bias                                            ├─24
│    │    └─0.batch_norm.weight                                    ├─24
│    │    └─0.batch_norm.bias                                      ├─24
│    │    └─1.conv.weight                                          ├─38,400
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─conv_block: 3-42             [1, 24, 14, 14]           12,360
│    │    │    └─conv.weight                                       ├─12,288
│    │    │    └─conv.bias                                         ├─24
│    │    │    └─batch_norm.weight                                 ├─24
│    │    │    └─batch_norm.bias                                   └─24
│    │    └─conv_block: 3-43             [1, 64, 14, 14]           38,592
│    │    │    └─conv.weight                                       ├─38,400
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
│    └─Sequential: 2-26                  [1, 64, 14, 14]           --
│    │    └─1.conv.weight                                          ├─32,768
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─MaxPool2d: 3-44              [1, 512, 14, 14]          --
│    │    └─conv_block: 3-45             [1, 64, 14, 14]           32,960
│    │    │    └─conv.weight                                       ├─32,768
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
├─inception_block: 1-11                  [1, 528, 14, 14]          --
│    └─branch1.conv.weight                                         ├─57,344
│    └─branch1.conv.bias                                           ├─112
│    └─branch1.batch_norm.weight                                   ├─112
│    └─branch1.batch_norm.bias                                     ├─112
│    └─branch2.0.conv.weight                                       ├─73,728
│    └─branch2.0.conv.bias                                         ├─144
│    └─branch2.0.batch_norm.weight                                 ├─144
│    └─branch2.0.batch_norm.bias                                   ├─144
│    └─branch2.1.conv.weight                                       ├─373,248
│    └─branch2.1.conv.bias                                         ├─288
│    └─branch2.1.batch_norm.weight                                 ├─288
│    └─branch2.1.batch_norm.bias                                   ├─288
│    └─branch3.0.conv.weight                                       ├─16,384
│    └─branch3.0.conv.bias                                         ├─32
│    └─branch3.0.batch_norm.weight                                 ├─32
│    └─branch3.0.batch_norm.bias                                   ├─32
│    └─branch3.1.conv.weight                                       ├─51,200
│    └─branch3.1.conv.bias                                         ├─64
│    └─branch3.1.batch_norm.weight                                 ├─64
│    └─branch3.1.batch_norm.bias                                   ├─64
│    └─branch4.1.conv.weight                                       ├─32,768
│    └─branch4.1.conv.bias                                         ├─64
│    └─branch4.1.batch_norm.weight                                 ├─64
│    └─branch4.1.batch_norm.bias                                   └─64
│    └─conv_block: 2-27                  [1, 112, 14, 14]          --
│    │    └─conv.weight                                            ├─57,344
│    │    └─conv.bias                                              ├─112
│    │    └─batch_norm.weight                                      ├─112
│    │    └─batch_norm.bias                                        └─112
│    │    └─Conv2d: 3-46                 [1, 112, 14, 14]          57,456
│    │    │    └─weight                                            ├─57,344
│    │    │    └─bias                                              └─112
│    │    └─BatchNorm2d: 3-47            [1, 112, 14, 14]          224
│    │    │    └─weight                                            ├─112
│    │    │    └─bias                                              └─112
│    │    └─ReLU: 3-48                   [1, 112, 14, 14]          --
│    └─Sequential: 2-28                  [1, 288, 14, 14]          --
│    │    └─0.conv.weight                                          ├─73,728
│    │    └─0.conv.bias                                            ├─144
│    │    └─0.batch_norm.weight                                    ├─144
│    │    └─0.batch_norm.bias                                      ├─144
│    │    └─1.conv.weight                                          ├─373,248
│    │    └─1.conv.bias                                            ├─288
│    │    └─1.batch_norm.weight                                    ├─288
│    │    └─1.batch_norm.bias                                      └─288
│    │    └─conv_block: 3-49             [1, 144, 14, 14]          74,160
│    │    │    └─conv.weight                                       ├─73,728
│    │    │    └─conv.bias                                         ├─144
│    │    │    └─batch_norm.weight                                 ├─144
│    │    │    └─batch_norm.bias                                   └─144
│    │    └─conv_block: 3-50             [1, 288, 14, 14]          374,112
│    │    │    └─conv.weight                                       ├─373,248
│    │    │    └─conv.bias                                         ├─288
│    │    │    └─batch_norm.weight                                 ├─288
│    │    │    └─batch_norm.bias                                   └─288
│    └─Sequential: 2-29                  [1, 64, 14, 14]           --
│    │    └─0.conv.weight                                          ├─16,384
│    │    └─0.conv.bias                                            ├─32
│    │    └─0.batch_norm.weight                                    ├─32
│    │    └─0.batch_norm.bias                                      ├─32
│    │    └─1.conv.weight                                          ├─51,200
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─conv_block: 3-51             [1, 32, 14, 14]           16,480
│    │    │    └─conv.weight                                       ├─16,384
│    │    │    └─conv.bias                                         ├─32
│    │    │    └─batch_norm.weight                                 ├─32
│    │    │    └─batch_norm.bias                                   └─32
│    │    └─conv_block: 3-52             [1, 64, 14, 14]           51,392
│    │    │    └─conv.weight                                       ├─51,200
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
│    └─Sequential: 2-30                  [1, 64, 14, 14]           --
│    │    └─1.conv.weight                                          ├─32,768
│    │    └─1.conv.bias                                            ├─64
│    │    └─1.batch_norm.weight                                    ├─64
│    │    └─1.batch_norm.bias                                      └─64
│    │    └─MaxPool2d: 3-53              [1, 512, 14, 14]          --
│    │    └─conv_block: 3-54             [1, 64, 14, 14]           32,960
│    │    │    └─conv.weight                                       ├─32,768
│    │    │    └─conv.bias                                         ├─64
│    │    │    └─batch_norm.weight                                 ├─64
│    │    │    └─batch_norm.bias                                   └─64
├─inception_block: 1-12                  [1, 832, 14, 14]          --
│    └─branch1.conv.weight                                         ├─135,168
│    └─branch1.conv.bias                                           ├─256
│    └─branch1.batch_norm.weight                                   ├─256
│    └─branch1.batch_norm.bias                                     ├─256
│    └─branch2.0.conv.weight                                       ├─84,480
│    └─branch2.0.conv.bias                                         ├─160
│    └─branch2.0.batch_norm.weight                                 ├─160
│    └─branch2.0.batch_norm.bias                                   ├─160
│    └─branch2.1.conv.weight                                       ├─460,800
│    └─branch2.1.conv.bias                                         ├─320
│    └─branch2.1.batch_norm.weight                                 ├─320
│    └─branch2.1.batch_norm.bias                                   ├─320
│    └─branch3.0.conv.weight                                       ├─16,896
│    └─branch3.0.conv.bias                                         ├─32
│    └─branch3.0.batch_norm.weight                                 ├─32
│    └─branch3.0.batch_norm.bias                                   ├─32
│    └─branch3.1.conv.weight                                       ├─102,400
│    └─branch3.1.conv.bias                                         ├─128
│    └─branch3.1.batch_norm.weight                                 ├─128
│    └─branch3.1.batch_norm.bias                                   ├─128
│    └─branch4.1.conv.weight                                       ├─67,584
│    └─branch4.1.conv.bias                                         ├─128
│    └─branch4.1.batch_norm.weight                                 ├─128
│    └─branch4.1.batch_norm.bias                                   └─128
│    └─conv_block: 2-31                  [1, 256, 14, 14]          --
│    │    └─conv.weight                                            ├─135,168
│    │    └─conv.bias                                              ├─256
│    │    └─batch_norm.weight                                      ├─256
│    │    └─batch_norm.bias                                        └─256
│    │    └─Conv2d: 3-55                 [1, 256, 14, 14]          135,424
│    │    │    └─weight                                            ├─135,168
│    │    │    └─bias                                              └─256
│    │    └─BatchNorm2d: 3-56            [1, 256, 14, 14]          512
│    │    │    └─weight                                            ├─256
│    │    │    └─bias                                              └─256
│    │    └─ReLU: 3-57                   [1, 256, 14, 14]          --
│    └─Sequential: 2-32                  [1, 320, 14, 14]          --
│    │    └─0.conv.weight                                          ├─84,480
│    │    └─0.conv.bias                                            ├─160
│    │    └─0.batch_norm.weight                                    ├─160
│    │    └─0.batch_norm.bias                                      ├─160
│    │    └─1.conv.weight                                          ├─460,800
│    │    └─1.conv.bias                                            ├─320
│    │    └─1.batch_norm.weight                                    ├─320
│    │    └─1.batch_norm.bias                                      └─320
│    │    └─conv_block: 3-58             [1, 160, 14, 14]          84,960
│    │    │    └─conv.weight                                       ├─84,480
│    │    │    └─conv.bias                                         ├─160
│    │    │    └─batch_norm.weight                                 ├─160
│    │    │    └─batch_norm.bias                                   └─160
│    │    └─conv_block: 3-59             [1, 320, 14, 14]          461,760
│    │    │    └─conv.weight                                       ├─460,800
│    │    │    └─conv.bias                                         ├─320
│    │    │    └─batch_norm.weight                                 ├─320
│    │    │    └─batch_norm.bias                                   └─320
│    └─Sequential: 2-33                  [1, 128, 14, 14]          --
│    │    └─0.conv.weight                                          ├─16,896
│    │    └─0.conv.bias                                            ├─32
│    │    └─0.batch_norm.weight                                    ├─32
│    │    └─0.batch_norm.bias                                      ├─32
│    │    └─1.conv.weight                                          ├─102,400
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─conv_block: 3-60             [1, 32, 14, 14]           16,992
│    │    │    └─conv.weight                                       ├─16,896
│    │    │    └─conv.bias                                         ├─32
│    │    │    └─batch_norm.weight                                 ├─32
│    │    │    └─batch_norm.bias                                   └─32
│    │    └─conv_block: 3-61             [1, 128, 14, 14]          102,784
│    │    │    └─conv.weight                                       ├─102,400
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
│    └─Sequential: 2-34                  [1, 128, 14, 14]          --
│    │    └─1.conv.weight                                          ├─67,584
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─MaxPool2d: 3-62              [1, 528, 14, 14]          --
│    │    └─conv_block: 3-63             [1, 128, 14, 14]          67,968
│    │    │    └─conv.weight                                       ├─67,584
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
├─MaxPool2d: 1-13                        [1, 832, 7, 7]            --
├─inception_block: 1-14                  [1, 832, 7, 7]            --
│    └─branch1.conv.weight                                         ├─212,992
│    └─branch1.conv.bias                                           ├─256
│    └─branch1.batch_norm.weight                                   ├─256
│    └─branch1.batch_norm.bias                                     ├─256
│    └─branch2.0.conv.weight                                       ├─133,120
│    └─branch2.0.conv.bias                                         ├─160
│    └─branch2.0.batch_norm.weight                                 ├─160
│    └─branch2.0.batch_norm.bias                                   ├─160
│    └─branch2.1.conv.weight                                       ├─460,800
│    └─branch2.1.conv.bias                                         ├─320
│    └─branch2.1.batch_norm.weight                                 ├─320
│    └─branch2.1.batch_norm.bias                                   ├─320
│    └─branch3.0.conv.weight                                       ├─26,624
│    └─branch3.0.conv.bias                                         ├─32
│    └─branch3.0.batch_norm.weight                                 ├─32
│    └─branch3.0.batch_norm.bias                                   ├─32
│    └─branch3.1.conv.weight                                       ├─102,400
│    └─branch3.1.conv.bias                                         ├─128
│    └─branch3.1.batch_norm.weight                                 ├─128
│    └─branch3.1.batch_norm.bias                                   ├─128
│    └─branch4.1.conv.weight                                       ├─106,496
│    └─branch4.1.conv.bias                                         ├─128
│    └─branch4.1.batch_norm.weight                                 ├─128
│    └─branch4.1.batch_norm.bias                                   └─128
│    └─conv_block: 2-35                  [1, 256, 7, 7]            --
│    │    └─conv.weight                                            ├─212,992
│    │    └─conv.bias                                              ├─256
│    │    └─batch_norm.weight                                      ├─256
│    │    └─batch_norm.bias                                        └─256
│    │    └─Conv2d: 3-64                 [1, 256, 7, 7]            213,248
│    │    │    └─weight                                            ├─212,992
│    │    │    └─bias                                              └─256
│    │    └─BatchNorm2d: 3-65            [1, 256, 7, 7]            512
│    │    │    └─weight                                            ├─256
│    │    │    └─bias                                              └─256
│    │    └─ReLU: 3-66                   [1, 256, 7, 7]            --
│    └─Sequential: 2-36                  [1, 320, 7, 7]            --
│    │    └─0.conv.weight                                          ├─133,120
│    │    └─0.conv.bias                                            ├─160
│    │    └─0.batch_norm.weight                                    ├─160
│    │    └─0.batch_norm.bias                                      ├─160
│    │    └─1.conv.weight                                          ├─460,800
│    │    └─1.conv.bias                                            ├─320
│    │    └─1.batch_norm.weight                                    ├─320
│    │    └─1.batch_norm.bias                                      └─320
│    │    └─conv_block: 3-67             [1, 160, 7, 7]            133,600
│    │    │    └─conv.weight                                       ├─133,120
│    │    │    └─conv.bias                                         ├─160
│    │    │    └─batch_norm.weight                                 ├─160
│    │    │    └─batch_norm.bias                                   └─160
│    │    └─conv_block: 3-68             [1, 320, 7, 7]            461,760
│    │    │    └─conv.weight                                       ├─460,800
│    │    │    └─conv.bias                                         ├─320
│    │    │    └─batch_norm.weight                                 ├─320
│    │    │    └─batch_norm.bias                                   └─320
│    └─Sequential: 2-37                  [1, 128, 7, 7]            --
│    │    └─0.conv.weight                                          ├─26,624
│    │    └─0.conv.bias                                            ├─32
│    │    └─0.batch_norm.weight                                    ├─32
│    │    └─0.batch_norm.bias                                      ├─32
│    │    └─1.conv.weight                                          ├─102,400
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─conv_block: 3-69             [1, 32, 7, 7]             26,720
│    │    │    └─conv.weight                                       ├─26,624
│    │    │    └─conv.bias                                         ├─32
│    │    │    └─batch_norm.weight                                 ├─32
│    │    │    └─batch_norm.bias                                   └─32
│    │    └─conv_block: 3-70             [1, 128, 7, 7]            102,784
│    │    │    └─conv.weight                                       ├─102,400
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
│    └─Sequential: 2-38                  [1, 128, 7, 7]            --
│    │    └─1.conv.weight                                          ├─106,496
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─MaxPool2d: 3-71              [1, 832, 7, 7]            --
│    │    └─conv_block: 3-72             [1, 128, 7, 7]            106,880
│    │    │    └─conv.weight                                       ├─106,496
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
├─inception_block: 1-15                  [1, 1024, 7, 7]           --
│    └─branch1.conv.weight                                         ├─319,488
│    └─branch1.conv.bias                                           ├─384
│    └─branch1.batch_norm.weight                                   ├─384
│    └─branch1.batch_norm.bias                                     ├─384
│    └─branch2.0.conv.weight                                       ├─159,744
│    └─branch2.0.conv.bias                                         ├─192
│    └─branch2.0.batch_norm.weight                                 ├─192
│    └─branch2.0.batch_norm.bias                                   ├─192
│    └─branch2.1.conv.weight                                       ├─663,552
│    └─branch2.1.conv.bias                                         ├─384
│    └─branch2.1.batch_norm.weight                                 ├─384
│    └─branch2.1.batch_norm.bias                                   ├─384
│    └─branch3.0.conv.weight                                       ├─39,936
│    └─branch3.0.conv.bias                                         ├─48
│    └─branch3.0.batch_norm.weight                                 ├─48
│    └─branch3.0.batch_norm.bias                                   ├─48
│    └─branch3.1.conv.weight                                       ├─153,600
│    └─branch3.1.conv.bias                                         ├─128
│    └─branch3.1.batch_norm.weight                                 ├─128
│    └─branch3.1.batch_norm.bias                                   ├─128
│    └─branch4.1.conv.weight                                       ├─106,496
│    └─branch4.1.conv.bias                                         ├─128
│    └─branch4.1.batch_norm.weight                                 ├─128
│    └─branch4.1.batch_norm.bias                                   └─128
│    └─conv_block: 2-39                  [1, 384, 7, 7]            --
│    │    └─conv.weight                                            ├─319,488
│    │    └─conv.bias                                              ├─384
│    │    └─batch_norm.weight                                      ├─384
│    │    └─batch_norm.bias                                        └─384
│    │    └─Conv2d: 3-73                 [1, 384, 7, 7]            319,872
│    │    │    └─weight                                            ├─319,488
│    │    │    └─bias                                              └─384
│    │    └─BatchNorm2d: 3-74            [1, 384, 7, 7]            768
│    │    │    └─weight                                            ├─384
│    │    │    └─bias                                              └─384
│    │    └─ReLU: 3-75                   [1, 384, 7, 7]            --
│    └─Sequential: 2-40                  [1, 384, 7, 7]            --
│    │    └─0.conv.weight                                          ├─159,744
│    │    └─0.conv.bias                                            ├─192
│    │    └─0.batch_norm.weight                                    ├─192
│    │    └─0.batch_norm.bias                                      ├─192
│    │    └─1.conv.weight                                          ├─663,552
│    │    └─1.conv.bias                                            ├─384
│    │    └─1.batch_norm.weight                                    ├─384
│    │    └─1.batch_norm.bias                                      └─384
│    │    └─conv_block: 3-76             [1, 192, 7, 7]            160,320
│    │    │    └─conv.weight                                       ├─159,744
│    │    │    └─conv.bias                                         ├─192
│    │    │    └─batch_norm.weight                                 ├─192
│    │    │    └─batch_norm.bias                                   └─192
│    │    └─conv_block: 3-77             [1, 384, 7, 7]            664,704
│    │    │    └─conv.weight                                       ├─663,552
│    │    │    └─conv.bias                                         ├─384
│    │    │    └─batch_norm.weight                                 ├─384
│    │    │    └─batch_norm.bias                                   └─384
│    └─Sequential: 2-41                  [1, 128, 7, 7]            --
│    │    └─0.conv.weight                                          ├─39,936
│    │    └─0.conv.bias                                            ├─48
│    │    └─0.batch_norm.weight                                    ├─48
│    │    └─0.batch_norm.bias                                      ├─48
│    │    └─1.conv.weight                                          ├─153,600
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─conv_block: 3-78             [1, 48, 7, 7]             40,080
│    │    │    └─conv.weight                                       ├─39,936
│    │    │    └─conv.bias                                         ├─48
│    │    │    └─batch_norm.weight                                 ├─48
│    │    │    └─batch_norm.bias                                   └─48
│    │    └─conv_block: 3-79             [1, 128, 7, 7]            153,984
│    │    │    └─conv.weight                                       ├─153,600
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
│    └─Sequential: 2-42                  [1, 128, 7, 7]            --
│    │    └─1.conv.weight                                          ├─106,496
│    │    └─1.conv.bias                                            ├─128
│    │    └─1.batch_norm.weight                                    ├─128
│    │    └─1.batch_norm.bias                                      └─128
│    │    └─MaxPool2d: 3-80              [1, 832, 7, 7]            --
│    │    └─conv_block: 3-81             [1, 128, 7, 7]            106,880
│    │    │    └─conv.weight                                       ├─106,496
│    │    │    └─conv.bias                                         ├─128
│    │    │    └─batch_norm.weight                                 ├─128
│    │    │    └─batch_norm.bias                                   └─128
├─AvgPool2d: 1-16                        [1, 1024, 1, 1]           --
├─Dropout: 1-17                          [1, 1024]                 --
├─Linear: 1-18                           [1, 1000]                 1,025,000
│    └─weight                                                      ├─1,024,000
│    └─bias                                                        └─1,000
==========================================================================================
Total params: 7,008,824
Trainable params: 7,008,824
Non-trainable params: 0
Total mult-adds (Units.GIGABYTES): 1.57
==========================================================================================
Input size (MB): 0.60
Forward/backward pass size (MB): 48.42
Params size (MB): 28.04
Estimated Total Size (MB): 77.05
==========================================================================================
```