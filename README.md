# OpenClaw Skills

A collection of OpenClaw agent skills for extending agent capabilities.

## Skills

### gemini-image

Generate images from text prompts using Google Gemini 3.1 Flash Image Preview.

**Features:**
- Text-to-image generation via Gemini API
- Automatic workspace organization (saves to `gemini-images/` folder)
- Timestamp-based file naming
- JSON response with image metadata

**Quick Start:**
```bash
scripts/generate_image.py "A cute robot assistant working at a desk"
```

See [gemini-image/SKILL.md](gemini-image/SKILL.md) for full documentation.

## Installation

To use these skills with OpenClaw:

1. Copy the skill directory to your OpenClaw workspace skills folder
2. The skill will be automatically available to all agents

## Requirements

- OpenClaw 2026.3.x or later
- Gemini API key configured in `~/.gemini/settings.json` or `GEMINI_API_KEY` environment variable

## License

MIT
