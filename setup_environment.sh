#!/bin/bash

# Setup script for the image generation environment

echo "Setting up Python environment for image generation..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing required dependencies..."
pip install google-genai

echo "Setup complete!"
echo ""
echo "To use the script:"
echo "1. Make sure you have your GEMINI_API_KEY environment variable set:"
echo "   export GEMINI_API_KEY='your-api-key-here'"
echo ""
echo "2. Run the image generation script:"
echo "   python generate_image.py 'Your prompt text here' ./output_directory"
echo ""
echo "Example:"
echo "   python generate_image.py 'A beautiful sunset over mountains' ./generated_images"