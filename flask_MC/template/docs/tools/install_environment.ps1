cd ..
python -m venv venv_docs
./venv_docs/Scripts/Activate.ps1
pip install -r REQUIREMENTS.txt
python ./tools/install_pandoc.py
cd tools