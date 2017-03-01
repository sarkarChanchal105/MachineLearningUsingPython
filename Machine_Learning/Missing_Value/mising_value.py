from fancyimpute import NuclearNormMinimization

solver = NuclearNormMinimization(
    min_value=0.0,
    max_value=1.0,
    error_tolerance=0.0005)

# X_incomplete has missing data which is represented with NaN values
X_filled = solver.complete(X_incomplete)