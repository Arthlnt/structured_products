"""HTML slide-deck generation for structured product marketing
presentations.

Produces a self-contained, printable HTML presentation ("slides")
styled with the brand's colors and logo. Each presentation gets its own
driver script (e.g. ``build_presentation.py``) that assembles slides
from the shared building blocks defined here (``theme``, ``charts``,
``deck``).
"""

from __future__ import annotations
