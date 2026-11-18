import PaperTheory.Core
import Mathlib.Tactic.Ring

set_option autoImplicit false

namespace PaperTheory

/-- A synthetic scalar example; it is not a formalization of a source paper. -/
def quadratic (target x : ℝ) : ℝ := (x - target) ^ 2

def quadraticStep (target η x : ℝ) : ℝ := (1 - η) * x + η * target

theorem quadratic_step_descent (target η x : ℝ)
    (hη : 0 ≤ η) (hη₂ : η ≤ 2) :
    quadratic target (quadraticStep target η x) ≤ quadratic target x := by
  have hfactor : (1 - η) ^ 2 ≤ 1 := by nlinarith
  have hid : quadratic target (quadraticStep target η x) =
      (1 - η) ^ 2 * quadratic target x := by
    unfold quadratic quadraticStep
    ring
  rw [hid]
  calc
    (1 - η) ^ 2 * quadratic target x ≤ 1 * quadratic target x :=
      mul_le_mul_of_nonneg_right hfactor (sq_nonneg (x - target))
    _ = quadratic target x := one_mul _

theorem quadratic_run_descent (target η x₀ : ℝ)
    (hη : 0 ≤ η) (hη₂ : η ≤ 2) (n : ℕ) :
    quadratic target (run (quadraticStep target η) x₀ (n + 1)) ≤
      quadratic target (run (quadraticStep target η) x₀ n) := by
  exact quadratic_step_descent target η _ hη hη₂

end PaperTheory
