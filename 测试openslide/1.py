import openslide
import matplotlib.pyplot as plt
# imgpath = r'E:\Code_library\测试openslide\11327473-2921-4916-a111-89d0eda6be8a\TCGA-A8-A06U-01A-01-TS1.63824040-373f-4c6c-a74e-881c127567a6.svs'
# imgpath = r'E:\Code_library\测试openslide\fffe77c5-f700-4ebf-b255-ecfee17bafe6\TCGA-52-7810-01A-01-BS1.ce43c735-840c-4f4a-88d3-d79b66d666d8.svs'
if __name__ == "__main__":
    imgpath = r'E:\Code_library\测试openslide\fb7c1578-f608-454b-bd48-caed5e768afb\TCGA-CW-6096-11A-01-TS1.aec08c0c-53bc-4174-a22e-cbe279f2db2d.svs'
    slide = openslide.OpenSlide(imgpath)


    from openslide.deepzoom import DeepZoomGenerator
    #实现DeepZoomGenerator的功能
    data_gen = DeepZoomGenerator(slide, tile_size=1023, overlap=1, limit_bounds=False)

    #Return an RGB Image for a tile.
    #level (int):the Deep Zoom level
    #address (tuple):  the address of the tile within the level as a (column, row) tuple


    tile_img1 = data_gen.get_tile(11,(0,0))
    tile_img2 = data_gen.get_tile(11,(0,1))
    plt.figure()
    plt.imshow(tile_img1)
    plt.show()

    plt.figure()
    plt.imshow(tile_img2)
    plt.show()

    print('done')