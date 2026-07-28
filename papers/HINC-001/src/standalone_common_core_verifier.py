"""Compatibility entry point for the standalone HINC verifier."""

from mcrc_hidden_infinitesimal_noncommutativity_standalone import *  # noqa: F401,F403
from mcrc_hidden_infinitesimal_noncommutativity_standalone import main


if __name__ == "__main__":
    raise SystemExit(main())
