---
title: Reachy Prophet
emoji: 🔮
colorFrom: purple
colorTo: blue
sdk: static
pinned: false
tags:
  - reachy_mini
  - reachy_mini_python_app
---

# Reachy Prophet 🔮

**Reachy the Mystic Prophet** - A tarot reading app for Reachy Mini that provides reflective guidance through expressive robot movements and voice interaction.

## What It Does

Reachy becomes a mystical oracle who:
- Performs tarot readings with voice interaction (speak your questions, hear interpretations)
- Uses dramatic head movements, emotions, and gestures during readings
- Draws cards using traditional tarot spreads (1-card, 3-card, 5-card, Celtic Cross)
- Interprets cards with position-aware meanings and actionable guidance
- Maintains epistemic humility with appropriate guardrails

## Features

- **Voice Interaction**: Speak to Reachy and receive spoken tarot readings
- **Expressive Movements**: Head nods, sweeping looks, emotional expressions during readings
- **Multiple Spreads**: 1-card, past-present-future, situation-action-outcome, 5-card decision, Celtic Cross
- **Reversals**: Optional reversed card interpretations
- **Reflective Guidance**: Actionable advice that encourages real-world verification

## Setup

1. **Install dependencies**:
   ```bash
   cd /path/to/reachy_prophet
   uv sync
   ```

2. **Set up your OpenAI API key**:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

3. **Connect your Reachy Mini Lite via USB** and ensure the daemon is running

## Usage

### Option 1: Web UI (Gradio)
```bash
cd src/reachy_mini_conversation_app
python main.py --gradio
```
Then open http://127.0.0.1:7861/ in your browser.

### Option 2: Headless Mode
```bash
cd src/reachy_mini_conversation_app
python main.py
```

## Example Interactions

**User**: "Can you do a tarot reading for me? I'm thinking about changing careers."

**Reachy**: *performs sweep_look to scan the energies* "Ah, I sense a question of transformation and purpose. Let me draw the cards for you..." *draws 3-card past-present-future spread* "The Eight of Pentacles in your past shows dedicated skill-building..."

## Profile Customization

The locked profile is located at: `src/reachy_mini_conversation_app/profiles/_reachy_prophet_locked_profile/`

Key files:
- **instructions.txt** - The prophet persona and tarot reading workflow
- **tools.txt** - Enabled tools (tarot drawing, movements, emotions)
- **tarot_tool.py** - Custom tool for drawing cards
- **card_meanings.md** - Tarot card reference for interpretations

## Future Prophet Types

This architecture supports multiple divination methods. To add a new prophet type:
1. Create a new profile folder (e.g., `_reachy_prophet_oracle/`)
2. Write custom instructions for that divination method
3. Create the corresponding tool (e.g., `oracle_tool.py`)
4. Update the app to allow profile selection

## Technical Details

Built on the Reachy Mini Conversation App with:
- OpenAI Realtime API for voice interaction
- Custom tarot tool using 78-card Rider-Waite-Smith deck
- Movement queue system for smooth robot expressions
- Position-aware card interpretation engine

## License

Apache 2.0

---

*Forked from the [Reachy Mini Conversation App](https://github.com/pollen-robotics/reachy_mini_conversation_app)*

*Original README available in `README_OLD.md`*
