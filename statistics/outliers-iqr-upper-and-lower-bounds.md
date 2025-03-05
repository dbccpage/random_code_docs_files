# Outliers, IQR, Upper & Lower Bounds

## Outlier Detection Function Explanation

### Function Overview

The `calculate_outliers()` function uses the Interquartile Range (IQR) method to identify statistical outliers in a dataset.

### Key Components

#### `numpy.percentile()`

* Calculates specified percentile values in a dataset
* In this context:
  * `np.percentile(numbers, 25)` finds the 25th percentile (Q1)
  * `np.percentile(numbers, 75)` finds the 75th percentile (Q3)

#### Calculation Steps

1. **Q1 (First Quartile)**: 25% of data points are below this value
2. **Q3 (Third Quartile)**: 75% of data points are below this value
3. **IQR (Interquartile Range)**: Q3 - Q1
   * Represents the spread of the middle 50% of the data

#### Outlier Boundary Calculation

* `lower_bound = Q1 - (scale_factor * IQR)`
* `upper_bound = Q3 + (scale_factor * IQR)`
* Default `scale_factor` is 1.5 (standard for outlier detection)

#### Outlier Identification

* Outliers are data points OUTSIDE the range:
  * Below: `lower_bound`
  * Above: `upper_bound`

### Mathematical Representation

```
Outliers = {x | x < (Q1 - 1.5 * IQR) or x > (Q3 + 1.5 * IQR)}
```

### Example

```python
numbers = [1, 2, 3, 4, 5, 100, 200]
outliers = calculate_outliers(numbers)
# Likely returns [100, 200]
```



{% file src="../.gitbook/assets/random-dot-plot.py" %}

{% file src="../.gitbook/assets/statistics_in_python_0.0.0.1.ipynb" %}

{% file src="../.gitbook/assets/statistics_in_excel_0.0.0.1.xlsx" %}
