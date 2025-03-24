#!/bin/bash

echo "🚀 imehmetech DDoS Tool Kuruluyor..."

# Python kontrol
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 yüklü değil. Lütfen yükleyip tekrar deneyin."
    exit 1
fi

# pip kontrol
if ! command -v pip3 &>/dev/null; then
    echo "❌ pip3 yüklü değil. Lütfen yükleyip tekrar deneyin."
    exit 1
fi

# Opsiyonel: virtual environment
read -p "🌱 Virtual environment oluşturulsun mu? (y/n): " use_venv
if [[ "$use_venv" == "y" ]]; then
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ venv aktif."
fi

# Modül kurulumu
echo "📦 Gerekli Python paketleri yükleniyor..."
pip3 install --upgrade pip
pip3 install rich requests

echo "✅ Kurulum tamamlandı."
echo "💡 Çalıştırmak için: python3 main.py"
