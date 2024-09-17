# 提取testing数据库数据

import os
import pandas as pd
from radiomics import featureextractor as FEE

def main(zero: str, ichi: str, ni: str, san: int, yon: int, go, roku: bool):
    file_path= ''.join(('database\\', zero))
    # file_path= r'database\testing'
    settings= {}
    settings['binWidth'] = 8
    settings['label']= san
    settings['resampledPixelSpacing']= [3, 3, 3]
    settings['normalize']= True
    # settings['normalizeScale']= 2
    extractor= FEE.RadiomicsFeatureExtractor(**settings)
    extractor.disableAllFeatures()
    if ichi == 'shape':
        extractor.enableFeaturesByName(shape= [ni])
    elif ichi == 'glcm':
        extractor.enableFeaturesByName(glcm= [ni])
    df= pd.DataFrame()
    for root, dirs, files in os.walk(file_path):
        ori_path= None
        lab_path= None
        for file in files:
            file_path= os.path.join(root, file) 
            if yon == 1:
                if file.endswith('01.nii.gz'):
                    ori_path= file_path
                elif file.endswith('01_gt.nii.gz'):
                    lab_path= file_path
            elif yon == 2:
                if file.endswith(".nii.gz") and not file.endswith('_gt.nii.gz') and not file.endswith("01.nii.gz") and not file.endswith('4d.nii.gz'):
                    ori_path= file_path
                elif file.endswith("_gt.nii.gz") and not file.endswith("01_gt.nii.gz") and not file.endswith('4d.nii.gz'):
                    lab_path= file_path
            # print("{}\n{}\n{}".format(file_path, ori_path, lab_path))
            if ori_path and lab_path != None:
                result= extractor.execute(ori_path, lab_path)
                if ichi == 'shape':
                    kol= "".join(('original_shape_', ni))
                elif ichi == 'glcm':
                    kol= "".join(('original_glcm_', ni))
                selected_features= [kol]
                for key, value in result.items():
                    if key in selected_features:
                        df = pd.concat([df, pd.DataFrame({key: [value]})], ignore_index= True)
                ori_path= None
                lab_path= None
    output_path= ''.join(('testing3\\result', str(go), '.csv'))
    # output_path= r'testing3\result1.csv'
    df.to_csv(output_path, index= roku)
    print("Saved!")
    
if __name__ == '__main__':
    # main('testing', 'shape', 'MeshVolume', 2, 1, 1)
    # main('testing', 'shape', 'SurfaceVolumeRatio', 3, 2, 2)
    # main('testing', 'shape', 'LeastAxisLength', 3, 2, 3)
    # main('testing', 'shape', 'Maximum3DDiameter', 1, 2, 5)
    # main('testing', 'glcm', 'Id', 1, 2, 6)
    # main('testing', 'shape', 'Compactness2', 3, 2, 7)
    # main('testing', 'shape', 'Maximum3DDiameter', 2, 2, 8)
    # main('testing', 'shape', 'SurfaceArea', 1, 1, 9)
    # main('testing', 'shape', 'MeshVolume', 1, 1, 10, False)
    # main('testing', 'shape', 'MeshVolume', 1, 2, 11, False)
    # main('testing', 'shape', 'MeshVolume', 3, 1, 12, False)
    # main('testing', 'shape', 'MeshVolume', 3, 2, 13, False)
    main('testing', 'shape', 'MeshVolume', 2, 2, 1.1, False)