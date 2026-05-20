#!/usr/bin/env python
"""
Render Deployment Checker
Validates your project is ready for Render deployment
"""

import os
import sys
from pathlib import Path

def check_file_exists(filename, description):
    if os.path.exists(filename):
        print(f"✓ {description}")
        return True
    else:
        print(f"✗ {description} - MISSING")
        return False

def check_content(filename, search_text, description):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if search_text in content:
                print(f"✓ {description}")
                return True
            else:
                print(f"✗ {description} - NOT FOUND")
                return False
    except FileNotFoundError:
        print(f"✗ {description} - FILE NOT FOUND")
        return False

def main():
    print("\n" + "="*50)
    print("  RENDER DEPLOYMENT CHECKER")
    print("="*50 + "\n")

    checks = []

    print("📋 Required Files:")
    checks.append(check_file_exists('requirements.txt', 'requirements.txt'))
    checks.append(check_file_exists('.env.example', '.env.example'))
    checks.append(check_file_exists('render.yaml', 'render.yaml'))
    checks.append(check_file_exists('.gitignore', '.gitignore'))

    print("\n🔧 Dependencies:")
    checks.append(check_content('requirements.txt', 'gunicorn', 'gunicorn in requirements.txt'))
    checks.append(check_content('requirements.txt', 'Django', 'Django in requirements.txt'))
    checks.append(check_content('requirements.txt', 'python-decouple', 'python-decouple in requirements.txt'))

    print("\n⚙️ Django Settings:")
    checks.append(check_content('JokesProject/JokesProject/settings.py', 'DEBUG = config', 'DEBUG configured'))
    checks.append(check_content('JokesProject/JokesProject/settings.py', 'ALLOWED_HOSTS', 'ALLOWED_HOSTS configured'))

    print("\n📦 Build Configuration:")
    checks.append(check_file_exists('JokesProject/manage.py', 'manage.py exists'))

    total = len(checks)
    passed = sum(checks)

    print("\n" + "="*50)
    print(f"Results: {passed}/{total} checks passed")
    print("="*50 + "\n")

    if passed == total:
        print("✓ Your project is READY for Render deployment! 🚀\n")
        return 0
    else:
        print(f"✗ {total - passed} issues need to be fixed\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())

