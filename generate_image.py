#!/usr/bin/env python3

import os
import sys
import argparse
from pathlib import Path
from google import genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv


def save_binary_file(file_name, data):
    """Save binary data to a file."""
    f = open(file_name, "wb")
    f.write(data)
    f.close()
    print(f"File saved to: {file_name}")


def generate_image(prompt_text, output_dir, api_key=None, filename_prefix=None):
    """Generate an image based on the given prompt and save to output directory."""

    # Clear any existing GEMINI_API_KEY from system environment
    if 'GEMINI_API_KEY' in os.environ:
        del os.environ['GEMINI_API_KEY']

    # Load environment variables ONLY from local .env file
    load_dotenv(override=True)

    # Use API key from parameter or environment variable
    if api_key is None:
        api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set or api_key parameter not provided")

    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-flash-image"

    # Create the enhanced prompt
    enhanced_prompt = f"""Create a vertical, ultra-realistic photograph with the following specifications:

Subject: {prompt_text}

Style and Composition:
- Aesthetic: Professional photography, authentic, candid, sharp focus, modern lifestyle
- Lighting: Bright natural daylight, cinematic, high contrast
- Camera shot: Medium shot, shallow depth of field
- Mood: Modern, high-quality, professional

Technical Requirements:
- Aspect ratio: 9:16 (vertical)
- Quality: Ultra-realistic, photorealistic, 8K
- Avoid: CGI, 3D render, abstract, illustration, diagram, chart, futuristic, glowing lines, blue interface, text, icons, symbols, unrealistic, cartoon, graphic"""

    file_index = 0
    saved_files = []

    print(f"Generating image for prompt: {prompt_text}")
    print(f"Output directory: {output_dir}")

    try:
        response = client.models.generate_content(
            model=model,
            contents=[enhanced_prompt],
        )

        if response.candidates and response.candidates[0].content:
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    print(f"Text response: {part.text}")
                elif part.inline_data is not None:
                    # Generate filename with custom prefix or default
                    import time
                    timestamp = int(time.time())
                    if filename_prefix:
                        file_name = f"{filename_prefix}_{file_index}"
                    else:
                        file_name = f"generated_image_{timestamp}_{file_index}"
                    file_index += 1

                    # Save image using PIL
                    image = Image.open(BytesIO(part.inline_data.data))
                    file_path = output_path / f"{file_name}.png"
                    image.save(str(file_path))
                    saved_files.append(str(file_path))
                    print(f"Image saved: {file_path}")

        print(f"\nGeneration complete! Saved {len(saved_files)} files:")
        for file in saved_files:
            print(f"  - {file}")

        return saved_files

    except Exception as e:
        print(f"Error during image generation: {e}")
        raise e


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description="Generate images using Google Gemini AI")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("output_dir", help="Output directory for generated images")
    parser.add_argument("--api-key", help="Google Gemini API key (or set GEMINI_API_KEY env var)")
    parser.add_argument("--filename", help="Custom filename prefix (without extension)")

    args = parser.parse_args()

    try:
        generate_image(args.prompt, args.output_dir, args.api_key, args.filename)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()