from macrolog_core import TOTAL_TARGETS, Variant


def test_variant_output_dims():
    assert Variant.A.num_outputs == 4
    assert Variant.B.num_outputs == 5
    assert Variant.C.num_outputs == 5
    assert not Variant.A.predicts_mass


def test_targets():
    assert TOTAL_TARGETS == ("energy_kcal", "fat_g", "carbs_g", "protein_g")
