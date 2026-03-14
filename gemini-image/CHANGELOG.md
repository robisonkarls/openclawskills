# CHANGELOG

## Version 2.0 - Subject Consistency & Logo Integration Update

**Date:** March 12, 2026

### Major Features Added

#### 1. Subject Consistency Support
- **Reference image input** via `--ref` flag (repeatable)
- Maintain logos, brand elements consistently across images
- Multi-reference support (logo + color palette + style guides)
- Base64 image encoding for API transmission

#### 2. Advanced Generation Controls
- **Aspect ratio** selection (`--aspect-ratio` or `--ar`)
  - 11 supported ratios: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
- **Temperature** control (`--temperature` or `-t`)
  - Range: 0.0 - 2.0
  - Fine-tune creativity vs consistency
- **Improved argument parsing** with named flags

#### 3. Enhanced Script Capabilities
- `encode_image()` function for reference image handling
- Support for PNG, JPG, JPEG, WebP, GIF formats
- Automatic MIME type detection
- Multiple reference images in single generation
- Better error messages and validation

### Documentation Additions

#### New Files
1. **README.md** - Skill overview and quick start guide
2. **references/api-reference.md** - Comprehensive technical documentation
   - Full API specification
   - Request/response formats
   - Error handling
   - Rate limits and quotas
   - Security best practices
3. **references/branding-workflows.md** - Professional branding guide
   - Setup recommendations
   - Product mockup workflows
   - Social media graphics
   - Marketing materials
   - Iterative refinement process
   - Batch generation scripts
4. **references/examples.md** - Real-world practical examples
   - Coffee shop branding suite
   - Tech startup assets
   - E-commerce product line
   - Event branding
   - Seasonal variations
5. **references/quick-reference.md** - Fast command lookup
   - Command structure
   - Common patterns
   - Troubleshooting quick fixes

#### Updated Files
1. **SKILL.md** - Complete rewrite with new features
   - Subject consistency guidelines
   - Creative brief prompt structure
   - Logo integration best practices
   - Conversational editing workflows
   - Advanced examples with multi-reference

### Script Changes

**scripts/generate_image.py**

#### Breaking Changes
- **Argument format changed** from positional to named flags
  - Old: `generate_image.py "prompt" output.png model`
  - New: `generate_image.py "prompt" --output output.png --model model`

#### New Functions
- `encode_image(image_path)` - Encode images to base64 with MIME detection
- Enhanced `generate_image()` signature:
  ```python
  def generate_image(
      prompt: str,
      output_path: str = None,
      model: str = 'gemini-3.1-flash-image-preview',
      reference_images: List[str] = None,
      aspect_ratio: str = None,
      temperature: float = 1.0
  ) -> dict:
  ```

#### New Parameters
- `reference_images` - List of image paths for subject consistency
- `aspect_ratio` - Control output dimensions
- `temperature` - Control creativity/consistency

#### API Request Changes
- `parts` array now supports both text and `inlineData` (images)
- Reference images prepended to parts list
- `aspectRatio` added to `generationConfig`
- Dynamic `temperature` instead of hardcoded 1.0

#### Improved Error Handling
- Validation for aspect ratios
- File existence checks for reference images
- Better error messages with context
- Temperature range validation (0.0-2.0)

### Use Cases Enabled

1. **Brand Consistency** - Use same logo across product mockups
2. **Multi-Channel Marketing** - Consistent branding across social platforms
3. **Product Photography** - Generate product photos with logo integration
4. **Packaging Design** - Logo on boxes, labels, tags
5. **Social Media Templates** - Branded post templates
6. **Marketing Collateral** - Business cards, flyers, banners
7. **Iterative Design** - Refine images by referencing previous outputs

### Technical Improvements

- Type hints added (`typing.List`, `typing.Optional`)
- Better separation of concerns
- Modular function design
- Comprehensive docstrings
- JSON error responses
- Exit codes (0 = success, 1 = error)

### Migration Guide

#### Old Usage
```bash
scripts/generate_image.py "A mountain landscape" ./output.png
```

#### New Usage (Equivalent)
```bash
scripts/generate_image.py "A mountain landscape" --output ./output.png
```

#### New Capabilities
```bash
# With logo
scripts/generate_image.py \
  "Coffee mug with logo" \
  --ref ./logo.png \
  --ar 4:5 \
  --output ./mug.png

# With multiple references
scripts/generate_image.py \
  "Instagram post" \
  --ref ./logo.png \
  --ref ./colors.png \
  --ar 1:1 \
  --temperature 0.5
```

### Documentation Structure

```
gemini-image/
├── README.md                      # Quick start & overview
├── SKILL.md                       # Complete documentation
├── CHANGELOG.md                   # This file
├── scripts/
│   └── generate_image.py          # Enhanced script
└── references/
    ├── api-reference.md           # Technical API docs
    ├── branding-workflows.md      # Professional workflows
    ├── examples.md                # Real-world examples
    └── quick-reference.md         # Command cheat sheet
```

### Known Limitations

- Reference images add to token cost (based on resolution)
- Maximum 10 reference images per generation (API limit)
- Aspect ratio must be from supported list
- Subject consistency works best with clean, high-contrast reference images

### Future Enhancements

Potential improvements for future versions:
- Batch processing wrapper script
- Style preset library
- Brand asset management helper
- Generation history/versioning
- A/B comparison tools

---

## Version 1.0 - Initial Release

**Date:** March 11, 2026

### Features
- Basic text-to-image generation
- Gemini 3.1 Flash Image Preview model support
- Automatic timestamped output
- JSON response format
- API key management via settings file
- Error handling

### Files
- `SKILL.md` - Basic documentation
- `scripts/generate_image.py` - Generation script
- `references/api-reference.md` - Basic API info
