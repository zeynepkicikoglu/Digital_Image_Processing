
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.morphology import remove_small_objects
from scipy.ndimage import binary_fill_holes

# Görüntüyü yükle
image_path = "yag.png"
image = cv2.imread(image_path)

# Görüntüyü gri tonlamalıya dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşikleme ile yağ dokusunu ve hücre içi boşlukları belirle
_, binary_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

# Structuring element (kernal) oluştur
# kernel = np.ones((3,3), np.uint8)

# Erode ve dilate işlemlerini uygula (Açma - Opening)
# eroded_image = cv2.erode(binary_image, kernel, iterations=4)
# opened_image = cv2.dilate(eroded_image, kernel, iterations=4)

opened_image_cleaned = remove_small_objects(binary_image.astype(bool), min_size=600)


# Yağ alanını ve toplam alanı hesapla
total_area = binary_image.size
fat_area = np.sum(binary_image == 255)

# Yağ oranını hesapla
fat_ratio = (fat_area / total_area) * 100

print(f"Yağ Oranı: {fat_ratio:.2f}%")

# Sonuçları görselleştirin
plt.figure(figsize=(20, 5))
plt.subplot(1, 3, 1)
plt.title("Orijinal Görüntü")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title("Eşiklenmiş Görüntü")
plt.imshow(binary_image, cmap='gray')

# plt.subplot(1, 3, 3)
# plt.title("Açma (Opening) Uygulanmış Görüntü")
# plt.imshow(opened_image, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Bwareaopen Uygulanmış Görüntü")
plt.imshow(opened_image_cleaned, cmap='gray')


plt.show()


# import cv2
# import numpy as np
# from skimage.measure import label, regionprops

# # Görüntüyü yükle ve gri tonlamalıya dönüştür
# image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# # Eşikleme ile ikili görüntü oluştur
# _, binary_image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

# # Her bir yağ öbeğini etiketle
# labeled_image, num_labels = label(binary_image, return_num=True)

# # Her bir öbeğin histogram bilgisini hesapla
# for region in regionprops(labeled_image):
#     minr, minc, maxr, maxc = region.bbox
#     region_image = image[minr:maxr, minc:maxc]
#     hist = cv2.calcHist([region_image], [0], None, [256], [0, 256])
    
#     plt.figure()
#     plt.title(f"Öbek ID: {region.label}")
#     plt.xlabel("Piksel Değerleri")
#     plt.ylabel("Frekans")
#     plt.plot(hist)
#     plt.xlim([0, 256])
#     plt.show()
