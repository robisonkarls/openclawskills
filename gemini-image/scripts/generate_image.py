#!/usr/bin/env python3
"""
Generate images using Google Gemini 3.1 Flash Image Preview API.
Supports subject consistency, logo integration, and advanced prompting.
"""
import sys
import json
import base64
import os
from pathlib import Path
from typing import Optional, List

def load_api_key():
    """Load Gemini API key from settings."""
    settings_path = Path.home() / '.gemini' / 'settings.json'
    if settings_path.exists():
        with open(settings_path) as f:
            settings = json.load(f)
            return settings.get('GEMINI_API_KEY')
    
    # Fallback to environment variable
    return os.environ.get('GEMINI_API_KEY')

def encode_image(image_path: str) -> tuple[str, str]:
    """
    Encode an image file to base64 and detect MIME type.
    
    Args:
        image_path: Path to image file
        
    Returns:
        Tuple of (base64_data, mime_type)
    """
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Detect MIME type from extension
    ext = path.suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.webp': 'image/webp',
        '.gif': 'image/gif'
    }
    mime_type = mime_types.get(ext, 'image/png')
    
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    return image_data, mime_type

def generate_image(
    prompt: str, 
    output_path: str = None, 
    model: str = 'gemini-3.1-flash-image-preview',
    reference_images: List[str] = None,
    aspect_ratio: str = None,
    temperature: float = 1.0
) -> dict:
    """
    Generate an image using Gemini API with subject consistency support.
    
    Args:
        prompt: Text description of the image to generate
        output_path: Optional path to save the image (default: gemini-images/<timestamp>.png in current directory)
        model: Gemini model to use (default: gemini-3.1-flash-image-preview)
        reference_images: List of paths to reference images (e.g., logos for subject consistency)
        aspect_ratio: Aspect ratio (e.g., '16:9', '1:1', '9:16'). Supported: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
        temperature: Generation temperature (default: 1.0, range: 0.0-2.0)
    
    Returns:
        dict with 'success', 'path', 'dimensions', 'size_bytes', 'model', and optional 'error'
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
    
    # Build parts list starting with prompt
    parts = [{'text': prompt}]
    
    # Add reference images if provided (for subject consistency/logo integration)
    if reference_images:
        for img_path in reference_images:
            try:
                img_data, mime_type = encode_image(img_path)
                parts.insert(0, {
                    'inlineData': {
                        'mimeType': mime_type,
                        'data': img_data
                    }
                })
            except Exception as e:
                return {
                    'success': False,
                    'error': f'Failed to encode reference image {img_path}: {str(e)}'
                }
    
    # Prepare request payload
    request = {
        'contents': [{
            'parts': parts
        }],
        'generationConfig': {
            'temperature': temperature,
            'topP': 0.95
        }
    }
    
    # Add aspect ratio if specified
    if aspect_ratio:
        valid_ratios = ['1:1', '3:2', '2:3', '3:4', '4:3', '4:5', '5:4', '8:1', '9:16', '16:9', '21:9']
        if aspect_ratio not in valid_ratios:
            return {
                'success': False,
                'error': f'Invalid aspect ratio. Supported: {", ".join(valid_ratios)}'
            }
        request['generationConfig']['aspectRatio'] = aspect_ratio
    
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
            'error': 'Usage: generate_image.py <prompt> [--output PATH] [--model MODEL] [--ref IMAGE...] [--aspect-ratio RATIO] [--temperature TEMP]'
        }, indent=2))
        sys.exit(1)
    
    # Parse arguments
    prompt = sys.argv[1]
    output_path = None
    model = 'gemini-3.1-flash-image-preview'
    reference_images = []
    aspect_ratio = None
    temperature = 1.0
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg in ['--output', '-o']:
            if i + 1 < len(sys.argv):
                output_path = sys.argv[i + 1]
                i += 2
            else:
                print(json.dumps({'success': False, 'error': f'{arg} requires a value'}, indent=2))
                sys.exit(1)
        
        elif arg in ['--model', '-m']:
            if i + 1 < len(sys.argv):
                model = sys.argv[i + 1]
                i += 2
            else:
                print(json.dumps({'success': False, 'error': f'{arg} requires a value'}, indent=2))
                sys.exit(1)
        
        elif arg in ['--ref', '--reference', '-r']:
            if i + 1 < len(sys.argv):
                reference_images.append(sys.argv[i + 1])
                i += 2
            else:
                print(json.dumps({'success': False, 'error': f'{arg} requires a value'}, indent=2))
                sys.exit(1)
        
        elif arg in ['--aspect-ratio', '--ar', '-a']:
            if i + 1 < len(sys.argv):
                aspect_ratio = sys.argv[i + 1]
                i += 2
            else:
                print(json.dumps({'success': False, 'error': f'{arg} requires a value'}, indent=2))
                sys.exit(1)
        
        elif arg in ['--temperature', '-t']:
            if i + 1 < len(sys.argv):
                try:
                    temperature = float(sys.argv[i + 1])
                    if not 0.0 <= temperature <= 2.0:
                        print(json.dumps({'success': False, 'error': 'Temperature must be between 0.0 and 2.0'}, indent=2))
                        sys.exit(1)
                except ValueError:
                    print(json.dumps({'success': False, 'error': 'Temperature must be a number'}, indent=2))
                    sys.exit(1)
                i += 2
            else:
                print(json.dumps({'success': False, 'error': f'{arg} requires a value'}, indent=2))
                sys.exit(1)
        
        else:
            print(json.dumps({'success': False, 'error': f'Unknown argument: {arg}'}, indent=2))
            sys.exit(1)
    
    result = generate_image(
        prompt=prompt,
        output_path=output_path,
        model=model,
        reference_images=reference_images if reference_images else None,
        aspect_ratio=aspect_ratio,
        temperature=temperature
    )
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result['success'] else 1)

if __name__ == '__main__':
    main()
