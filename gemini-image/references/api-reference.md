# Gemini Image Generation API Reference

## Available Models

### gemini-3.1-flash-image-preview (Recommended)

**Best for:** General-purpose image generation with fast response times

**Specifications:**
- Maximum input tokens: 131,072
- Maximum output tokens: 32,768
- Image consumption: Up to 2520 tokens per generated image
- Supported aspect ratios: 1:1, 3:2, 2:3, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
- Output format: PNG (typically 1408×768 or similar)
- Temperature: 0.0-2.0 (default 1.0)
- TopP: 0.0-1.0 (default 0.95)

## Model Selection

Use `gemini-3.1-flash-image-preview` unless you have a specific reason to use another model.

## Prompting Best Practices

### Effective Prompts

✅ **Good prompts are:**
- Descriptive and specific about the desired image
- Clear about style, mood, and composition
- Concrete about subjects and settings

**Examples:**
- "A futuristic robot assistant working at a computer desk with colorful code on the screen, warm lighting, cozy atmosphere"
- "Minimalist logo design for a tech startup, blue and orange color scheme, clean geometric shapes"
- "Photo-realistic portrait of a golden retriever puppy playing in a sunlit garden"

### Ineffective Prompts

❌ **Avoid:**
- Vague or overly broad descriptions ("a nice picture")
- Conflicting style instructions
- Extremely complex multi-subject scenes (limit to 2-3 main subjects)

## API Limits

- **Rate limits:** Subject to Google Cloud quotas
- **Context window:** 131,072 input tokens
- **Output tokens:** Up to 32,768 (images consume ~2520 tokens each)
- **File size:** Generated images typically 1-3 MB

## Troubleshooting

### No image returned
- Check API key is valid
- Verify prompt doesn't violate content policies
- Ensure network connectivity

### Poor quality images
- Add more detail to prompt (style, lighting, composition)
- Specify desired aspect ratio in prompt
- Adjust temperature (lower = more consistent, higher = more creative)

### Rate limit errors
- Wait before retrying
- Check Google Cloud quota status
- Consider batching requests
