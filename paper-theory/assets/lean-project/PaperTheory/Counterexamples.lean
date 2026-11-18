import PaperTheory.Core
import Mathlib.Tactic.NormNum

set_option autoImplicit false

namespace PaperTheory

theorem constant_has_two_minimizers :
    Minimizer (fun (_ : ℝ) => 0) Set.univ 0 ∧
    Minimizer (fun (_ : ℝ) => 0) Set.univ 1 ∧ (0 : ℝ) ≠ 1 := by
  norm_num [Minimizer]

/-- The pointwise minimum of two convex quadratics need not be convex. -/
def twoWell (x : ℝ) : ℝ := min (x ^ 2) ((x - 1) ^ 2)

theorem twoWell_not_convex : ¬ ConvexOn ℝ Set.univ twoWell := by
  intro h
  have hconvex := h.2
  have hmid := hconvex (x := (0 : ℝ)) (by trivial) (y := (1 : ℝ))
    (by trivial) (a := (1 / 2 : ℝ)) (b := (1 / 2 : ℝ))
    (by norm_num) (by norm_num) (by norm_num)
  norm_num [twoWell] at hmid

/-- Squaring a one-sided bound on a difference of maxima is not valid. -/
theorem squared_one_sided_max_bound_fails :
    ¬ ((max (0 : ℝ) 0 - max 1 2) ^ 2 ≤
      (max ((0 : ℝ) - 1) (0 - 2)) ^ 2) := by
  norm_num

end PaperTheory
