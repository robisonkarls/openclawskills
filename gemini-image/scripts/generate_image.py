#!/usr/bin/env python3
"""
Generate images using Google Gemini 3.1 Flash Image Preview API.
"""
import sys
import json
import base64
import os
from pathlib import Path

def load_api_key():
    """Load Gemini API key from settings."""
    settings_path = Path.home() / '.gemini' / 'settings.json'
    if settings_path.exists():
        with open(settings_path) as f:
            settings = json.load(f)
            return settings.get('GEMINI_API_KEY')
    
    # Fallback to environment variable
    return os.environ.get('GEMINI_API_KEY')

def generate_image(prompt: str, output_path: str = None, model: str = 'gemini-3.1-flash-image-preview') -> dict:
    """
    Generate an image using Gemini API.
    
    Args:
        prompt: Text description of the image to generate
        output_path: Optional path to save the image (default: gemini-images/<timestamp>.png in current directory)
        model: Gemini model to use (default: gemini-3.1-flash-image-preview)
    
    Returns:
        dict with 'success', 'path', 'width', 'height', 'size_bytes', and optional 'error'
    """
    import subprocess
    from datetime import datetime
    
    api_key = load_api_key()
    if not api_key:
        return {
            'success': False,
            'error': 'No Gemini API key found. Set GEMINI_API_KEY or configure ~/.gemini/settings.json'
        }
    
    if output_path is None:
        # Create gemini-images directory in current working directory
        images_dir = Path.cwd() / 'gemini-images'
        images_dir.mkdir(exist_ok=True)
        
        # Generate timestamp-based filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = str(images_dir / f'image_{timestamp}.png')
    
    # Prepare request payload
    request = {
        'contents': [{
            'parts': [{
                'text': f'Generate an image: {prompt}'
            }]
        }],
        'generationConfig': {
            'temperature': 1.0,
            'topP': 0.95
        }
    }
    
    # Write request to temp file
    request_file = '/tmp/gemini_image_request.json'
    with open(request_file, 'w') as f:
        json.dump(request, f)
    
    # Make API call
    try:
        result = subprocess.run([
            'curl', '-s', '-X', 'POST',
            f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}',
            '-H', 'Content-Type: application/json',
            '-d', f'@{request_file}'
        ], capture_output=True, text=True, check=True)
        
        response = json.loads(result.stdout)
        
        # Extract image data
        if 'candidates' not in response or not response['candidates']:
            return {
                'success': False,
                'error': f"No image generated. Response: {json.dumps(response, indent=2)}"
            }
        
        parts = response['candidates'][0]['content']['parts']
        image_data = None
        for part in parts:
            if 'inlineData' in part and part['inlineData'].get('mimeType', '').startswith('image/'):
                image_data = part['inlineData']['data']
                break
        
        if not image_data:
            return {
                'success': False,
                'error': 'No image data found in response'
            }
        
        # Decode and save image
        image_bytes = base64.b64decode(image_data)
        with open(output_path, 'wb') as f:
            f.write(image_bytes)
        
        # Get image dimensions using file command
        file_info = subprocess.run(['file', output_path], capture_output=True, text=True)
        dimensions = 'unknown'
        if 'PNG image data' in file_info.stdout:
            # Extract dimensions from file output
            parts = file_info.stdout.split(',')
            for part in parts:
                if 'x' in part and any(c.isdigit() for c in part):
                    dimensions = part.strip()
                    break
        
        return {
            'success': True,
            'path': output_path,
            'dimensions': dimensions,
            'size_bytes': len(image_bytes),
            'model': model
        }
        
    except subprocess.CalledProcessError as e:
        return {
            'success': False,
            'error': f'API call failed: {e.stderr}'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }

def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            'success': False,
            'error': 'Usage: generate_image.py <prompt> [output_path] [model]'
        }, indent=2))
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    model = sys.argv[3] if len(sys.argv) > 3 else 'gemini-3.1-flash-image-preview'
    
    result = generate_image(prompt, output_path, model)
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result['success'] else 1)

if __name__ == '__main__':
    main()
