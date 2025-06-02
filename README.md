# Proje Arşiv Otomasyonu | Project Archive Automation

## English

This project automates the process of adding category information in the project archive system using Firefox browser.

### Features

- Firefox browser automation
- Automatic login process
- Automatic category information addition for TIFF files
- Progress reporting
- Error handling and logging

### Requirements

```txt
selenium==4.33.0
webdriver-manager
numpy
pandas
```

### Installation

1. Install required Python packages:

```bash
pip install -r requirements.txt
```

2. Create `path.py` file and define the following variables:

```python
path_driver = "C:/chromedriver-win64/chromedriver.exe"
url_proje_firefox = "YOUR_URL"
User_Name = "YOUR_USERNAME"
User_Password = "YOUR_PASSWORD"
```

### Usage

1. Run the script:

```bash
python Selenium_Firefox.py
```

2. The script will automatically:
- Log into the system
- Navigate to the project archive
- Scan TIFF files in the specified folder
- Add necessary information to files without category information
- Print process report to console

### Important Notes

- Make sure Firefox browser is installed before running the script
- Ensure stable internet connection
- Use environment variables for sensitive information (username, password, etc.)
- Adjust waiting times (`time.sleep()`) according to your internet speed

---

## Türkçe

Bu proje, Firefox tarayıcısı kullanılarak proje arşiv sisteminde otomatik kategori bilgisi ekleme işlemlerini gerçekleştirir.

### Özellikler

- Firefox tarayıcı otomasyonu
- Otomatik login işlemi
- TIFF dosyalarının kategori bilgilerinin otomatik eklenmesi
- İlerleme durumu raporlama
- Hata yönetimi ve loglama

### Gereksinimler

```txt
selenium==4.33.0
webdriver-manager
numpy
pandas
```

### Kurulum

1. Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

2. `path.py` dosyasını oluşturun ve aşağıdaki değişkenleri tanımlayın:

```python
path_driver = "C:/chromedriver-win64/chromedriver.exe"
url_proje_firefox = "YOUR_URL"
User_Name = "YOUR_USERNAME"
User_Password = "YOUR_PASSWORD"
```

### Kullanım

1. Script'i çalıştırın:

```bash
python Selenium_Firefox.py
```

2. Script otomatik olarak:
- Sisteme login olacak
- Proje arşivine gidecek
- Belirtilen klasördeki TIFF dosyalarını tarayacak
- Kategori bilgisi olmayan dosyalara gerekli bilgileri ekleyecek
- İşlem raporunu konsola yazdıracak

### Önemli Notlar

- Script'i çalıştırmadan önce Firefox tarayıcısının yüklü olduğundan emin olun
- Internet bağlantınızın stabil olduğundan emin olun
- Hassas bilgiler (kullanıcı adı, şifre vb.) için environment variables kullanılması önerilir
- Scripteki bekleme sürelerini (`time.sleep()`) internet hızınıza göre ayarlayabilirsiniz



