import ABF.MomentKernel
import Mathlib

/-!
# ABF-001 A02: literal Reed--Muller foundation

This file begins A02 from Boolean functions on the literal binary cube. It
introduces monomial functions, Reed--Muller spans, the truth-table pairing, and
moment functionals. The complete duality theorem and degree criterion remain
separate obligations and are not claimed by this file.
-/

namespace ABF

/-- The coefficient field used throughout ABF-001. -/
abbrev Bit := ZMod 2

/-- The `n`-dimensional binary cube. -/
abbrev Cube (n : ℕ) := Fin n → Bit

/-- Scalar Boolean functions represented by their complete truth tables. -/
abbrev BooleanFunction (n : ℕ) := Cube n → Bit

/-- The squarefree monomial indexed by a finite variable set. -/
def monomial {n : ℕ} (variables : Finset (Fin n)) : BooleanFunction n :=
  fun x => ∏ i ∈ variables, x i

@[simp] theorem monomial_empty {n : ℕ} (x : Cube n) :
    monomial (∅ : Finset (Fin n)) x = 1 := by
  simp [monomial]

@[simp] theorem monomial_insert {n : ℕ} {variables : Finset (Fin n)}
    {i : Fin n} (hi : i ∉ variables) (x : Cube n) :
    monomial (insert i variables) x = x i * monomial variables x := by
  simp [monomial, hi]

/-- The set of squarefree monomials of degree at most `r`. -/
def reedMullerGenerators (r n : ℕ) : Set (BooleanFunction n) :=
  {f | ∃ variables : Finset (Fin n),
    variables.card ≤ r ∧ f = monomial variables}

/-- Reed--Muller functions of order at most `r`, defined as the span of the
literal squarefree monomial functions of degree at most `r`. -/
def reedMuller (r n : ℕ) : Submodule Bit (BooleanFunction n) :=
  Submodule.span Bit (reedMullerGenerators r n)

/-- Every allowed monomial lies in the corresponding Reed--Muller span. -/
theorem monomial_mem_reedMuller {r n : ℕ} {variables : Finset (Fin n)}
    (hdegree : variables.card ≤ r) :
    monomial variables ∈ reedMuller r n := by
  exact Submodule.subset_span ⟨variables, hdegree, rfl⟩

/-- Reed--Muller spans are monotone in their order parameter. -/
theorem reedMuller_mono {r s n : ℕ} (hrs : r ≤ s) :
    reedMuller r n ≤ reedMuller s n := by
  apply Submodule.span_mono
  rintro f ⟨variables, hdegree, rfl⟩
  exact ⟨variables, hdegree.trans hrs, rfl⟩

/-- The complete truth-table pairing over `GF(2)`. -/
def truthInner {n : ℕ} (f g : BooleanFunction n) : Bit :=
  ∑ x, f x * g x

@[simp] theorem truthInner_zero_left {n : ℕ} (g : BooleanFunction n) :
    truthInner 0 g = 0 := by
  simp [truthInner]

@[simp] theorem truthInner_zero_right {n : ℕ} (f : BooleanFunction n) :
    truthInner f 0 = 0 := by
  simp [truthInner]

/-- Additivity in the first argument of the truth-table pairing. -/
theorem truthInner_add_left {n : ℕ} (f g h : BooleanFunction n) :
    truthInner (f + g) h = truthInner f h + truthInner g h := by
  simp [truthInner, add_mul, Finset.sum_add_distrib]

/-- Additivity in the second argument of the truth-table pairing. -/
theorem truthInner_add_right {n : ℕ} (f g h : BooleanFunction n) :
    truthInner f (g + h) = truthInner f g + truthInner f h := by
  simp [truthInner, mul_add, Finset.sum_add_distrib]

/-- The moment of `f` indexed by the squarefree monomial on `variables`. -/
def moment {n : ℕ} (variables : Finset (Fin n)) (f : BooleanFunction n) : Bit :=
  truthInner (monomial variables) f

@[simp] theorem moment_zero {n : ℕ} (variables : Finset (Fin n)) :
    moment variables (0 : BooleanFunction n) = 0 := by
  simp [moment]

/-- Moment functionals are additive in the Boolean function. -/
theorem moment_add {n : ℕ} (variables : Finset (Fin n))
    (f g : BooleanFunction n) :
    moment variables (f + g) = moment variables f + moment variables g := by
  exact truthInner_add_right (monomial variables) f g

/-- The literal all-moments-vanish predicate used in the Reed--Muller degree
criterion. -/
def MomentsVanishThrough {n : ℕ} (r : ℕ) (f : BooleanFunction n) : Prop :=
  ∀ variables : Finset (Fin n), variables.card ≤ r → moment variables f = 0

#print axioms monomial_mem_reedMuller
#print axioms reedMuller_mono
#print axioms truthInner_add_left
#print axioms truthInner_add_right
#print axioms moment_add

end ABF
