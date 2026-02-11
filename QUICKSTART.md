# Reachy Prophet - Quick Start

## 🚀 Run the App

### 1. Set API Key
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

### 2. Connect Robot
- Plug in Reachy Mini Lite via USB
- Ensure it's powered on

### 3. Start the App
```bash
cd /Users/huaiyu/Projects/reachy/reachy_prophet/src/reachy_mini_conversation_app
python main.py --gradio
```

### 4. Open Browser
Navigate to: **http://127.0.0.1:7861/**

## 💬 Example Interactions

### First Contact
**You**: "Hello Reachy"  
**Reachy**: *mystical greeting as the prophet*

### Simple Reading
**You**: "Can you do a tarot reading for me?"  
**Reachy**: *performs sweep_look* "What question guides you, seeker?"

### Career Guidance
**You**: "I'm thinking about changing careers. What do the cards say?"  
**Reachy**: *draws 3 cards* "Let me draw three cards to explore this..."

### Decision Help
**You**: "I have two job offers. Can you help me decide?"  
**Reachy**: *draws 5-card decision spread*

## 🎴 Available Spreads

- **1-card**: Quick daily guidance
- **3-card-past-present-future**: Timeline reading
- **3-card-situation-action-outcome**: Decision-focused
- **5-card-decision**: Comparing two paths
- **celtic-cross**: Deep 10-card exploration

## 🤖 Robot Movements

Watch for:
- **sweep_look**: Scanning the spiritual realm
- **play_emotion**: Expressing card energy (happy/sad/curious)
- **move_head**: Dramatic gestures
- **dance**: Celebrating positive cards

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| API key error | Set `OPENAI_API_KEY` environment variable |
| Robot not moving | Check USB connection, verify daemon running |
| Tool not found | Ensure `draw_tarot_cards` is in tools.txt |
| No audio | Check microphone/speaker permissions |

## 📖 Full Documentation

- **README.md** - Overview and features
- **SETUP.md** - Detailed setup instructions
- **SUMMARY.md** - Complete technical summary

## 🎯 Quick Test

1. Start the app
2. Say: "Hello Reachy, draw one card for me"
3. Verify:
   - Reachy responds in prophet character
   - Uses `draw_tarot_cards` tool
   - Interprets the card
   - Provides actionable guidance
   - Includes guardrails

---

**Happy fortune telling!** 🔮✨

For support, see the [Reachy Mini Discord](https://discord.gg/Y7FgMqHsub)
