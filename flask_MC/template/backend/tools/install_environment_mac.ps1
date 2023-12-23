cd ..
echo "Generating development environment.."
python3 -m venv venv
echo "Starting development environment.."
./venv/bin/activate
echo "Installing libraries in development environment.."
pip install -r REQUIREMENTS.txt
echo "Development environment ready"
cd tools