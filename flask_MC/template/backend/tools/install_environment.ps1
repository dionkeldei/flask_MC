cd ..
echo "Generating development environment.."
python -m venv venv
echo "Starting development environment.."
./venv/Scripts/Activate.ps1
echo "Installing libraries in development environment.."
pip install -r REQUIREMENTS.txt
echo "Development environment ready"
cd tools
python generate_secretKey.py