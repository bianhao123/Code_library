# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/10/26 16:39:24
@Author  :   bian hao
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   这是一个可以自动下载TCGA数据集的脚本。只要指定gdc-client的路径，manifest的路径即可。
             用法：python main.py --gdc /home/bianhao/gdc-client /data/bianhao/tcga_segmentation
'''

import logging
import os
import subprocess
from tqdm import tqdm
import sys


def get_logger(filename_handler, verbose=False):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # file handler
        fh = logging.FileHandler(filename_handler)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG if verbose else logging.INFO)
        formatter = logging.Formatter('%(levelname)s     %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


def download_svs_files(source_folder, gdc_executable_path):
    assert os.path.exists(gdc_executable_path), "GDC executable not found at location %s" % gdc_executable_path

    # Retrieve files of the input folder, and seek the manifest file to be processed by GDC tool
    files = list(map(lambda x: os.path.abspath(os.path.join(source_folder, x)),
                     os.listdir(source_folder)))
    files = list(filter(os.path.isfile, files))
    manifest_file = [f for f in files if 'manifest' in f.lower()]
    assert len(manifest_file) == 1, 'found %d manifest files, expected 1' % len(manifest_file)
    manifest_file = manifest_file[0]

    # Compute output dir: put all downloaded content in source folder
    output_dir = os.path.dirname(manifest_file)

    # Opens manifest and retrieves the ids to be retrieved
    with open(manifest_file, 'r') as f:
        lines = f.read().splitlines()
    cells = [line.split('\t') for line in lines[1:]]
    ids = [cell[0] for cell in cells]
    filenames = [cell[1] for cell in cells]
    md5sums = [cell[2] for cell in cells]
    N_PROCESSES = 5

    # Extract patient id based on SVS names
    cases_ids = ['-'.join(filename.split('-')[:3]) for filename in filenames]

    for file_id in tqdm(ids):
        # Download file if not already downloaded
        if not os.path.exists(os.path.join(output_dir, file_id)):
            subprocess.check_output([gdc_executable_path, 'download', '--dir', output_dir,
                                     '--n-processes', str(N_PROCESSES), file_id])

    # Infer resulting SVS filepaths from output_dir, id and filename of files
    resulting_svs_filepaths = [os.path.abspath(os.path.join(output_dir, id_file, filename))
                               for id_file, filename in zip(ids, filenames)]

    assert len(resulting_svs_filepaths) == len(ids) == len(md5sums) == len(cases_ids)

    return resulting_svs_filepaths, md5sums, cases_ids


def main(source_folder, output_folder, gdc_executable_path):
    logger = get_logger(filename_handler='data_processing.log', verbose=True)
    logger.info('Source folder %s' % os.path.abspath(source_folder) if source_folder else 'None')
    logger.info('Output folder %s' % os.path.abspath(output_folder))
    logger.info('Meta-parameters:')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download SVS files using manifest and GDC extraction tool
    if not os.path.exists(os.path.join(output_folder, 'has_been_downloaded')):
        logger.info('Downloading slides...')
        svs_filepaths, md5sums, cases_ids = download_svs_files(source_folder, gdc_executable_path)

        # Write control file after download is finished
        with open(os.path.join(output_folder, 'has_been_downloaded'), 'w') as f:
            f.write('\n'.join(','.join(a) for a in zip(svs_filepaths, md5sums, cases_ids)))
        logger.info('  done')
    else:
        logger.info('Slides already downloaded -> skipping')


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: python main.py --gdc-executable gdc_executable_path '
              'source_folder_containing_manifest')
        exit(-1)
    gdc_client = sys.argv[-2]
    source_folder = sys.argv[-1]
    output_folder = os.path.join(source_folder, 'preprocessed')
    main(source_folder, output_folder, gdc_client)
