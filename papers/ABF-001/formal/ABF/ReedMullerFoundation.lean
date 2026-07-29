import ABF.MomentKernel
import Mathlib

namespace ABF

abbrev Bit := ZMod 2
abbrev Cube (n : ℕ) := Fin n → Bit
abbrev BooleanFunction (n : ℕ) := Cube n → Bit

end ABF
