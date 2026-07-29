import HINC.Core
import Mathlib

/-!
# HINC normalized Hochschild foundation: first formal lane

This file models the dual numbers as the trivial square-zero extension and
formalizes the square-zero generator and characteristic-two boundary
cancellation used in Proposition 2.1 of the manuscript. It is a foundation for,
not yet the completion of, the normalized-cochain and Gerstenhaber-bracket proof.
-/

namespace HINC

variable {R : Type*} [CommRing R] [CharP R 2]

/-- The dual-number algebra `R[epsilon]/(epsilon^2)` as `R ⊕ R epsilon`. -/
abbrev DualNumber (R : Type*) [CommRing R] :=
  TrivSqZeroExt R R

/-- The square-zero generator `epsilon = (0,1)`. -/
def epsilon (R : Type*) [CommRing R] : DualNumber R :=
  TrivSqZeroExt.inr 1

/-- The generator of the dual numbers has square zero. -/
@[simp] theorem epsilon_sq : epsilon R * epsilon R = 0 := by
  ext <;> simp [epsilon]

/-- The two boundary terms in the normalized Hochschild differential cancel in
characteristic two. -/
theorem epsilon_boundary_cancel (x : DualNumber R) :
    epsilon R * x + x * epsilon R = 0 := by
  ext <;> simp [epsilon, CharTwo.add_self_eq_zero]

/-- Evaluation of the normalized differential on the unique basis tensor after
all interior `epsilon^2` terms have vanished. -/
def normalizedDifferentialValue (x : DualNumber R) : DualNumber R :=
  epsilon R * x + x * epsilon R

/-- The normalized differential evaluation vanishes for every represented
cochain value. -/
@[simp] theorem normalizedDifferentialValue_zero (x : DualNumber R) :
    normalizedDifferentialValue x = 0 := by
  exact epsilon_boundary_cancel x

/-- On represented normalized cochain values, cup product is multiplication in
the dual-number algebra. -/
def normalizedCupValue (x y : DualNumber R) : DualNumber R :=
  x * y

/-- The represented cup product is associative. -/
theorem normalizedCupValue_assoc (x y z : DualNumber R) :
    normalizedCupValue (normalizedCupValue x y) z =
      normalizedCupValue x (normalizedCupValue y z) := by
  simp [normalizedCupValue, mul_assoc]

/-- Projection to the `epsilon` coefficient. -/
def epsilonCoefficient : DualNumber R →ₗ[R] R :=
  TrivSqZeroExt.sndHom R R

@[simp] theorem epsilonCoefficient_epsilon :
    epsilonCoefficient (epsilon R) = 1 := by
  simp [epsilonCoefficient, epsilon]

/-- The coefficient projection obeys the dual-number product rule. -/
theorem epsilonCoefficient_mul (x y : DualNumber R) :
    epsilonCoefficient (x * y) =
      x.fst * epsilonCoefficient y + y.fst * epsilonCoefficient x := by
  simp [epsilonCoefficient, TrivSqZeroExt.snd_mul, mul_comm]

#print axioms epsilon_sq
#print axioms epsilon_boundary_cancel
#print axioms normalizedDifferentialValue_zero
#print axioms normalizedCupValue_assoc
#print axioms epsilonCoefficient_mul

end HINC
