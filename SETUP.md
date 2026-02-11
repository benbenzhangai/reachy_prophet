# Reachy Prophet - Setup & Testing Guide

## Prerequisites

1. **Reachy Mini Lite** connected via USB
2. **OpenAI API Key** with access to Realtime API
3. **Python 3.10+** installed
4. **Reachy Mini daemon** running (robot control software)

## Quick Setup

### 1. Install Dependencies

The dependencies are already synced. If you need to re-sync:

```bash
cd /Users/huaiyu/Projects/reachy/reachy_prophet
uv sync
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root or export the variable:

```bash
export OPENAI_API_KEY="sk-your-key-here"
```

### 3. Verify Reachy Mini Connection

Make sure your Reachy Mini Lite is:
- Connected via USB
- Powered on
- Has the daemon running (usually auto-starts)

You can verify connection by checking if the robot is visible to the system.

## Running the App

### Option 1: Web Interface (Recommended for Testing)

```bash
cd /Users/huaiyu/Projects/reachy/reachy_prophet/src/reachy_mini_conversation_app
python main.py --gradio
```

Then open: http://127.0.0.1:7861/

### Option 2: Headless Mode (Voice Only)

```bash
cd /Users/huaiyu/Projects/reachy/reachy_prophet/src/reachy_mini_conversation_app
python main.py
```

This runs without a web interface - pure voice interaction.

## Testing Tarot Readings

### Test Flow

1. **Start the app** using one of the methods above
2. **Greet Reachy**: "Hello Reachy"
3. **Request a reading**: Try these examples:
   - "Can you do a tarot reading for me?"
   - "I need guidance about my career"
   - "Draw three cards for me about my relationship"
   - "Do a Celtic Cross spread about my future"

### What to Expect

1. **Reachy will respond** and may perform a `sweep_look` to "scan the energies"
2. **Clarify the question** if needed
3. **Draw cards** using the `draw_tarot_cards` tool
4. **Interpret each card** with position-aware meanings
5. **Provide synthesis** connecting all cards together
6. **Give actionable guidance** (3-7 concrete steps)
7. **Express emotions** matching the card energy (happy, curious, sad)
8. **End with guardrails** about real-world verification

### Example Test Questions

**Simple 1-Card Reading:**
- "Draw one card for today's guidance"
- "What do I need to know right now?"

**3-Card Timeline:**
- "Show me past, present, and future for my career change"
- "Draw three cards about my relationship"

**Decision Reading:**
- "I'm deciding between two job offers, can you help?"
- "Should I move to a new city or stay?"

**Deep Exploration:**
- "Do a Celtic Cross reading about my life purpose"
- "I need deep guidance about a major life transition"

## Troubleshooting

### Robot Not Moving

If Reachy doesn't move during readings:
1. Check USB connection
2. Verify daemon is running
3. Check motor status (should be enabled)

### No Voice Input/Output

1. Verify `OPENAI_API_KEY` is set
2. Check microphone permissions
3. Test with gradio interface first (easier to debug)

### Cards Not Drawing

If the `draw_tarot_cards` tool isn't being called:
1. Check that `tarot_tool.py` is in the profile folder
2. Verify `draw_tarot_cards` is listed in `tools.txt`
3. Look at console logs for errors

### LLM Not Following Instructions

If interpretations seem off:
1. Check `instructions.txt` is properly formatted
2. Verify the profile is locked to `_reachy_prophet_locked_profile`
3. Review the system prompt in console logs

## Development Tips

### Modify the Prophet Personality

Edit: `src/reachy_mini_conversation_app/profiles/_reachy_prophet_locked_profile/instructions.txt`

### Add New Tools

Create a new `.py` file in the profile folder, subclass `Tool`, and add the tool name to `tools.txt`

### Change Card Meanings

Edit: `src/reachy_mini_conversation_app/profiles/_reachy_prophet_locked_profile/card_meanings.md`

### Add More Movement

Look at `sweep_look.py` for examples of how to queue complex movement sequences.

## Next Steps

Once the basic tarot reading works:

1. **Add more dramatic movements** during card reveals
2. **Create custom emotions** for specific cards (e.g., mysterious look for The Moon)
3. **Add visual card display** (enable camera tool and show card images)
4. **Create additional prophet types** (oracle, I-Ching, runes) as separate profiles
5. **Publish to Hugging Face** for others to use

## Support

- **Reachy Mini Docs**: https://huggingface.co/docs/reachy_mini/
- **Discord Community**: https://discord.gg/Y7FgMqHsub
- **GitHub Issues**: For bugs and feature requests

---

Happy fortune telling! 🔮✨
