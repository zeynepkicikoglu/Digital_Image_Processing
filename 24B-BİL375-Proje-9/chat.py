import cv2
import matplotlib.pyplot as plt
from skimage import morphology
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from scipy import ndimage

# Görüntüyü yükleme
I = cv2.imread("I.png")

# BGR'den RGB'ye dönüştürme
I_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

# Gri tonlamaya dönüştürme
Igry = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Medyan filtresi uygulama
# Imed = cv2.medianBlur(Igry, 5)

# # Kenar tespiti (Canny)
# tresh = 0.3
# I_edg_med = cv2.Canny(Imed, int(tresh * 255 * 2), int(tresh * 255))

# # Threshold ile ikili kenar tespiti (Canny)
# I_edg_gry = cv2.Canny(Igry, int(tresh * 255 * 2), int(tresh * 255))

# Adaptif thresholding
T = threshold_otsu(Igry)
Ibw = Igry > T

# Boşlukları doldurma
I_fil = ndimage.binary_fill_holes(Ibw)

# Morfolojik açma (opening)
selem = morphology.rectangle(25, 50)
I_cls = morphology.opening(I_fil, selem)

# Sonuçları gösterme
plt.figure(figsize=(16, 10))
plt.subplot(3, 3, 1)
plt.imshow(Igry, cmap='gray')
plt.title('Gri Tonlama')
plt.subplot(3, 3, 2)
# plt.imshow(Imed, cmap='gray')
# plt.title('Medyan Filtre')
# plt.subplot(3, 3, 3)
# plt.imshow(I_edg_gry, cmap='gray')
# plt.title('Kenarlar (Gri Tonlama)')
# plt.subplot(3, 3, 4)
# plt.imshow(I_edg_med, cmap='gray')
# plt.title('Kenarlar (Medyan Filtre)')
# plt.subplot(3, 3, 5)
plt.imshow(Ibw, cmap='gray')
plt.title('Adaptif Threshold')
plt.subplot(3, 3, 6)
plt.imshow(I_fil, cmap='gray')
plt.title('Delikleri Doldur')
plt.subplot(3, 3, 7)
plt.imshow(I_cls, cmap='gray')
plt.title('Morfolojik Açma')
plt.show()

# Etiketleme
label_image, num_labels = label(I_cls, return_num=True)

# Eşit büyüklükteki kutucukları bulma ve sıralama
regions = regionprops(label_image)

# 3. etiketli bölgeyi al
selected_region = None
for region in regions:
    if region.label == 3:
        selected_region = region
        break

# Eğer 3. etiketli bölge bulunduysa, onu göster
if selected_region:
    minr, minc, maxr, maxc = selected_region.bbox
    plt.text(minc, minr, '3', color='red', fontsize=12, ha='right', va='bottom')

# Sonuçları gösterme
plt.imshow(I_cls, cmap='gray')
plt.title('Etiketlenmiş Görüntü')
plt.axis('off')
plt.show()

# Kaldırılacak etiketleri belirle
labels_to_remove = [1, 2, 4, 5]

# Seçili etiketlere sahip kutucukları kaldır
for region in regions:
    if region.label in labels_to_remove:
        minr, minc, maxr, maxc = region.bbox
        I_cls[minr:maxr, minc:maxc] = 0

plt.imshow(I_cls, cmap='gray')
plt.axis('off')
plt.show()

# Yeniden Etiketleme
label_image = label(I_cls)
regions = regionprops(label_image)

# Sonuçları gösterme
plt.imshow(I_rgb)  # Renkli görüntü
plt.title('Orijinal Görüntü')
plt.axis('off')

# Etiketleri gösterme
for region in regions:
    minr, minc, maxr, maxc = region.bbox
    plt.text(minc, minr, f'{region.label}', color='red', fontsize=12, ha='right', va='bottom')

plt.show()

# Bulanıklaştırma için etiketlenmiş bölgeyi bulma
blurred_region = None
for region in regions:
    if region.label == 1:
        blurred_region = region
        break

# Eğer bulanıklaştırılacak bölge bulunduysa, onu bulanıklaştır
if blurred_region:
    minr, minc, maxr, maxc = blurred_region.bbox
    plate_area = I[minr:maxr, minc:maxc]
    blurred_plate_area = cv2.GaussianBlur(plate_area, (15, 15), 10)  # Gauss filtresi uygula
    I[minr:maxr, minc:maxc] = blurred_plate_area

# Sonuçları gösterme
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))  # Renkli görüntü
plt.title('Bulanıklaştırılmış Plaka')
plt.axis('off')
plt.show()
