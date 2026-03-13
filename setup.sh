#!/bin/bash

# CyberExpert APK Builder - Complete Setup
# রান করো: chmod +x setup.sh && ./setup.sh

echo "===================================="
echo "🚀 CyberExpert APK Builder Setup"
echo "===================================="
echo ""

# Check if main.py exists
if [ ! -f main.py ]; then
    echo "❌ ERROR: main.py not found!"
    echo "📁 Please place main.py in current folder first"
    exit 1
fi

echo "✅ main.py found"

# Create directories
echo "📁 Creating directories..."
mkdir -p .github/workflows
echo "✅ Directories created"

# Create buildozer.spec
echo "📝 Creating buildozer.spec..."
cat > buildozer.spec << 'EOF'
[app]
title = CyberExpert
package.name = cyberexpert
package.domain = com.sakib
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 1.0.0
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.private_storage = True
android.accept_sdk_license = True
android.arch = arm64-v8a
android.log_level = 2

[buildozer]
log_level = 2
EOF
echo "✅ buildozer.spec created"

# Create main.yml workflow
echo "📝 Creating GitHub workflow..."
cat > .github/workflows/main.yml << 'EOF'
name: Build Android APK

on:
  push:
    branches: [ "main", "master" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-20.04
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y \
          git \
          wget \
          unzip \
          python3-pip \
          autoconf \
          automake \
          libtool \
          pkg-config \
          zlib1g-dev \
          libncurses5-dev \
          libgdbm-dev \
          libnss3-dev \
          libssl-dev \
          libreadline-dev \
          libffi-dev \
          libsqlite3-dev \
          libbz2-dev \
          openjdk-17-jdk \
          ccache

    - name: Install Python packages
      run: |
        pip install --upgrade pip
        pip install cython==0.29.33
        pip install buildozer==1.5.0

    - name: Build APK
      run: buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: CyberExpert-APK
        path: bin/*.debug.apk
EOF
echo "✅ GitHub workflow created"

# Create README.md
echo "📝 Creating README.md..."
cat > README.md << 'EOF'
# CyberExpert App 🔐

A secure Android app that can only be closed with password.

## Features
- 🔒 Password protected exit (password: sakib123)
- 📱 Mobile keyboard support
- 👤 Developer contact info
- 🎨 Beautiful animations

## How to Install
1. Download APK from GitHub Actions
2. Enable "Unknown sources" in Android settings
3. Install and open

## Build Instructions
This app uses GitHub Actions for automatic APK building.

## Password
**sakib123**
EOF
echo "✅ README.md created"

# Create .gitignore
echo "📝 Creating .gitignore..."
cat > .gitignore << 'EOF'
# Buildozer
.buildozer/
bin/
*.pyc
__pycache__/
.DS_Store
EOF
echo "✅ .gitignore created"

# Show summary
echo ""
echo "===================================="
echo "✅ SETUP COMPLETE!"
echo "===================================="
echo ""
echo "📁 Files created:"
echo "   - main.py (existing)"
echo "   - buildozer.spec"
echo "   - .github/workflows/main.yml"
echo "   - README.md"
echo "   - .gitignore"
echo ""
echo "📦 Total files: 5"
echo ""
echo "🚀 Next steps:"
echo "   1. git init (if not already)"
echo "   2. git add ."
echo "   3. git commit -m 'Initial commit'"
echo "   4. git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo "   5. git push -u origin main"
echo ""
echo "📱 After push:"
echo "   - Go to GitHub -> Actions tab"
echo "   - Wait 10-15 minutes"
echo "   - Download APK from Artifacts"
echo ""
echo "🔑 PASSWORD: sakib123"
echo "===================================="
