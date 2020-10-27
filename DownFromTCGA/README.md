这是一个可以自动下载TCGA数据集的脚本。下载过的文件不会重复下载，避免网络不佳的情况。

指定gdc-client的路径、manifest文件的路径即可。

source_folder = /data/bianhao/tcga_segmentation

gdc_executable_path = /home/bianhao/gdc-client

```shell./download.sh /home/bianhao/gdc-client /data/bianhao/tcga_segmentation
./download.sh /home/bianhao/gdc-client /data/bianhao/tcga_segmentation
```

