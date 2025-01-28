import requests
from bs4 import BeautifulSoup
import json

# Web sayfasını analiz etmek için temel fonksiyon
def analyze_website(url):
    try:
        # Sayfa verilerini al
        response = requests.get(url)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        
        # Analiz sonuçlarını tutacak sözlük
        result = {
            "URL": url,
            "Durum Kodu": response.status_code,
            "CMS": None,
            "Framework": None,
            "Versiyon Bilgisi": None
        }

        # HTML içerik analizi
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # CMS ve Framework tespiti
        cms, framework = cms_framework_detection(soup, response)
        result["CMS"] = cms
        result["Framework"] = framework

        # Versiyon tespiti
        version_info = version_detection(soup)
        result["Versiyon Bilgisi"] = version_info

        # JSON formatında çıktı
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except requests.RequestException as e:
        print(json.dumps({"Hata": str(e)}, indent=4, ensure_ascii=False))

# CMS ve Framework analizi
def cms_framework_detection(soup, response):
    # CMS Tespiti
    cms_keywords = ["WordPress", "Joomla", "Drupal", "Magento", "Shopify", "Wix"]
    cms_found = None
    for keyword in cms_keywords:
        if keyword.lower() in response.text.lower():
            cms_found = keyword
            break

    # Framework Tespiti
    frameworks = ["Django", "Ruby on Rails", "Laravel", "Flask", "Angular", "React", "Vue"]
    framework_found = None
    for framework in frameworks:
        if framework.lower() in response.text.lower():
            framework_found = framework
            break

    return cms_found, framework_found

# Versiyon tespiti (Örnek olarak HTML meta etiketlerini kontrol ediyor)
def version_detection(soup):
    # Örnek olarak meta tag'lerden versiyon arama
    meta_tags = soup.find_all("meta")
    for meta in meta_tags:
        if 'generator' in meta.attrs:
            return meta.attrs.get('generator')
    return None

# Ana fonksiyon
def main():
    url = input("Analiz edilecek web sitesi URL'sini girin: ")
    if not url.startswith("http"):
        url = "http://" + url
    analyze_website(url)

if __name__ == "__main__":
    main()
