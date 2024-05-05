import cv2
import ultralytics
from ultralytics import YOLO
import matplotlib.pyplot as plt

video = cv2.VideoCapture("C:/Users/topkapi/Desktop/Teknofest/Ornek Video.mp4")

kare_genislik = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
kare_yukseklik = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
kare_hizi = video.get(cv2.CAP_PROP_FPS)
toplam_kare = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # yarismada  75*5*60 adet frame olacak

# Hedef noktanın koordinatları
hedef_x = 955
hedef_y = 540  # bu iki kordinat 1920*1080 in olan goruntunun tam orta noktası olacak ve oraya (0,0 noktası diyecegiz)

# Video çıkış dosyası için ayarlar
cikti_yolu = "video_cikti.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
cikti = cv2.VideoWriter(cikti_yolu, fourcc, kare_hizi, (kare_genislik, kare_yukseklik))

# İlk kareyi oku ve işaretle(0,0) noktası icin olacak burası
ret, kare = video.read()
if ret:
    cv2.circle(kare, (hedef_x, hedef_y), 5, (0, 0, 255),
               -1)  # matrisin 0,0 noktası yani 955,540 noktasına ilk nokta cizdirdik burada burhan seckin sadasd

    # İlk kareyi kaydet
    cikti.write(kare)

# İlk karedeki hedef noktayı takip et
onceki_kare = kare
onceki_hedef_x = hedef_x
onceki_hedef_y = hedef_y

plt.imshow(cv2.cvtColor(kare, cv2.COLOR_BGR2RGB))  # Görüntüyü doğru renk formatına dönüştürün
plt.scatter(hedef_x, hedef_y, color='red', marker='o')  # Hedef noktayı işaretleyin
plt.show()