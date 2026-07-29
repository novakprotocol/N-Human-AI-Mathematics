import Mathlib.LinearAlgebra.Basic
import Mathlib.Tactic

namespace ABF

universe u v w x

variable {K : Type u} [Field K]
variable {V : Type v} [AddCommGroup V] [Module K V]
variable {Q : Type w} [AddCommGroup Q] [Module K Q]
variable {ι : Type x}

def generatorSpan (μ : ι → V) : Submodule K V :=
  Submodule.span K (Set.range μ)

def AnnihilatesMoments (ell : V →ₗ[K] K) (μ : ι → V) : Prop :=
  ∀ i, ell (μ i) = 0

theorem generatorSpan_le_ker_iff
    (ell : V →ₗ[K] K) (μ : ι → V) :
    generatorSpan μ ≤ LinearMap.ker ell ↔ AnnihilatesMoments ell μ := by
  constructor
  · intro h i
    have hmem : μ i ∈ generatorSpan μ := by
      exact Submodule.subset_span (Set.mem_range_self i)
    have hker := h hmem
    simpa using hker
  · intro h
    rw [generatorSpan, Submodule.span_le]
    rintro y ⟨i, rfl⟩
    simpa using h i

def CoordinatesZero (y : ι → K) : Prop :=
  ∀ i, y i = 0

theorem mem_ker_iff_coordinatesZero
    (Phi : Q →ₗ[K] (ι → K)) (q : Q) :
    q ∈ LinearMap.ker Phi ↔ CoordinatesZero (Phi q) := by
  change Phi q = 0 ↔ ∀ i, Phi q i = 0
  constructor
  · intro h i
    rw [h]
    rfl
  · intro h
    funext i
    exact h i

theorem bidual_moment_incidence
    (moment : Q → ι → V)
    (ell : V →ₗ[K] K)
    (Phi : Q →ₗ[K] (ι → K))
    (compat : ∀ q i, Phi q i = ell (moment q i))
    (q : Q) :
    AnnihilatesMoments ell (moment q) ↔ q ∈ LinearMap.ker Phi := by
  rw [mem_ker_iff_coordinatesZero]
  constructor
  · intro h i
    rw [compat q i]
    exact h i
  · intro h i
    rw [← compat q i]
    exact h i

theorem bidual_span_kernel_incidence
    (moment : Q → ι → V)
    (ell : V →ₗ[K] K)
    (Phi : Q →ₗ[K] (ι → K))
    (compat : ∀ q i, Phi q i = ell (moment q i))
    (q : Q) :
    generatorSpan (moment q) ≤ LinearMap.ker ell ↔
      q ∈ LinearMap.ker Phi := by
  rw [generatorSpan_le_ker_iff]
  exact bidual_moment_incidence moment ell Phi compat q

#print axioms generatorSpan_le_ker_iff
#print axioms mem_ker_iff_coordinatesZero
#print axioms bidual_moment_incidence
#print axioms bidual_span_kernel_incidence

end ABF
