# trajectory

Input:
  - angle = 50
  - velocity = 100
  - gravity = 9.8
  - initial height = 50

Used formulas:
  - y = h + v * sin(α) * t - g * t² / 2
  - x = v * cos(α) * t
  - t = (v * sin(α) + √((v * sin(α))² + 2 * g * h)) / g

Result:

![](animation_.gif)

Some others:
  - x = v * cos(α) * t
  - y = h + v * sin(α) * t - g * t² / 2
  - y = h + x * tan(α) - g * x² / 2 * v² * cos²(α)
  - y = h + x * (v * sin(α)) / (v * cos(α)) - g * (x / v * cos(α))² / 2
  - t = 2 * v * sin(α) / g
  - t = (v * sin(α) + √((v * sin(α))² + 2 * g * h)) / g
  - h_max = h + v² * sin(α)² / (2 * g)
