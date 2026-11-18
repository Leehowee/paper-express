import Mathlib.Analysis.Convex.Function
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

set_option autoImplicit false

namespace PaperTheory

/-- Feasibility is part of the definition, preventing an empty-domain optimum. -/
def Minimizer {X : Type*} (f : X → ℝ) (S : Set X) (x : X) : Prop :=
  x ∈ S ∧ ∀ y ∈ S, f x ≤ f y

/-- An optimum transfers only when the parameterization covers the original set. -/
theorem minimizer_transfer {X Z : Type*} (f : X → ℝ)
    (S : Set X) (T : Set Z) (encode : Z → X) (z : Z)
    (feasible : ∀ w ∈ T, encode w ∈ S)
    (covers : ∀ x ∈ S, ∃ w ∈ T, encode w = x)
    (optimal : Minimizer (fun w => f (encode w)) T z) :
    Minimizer f S (encode z) := by
  refine ⟨feasible z optimal.1, ?_⟩
  intro x hx
  obtain ⟨w, hw, heq⟩ := covers x hx
  simpa only [heq] using optimal.2 w hw

/-- Two exact block minima improve the same objective on a product domain. -/
theorem two_block_descent {X Y : Type*} (f : X → Y → ℝ)
    (S : Set X) (T : Set Y) (x₀ x₁ : X) (y₀ y₁ : Y)
    (hx₀ : x₀ ∈ S) (hy₀ : y₀ ∈ T)
    (first : Minimizer (fun x => f x y₀) S x₁)
    (second : Minimizer (fun y => f x₁ y) T y₁) :
    f x₁ y₁ ≤ f x₀ y₀ :=
  le_trans (second.2 y₀ hy₀) (first.2 x₀ hx₀)

/-- A recursive run records the actual update operation. -/
def run {X : Type*} (step : X → X) (x₀ : X) : ℕ → X
  | 0 => x₀
  | n + 1 => step (run step x₀ n)

theorem run_feasible {X : Type*} (S : Set X) (step : X → X) (x₀ : X)
    (initial : x₀ ∈ S) (preserves : ∀ x ∈ S, step x ∈ S) :
    ∀ n, run step x₀ n ∈ S := by
  intro n
  induction n with
  | zero => exact initial
  | succ n ih => exact preserves _ ih

/-- This proves consecutive objective descent, not iterate convergence. -/
theorem run_descent {X : Type*} (S : Set X) (f : X → ℝ)
    (step : X → X) (x₀ : X)
    (initial : x₀ ∈ S) (preserves : ∀ x ∈ S, step x ∈ S)
    (decreases : ∀ x ∈ S, f (step x) ≤ f x) (n : ℕ) :
    f (run step x₀ (n + 1)) ≤ f (run step x₀ n) := by
  exact decreases _ (run_feasible S step x₀ initial preserves n)

/-- A uniform approximation plus approximate optimization yields an explicit gap. -/
theorem approximate_optimum_transfer {X : Type*}
    (f g : X → ℝ) (S : Set X) (x y : X) (ε η : ℝ)
    (hx : x ∈ S) (hy : y ∈ S)
    (uniform : ∀ z ∈ S, |f z - g z| ≤ ε)
    (approximate : g x ≤ g y + η) :
    f x ≤ f y + η + 2 * ε := by
  have hxu := (abs_le.mp (uniform x hx)).2
  have hyl := (abs_le.mp (uniform y hy)).1
  linarith

/-- Convex slices give a convex upper envelope when an attaining selector exists.
The selector and envelope identities remain obligations for each application. -/
theorem convex_attained_envelope {E Y : Type*}
    [AddCommMonoid E] [Module ℝ E]
    (S : Set E) (T : Set Y) (F : E → Y → ℝ)
    (J : E → ℝ) (select : E → Y)
    (domain : Convex ℝ S)
    (slice : ∀ y ∈ T, ConvexOn ℝ S (fun x => F x y))
    (selected : ∀ x ∈ S, select x ∈ T)
    (attains : ∀ x ∈ S, J x = F x (select x))
    (upper : ∀ x ∈ S, ∀ y ∈ T, F x y ≤ J x) :
    ConvexOn ℝ S J := by
  refine ⟨domain, ?_⟩
  intro x hx y hy a b ha hb hab
  have hz : a • x + b • y ∈ S := domain hx hy ha hb hab
  have hs := selected (a • x + b • y) hz
  rw [attains _ hz]
  calc
    F (a • x + b • y) (select (a • x + b • y)) ≤
        a • F x (select (a • x + b • y)) +
        b • F y (select (a • x + b • y)) :=
      (slice _ hs).2 hx hy ha hb hab
    _ ≤ a • J x + b • J y := by
      simpa only [smul_eq_mul] using
        add_le_add (mul_le_mul_of_nonneg_left (upper x hx _ hs) ha)
          (mul_le_mul_of_nonneg_left (upper y hy _ hs) hb)

end PaperTheory
