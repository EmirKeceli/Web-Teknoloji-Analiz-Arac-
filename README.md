# Web Teknoloji Analiz Aracı

## Projenin Amacı ve Genel İşleyişi

Bu proje, bir web sitesinin **CMS (İçerik Yönetim Sistemi)**, **framework** ve olası **versiyon bilgilerini** tespit etmek için Python kullanılarak geliştirilmiştir.

- Kullanıcı, analiz etmek istediği bir web sitesinin URL'sini girer.
- Program, HTTP yanıtlarını ve web sayfası HTML içeriğini analiz ederek sonuçları JSON formatında döndürür.
- Elde edilen bilgiler, web teknolojileriyle ilgilenen geliştiricilere veya siber güvenlik uzmanlarına faydalı olabilir.

---

## Proje Sahibi Bilgileri

| Proje Sahibi | Öğrenci Numarası |
| ------------- | ---------------- |
| Emir Keçeli  | 2320191016       |

## Kullanılan Kütüphaneler ve Versiyonları

Proje, aşağıdaki Python kütüphanelerini kullanmaktadır:

- `requests` (v2.31.0): HTTP isteklerini yapmak için.
- `beautifulsoup4` (v4.12.2): HTML ve XML dosyalarını parse etmek için.
- `json` (Dahili kütüphane): JSON formatında çıktı oluşturmak için.

---

## Gerekli Araçlar ve Kurulum Gereksinimleri

Projenin çalıştırılması için aşağıdaki araç ve gereksinimlere ihtiyacınız vardır:

- **Python 3.7+**
- `pip` paket yöneticisi

Gerekli kütüphaneleri yüklemek için aşağıdaki komut çalıştırılabilir:

```bash
pip install -r requirements.txt
```

---

## Zorunlu Çalışma Parametreleri

- Kullanıcıdan bir web sitesi URL'si girilmesi beklenir.
- URL, "http" veya "https" ile başlamıyorsa, program otomatik olarak başına "http\://" ekler.

---

## Opsiyonel Parametreler ve Kullanımları

Bu kodda opsiyonel bir parametre bulunmamaktadır.

---

## Kurulum ve Çalıştırma Talimatları

1. **Proje deposunu klonlayın veya dosyaları indirin:**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Gerekli Python kütüphanelerini yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```

3. **`main.py`**\*\* dosyasını çalıştırın:\*\*

   ```bash
   python main.py
   ```

4. **Analiz etmek istediğiniz URL'yi girin:**
   Program çalıştığında, analiz edilecek web sitesinin URL'sini girmeniz istenecektir.

---

