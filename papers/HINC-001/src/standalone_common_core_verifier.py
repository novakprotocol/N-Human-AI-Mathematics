"""Compatibility entry point for the standalone hidden-noncommutativity verifier."""

from n_mathlab.mcrc_hidden_infinitesimal_noncommutativity_standalone import *  # noqa: F401,F403
from n_mathlab.mcrc_hidden_infinitesimal_noncommutativity_standalone import main


if __name__ == "__main__":
    raise SystemExit(main())
