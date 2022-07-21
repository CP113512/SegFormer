import numpy as np
import matplotlib.pyplot as plt
# 标签
classes=['0','1',' 2', '3','4', '5']

# 标签的个数
classNamber=6 #表情的数量

# 在标签中的矩阵
confusion_matrix = np.array([[0, 0, 0, 0, 0, 0], [0, 12, 0, 0, 0, 0], [0, 1, 20, 10, 2, 0], [0, 0, 0, 28, 5, 1], [0, 0, 0, 2, 9, 0], [0, 0, 0, 0, 0, 2]]
                            ,dtype=np.float64)

plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.GnBu)  #按照像素显示出矩阵
plt.title('混淆矩阵')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=-45)
plt.yticks(tick_marks, classes)

thresh = confusion_matrix.max() / 2.
#iters = [[i,j] for i in range(len(classes)) for j in range((classes))]
#ij配对，遍历矩阵迭代器
iters = np.reshape([[[i,j] for j in range(classNamber)] for i in range(classNamber)],(confusion_matrix.size,2))
for i, j in iters:
    plt.text(j, i, format(confusion_matrix[i, j]),va='center',ha='center')   #显示对应的数字

plt.ylabel('预测标签')
plt.xlabel('真实标签')
plt.tight_layout()
plt.show()