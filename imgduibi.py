import cv2
 # 读取第一张图片
image1 = cv2.imread('image1.jpg')
# 读取第二张图片
image2 = cv2.imread('image2.jpg')
 # 将图片转换为灰度图像
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
 # 使用ORB算法检测特征点
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(gray_image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray_image2, None)
 # 使用BFMatcher进行特征点匹配
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)
 # 根据匹配结果计算匹配度
matching_score = len(matches) / max(len(keypoints1), len(keypoints2))
 # 打印匹配度
print("Matching score: ", matching_score)