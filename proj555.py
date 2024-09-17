# 使用random forest算法分类，分别使用了纯影像组学数据（注释掉的部分）和基于影像组学提取的心室体积和射血分数的数据。
# 在前一种模型中，实现了0.84的准确率；而在后一种模型中实现了0.96的准确率，并绘制了该模型的混淆矩阵。
# random forest分类器在默认条件下即可达到最佳效果。

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.svm import SVC
# from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score

# svc= SVC(C= 12, gamma= 6) # 未重采样
# svc= SVC(C= 25, gamma= 6) # 重采样[3, 3, 3]
rfc= RandomForestClassifier(random_state= 0)
pql= pd.read_csv(r'training3\sumup1.csv')
lpo= pd.read_csv(r'testing3\sumup2.csv')

# 选择需要的列并转换为numpy数组
# columns_of_interest_1 = ['original_shape_MeshVolume1', 'original_shape_SurfaceVolumeRatio', 'original_shape_LeastAxisLength', 'original_shape_Maximum3DDiameter1', 'original_glcm_Id', 'original_shape_Compactness2', 'original_shape_Maximum3DDiameter2', 'original_shape_SurfaceArea', 'Height','Result']
columns_of_interest_1 = ['original_shape_MeshVolume1', 'original_shape_MeshVolume2','original_shape_MeshVolume3','original_shape_MeshVolume4','original_shape_MeshVolume5','original_shape_MeshVolume6','RVEF','LVEF','Height','Result']

# 提取指定列并转换为numpy数组
training_data_1= pql[columns_of_interest_1].to_numpy()
testing_data_1= lpo[columns_of_interest_1].to_numpy()

# 返回数据的形状以确认正确加载
# print(training_data_1.shape)

columns_of_interest_2= ['Result']

training_data_2= pql[columns_of_interest_2].to_numpy()
testing_data_2= lpo[columns_of_interest_2].to_numpy()

# print(training_data_2.shape)

# scaler = MinMaxScaler()
# scaler.fit(training_data_1)
# training_data_x= scaler.transform(training_data_1)
# testing_data_x= scaler.transform(testing_data_1)

# svc.fit(training_data_x, training_data_2.ravel())
rfc.fit(training_data_1, training_data_2.ravel())

print("training: {}\ntesting: {}".format(rfc.score(training_data_1, training_data_2.ravel()),\
    rfc.score(testing_data_1, testing_data_2.ravel())))

# print(confusion_matrix(testing_data_2, rfc.predict(testing_data_1)))
# Generate confusion matrix
y1= testing_data_2
y2= rfc.predict(testing_data_1)
cm = confusion_matrix(y1, y2, labels=[1, 2, 3, 4, 5])

# Define the labels for x and y axes
labels = ['NOR', 'DCM', 'HCM', 'MINF', 'RV']

# Create a heatmap with seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Oranges", xticklabels=labels, yticklabels=labels)

# Set labels, title, and show the plot
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

print(roc_auc_score(testing_data_2, rfc.predict_proba(testing_data_1), multi_class= 'ovr'))