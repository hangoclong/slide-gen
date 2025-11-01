# Image Generation Script

This script generates images using Google Gemini AI based on text prompts.

## Quick Start

### 1. Setup Environment

#### Option A: Automated Setup (Recommended)
```bash
# Run the automated setup script
./setup_environment.sh
```

#### Option B: Manual Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

Both options will:
- Create a Python virtual environment (`venv/`)
- Install required dependencies (`google-genai`, `Pillow`, `python-dotenv`)

### 2. Set API Key

You need a Google Gemini API key to use this script.

```bash
# Option 1: Using .env file (Recommended)
cp .env.example .env
# Edit .env file and replace 'your-gemini-api-key-here' with your actual API key

# Option 2: Set as environment variable
export GEMINI_API_KEY='your-gemini-api-key-here'

# Option 3: Pass as command line argument (less secure)
```

Get your API key from: https://aistudio.google.com/app/apikey

### 3. Generate Images

```bash
# Activate the virtual environment
source venv/bin/activate

# Generate an image
python generate_image.py "your prompt text here" ./output_directory
```

## Usage Examples

### Basic Usage
```bash
python generate_image.py "A beautiful sunset over mountains" ./generated_images
```

### Advanced Examples
```bash
# Portrait style
python generate_image.py "A professional headshot of a business person in office lighting" ./portraits

# Artistic style
python generate_image.py "Abstract painting with vibrant colors and geometric shapes" ./art

# Product visualization
python generate_image.py "Modern smartphone on a minimalist desk with good lighting" ./product_shots
```

### Using API Key Parameter
```bash
python generate_image.py "your prompt" ./output_dir --api-key "your-api-key"
```

## Command Line Arguments

- **`prompt`** (required): Text description of the image you want to generate
- **`output_dir`** (required): Directory where generated images will be saved
- **`--api-key`** (optional): Your Gemini API key (alternative to environment variable)

## Output

- Images are saved as high-quality files in the specified output directory
- Filenames include timestamps to avoid conflicts: `generated_image_1699123456_0.png`
- The script automatically creates the output directory if it doesn't exist
- Supports multiple images per request (when applicable)

## Technical Details

### Image Configuration
- **Model**: Gemini 2.5 Flash Image
- **Aspect Ratio**: 9:16 (vertical)
- **Quality**: 1K resolution
- **Format**: PNG (automatically determined)

### Default Style Settings
The script applies professional photography settings:
- **Aesthetic**: Professional, authentic, sharp focus
- **Lighting**: Bright natural daylight, cinematic, high contrast
- **Quality**: Ultra-realistic, photorealistic, 8K
- **Negative prompts**: CGI, 3D renders, illustrations, graphics

## Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY environment variable is not set"**
   ```bash
   export GEMINI_API_KEY='your-actual-api-key'
   ```

2. **"ModuleNotFoundError: No module named 'google'"**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   # or manually: pip install google-genai
   ```

3. **Permission errors**
   ```bash
   chmod +x setup_environment.sh
   ```

### Getting Help
```bash
python generate_image.py --help
```

## Dependencies

- `google-genai`: Google's generative AI SDK
- `Pillow`: Image processing library
- `python-dotenv`: Environment variable management
- Python 3.7+

## File Structure

```
slides-gen/
├── generate_image.py          # Main script
├── setup_environment.sh       # Automated setup
├── requirements.txt           # Dependencies
├── .env.example              # Environment variables template
├── Img-Gen-Readme.md         # This file
└── venv/                      # Virtual environment (created by setup)
```

## Best Practices

1. **API Security**: Use environment variables for API keys, not command line arguments
2. **Prompts**: Be descriptive and specific for better results
3. **Output Organization**: Use separate directories for different types of images
4. **Batch Processing**: Run multiple commands for different prompts

## Full Command Template

```bash
# Complete one-liner for image generation
source venv/bin/activate && python generate_image.py "YOUR_PROMPT_HERE" ./output_directory
```

### Template with API Key
```bash
source venv/bin/activate && python generate_image.py "YOUR_PROMPT_HERE" ./output_directory --api-key "YOUR_API_KEY"
```

### Template with Custom Filename
```bash
source venv/bin/activate && python generate_image.py "YOUR_PROMPT_HERE" ./output_directory --filename "slide-2"
```

## Example Workflow

```bash
# 1. Setup
./setup_environment.sh

# 2. Set API key (do this once per session)
export GEMINI_API_KEY='your-api-key-here'

# 3. Create output directories
mkdir -p generated_images/{portraits,landscapes,products}

# 4. Generate different types of images
source venv/bin/activate && python generate_image.py "Professional business portrait, office lighting" ./generated_images/portraits
source venv/bin/activate && python generate_image.py "Mountain landscape at sunrise" ./generated_images/landscapes
source venv/bin/activate && python generate_image.py "Modern laptop on wooden desk" ./generated_images/products
```

### Quick Test Command
```bash
# Test with a simple prompt
source venv/bin/activate && python generate_image.py "A simple red apple on a white background" ./test_output

# Test with custom filename
source venv/bin/activate && python generate_image.py "A simple red apple on a white background" ./test_output --filename "slide-2"
```