# Environment
ENVIRONMENT="./venv"

if [ ! -d "$ENVIRONMENT" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
  echo "VENVIRONMENT DOES NOT EXIST..."
  echo "Creating VENVIRONMENT..."
  virtualenv -p python3 venv
  echo "VENVIRONMENT created"
fi

source venv/bin/activate
echo "venv activated"
echo "Installing packages..."
pip install -r requeriments.txt
deactivate


echo ""
echo "Installation complete."
echo ""
