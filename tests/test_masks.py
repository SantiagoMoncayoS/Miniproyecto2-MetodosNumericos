
from src.geometry import make_grid, plate_masks

def test_plate_masks_exist():
    # choose ny that doesn't align exactly to stress the robust selection
    x, y, dx, dy = make_grid(137, 109, 8.0, 6.0)
    m1, m2 = plate_masks(x, y)
    assert m1.any() and m2.any()
    # rows are single lines
    assert m1.sum(axis=1).max() > 0 and m2.sum(axis=1).max() > 0
