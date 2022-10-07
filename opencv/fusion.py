# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

def sift_keypoints_detect(image):
    # 将图像转换为灰度图
    grayImg = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    sift = cv.xfeatures2d.SIFT_create()                
    
    # keypoints:特征点向量,向量内的每一个元素是一个KeyPoint对象，包含了特征点的各种属性信息(角度、关键点坐标等)
    # features:表示输出的sift特征向量，通常是128维的
    keypoints, features = sift.detectAndCompute(image, None)
    
    # cv.drawKeyPoints():在关键点处绘制一个小圆圈
    # 如果传递标志flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,它将绘制一个大小为keypoint的圆圈并显示它的方向
    # 这种方法同时显示图像的坐标，size和方向，是最能显示特征的一种绘制方式
    keypoints_image = cv.drawKeypoints(
        grayImg, keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    
    # 返回带关键点的图像、关键点和sift的特征向量
    return keypoints_image, keypoints, features


# 使用KNN检测来自左右图像的SIFT特征，随后进行匹配
def get_feature_point_ensemble(features_right, features_left):
    # 创建BFMatcher对象解决匹配
    bf = cv.BFMatcher()
    # knnMatch()函数：返回每个特征点的最佳匹配k个匹配点
    matches = bf.knnMatch(features_right, features_left, k=2)  # des1为模板图，des2为匹配图
    # 利用sorted()函数对matches对象进行升序(默认)操作
    matches = sorted(matches, key=lambda x: x[0].distance / x[1].distance)
    # x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序

    # 建立列表good用于存储匹配的点集
    good = []
    for m, n in matches:# ratio的值越大，匹配的线条越密集，但错误匹配点也会增多
        ratio=0.6
        if m.distance < ratio * n.distance:
            good.append(m)
    return good


# 计算视角变换矩阵H，用H对右图进行变换并返回全景拼接图像
def Panorama_stitching(image_right, image_left):
    _, keypoints_right, features_right = sift_keypoints_detect(image_right)
    _, keypoints_left, features_left = sift_keypoints_detect(image_left)
    goodMatch = get_feature_point_ensemble(features_right, features_left)

    # 当筛选项的匹配对大于4对(因为homography单应性矩阵的计算需要至少四个点)时,计算视角变换矩阵
    if len(goodMatch) > 4:
        # 获取匹配对的点坐标
        ptsR = np.float32(
            [keypoints_right[m.queryIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
        ptsL = np.float32(
            [keypoints_left[m.trainIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
        
        # ransacReprojThreshold：将点对视为内点的最大允许重投影错误阈值(仅用于RANSAC和RHO方法时),若srcPoints和dstPoints是以像素为单位的，该参数通常设置在1到10的范围内
        ransacReprojThreshold = 4
        
        # cv.findHomography():计算多个二维点对之间的最优单映射变换矩阵 H(3行x3列),使用最小均方误差或者RANSAC方法
        # 函数作用:利用基于RANSAC的鲁棒算法选择最优的四组配对点，再计算转换矩阵H(3*3)并返回,以便于反向投影错误率达到最小
        Homography, status = cv.findHomography(
            ptsR, ptsL, cv.RANSAC, ransacReprojThreshold)

        # cv.warpPerspective()：透视变换函数，用于解决cv2.warpAffine()不能处理视场和图像不平行的问题
        # 作用：就是对图像进行透视变换，可保持直线不变形，但是平行线可能不再平行
        result = cv.warpPerspective(
            image_right, Homography, (image_right.shape[1] + image_left.shape[1], image_right.shape[0]))
        
        # cv.imshow("warp convert", result)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        # 将左图加入到变换后的右图像的左端即获得最终图像
        result[0:image_left.shape[0], 0:image_left.shape[1]] = image_left
        
        # 返回全景拼接的图像
        return result


if __name__ == '__main__':

    # 注意图像顺序
    m1 = r"C:\Users\Administrator\Desktop\\133.png"
    m2 = r"C:\Users\Administrator\Desktop\\144.png"

    imgLeft = cv.imread(m1)
    imgRight = cv.imread(m2)

    # 统一尺寸
    height, width, chan = imgLeft.shape
    decrease = (width, height)
    imgRight = cv.resize(imgRight, decrease, interpolation = cv.INTER_CUBIC)
    imgLeft = cv.resize(imgLeft, decrease, interpolation = cv.INTER_CUBIC)

    # 带关键点的图像、关键点和sift的特征向量
    keypointsImgRight, keypointsRight, featuresRight = sift_keypoints_detect(imgRight)
    keypointsImgLeft, keypointsLeft, featuresLeft = sift_keypoints_detect(imgLeft)

    hm1 = np.hstack((keypointsImgLeft, imgRight))
    hm2 = np.hstack((imgLeft, keypointsImgRight))
    hm = np.vstack((hm1, hm2))
    cv.imshow("keypoints mark", hm)
    cv.waitKey(0)
    cv.destroyAllWindows()
    goodMatch = get_feature_point_ensemble(featuresRight, featuresLeft)

    # cv.drawMatches():在提取两幅图像特征之后，画出匹配点对连线
    # matchColor – 匹配的颜色（特征点和连线),若matchColor==Scalar::all(-1),颜色随机
    matchImg = cv.drawMatches(
        imgRight, keypointsRight, imgLeft, keypointsLeft, goodMatch, None, None, None, None, flags=2)
    cv.imshow("keypoint_link", matchImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # 把图片拼接成全景图并保存
    result = Panorama_stitching(imgRight, imgLeft)
    cv.namedWindow("panorama", cv.WINDOW_AUTOSIZE)
    cv.imshow("panorama", result)
    cv.waitKey(0)
    cv.destroyAllWindows()