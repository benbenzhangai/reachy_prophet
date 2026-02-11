"""Tarot card drawing tool for Reachy Prophet."""

import logging
import random
from typing import Any

from reachy_mini_conversation_app.tools.core_tools import Tool, ToolDependencies

logger = logging.getLogger(__name__)

# 78-card Rider-Waite-Smith deck
MAJOR_ARCANA = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

MINOR_ARCANA = {
    "Wands": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
              "Page", "Knight", "Queen", "King"],
    "Cups": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
             "Page", "Knight", "Queen", "King"],
    "Swords": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
               "Page", "Knight", "Queen", "King"],
    "Pentacles": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                  "Page", "Knight", "Queen", "King"]
}

# Spread definitions
SPREADS = {
    "1-card": ["Present/Focus"],
    "3-card-past-present-future": ["Past", "Present", "Future"],
    "3-card-situation-action-outcome": ["Situation", "Action", "Outcome"],
    "5-card-decision": ["Current State", "Path A", "Path B", "Advice", "Likely Outcome"],
    "celtic-cross": [
        "Present", "Challenge", "Past", "Future", "Above/Goal",
        "Below/Foundation", "Advice", "External", "Hopes/Fears", "Outcome"
    ]
}


def get_full_deck() -> list[str]:
    """Return complete 78-card deck."""
    deck = MAJOR_ARCANA.copy()
    for suit, ranks in MINOR_ARCANA.items():
        deck.extend([f"{rank} of {suit}" for rank in ranks])
    return deck


class DrawTarotCards(Tool):
    """Draw tarot cards for a reading with optional reversals."""

    name = "draw_tarot_cards"
    description = (
        "Draw tarot cards for a reading. Use this at the START of a reading to draw cards. "
        "Returns the drawn cards with their positions and orientations. "
        "Common spreads: 1-card (quick insight), 3-card-past-present-future (timeline), "
        "3-card-situation-action-outcome (decision-focused), 5-card-decision (comparing paths), "
        "celtic-cross (deep exploration)."
    )
    parameters_schema = {
        "type": "object",
        "properties": {
            "count": {
                "type": "integer",
                "description": "Number of cards to draw (1-10)",
                "minimum": 1,
                "maximum": 10,
            },
            "spread": {
                "type": "string",
                "description": (
                    "The spread type: '1-card', '3-card-past-present-future', "
                    "'3-card-situation-action-outcome', '5-card-decision', or 'celtic-cross'"
                ),
                "enum": list(SPREADS.keys()),
            },
            "allow_reversals": {
                "type": "boolean",
                "description": "Whether to allow reversed cards (default: true)",
                "default": True,
            },
        },
        "required": ["count", "spread"],
    }

    async def __call__(self, deps: ToolDependencies, **kwargs: Any) -> dict[str, Any]:
        """Execute tarot card drawing."""
        count = kwargs.get("count", 1)
        spread = kwargs.get("spread", "1-card")
        allow_reversals = kwargs.get("allow_reversals", True)

        logger.info(f"Drawing {count} tarot cards with spread: {spread}")

        # Get the deck and draw cards
        deck = get_full_deck()
        drawn_cards = random.sample(deck, min(count, len(deck)))

        # Get positions for the spread
        positions = SPREADS.get(spread, SPREADS["1-card"])
        if len(positions) != count:
            logger.warning(
                f"Spread {spread} has {len(positions)} positions but {count} cards requested"
            )
            # Pad or truncate positions as needed
            if len(positions) < count:
                positions = positions + [f"Position {i+1}" for i in range(len(positions), count)]
            else:
                positions = positions[:count]

        # Determine orientations
        results = []
        for card, position in zip(drawn_cards, positions):
            if allow_reversals and random.random() < 0.5:
                orientation = "Reversed"
            else:
                orientation = "Upright"

            results.append({
                "position": position,
                "card": card,
                "orientation": orientation
            })

        # Format the output
        cards_summary = "\n".join(
            [f"- **{r['position']}**: {r['card']} ({r['orientation']})" for r in results]
        )

        return {
            "status": "success",
            "spread": spread,
            "reversals_enabled": allow_reversals,
            "cards": results,
            "summary": f"Drew {count} cards:\n{cards_summary}"
        }
