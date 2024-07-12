# I.png görseli RGB bir görüntüdür.
# Üzerinde tuz biber görüntüsü vardır. 
 

# >> Görüntüdeki plakayı tespit ediniz. 
# >> Sadece buradaki kısmı blur maskesi ile filtreleyiniz.
# >> Filtrelenmiş olan kısmı orijinal görüntüye ekleyiniz.


# clear all, close all; clc
# I = imread("A-png"); % B
# Igry = rgb2gray(I);
# figure,imshow (Igry , [])


# Imed = medfilt2(Igry , [5,5]);
# figure
# subplot (1,2,1) , imshow(Igry , []) 
# subplot (1,2,2) , imshow(Imed , [])


# tresh = 0.3;
# I_edg_med = edge(Imed, 'canny', tresh);
# I_edg_gry = edge(Igry, 'canny', tresh);


# figure
# subplot (2,2,1) , imshow(Igry , []) 
# subplot (2,2,2) , imshow(Imed , [])
# subplot (2,2,3) , imshow(I_edg_gry , [])
# subplot (2,2,4) , imshow(I_edg_med , [])

# Ibw = I_edg_med;

# T = adaptthresh(Igry , 0.9 ,'ForegroundPolarity', 'dark');
# Igry = im2double(Igry);
# Ibw = Igry > T;

# figure,
# imshow (Ibw , [])

# I_fil = imfill(Ibw, 'holes');

# figure,
# subplot (1,2,1) , imshow(Ibw, [])
# subplot (1, 2, 2) , imshow (I_fil , [])
# h = ones (25,50);

# se = strel (h);
# I_cls = imopen(I_fil , se);

# figure 
# subplot (1,2,1), imshow (I_fil , [])
# subplot(1,2,2) , imshow(I_cls , [])

# I _bwo = bwareaopen (I_cls , 1e3) ;
# figure
# subplot (1,2,1) , imshow(I_cls , []) 
# subplot (1,2,2) , imshow (I_bwo , [])
                         
# B = labeloverlay(I , I_bwo);
# figure,
# imshow (B, [])

# clear all, close all; clc
# I = imread('A.png');


#1- Görüntüyü griye cevirme
# 2- median filtre ile gürültüleri temizleme
# 3-kenarları bulmak ( en iyisi canny idi hiç kesiklik olmadan buldu thresholdu 0.1 seçtik. Prewitt ve sobel güzel bulamadı kenarları delation da uygulamak istemedim daha sonrasında)
# 4- daha sonra canny  uyguladığımız thresholdu degerını 0.3 yaptık çünkü çok detay kenar bılgılerı geldi bızım ısımıze onlar yaramıyordu
# 5- daha sonra imfill komutu ile etrafı kaplı kenarların içini doldurduk

# 6-daha sonra acma yapıyoruz 5x5 ilk boyutta çünkü acma ile once bağlantısız kenarlar silinicek ve elimizde sadece içi dolu olan şekiller kalıcak

# 7-bwareaopen ile bilmem ne (1e3) pikselin altındaki sekıllerı sil dedik.

# 8-labeloverlay ile daha sonra ilk görüntümüzün üstüne cızdııryoruz

# 9- UYARI: imfill kısmını ones(25,75) gibi büyük eşik değeri secseydik bwareaopen lara gerek kalmazdı.


# 10- normalde bwareaopen ile 1e3 seçince birkaç kutucuk seçerken 5e3 seçince ıstedıgımız çıktıyı verdi.(hocanın yaptığında)