# Independent audit, round 3

I rebuilt every scored carrier from numeric `sheets[].cells`, sorted by `sheets[].order`, and cut it at the raw `verses[].s/e` ranks. No predecoded grid letters or run-reported identity, p-value, or matched span enters a score. Public source bytes and their SHA-256 values are in [SOURCES3.json](SOURCES3.json); the full computed records are in [RESULTS3.json](RESULTS3.json).

Identity is exact written-unit matches divided by source units in a semiglobal alignment (match +2, substitution −1, gap −2; free carrier flanks). `CONFIRMED` requires at least 75% across at least 40 source units, more matches than all 1,000 within-column shuffles, and, for R1, more than all 1,000 sampled equal-length Gītā decoys. `WEAK` beats the shuffles and decoys but misses the length or identity gate. `NOT CONFIRMED` fails a control. `NOT REPRODUCIBLE` means a specific source or fixed raw-grid position cannot be obtained under the permitted rules. Shuffles test only the named carrier, so they do not adjust for the earlier search over many columns.

For R1, the W138 in-range ledger contains 437 distinct locators; two name Gītā-dhyāna rather than a Gītā verse and are explicitly marked. The GRETIL witness contains 700 numbered Gītā verses. Decoys are drawn with replacement from other verses with exactly the same written-unit length. The displayed `decoys ≥` is the number of those 1,000 whose alignment score (+2/−1/−2) is at least the claimed verse’s alignment score.

Witness limits matter: the public Ācāryabhakti and Pañcamahāguru pages print Prakrit despite Sanskrit labels, and the GRETIL Mahābhārata maṅgala has `caiva` where the claimed variant has `vyāsam`. The table scores the downloaded witnesses as printed; it does not silently replace their readings. Copyist-group carriers use only the marked group intervals allowed by BRIEF2, with numeric sounds decoded afresh. Archived band labels without a rank or marked-group rule remain unscored.

## Summary

| Group | Rows | Confirmed | Weak | Not confirmed | Not reproducible |
|---|---:|---:|---:|---:|---:|
| R1 | 437 | 42 | 297 | 66 | 32 |
| R2 | 17 | 3 | 12 | 2 | 0 |
| R3 | 88 | 15 | 41 | 32 | 0 |
| R4 | 165 | 23 | 112 | 17 | 13 |
| R5 | 2 | 1 | 1 | 0 | 0 |
| R6 | 5 | 0 | 2 | 2 | 1 |
| R7 | 5 | 0 | 2 | 0 | 3 |

## Every row

| Claim | Location | Verdict | Identity | Best shuffle | Decoys ≥ |
|---|---|---|---:|---:|---:|
| 1. R1 Gītā 1.27 | ch.14 mixed:E1:down | **WEAK** | 23/47 (48.9%) | 12 | 0 |
| 2. R1 Gītā 1.39 | ch.14 mixed:E1:down | **NOT CONFIRMED** | 27/46 (58.7%) | 12 | 19 |
| 3. R1 Gītā 18.2 | ch.14 mixed:E1:down | **WEAK** | 26/43 (60.5%) | 13 | 0 |
| 4. R1 Gītā 18.6 | ch.14 mixed:E1:down | **WEAK** | 32/46 (69.6%) | 13 | 0 |
| 5. R1 Gītā 1.39 | ch.14 short:E1:down | **NOT CONFIRMED** | 20/46 (43.5%) | 11 | 18 |
| 6. R1 Gītā 18.2 | ch.14 short:E1:down | **WEAK** | 24/43 (55.8%) | 12 | 0 |
| 7. R1 Gītā 18.6 | ch.14 short:E1:down | **WEAK** | 34/46 (73.9%) | 13 | 0 |
| 8. R1 Gītā 1.21 | ch.15 mixed:E1:down | **NOT CONFIRMED** | 15/40 (37.5%) | 10 | 19 |
| 9. R1 Gītā 2.50 | ch.15 mixed:E1:down | **CONFIRMED** | 32/41 (78.0%) | 10 | 0 |
| 10. R1 Gītā 3.30 | ch.15 mixed:E1:down | **CONFIRMED** | 35/44 (79.5%) | 11 | 0 |
| 11. R1 Gītā 7.1 | ch.15 mixed:E1:down | **WEAK** | 18/43 (41.9%) | 10 | 0 |
| 12. R1 Gītā 7.8 | ch.15 mixed:E1:down | **NOT CONFIRMED** | 24/41 (58.5%) | 10 | 20 |
| 13. R1 Gītā 2.50 | ch.15 short:E1:down | **WEAK** | 27/41 (65.9%) | 10 | 0 |
| 14. R1 Gītā 3.30 | ch.15 short:E1:down | **WEAK** | 30/44 (68.2%) | 12 | 0 |
| 15. R1 Gītā 1.34 | ch.16 mixed:E1:down | **WEAK** | 21/40 (52.5%) | 10 | 0 |
| 16. R1 Gītā 1.4 | ch.16 mixed:E1:down | **NOT CONFIRMED** | 9/38 (23.7%) | 9 | 0 |
| 17. R1 Gītā 1.46 | ch.16 mixed:E1:down | **WEAK** | 19/47 (40.4%) | 13 | 0 |
| 18. R1 Gītā 2.41 | ch.16 mixed:E1:down | **WEAK** | 27/44 (61.4%) | 12 | 0 |
| 19. R1 Gītā 1.4 | ch.16 package:16-short:E1:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 20. R1 Gītā 2.41 | ch.16 package:16-short:E1:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 21. R1 Gītā 1.4 | ch.16 short:E1:down | **WEAK** | 13/38 (34.2%) | 9 | 0 |
| 22. R1 Gītā 2.41 | ch.16 short:E1:down | **WEAK** | 24/44 (54.5%) | 10 | 0 |
| 23. R1 Gītā 14.10 | ch.17 mixed:E1:down | **WEAK** | 25/42 (59.5%) | 13 | 0 |
| 24. R1 Gītā 2.14 | ch.17 mixed:E1:down | **WEAK** | 30/43 (69.8%) | 11 | 0 |
| 25. R1 Gītā 2.6 | ch.17 mixed:E1:down | **WEAK** | 38/58 (65.5%) | 14 | 0 |
| 26. R1 Gītā 7.3 | ch.17 mixed:E1:down | **WEAK** | 24/44 (54.5%) | 12 | 0 |
| 27. R1 Gītā 14.10 | ch.17 short:E1:down | **WEAK** | 19/42 (45.2%) | 11 | 0 |
| 28. R1 Gītā 2.6 | ch.17 short:E1:down | **WEAK** | 32/58 (55.2%) | 13 | 0 |
| 29. R1 Gītā 7.3 | ch.17 short:E1:down | **WEAK** | 20/44 (45.5%) | 13 | 0 |
| 30. R1 Gītā 14.15 | ch.18 mixed:E1:down | **WEAK** | 32/38 (84.2%) | 11 | 0 |
| 31. R1 Gītā 18.62 | ch.18 mixed:E2:up | **WEAK** | 24/45 (53.3%) | 12 | 0 |
| 32. R1 Gītā 2.67 | ch.18 mixed:E2:up | **CONFIRMED** | 33/42 (78.6%) | 12 | 0 |
| 33. R1 Gītā 8.13 | ch.18 mixed:E2:up | **WEAK** | 35/47 (74.5%) | 15 | 0 |
| 34. R1 Gītā 14.15 | ch.18 package:18-short:E1:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 35. R1 Gītā 18.62 | ch.18 package:18-short:E2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 36. R1 Gītā 2.67 | ch.18 package:18-short:E2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 37. R1 Gītā 8.13 | ch.18 package:18-short:E2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 38. R1 Gītā 14.15 | ch.18 short:E1:down | **WEAK** | 27/38 (71.1%) | 10 | 0 |
| 39. R1 Gītā 18.62 | ch.18 short:E2:up | **NOT CONFIRMED** | 17/45 (37.8%) | 13 | 21 |
| 40. R1 Gītā 2.67 | ch.18 short:E2:up | **WEAK** | 24/42 (57.1%) | 12 | 0 |
| 41. R1 Gītā 8.13 | ch.18 short:E2:up | **WEAK** | 24/47 (51.1%) | 15 | 0 |
| 42. R1 Gītā 3.18 | ch.19 mixed:E1:down | **WEAK** | 31/42 (73.8%) | 12 | 0 |
| 43. R1 Gītā 3.21 | ch.19 mixed:E1:down | **CONFIRMED** | 34/44 (77.3%) | 13 | 0 |
| 44. R1 Gītā 1.27 | ch.19 mixed:E2:up | **WEAK** | 35/47 (74.5%) | 13 | 0 |
| 45. R1 Gītā 1.39 | ch.19 mixed:E2:up | **NOT CONFIRMED** | 32/46 (69.6%) | 13 | 18 |
| 46. R1 Gītā 1.45 | ch.19 mixed:E2:up | **WEAK** | 20/42 (47.6%) | 13 | 0 |
| 47. R1 Gītā 18.2 | ch.19 mixed:E2:up | **WEAK** | 32/43 (74.4%) | 12 | 0 |
| 48. R1 Gītā 18.6 | ch.19 mixed:E2:up | **CONFIRMED** | 36/46 (78.3%) | 13 | 0 |
| 49. R1 Gītā 3.18 | ch.19 short:E1:down | **WEAK** | 27/42 (64.3%) | 12 | 0 |
| 50. R1 Gītā 3.21 | ch.19 short:E1:down | **WEAK** | 23/44 (52.3%) | 12 | 0 |
| 51. R1 Gītā 1.27 | ch.19 short:E2:up | **WEAK** | 27/47 (57.4%) | 14 | 0 |
| 52. R1 Gītā 18.2 | ch.19 short:E2:up | **WEAK** | 28/43 (65.1%) | 13 | 0 |
| 53. R1 Gītā 18.6 | ch.19 short:E2:up | **WEAK** | 30/46 (65.2%) | 13 | 0 |
| 54. R1 Gītā 2.12 | ch.20 mixed:E1:down | **WEAK** | 25/39 (64.1%) | 11 | 0 |
| 55. R1 Gītā 3.11 | ch.20 mixed:E1:down | **CONFIRMED** | 31/40 (77.5%) | 12 | 0 |
| 56. R1 Gītā 4.9 | ch.20 mixed:E1:down | **CONFIRMED** | 37/46 (80.4%) | 17 | 0 |
| 57. R1 Gītā 1.21 | ch.20 mixed:E2:up | **CONFIRMED** | 31/40 (77.5%) | 11 | 0 |
| 58. R1 Gītā 1.4 | ch.20 mixed:E2:up | **WEAK** | 16/38 (42.1%) | 9 | 0 |
| 59. R1 Gītā 14.7 | ch.20 mixed:E2:up | **NOT CONFIRMED** | 34/44 (77.3%) | 11 | 12 |
| 60. R1 Gītā 2.50 | ch.20 mixed:E2:up | **CONFIRMED** | 31/41 (75.6%) | 10 | 0 |
| 61. R1 Gītā 3.30 | ch.20 mixed:E2:up | **CONFIRMED** | 37/44 (84.1%) | 12 | 0 |
| 62. R1 Gītā 7.1 | ch.20 mixed:E2:up | **WEAK** | 28/43 (65.1%) | 10 | 0 |
| 63. R1 Gītā 7.8 | ch.20 mixed:E2:up | **NOT CONFIRMED** | 29/41 (70.7%) | 10 | 17 |
| 64. R1 Gītā 2.12 | ch.20 short:E1:down | **WEAK** | 18/39 (46.2%) | 11 | 0 |
| 65. R1 Gītā 4.9 | ch.20 short:E1:down | **WEAK** | 27/46 (58.7%) | 14 | 0 |
| 66. R1 Gītā 1.21 | ch.20 short:E2:up | **WEAK** | 25/40 (62.5%) | 11 | 0 |
| 67. R1 Gītā 2.50 | ch.20 short:E2:up | **WEAK** | 27/41 (65.9%) | 12 | 0 |
| 68. R1 Gītā 3.30 | ch.20 short:E2:up | **WEAK** | 29/44 (65.9%) | 12 | 0 |
| 69. R1 Gītā 7.1 | ch.20 short:E2:up | **WEAK** | 20/43 (46.5%) | 11 | 0 |
| 70. R1 Gītā 7.8 | ch.20 short:E2:up | **NOT CONFIRMED** | 21/41 (51.2%) | 11 | 16 |
| 71. R1 Gītā 14.1 | ch.21 mixed:E1:down | **NOT CONFIRMED** | 34/46 (73.9%) | 13 | 22 |
| 72. R1 Gītā 14.11 | ch.21 mixed:E1:down | **CONFIRMED** | 37/46 (80.4%) | 12 | 0 |
| 73. R1 Gītā 14.25 | ch.21 mixed:E1:down | **CONFIRMED** | 34/42 (81.0%) | 12 | 0 |
| 74. R1 Gītā 2.64 | ch.21 mixed:E1:down | **WEAK** | 35/47 (74.5%) | 11 | 0 |
| 75. R1 Gītā 2.69 | ch.21 mixed:E1:down | **WEAK** | 30/38 (78.9%) | 11 | 0 |
| 76. R1 Gītā 7.13 | ch.21 mixed:E1:down | **WEAK** | 29/44 (65.9%) | 13 | 0 |
| 77. R1 Gītā 1.34 | ch.21 mixed:E2:up | **WEAK** | 27/40 (67.5%) | 12 | 0 |
| 78. R1 Gītā 1.46 | ch.21 mixed:E2:up | **CONFIRMED** | 41/47 (87.2%) | 13 | 0 |
| 79. R1 Gītā 14.10 | ch.21 mixed:E2:up | **WEAK** | 29/42 (69.0%) | 13 | 0 |
| 80. R1 Gītā 2.37 | ch.21 mixed:E2:up | **CONFIRMED** | 37/48 (77.1%) | 14 | 0 |
| 81. R1 Gītā 2.41 | ch.21 mixed:E2:up | **CONFIRMED** | 38/44 (86.4%) | 10 | 0 |
| 82. R1 Gītā 2.6 | ch.21 mixed:E2:up | **WEAK** | 34/58 (58.6%) | 14 | 0 |
| 83. R1 Gītā 14.1 | ch.21 short:E1:down | **NOT CONFIRMED** | 24/46 (52.2%) | 13 | 17 |
| 84. R1 Gītā 14.11 | ch.21 short:E1:down | **WEAK** | 25/46 (54.3%) | 13 | 0 |
| 85. R1 Gītā 2.64 | ch.21 short:E1:down | **WEAK** | 29/47 (61.7%) | 12 | 0 |
| 86. R1 Gītā 2.69 | ch.21 short:E1:down | **WEAK** | 18/38 (47.4%) | 10 | 0 |
| 87. R1 Gītā 7.13 | ch.21 short:E1:down | **WEAK** | 24/44 (54.5%) | 12 | 0 |
| 88. R1 Gītā 1.46 | ch.21 short:E2:up | **WEAK** | 29/47 (61.7%) | 15 | 0 |
| 89. R1 Gītā 2.37 | ch.21 short:E2:up | **WEAK** | 25/48 (52.1%) | 12 | 0 |
| 90. R1 Gītā 2.41 | ch.21 short:E2:up | **WEAK** | 27/44 (61.4%) | 11 | 0 |
| 91. R1 Gītā 13.5 | ch.22 mixed:E1:down | **NOT CONFIRMED** | 26/44 (59.1%) | 12 | 24 |
| 92. R1 Gītā 14.3 | ch.22 mixed:E1:down | **WEAK** | 29/43 (67.4%) | 13 | 0 |
| 93. R1 Gītā 17.16 | ch.22 mixed:E1:down | **WEAK** | 24/45 (53.3%) | 13 | 0 |
| 94. R1 Gītā 17.2 | ch.22 mixed:E1:down | **WEAK** | 29/38 (76.3%) | 10 | 0 |
| 95. R1 Gītā 18.65 | ch.22 mixed:E1:down | **NOT CONFIRMED** | 24/42 (57.1%) | 11 | 8 |
| 96. R1 Gītā 4.23 | ch.22 mixed:E1:down | **CONFIRMED** | 37/42 (88.1%) | 12 | 0 |
| 97. R1 Gītā 9.34 | ch.22 mixed:E1:down | **CONFIRMED** | 34/44 (77.3%) | 13 | 0 |
| 98. R1 Gītā 14.15 | ch.22 mixed:E2:up | **WEAK** | 32/38 (84.2%) | 10 | 0 |
| 99. R1 Gītā 2.14 | ch.22 mixed:E2:up | **CONFIRMED** | 35/43 (81.4%) | 11 | 0 |
| 100. R1 Gītā 7.3 | ch.22 mixed:E2:up | **CONFIRMED** | 35/44 (79.5%) | 12 | 0 |
| 101. R1 Gītā 14.3 | ch.22 short:E1:down | **WEAK** | 25/43 (58.1%) | 13 | 0 |
| 102. R1 Gītā 17.2 | ch.22 short:E1:down | **WEAK** | 22/38 (57.9%) | 10 | 0 |
| 103. R1 Gītā 18.65 | ch.22 short:E1:down | **NOT CONFIRMED** | 16/42 (38.1%) | 11 | 19 |
| 104. R1 Gītā 4.23 | ch.22 short:E1:down | **WEAK** | 30/42 (71.4%) | 11 | 0 |
| 105. R1 Gītā 9.34 | ch.22 short:E1:down | **WEAK** | 22/44 (50.0%) | 13 | 0 |
| 106. R1 Gītā 14.15 | ch.22 short:E2:up | **WEAK** | 20/38 (52.6%) | 10 | 0 |
| 107. R1 Gītā 7.3 | ch.22 short:E2:up | **WEAK** | 23/44 (52.3%) | 13 | 0 |
| 108. R1 Gītā 13.23 | ch.23 mixed:E1:down | **WEAK** | 30/36 (83.3%) | 10 | 0 |
| 109. R1 Gītā 13.7 | ch.23 mixed:E1:down | **NOT CONFIRMED** | 33/48 (68.8%) | 13 | 44 |
| 110. R1 Gītā 13.8 | ch.23 mixed:E1:down | **CONFIRMED** | 34/42 (81.0%) | 12 | 0 |
| 111. R1 Gītā 15.5 | ch.23 mixed:E1:down | **WEAK** | 46/63 (73.0%) | 14 | 0 |
| 112. R1 Gītā 15.7 | ch.23 mixed:E1:down | **WEAK** | 29/38 (76.3%) | 9 | 0 |
| 113. R1 Gītā 17.23 | ch.23 mixed:E1:down | **WEAK** | 31/46 (67.4%) | 11 | 0 |
| 114. R1 Gītā 9.2 | ch.23 mixed:E1:down | **CONFIRMED** | 36/48 (75.0%) | 14 | 0 |
| 115. R1 Gītā 3.18 | ch.23 mixed:E2:up | **CONFIRMED** | 34/42 (81.0%) | 13 | 0 |
| 116. R1 Gītā 3.21 | ch.23 mixed:E2:up | **CONFIRMED** | 33/44 (75.0%) | 13 | 0 |
| 117. R1 Gītā 13.23 | ch.23 short:E1:down | **WEAK** | 15/36 (41.7%) | 9 | 0 |
| 118. R1 Gītā 13.7 | ch.23 short:E1:down | **NOT CONFIRMED** | 25/48 (52.1%) | 15 | 41 |
| 119. R1 Gītā 13.8 | ch.23 short:E1:down | **WEAK** | 23/42 (54.8%) | 11 | 0 |
| 120. R1 Gītā 15.5 | ch.23 short:E1:down | **WEAK** | 32/63 (50.8%) | 15 | 0 |
| 121. R1 Gītā 15.7 | ch.23 short:E1:down | **WEAK** | 17/38 (44.7%) | 9 | 0 |
| 122. R1 Gītā 17.23 | ch.23 short:E1:down | **WEAK** | 25/46 (54.3%) | 11 | 0 |
| 123. R1 Gītā 9.2 | ch.23 short:E1:down | **WEAK** | 27/48 (56.2%) | 14 | 0 |
| 124. R1 Gītā 3.18 | ch.23 short:E2:up | **WEAK** | 25/42 (59.5%) | 13 | 0 |
| 125. R1 Gītā 3.21 | ch.23 short:E2:up | **WEAK** | 29/44 (65.9%) | 14 | 0 |
| 126. R1 Gītā 10.2 | ch.24 mixed:E1:down | **WEAK** | 27/38 (71.1%) | 11 | 0 |
| 127. R1 Gītā 10.6 | ch.24 mixed:E1:down | **WEAK** | 32/39 (82.1%) | 12 | 0 |
| 128. R1 Gītā 11.1 | ch.24 mixed:E1:down | **CONFIRMED** | 35/44 (79.5%) | 13 | 0 |
| 129. R1 Gītā 11.28 | ch.24 mixed:E1:down | **CONFIRMED** | 47/56 (83.9%) | 14 | 0 |
| 130. R1 Gītā 11.51 | ch.24 mixed:E1:down | **WEAK** | 21/40 (52.5%) | 9 | 0 |
| 131. R1 Gītā 11.52 | ch.24 mixed:E1:down | **NOT CONFIRMED** | 29/46 (63.0%) | 12 | 16 |
| 132. R1 Gītā 13.27 | ch.24 mixed:E1:down | **CONFIRMED** | 37/45 (82.2%) | 17 | 0 |
| 133. R1 Gītā 4.25 | ch.24 mixed:E1:down | **WEAK** | 24/42 (57.1%) | 11 | 0 |
| 134. R1 Gītā 5.10 | ch.24 mixed:E1:down | **CONFIRMED** | 35/46 (76.1%) | 14 | 0 |
| 135. R1 Gītā 14.1 | ch.24 mixed:E2:up | **NOT CONFIRMED** | 32/46 (69.6%) | 12 | 35 |
| 136. R1 Gītā 14.11 | ch.24 mixed:E2:up | **NOT CONFIRMED** | 36/46 (78.3%) | 14 | 9 |
| 137. R1 Gītā 2.12 | ch.24 mixed:E2:up | **WEAK** | 27/39 (69.2%) | 11 | 0 |
| 138. R1 Gītā 2.69 | ch.24 mixed:E2:up | **WEAK** | 32/38 (84.2%) | 10 | 0 |
| 139. R1 Gītā 3.11 | ch.24 mixed:E2:up | **CONFIRMED** | 34/40 (85.0%) | 12 | 0 |
| 140. R1 Gītā 4.9 | ch.24 mixed:E2:up | **CONFIRMED** | 37/46 (80.4%) | 13 | 0 |
| 141. R1 Gītā 7.13 | ch.24 mixed:E2:up | **WEAK** | 27/44 (61.4%) | 12 | 0 |
| 142. R1 Gītā 7.7 | ch.24 mixed:E2:up | **WEAK** | 28/41 (68.3%) | 12 | 0 |
| 143. R1 Gītā 10.2 | ch.24 short:E1:down | **WEAK** | 21/38 (55.3%) | 10 | 0 |
| 144. R1 Gītā 10.6 | ch.24 short:E1:down | **WEAK** | 24/39 (61.5%) | 11 | 0 |
| 145. R1 Gītā 11.1 | ch.24 short:E1:down | **WEAK** | 21/44 (47.7%) | 13 | 0 |
| 146. R1 Gītā 11.28 | ch.24 short:E1:down | **WEAK** | 35/56 (62.5%) | 13 | 0 |
| 147. R1 Gītā 11.51 | ch.24 short:E1:down | **WEAK** | 17/40 (42.5%) | 9 | 0 |
| 148. R1 Gītā 11.52 | ch.24 short:E1:down | **NOT CONFIRMED** | 20/46 (43.5%) | 12 | 20 |
| 149. R1 Gītā 13.27 | ch.24 short:E1:down | **WEAK** | 27/45 (60.0%) | 14 | 0 |
| 150. R1 Gītā 4.25 | ch.24 short:E1:down | **WEAK** | 16/42 (38.1%) | 10 | 0 |
| 151. R1 Gītā 5.10 | ch.24 short:E1:down | **WEAK** | 23/46 (50.0%) | 15 | 0 |
| 152. R1 Gītā 2.69 | ch.24 short:E2:mod3:up | **WEAK** | 16/38 (42.1%) | 11 | 0 |
| 153. R1 Gītā 14.1 | ch.24 short:E2:up | **NOT CONFIRMED** | 24/46 (52.2%) | 12 | 38 |
| 154. R1 Gītā 14.11 | ch.24 short:E2:up | **NOT CONFIRMED** | 30/46 (65.2%) | 13 | 11 |
| 155. R1 Gītā 2.12 | ch.24 short:E2:up | **WEAK** | 17/39 (43.6%) | 11 | 0 |
| 156. R1 Gītā 2.69 | ch.24 short:E2:up | **WEAK** | 20/38 (52.6%) | 10 | 0 |
| 157. R1 Gītā 3.11 | ch.24 short:E2:up | **WEAK** | 28/40 (70.0%) | 12 | 0 |
| 158. R1 Gītā 4.9 | ch.24 short:E2:up | **WEAK** | 30/46 (65.2%) | 16 | 0 |
| 159. R1 Gītā 7.13 | ch.24 short:E2:up | **WEAK** | 21/44 (47.7%) | 12 | 0 |
| 160. R1 Gītā 7.7 | ch.24 short:E2:up | **WEAK** | 16/41 (39.0%) | 12 | 0 |
| 161. R1 Gītā 11.47 | ch.25 mixed:E1:down | **WEAK** | 44/63 (69.8%) | 18 | 0 |
| 162. R1 Gītā 11.54 | ch.25 mixed:E1:down | **WEAK** | 33/47 (70.2%) | 12 | 0 |
| 163. R1 Gītā 11.55 | ch.25 mixed:E1:down | **CONFIRMED** | 34/44 (77.3%) | 13 | 0 |
| 164. R1 Gītā 17.20 | ch.25 mixed:E1:down | **CONFIRMED** | 32/41 (78.0%) | 10 | 0 |
| 165. R1 Gītā 18.65 | ch.25 mixed:E1:down | **CONFIRMED** | 34/42 (81.0%) | 12 | 0 |
| 166. R1 Gītā 3.6 | ch.25 mixed:E1:down | **WEAK** | 28/46 (60.9%) | 13 | 0 |
| 167. R1 Gītā 4.22 | ch.25 mixed:E1:down | **NOT CONFIRMED** | 18/42 (42.9%) | 10 | 11 |
| 168. R1 Gītā 8.9 | ch.25 mixed:E1:down | **WEAK** | 40/60 (66.7%) | 17 | 0 |
| 169. R1 Gītā 9.34 | ch.25 mixed:E1:down | **NOT CONFIRMED** | 22/44 (50.0%) | 13 | 9 |
| 170. R1 Gītā 14.25 | ch.25 mixed:E2:up | **CONFIRMED** | 39/42 (92.9%) | 11 | 0 |
| 171. R1 Gītā 17.16 | ch.25 mixed:E2:up | **WEAK** | 25/45 (55.6%) | 12 | 0 |
| 172. R1 Gītā 17.2 | ch.25 mixed:E2:up | **WEAK** | 26/38 (68.4%) | 10 | 0 |
| 173. R1 Gītā 18.65 | ch.25 mixed:E2:up | **NOT CONFIRMED** | 21/42 (50.0%) | 12 | 32 |
| 174. R1 Gītā 2.64 | ch.25 mixed:E2:up | **WEAK** | 28/47 (59.6%) | 11 | 0 |
| 175. R1 Gītā 4.23 | ch.25 mixed:E2:up | **NOT CONFIRMED** | 33/42 (78.6%) | 14 | 15 |
| 176. R1 Gītā 9.34 | ch.25 mixed:E2:up | **WEAK** | 28/44 (63.6%) | 12 | 0 |
| 177. R1 Gītā 11.55 | ch.25 short:E1:down | **WEAK** | 29/44 (65.9%) | 11 | 0 |
| 178. R1 Gītā 17.20 | ch.25 short:E1:down | **WEAK** | 22/41 (53.7%) | 10 | 0 |
| 179. R1 Gītā 18.65 | ch.25 short:E1:down | **WEAK** | 28/42 (66.7%) | 13 | 0 |
| 180. R1 Gītā 8.9 | ch.25 short:E1:down | **WEAK** | 28/60 (46.7%) | 16 | 0 |
| 181. R1 Gītā 9.34 | ch.25 short:E1:down | **NOT CONFIRMED** | 19/44 (43.2%) | 13 | 16 |
| 182. R1 Gītā 14.25 | ch.25 short:E2:up | **WEAK** | 26/42 (61.9%) | 10 | 0 |
| 183. R1 Gītā 17.2 | ch.25 short:E2:up | **WEAK** | 21/38 (55.3%) | 10 | 0 |
| 184. R1 Gītā 4.23 | ch.25 short:E2:up | **NOT CONFIRMED** | 22/42 (52.4%) | 13 | 18 |
| 185. R1 Gītā 9.34 | ch.25 short:E2:up | **WEAK** | 22/44 (50.0%) | 12 | 0 |
| 186. R1 Gītā 14.18 | ch.26 mixed:E1:down | **CONFIRMED** | 41/47 (87.2%) | 13 | 0 |
| 187. R1 Gītā 14.4 | ch.26 mixed:E1:down | **NOT CONFIRMED** | 30/41 (73.2%) | 11 | 12 |
| 188. R1 Gītā 16.1 | ch.26 mixed:E1:down | **NOT CONFIRMED** | 24/47 (51.1%) | 11 | 27 |
| 189. R1 Gītā 17.4 | ch.26 mixed:E1:down | **WEAK** | 30/43 (69.8%) | 14 | 0 |
| 190. R1 Gītā 18.37 | ch.26 mixed:E1:down | **WEAK** | 33/46 (71.7%) | 11 | 0 |
| 191. R1 Gītā 2.50 | ch.26 mixed:E1:down | **CONFIRMED** | 32/41 (78.0%) | 10 | 0 |
| 192. R1 Gītā 8.11 | ch.26 mixed:E1:down | **WEAK** | 43/61 (70.5%) | 17 | 0 |
| 193. R1 Gītā 13.5 | ch.26 mixed:E2:up | **WEAK** | 25/44 (56.8%) | 12 | 0 |
| 194. R1 Gītā 13.7 | ch.26 mixed:E2:up | **WEAK** | 29/48 (60.4%) | 13 | 0 |
| 195. R1 Gītā 13.8 | ch.26 mixed:E2:up | **WEAK** | 30/42 (71.4%) | 11 | 0 |
| 196. R1 Gītā 14.3 | ch.26 mixed:E2:up | **WEAK** | 29/43 (67.4%) | 12 | 0 |
| 197. R1 Gītā 15.5 | ch.26 mixed:E2:up | **WEAK** | 27/63 (42.9%) | 15 | 0 |
| 198. R1 Gītā 17.23 | ch.26 mixed:E2:up | **WEAK** | 30/46 (65.2%) | 11 | 0 |
| 199. R1 Gītā 14.18 | ch.26 short:E1:down | **WEAK** | 34/47 (72.3%) | 13 | 0 |
| 200. R1 Gītā 18.37 | ch.26 short:E1:down | **WEAK** | 30/46 (65.2%) | 11 | 0 |
| 201. R1 Gītā 2.50 | ch.26 short:E1:down | **WEAK** | 26/41 (63.4%) | 10 | 0 |
| 202. R1 Gītā 8.11 | ch.26 short:E1:down | **WEAK** | 32/61 (52.5%) | 14 | 0 |
| 203. R1 Gītā 13.5 | ch.26 short:E2:up | **WEAK** | 15/44 (34.1%) | 12 | 0 |
| 204. R1 Gītā 13.7 | ch.26 short:E2:up | **WEAK** | 21/48 (43.8%) | 11 | 0 |
| 205. R1 Gītā 14.3 | ch.26 short:E2:up | **WEAK** | 26/43 (60.5%) | 12 | 0 |
| 206. R1 Gītā 10.1 | ch.27 mixed:E1:down | **WEAK** | 31/37 (83.8%) | 11 | 0 |
| 207. R1 Gītā 10.23 | ch.27 mixed:E1:down | **NOT CONFIRMED** | 30/43 (69.8%) | 10 | 23 |
| 208. R1 Gītā 12.12 | ch.27 mixed:E1:down | **CONFIRMED** | 40/52 (76.9%) | 12 | 0 |
| 209. R1 Gītā 12.14 | ch.27 mixed:E1:down | **NOT CONFIRMED** | 33/43 (76.7%) | 11 | 18 |
| 210. R1 Gītā 13.22 | ch.27 mixed:E1:down | **WEAK** | 17/44 (38.6%) | 11 | 0 |
| 211. R1 Gītā 17.7 | ch.27 mixed:E1:down | **CONFIRMED** | 33/43 (76.7%) | 11 | 0 |
| 212. R1 Gītā 2.45 | ch.27 mixed:E1:down | **CONFIRMED** | 44/49 (89.8%) | 13 | 0 |
| 213. R1 Gītā 10.6 | ch.27 mixed:E2:up | **WEAK** | 31/39 (79.5%) | 10 | 0 |
| 214. R1 Gītā 11.28 | ch.27 mixed:E2:up | **CONFIRMED** | 45/56 (80.4%) | 14 | 0 |
| 215. R1 Gītā 13.23 | ch.27 mixed:E2:up | **WEAK** | 24/36 (66.7%) | 10 | 0 |
| 216. R1 Gītā 15.7 | ch.27 mixed:E2:up | **WEAK** | 28/38 (73.7%) | 10 | 0 |
| 217. R1 Gītā 4.25 | ch.27 mixed:E2:up | **WEAK** | 27/42 (64.3%) | 10 | 0 |
| 218. R1 Gītā 5.10 | ch.27 mixed:E2:up | **WEAK** | 31/46 (67.4%) | 14 | 0 |
| 219. R1 Gītā 9.2 | ch.27 mixed:E2:up | **WEAK** | 33/48 (68.8%) | 13 | 0 |
| 220. R1 Gītā 10.1 | ch.27 short:E1:down | **WEAK** | 25/37 (67.6%) | 10 | 0 |
| 221. R1 Gītā 10.23 | ch.27 short:E1:down | **NOT CONFIRMED** | 23/43 (53.5%) | 10 | 24 |
| 222. R1 Gītā 12.12 | ch.27 short:E1:down | **WEAK** | 35/52 (67.3%) | 14 | 0 |
| 223. R1 Gītā 12.14 | ch.27 short:E1:down | **NOT CONFIRMED** | 23/43 (53.5%) | 11 | 12 |
| 224. R1 Gītā 17.7 | ch.27 short:E1:down | **WEAK** | 24/43 (55.8%) | 11 | 0 |
| 225. R1 Gītā 2.45 | ch.27 short:E1:down | **WEAK** | 32/49 (65.3%) | 14 | 0 |
| 226. R1 Gītā 10.6 | ch.27 short:E2:up | **WEAK** | 21/39 (53.8%) | 10 | 0 |
| 227. R1 Gītā 11.28 | ch.27 short:E2:up | **WEAK** | 34/56 (60.7%) | 13 | 0 |
| 228. R1 Gītā 13.23 | ch.27 short:E2:up | **WEAK** | 20/36 (55.6%) | 12 | 0 |
| 229. R1 Gītā 4.25 | ch.27 short:E2:up | **WEAK** | 21/42 (50.0%) | 10 | 0 |
| 230. R1 Gītā 5.10 | ch.27 short:E2:up | **WEAK** | 21/46 (45.7%) | 13 | 0 |
| 231. R1 Gītā 9.2 | ch.27 short:E2:up | **WEAK** | 27/48 (56.2%) | 12 | 0 |
| 232. R1 Gītā 11.53 | ch.28 long:E1:down | **WEAK** | 25/39 (64.1%) | 11 | 0 |
| 233. R1 Gītā 13.10 | ch.28 long:E1:down | **CONFIRMED** | 30/40 (75.0%) | 12 | 0 |
| 234. R1 Gītā 11.51 | ch.28 long:E2:up | **WEAK** | 14/40 (35.0%) | 9 | 0 |
| 235. R1 Gītā 11.52 | ch.28 long:E2:up | **WEAK** | 33/46 (71.7%) | 13 | 0 |
| 236. R1 Gītā 16.2 | ch.28 mixed:E1:down | **WEAK** | 25/48 (52.1%) | 10 | 0 |
| 237. R1 Gītā 16.21 | ch.28 mixed:E1:down | **NOT CONFIRMED** | 23/46 (50.0%) | 13 | 16 |
| 238. R1 Gītā 18.55 | ch.28 mixed:E1:down | **WEAK** | 28/46 (60.9%) | 13 | 0 |
| 239. R1 Gītā 3.25 | ch.28 mixed:E1:down | **WEAK** | 24/49 (49.0%) | 11 | 0 |
| 240. R1 Gītā 7.4 | ch.28 mixed:E1:down | **WEAK** | 18/39 (46.2%) | 9 | 0 |
| 241. R1 Gītā 11.47 | ch.28 mixed:E2:up | **WEAK** | 33/63 (52.4%) | 15 | 0 |
| 242. R1 Gītā 11.54 | ch.28 mixed:E2:up | **WEAK** | 22/47 (46.8%) | 12 | 0 |
| 243. R1 Gītā 11.55 | ch.28 mixed:E2:up | **WEAK** | 26/44 (59.1%) | 12 | 0 |
| 244. R1 Gītā 17.20 | ch.28 mixed:E2:up | **WEAK** | 21/41 (51.2%) | 11 | 0 |
| 245. R1 Gītā 3.6 | ch.28 mixed:E2:up | **WEAK** | 24/46 (52.2%) | 12 | 0 |
| 246. R1 Gītā 8.9 | ch.28 mixed:E2:up | **WEAK** | 27/60 (45.0%) | 14 | 0 |
| 247. R1 Gītā 11.1 | ch.28 package:28-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 248. R1 Gītā 13.27 | ch.28 package:28-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 249. R1 Gītā 11.18 | ch.28 package:28-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 250. R1 Gītā 16.2 | ch.28 short:E1:down | **WEAK** | 25/48 (52.1%) | 11 | 0 |
| 251. R1 Gītā 16.21 | ch.28 short:E1:down | **NOT CONFIRMED** | 25/46 (54.3%) | 12 | 17 |
| 252. R1 Gītā 18.55 | ch.28 short:E1:down | **WEAK** | 29/46 (63.0%) | 13 | 0 |
| 253. R1 Gītā 7.4 | ch.28 short:E1:down | **WEAK** | 18/39 (46.2%) | 9 | 0 |
| 254. R1 Gītā 11.47 | ch.28 short:E2:up | **WEAK** | 31/63 (49.2%) | 16 | 0 |
| 255. R1 Gītā 11.54 | ch.28 short:E2:up | **WEAK** | 21/47 (44.7%) | 12 | 0 |
| 256. R1 Gītā 11.55 | ch.28 short:E2:up | **WEAK** | 25/44 (56.8%) | 11 | 0 |
| 257. R1 Gītā 17.20 | ch.28 short:E2:up | **WEAK** | 16/41 (39.0%) | 11 | 0 |
| 258. R1 Gītā 8.9 | ch.28 short:E2:up | **WEAK** | 27/60 (45.0%) | 15 | 0 |
| 259. R1 Gītā 16.3 | ch.29 long:E1:down | **WEAK** | 17/38 (44.7%) | 10 | 0 |
| 260. R1 Gītā 8.21 | ch.29 long:E1:down | **WEAK** | 33/46 (71.7%) | 13 | 0 |
| 261. R1 Gītā 18.65 | ch.29 long:E2:up | **NOT CONFIRMED** | 20/42 (47.6%) | 11 | 5 |
| 262. R1 Gītā 4.22 | ch.29 long:E2:up | **WEAK** | 22/42 (52.4%) | 11 | 0 |
| 263. R1 Gītā 8.11 | ch.29 long:E2:up | **WEAK** | 22/61 (36.1%) | 16 | 0 |
| 264. R1 Gītā 9.34 | ch.29 long:E2:up | **WEAK** | 19/44 (43.2%) | 12 | 0 |
| 265. R1 Gītā 13.4 | ch.29 mixed:E1:down | **WEAK** | 25/43 (58.1%) | 9 | 0 |
| 266. R1 Gītā 18.34 | ch.29 mixed:E1:down | **WEAK** | 31/42 (73.8%) | 11 | 0 |
| 267. R1 Gītā 18.63 | ch.29 mixed:E1:down | **WEAK** | 26/41 (63.4%) | 10 | 0 |
| 268. R1 Gītā 9.20 | ch.29 mixed:E1:down | **WEAK** | 23/66 (34.8%) | 16 | 0 |
| 269. R1 Gītā 10.23 | ch.29 mixed:E2:up | **NOT CONFIRMED** | 21/43 (48.8%) | 10 | 9 |
| 270. R1 Gītā 12.12 | ch.29 mixed:E2:up | **WEAK** | 28/52 (53.8%) | 12 | 0 |
| 271. R1 Gītā 12.14 | ch.29 mixed:E2:up | **NOT CONFIRMED** | 20/43 (46.5%) | 11 | 27 |
| 272. R1 Gītā 14.18 | ch.29 mixed:E2:up | **NOT CONFIRMED** | 27/47 (57.4%) | 11 | 35 |
| 273. R1 Gītā 16.1 | ch.29 mixed:E2:up | **WEAK** | 33/47 (70.2%) | 13 | 0 |
| 274. R1 Gītā 17.4 | ch.29 mixed:E2:up | **WEAK** | 23/43 (53.5%) | 12 | 0 |
| 275. R1 Gītā 2.50 | ch.29 mixed:E2:up | **WEAK** | 20/41 (48.8%) | 10 | 0 |
| 276. R1 Gītā 14.4 | ch.29 package:29-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 277. R1 Gītā 16.3 | ch.29 package:29-long_last:as_archived | **WEAK** | 17/38 (44.7%) | 12 | 0 |
| 278. R1 Gītā 8.21 | ch.29 package:29-long_last:as_archived | **WEAK** | 33/46 (71.7%) | 14 | 0 |
| 279. R1 Gītā 18.65 | ch.29 package:29-long_second_from_last:as_archived | **NOT CONFIRMED** | 20/42 (47.6%) | 12 | 12 |
| 280. R1 Gītā 4.22 | ch.29 package:29-long_second_from_last:as_archived | **WEAK** | 22/42 (52.4%) | 11 | 0 |
| 281. R1 Gītā 8.11 | ch.29 package:29-long_second_from_last:as_archived | **WEAK** | 22/61 (36.1%) | 13 | 0 |
| 282. R1 Gītā 9.34 | ch.29 package:29-long_second_from_last:as_archived | **WEAK** | 19/44 (43.2%) | 12 | 0 |
| 283. R1 Gītā 13.4 | ch.29 short:E1:down | **WEAK** | 23/43 (53.5%) | 11 | 0 |
| 284. R1 Gītā 18.34 | ch.29 short:E1:down | **WEAK** | 30/42 (71.4%) | 10 | 0 |
| 285. R1 Gītā 18.63 | ch.29 short:E1:down | **WEAK** | 25/41 (61.0%) | 10 | 0 |
| 286. R1 Gītā 10.23 | ch.29 short:E2:up | **WEAK** | 20/43 (46.5%) | 10 | 0 |
| 287. R1 Gītā 12.12 | ch.29 short:E2:up | **WEAK** | 25/52 (48.1%) | 13 | 0 |
| 288. R1 Gītā 12.14 | ch.29 short:E2:up | **NOT CONFIRMED** | 20/43 (46.5%) | 10 | 14 |
| 289. R1 Gītā 14.18 | ch.29 short:E2:up | **NOT CONFIRMED** | 25/47 (53.2%) | 12 | 21 |
| 290. R1 Gītā 16.1 | ch.29 short:E2:up | **WEAK** | 31/47 (66.0%) | 14 | 0 |
| 291. R1 Gītā 17.4 | ch.29 short:E2:up | **NOT CONFIRMED** | 21/43 (48.8%) | 12 | 16 |
| 292. R1 Gītā 10.1 | ch.30 long:E2:up | **WEAK** | 13/37 (35.1%) | 9 | 0 |
| 293. R1 Gītā 17.7 | ch.30 long:E2:up | **WEAK** | 30/43 (69.8%) | 12 | 0 |
| 294. R1 Gītā 2.45 | ch.30 long:E2:up | **WEAK** | 35/49 (71.4%) | 15 | 0 |
| 295. R1 Gītā 10.25 | ch.30 mixed:E1:down | **NOT CONFIRMED** | 20/45 (44.4%) | 10 | 14 |
| 296. R1 Gītā 10.27 | ch.30 mixed:E1:down | **WEAK** | 22/43 (51.2%) | 10 | 0 |
| 297. R1 Gītā 12.3 | ch.30 mixed:E1:down | **WEAK** | 26/51 (51.0%) | 12 | 0 |
| 298. R1 Gītā 13.20 | ch.30 mixed:E1:down | **WEAK** | 26/42 (61.9%) | 13 | 0 |
| 299. R1 Gītā 17.8 | ch.30 mixed:E1:down | **WEAK** | 28/45 (62.2%) | 11 | 0 |
| 300. R1 Gītā 18.11 | ch.30 mixed:E1:down | **WEAK** | 29/44 (65.9%) | 12 | 0 |
| 301. R1 Gītā 18.16 | ch.30 mixed:E1:down | **NOT CONFIRMED** | 26/44 (59.1%) | 12 | 24 |
| 302. R1 Gītā 18.58 | ch.30 mixed:E1:down | **WEAK** | 31/49 (63.3%) | 14 | 0 |
| 303. R1 Gītā 8.3 | ch.30 mixed:E1:down | **NOT CONFIRMED** | 25/44 (56.8%) | 13 | 15 |
| 304. R1 Gītā 9.18 | ch.30 mixed:E1:down | **NOT CONFIRMED** | 16/43 (37.2%) | 10 | 14 |
| 305. R1 Gītā 11.18 | ch.30 mixed:E2:up | **WEAK** | 30/62 (48.4%) | 15 | 0 |
| 306. R1 Gītā 16.2 | ch.30 mixed:E2:up | **WEAK** | 19/48 (39.6%) | 11 | 0 |
| 307. R1 Gītā 16.21 | ch.30 mixed:E2:up | **NOT CONFIRMED** | 21/46 (45.7%) | 13 | 39 |
| 308. R1 Gītā 16.3 | ch.30 mixed:E2:up | **WEAK** | 17/38 (44.7%) | 9 | 0 |
| 309. R1 Gītā 18.55 | ch.30 mixed:E2:up | **NOT CONFIRMED** | 21/46 (45.7%) | 13 | 16 |
| 310. R1 Gītā 3.25 | ch.30 mixed:E2:up | **WEAK** | 28/49 (57.1%) | 11 | 0 |
| 311. R1 Gītā 7.4 | ch.30 mixed:E2:up | **WEAK** | 20/39 (51.3%) | 10 | 0 |
| 312. R1 Gītā 8.21 | ch.30 mixed:E2:up | **WEAK** | 28/46 (60.9%) | 13 | 0 |
| 313. R1 Gītā 11.53 | ch.30 package:30-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 314. R1 Gītā 13.10 | ch.30 package:30-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 315. R1 Gītā 7.27 | ch.30 package:30-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 316. R1 Gītā 9.13 | ch.30 package:30-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 317. R1 Gītā 10.25 | ch.30 short:E1:down | **NOT CONFIRMED** | 19/45 (42.2%) | 10 | 9 |
| 318. R1 Gītā 10.27 | ch.30 short:E1:down | **WEAK** | 21/43 (48.8%) | 9 | 0 |
| 319. R1 Gītā 12.3 | ch.30 short:E1:down | **WEAK** | 26/51 (51.0%) | 13 | 0 |
| 320. R1 Gītā 13.20 | ch.30 short:E1:down | **WEAK** | 26/42 (61.9%) | 11 | 0 |
| 321. R1 Gītā 17.8 | ch.30 short:E1:down | **WEAK** | 28/45 (62.2%) | 12 | 0 |
| 322. R1 Gītā 18.11 | ch.30 short:E1:down | **WEAK** | 27/44 (61.4%) | 12 | 0 |
| 323. R1 Gītā 18.16 | ch.30 short:E1:down | **NOT CONFIRMED** | 26/44 (59.1%) | 12 | 8 |
| 324. R1 Gītā 18.58 | ch.30 short:E1:down | **WEAK** | 31/49 (63.3%) | 14 | 0 |
| 325. R1 Gītā 8.3 | ch.30 short:E1:down | **NOT CONFIRMED** | 23/44 (52.3%) | 12 | 31 |
| 326. R1 Gītā 9.18 | ch.30 short:E1:down | **NOT CONFIRMED** | 16/43 (37.2%) | 10 | 8 |
| 327. R1 Gītā 16.2 | ch.30 short:E2:up | **WEAK** | 20/48 (41.7%) | 11 | 0 |
| 328. R1 Gītā 16.21 | ch.30 short:E2:up | **NOT CONFIRMED** | 22/46 (47.8%) | 13 | 18 |
| 329. R1 Gītā 16.3 | ch.30 short:E2:up | **WEAK** | 15/38 (39.5%) | 9 | 0 |
| 330. R1 Gītā 18.55 | ch.30 short:E2:up | **NOT CONFIRMED** | 21/46 (45.7%) | 13 | 44 |
| 331. R1 Gītā 3.25 | ch.30 short:E2:up | **WEAK** | 27/49 (55.1%) | 12 | 0 |
| 332. R1 Gītā 7.4 | ch.30 short:E2:up | **WEAK** | 20/39 (51.3%) | 11 | 0 |
| 333. R1 Gītā 8.21 | ch.30 short:E2:up | **WEAK** | 27/46 (58.7%) | 13 | 0 |
| 334. R1 Gītā 9.19 | ch.31 long:E1:down | **WEAK** | 24/46 (52.2%) | 11 | 0 |
| 335. R1 Gītā 15.20 | ch.31 long:E2:up | **WEAK** | 24/47 (51.1%) | 12 | 0 |
| 336. R1 Gītā 14.26 | ch.31 mixed:E1:down | **WEAK** | 19/40 (47.5%) | 10 | 0 |
| 337. R1 Gītā 16.5 | ch.31 mixed:E1:down | **WEAK** | 12/37 (32.4%) | 8 | 0 |
| 338. R1 Gītā 17.14 | ch.31 mixed:E1:down | **WEAK** | 20/43 (46.5%) | 11 | 0 |
| 339. R1 Gītā 18.33 | ch.31 mixed:E1:down | **WEAK** | 22/42 (52.4%) | 12 | 0 |
| 340. R1 Gītā 18.51 | ch.31 mixed:E1:down | **WEAK** | 34/48 (70.8%) | 12 | 0 |
| 341. R1 Gītā 4.15 | ch.31 mixed:E1:down | **WEAK** | 21/45 (46.7%) | 10 | 0 |
| 342. R1 Gītā 6.32 | ch.31 mixed:E1:down | **WEAK** | 23/38 (60.5%) | 11 | 0 |
| 343. R1 Gītā 8.28 | ch.31 mixed:E1:down | **WEAK** | 33/59 (55.9%) | 13 | 0 |
| 344. R1 Gītā 13.4 | ch.31 mixed:E2:up | **WEAK** | 21/43 (48.8%) | 9 | 0 |
| 345. R1 Gītā 14.20 | ch.31 mixed:E2:up | **WEAK** | 27/45 (60.0%) | 11 | 0 |
| 346. R1 Gītā 18.34 | ch.31 mixed:E2:up | **WEAK** | 26/42 (61.9%) | 11 | 0 |
| 347. R1 Gītā 9.20 | ch.31 package:31-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 348. R1 Gītā 18.29 | ch.31 package:31-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 349. R1 Gītā 18.8 | ch.31 package:31-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 350. R1 Gītā 14.26 | ch.31 short:E1:down | **WEAK** | 19/40 (47.5%) | 11 | 0 |
| 351. R1 Gītā 17.14 | ch.31 short:E1:down | **WEAK** | 19/43 (44.2%) | 11 | 0 |
| 352. R1 Gītā 18.51 | ch.31 short:E1:down | **WEAK** | 33/48 (68.8%) | 12 | 0 |
| 353. R1 Gītā 6.32 | ch.31 short:E1:down | **WEAK** | 22/38 (57.9%) | 11 | 0 |
| 354. R1 Gītā 8.28 | ch.31 short:E1:down | **WEAK** | 32/59 (54.2%) | 13 | 0 |
| 355. R1 Gītā 14.20 | ch.31 short:E2:up | **WEAK** | 27/45 (60.0%) | 9 | 0 |
| 356. R1 Gītā 18.34 | ch.31 short:E2:up | **WEAK** | 26/42 (61.9%) | 11 | 0 |
| 357. R1 Gītā 12.4 | ch.32 long:E1:down | **CONFIRMED** | 37/44 (84.1%) | 13 | 0 |
| 358. R1 Gītā 13.26 | ch.32 long:E1:down | **WEAK** | 28/48 (58.3%) | 13 | 0 |
| 359. R1 Gītā 17.27 | ch.32 mixed:E1:down | **WEAK** | 22/41 (53.7%) | 11 | 0 |
| 360. R1 Gītā 10.25 | ch.32 mixed:E2:up | **WEAK** | 18/45 (40.0%) | 10 | 0 |
| 361. R1 Gītā 10.27 | ch.32 mixed:E2:up | **WEAK** | 20/43 (46.5%) | 9 | 0 |
| 362. R1 Gītā 12.3 | ch.32 mixed:E2:up | **WEAK** | 25/51 (49.0%) | 13 | 0 |
| 363. R1 Gītā 18.16 | ch.32 mixed:E2:up | **NOT CONFIRMED** | 22/44 (50.0%) | 12 | 9 |
| 364. R1 Gītā 18.58 | ch.32 mixed:E2:up | **WEAK** | 27/49 (55.1%) | 14 | 0 |
| 365. R1 Gītā 8.3 | ch.32 mixed:E2:up | **WEAK** | 23/44 (52.3%) | 12 | 0 |
| 366. R1 Gītā 7.27 | ch.32 package:32-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 367. R1 Gītā 11.38 | ch.32 package:32-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 368. R1 Gītā 17.27 | ch.32 short:E1:down | **WEAK** | 23/41 (56.1%) | 10 | 0 |
| 369. R1 Gītā 10.25 | ch.32 short:E2:up | **WEAK** | 16/45 (35.6%) | 10 | 0 |
| 370. R1 Gītā 10.27 | ch.32 short:E2:up | **WEAK** | 20/43 (46.5%) | 10 | 0 |
| 371. R1 Gītā 12.3 | ch.32 short:E2:up | **WEAK** | 24/51 (47.1%) | 12 | 0 |
| 372. R1 Gītā 13.20 | ch.32 short:E2:up | **WEAK** | 18/42 (42.9%) | 10 | 0 |
| 373. R1 Gītā 18.16 | ch.32 short:E2:up | **NOT CONFIRMED** | 21/44 (47.7%) | 13 | 10 |
| 374. R1 Gītā 8.3 | ch.32 short:E2:up | **NOT CONFIRMED** | 22/44 (50.0%) | 11 | 15 |
| 375. R1 Gītā 16.23 | ch.33 long:E1:down | **WEAK** | 25/42 (59.5%) | 9 | 0 |
| 376. R1 Gītā 17.8 | ch.33 long:E2:up | **WEAK** | 23/45 (51.1%) | 12 | 0 |
| 377. R1 Gītā 18.11 | ch.33 long:E2:up | **WEAK** | 32/44 (72.7%) | 11 | 0 |
| 378. R1 Gītā 9.18 | ch.33 long:E2:up | **NOT CONFIRMED** | 14/43 (32.6%) | 11 | 480 |
| 379. R1 Gītā 10.18 | ch.33 mixed:E1:down | **WEAK** | 26/40 (65.0%) | 10 | 0 |
| 380. R1 Gītā 10.41 | ch.33 mixed:E1:down | **WEAK** | 24/46 (52.2%) | 12 | 0 |
| 381. R1 Gītā 11.31 | ch.33 mixed:E1:down | **NOT CONFIRMED** | 29/59 (49.2%) | 13 | 108 |
| 382. R1 Gītā 11.39 | ch.33 mixed:E1:down | **WEAK** | 42/59 (71.2%) | 16 | 0 |
| 383. R1 Gītā 18.72 | ch.33 mixed:E1:down | **WEAK** | 17/45 (37.8%) | 10 | 0 |
| 384. R1 Gītā 16.5 | ch.33 mixed:E2:up | **WEAK** | 14/37 (37.8%) | 9 | 0 |
| 385. R1 Gītā 17.14 | ch.33 mixed:E2:up | **WEAK** | 20/43 (46.5%) | 11 | 0 |
| 386. R1 Gītā 18.29 | ch.33 mixed:E2:up | **NOT CONFIRMED** | 16/42 (38.1%) | 10 | 5 |
| 387. R1 Gītā 18.33 | ch.33 mixed:E2:up | **WEAK** | 28/42 (66.7%) | 11 | 0 |
| 388. R1 Gītā 18.51 | ch.33 mixed:E2:up | **WEAK** | 29/48 (60.4%) | 13 | 0 |
| 389. R1 Gītā 18.8 | ch.33 mixed:E2:up | **WEAK** | 21/45 (46.7%) | 12 | 0 |
| 390. R1 Gītā 6.32 | ch.33 mixed:E2:up | **WEAK** | 21/38 (55.3%) | 10 | 0 |
| 391. R1 Gītā 8.28 | ch.33 mixed:E2:up | **WEAK** | 25/59 (42.4%) | 13 | 0 |
| 392. R1 Gītā 9.19 | ch.33 package:33-B4_3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 393. R1 Gītā 17.24 | ch.33 package:33-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 394. R1 Gītā 18.46 | ch.33 package:33-B4_4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 395. R1 Gītā 16.23 | ch.33 package:33-long_last:as_archived | **WEAK** | 25/42 (59.5%) | 10 | 0 |
| 396. R1 Gītā 17.8 | ch.33 package:33-long_second_from_last:as_archived | **WEAK** | 23/45 (51.1%) | 11 | 0 |
| 397. R1 Gītā 18.11 | ch.33 package:33-long_second_from_last:as_archived | **WEAK** | 32/44 (72.7%) | 12 | 0 |
| 398. R1 Gītā 9.18 | ch.33 package:33-long_second_from_last:as_archived | **NOT CONFIRMED** | 14/43 (32.6%) | 10 | 473 |
| 399. R1 Gītā 10.18 | ch.33 short:E1:down | **WEAK** | 25/40 (62.5%) | 10 | 0 |
| 400. R1 Gītā 11.31 | ch.33 short:E1:down | **NOT CONFIRMED** | 31/59 (52.5%) | 13 | 97 |
| 401. R1 Gītā 11.39 | ch.33 short:E1:down | **WEAK** | 40/59 (67.8%) | 14 | 0 |
| 402. R1 Gītā 18.72 | ch.33 short:E1:down | **WEAK** | 16/45 (35.6%) | 10 | 0 |
| 403. R1 Gītā 16.5 | ch.33 short:E2:up | **WEAK** | 14/37 (37.8%) | 9 | 0 |
| 404. R1 Gītā 18.29 | ch.33 short:E2:up | **NOT CONFIRMED** | 14/42 (33.3%) | 9 | 8 |
| 405. R1 Gītā 18.33 | ch.33 short:E2:up | **WEAK** | 27/42 (64.3%) | 11 | 0 |
| 406. R1 Gītā 18.51 | ch.33 short:E2:up | **WEAK** | 29/48 (60.4%) | 12 | 0 |
| 407. R1 Gītā 6.32 | ch.33 short:E2:up | **WEAK** | 21/38 (55.3%) | 10 | 0 |
| 408. R1 Gītā 8.28 | ch.33 short:E2:up | **WEAK** | 24/59 (40.7%) | 15 | 0 |
| 409. R1 Gītā 14.26 | ch.34 long:E2:up | **WEAK** | 29/40 (72.5%) | 12 | 0 |
| 410. R1 Gītā 4.15 | ch.34 long:E2:up | **WEAK** | 25/45 (55.6%) | 11 | 0 |
| 411. R1 Gītā 11.36 | ch.34 mixed:E1:down | **WEAK** | 37/61 (60.7%) | 14 | 0 |
| 412. R1 Gītā 11.17 | ch.34 mixed:E2:up | **WEAK** | 26/62 (41.9%) | 14 | 0 |
| 413. R1 Gītā 11.38 | ch.34 mixed:E2:up | **WEAK** | 32/59 (54.2%) | 14 | 0 |
| 414. R1 Gītā 12.4 | ch.34 package:34-4-3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 415. R1 Gītā 11.11 | ch.34 package:34-4-4:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 416. R1 Gītā 14.26 | ch.34 package:34-5-2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 417. R1 Gītā 4.15 | ch.34 package:34-5-2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 418. R1 Gītā 11.36 | ch.34 short:E1:down | **WEAK** | 36/61 (59.0%) | 14 | 0 |
| 419. R1 Gītā 11.17 | ch.34 short:E2:up | **WEAK** | 25/62 (40.3%) | 13 | 0 |
| 420. R1 Gītā 11.38 | ch.34 short:E2:up | **WEAK** | 28/59 (47.5%) | 15 | 0 |
| 421. R1 Gītā 11.12 | ch.35 long:E1:down | **CONFIRMED** | 34/43 (79.1%) | 13 | 0 |
| 422. R1 Gītā 16.23 | ch.35 long:E2:up | **WEAK** | 30/42 (71.4%) | 11 | 0 |
| 423. R1 Gītā 17.27 | ch.35 long:E2:up | **WEAK** | 29/41 (70.7%) | 11 | 0 |
| 424. R1 Gītā 11.39 | ch.35 mixed:E1:down | **WEAK** | 43/59 (72.9%) | 15 | 0 |
| 425. R1 Gītā dhyana.5 | ch.35 mixed:E2:down | **NOT REPRODUCIBLE** | — | — | — |
| 426. R1 Gītā 10.18 | ch.35 mixed:E2:up | **WEAK** | 25/40 (62.5%) | 10 | 0 |
| 427. R1 Gītā 11.31 | ch.35 mixed:E2:up | **WEAK** | 29/59 (49.2%) | 13 | 0 |
| 428. R1 Gītā 18.72 | ch.35 mixed:E2:up | **WEAK** | 22/45 (48.9%) | 10 | 0 |
| 429. R1 Gītā 18.46 | ch.35 package:35-4-3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 430. R1 Gītā 16.23 | ch.35 package:35-5-2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 431. R1 Gītā 17.27 | ch.35 package:35-5-2:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 432. R1 Gītā 11.12 | ch.35 package:35-5-3:as_archived | **NOT REPRODUCIBLE** | — | — | — |
| 433. R1 Gītā 11.39 | ch.35 short:E1:down | **WEAK** | 40/59 (67.8%) | 14 | 0 |
| 434. R1 Gītā dhyana.5 | ch.35 short:E2:down | **NOT REPRODUCIBLE** | — | — | — |
| 435. R1 Gītā 10.18 | ch.35 short:E2:up | **WEAK** | 24/40 (60.0%) | 10 | 0 |
| 436. R1 Gītā 11.31 | ch.35 short:E2:up | **WEAK** | 29/59 (49.2%) | 15 | 0 |
| 437. R1 Gītā 18.72 | ch.35 short:E2:up | **WEAK** | 21/45 (46.7%) | 12 | 0 |
| 438. R2 Nirvāṇa-bhakti 8 | ch.10 long S1 down (strict) | **WEAK** | 24/40 (60.0%) | 13 | — |
| 439. R2 Nirvāṇa-bhakti 3 | ch.11 long S1 down (loose) | **WEAK** | 18/42 (42.9%) | 12 | — |
| 440. R2 Nirvāṇa-bhakti 6 | ch.11 long S1 down (loose) | **WEAK** | 25/40 (62.5%) | 14 | — |
| 441. R2 Nirvāṇa-bhakti 11 | ch.12 long S1 down (loose) | **WEAK** | 19/44 (43.2%) | 10 | — |
| 442. R2 Nirvāṇa-bhakti 5 | ch.13 long S1 down (loose) | **WEAK** | 23/42 (54.8%) | 12 | — |
| 443. R2 Nirvāṇa-bhakti 2 | ch.14 long S1 down (strict) | **WEAK** | 20/40 (50.0%) | 9 | — |
| 444. R2 Nirvāṇa-bhakti 1 | ch.15 long S1 down (loose) | **NOT CONFIRMED** | 8/86 (9.3%) | 12 | — |
| 445. R2 Nirvāṇa-bhakti 18 | ch.16 long S1 down (strict) | **NOT CONFIRMED** | 8/40 (20.0%) | 8 | — |
| 446. R2 Nirvāṇa-bhakti 25 | ch.18 long S1 down (strict) | **WEAK** | 18/42 (42.9%) | 12 | — |
| 447. R2 Nirvāṇa-bhakti 8 | ch.31 long S1 down (loose) | **WEAK** | 19/40 (47.5%) | 10 | — |
| 448. R2 Nirvāṇa-bhakti 11 | ch.32 long S1 down (loose) | **WEAK** | 31/44 (70.5%) | 10 | — |
| 449. R2 Nirvāṇa-bhakti 5 | ch.33 long S1 down (loose) | **CONFIRMED** | 32/42 (76.2%) | 11 | — |
| 450. R2 Nirvāṇa-bhakti 1 | ch.34 long S1 down (loose) | **WEAK** | 26/86 (30.2%) | 15 | — |
| 451. R2 Nirvāṇa-bhakti 2 | ch.34 long S1 down (loose) | **CONFIRMED** | 31/40 (77.5%) | 10 | — |
| 452. R2 Nirvāṇa-bhakti 18 | ch.35 long S1 down (loose) | **CONFIRMED** | 31/40 (77.5%) | 10 | — |
| 453. R2 Nirvāṇa-bhakti 23 | ch.35 long S1 down (loose) | **WEAK** | 12/41 (29.3%) | 10 | — |
| 454. R2 Nirvāṇa-bhakti 25 | ch.36 long S1 down (loose) | **WEAK** | 27/42 (64.3%) | 12 | — |
| 455. R3 Samadhibhakti Sanskrit:6 | ch.49 short:E2:down | **WEAK** | 34/51 (66.7%) | 16 | — |
| 456. R3 Samadhibhakti Sanskrit:6 | ch.49 merged:E2:down | **WEAK** | 28/51 (54.9%) | 13 | — |
| 457. R3 Santibhakti Sanskrit:16 | ch.50 short:E1:down | **WEAK** | 45/69 (65.2%) | 16 | — |
| 458. R3 Samadhibhakti Sanskrit:11 | ch.50 short:E1:down | **CONFIRMED** | 35/45 (77.8%) | 11 | — |
| 459. R3 Acaryabhakti Sanskrit:5 | ch.50 short:E1:down | **NOT CONFIRMED** | 5/43 (11.6%) | 7 | — |
| 460. R3 Samadhibhakti Sanskrit:11 | ch.50 merged:E1:down | **CONFIRMED** | 36/45 (80.0%) | 11 | — |
| 461. R3 Acaryabhakti Sanskrit:5 | ch.50 merged:E1:down | **NOT CONFIRMED** | 4/43 (9.3%) | 8 | — |
| 462. R3 Santibhakti Sanskrit:5 | ch.51 short:E1:down | **WEAK** | 36/52 (69.2%) | 15 | — |
| 463. R3 Pancamahaguru Sanskrit:2 | ch.51 short:E2:down | **NOT CONFIRMED** | 7/59 (11.9%) | 9 | — |
| 464. R3 Santibhakti Sanskrit:5 | ch.51 merged:E1:down | **WEAK** | 31/52 (59.6%) | 16 | — |
| 465. R3 Pancamahaguru Sanskrit:2 | ch.51 merged:E2:down | **NOT CONFIRMED** | 6/59 (10.2%) | 11 | — |
| 466. R3 Samadhibhakti Sanskrit:7 | ch.52 short:E1:down | **WEAK** | 30/48 (62.5%) | 12 | — |
| 467. R3 Santibhakti Sanskrit:11 | ch.53 short:E1:down | **CONFIRMED** | 42/51 (82.4%) | 13 | — |
| 468. R3 Siddhabhakti Sanskrit:7 | ch.53 short:E2:down | **WEAK** | 63/111 (56.8%) | 21 | — |
| 469. R3 Santibhakti Sanskrit:11 | ch.53 merged:E1:down | **WEAK** | 36/51 (70.6%) | 12 | — |
| 470. R3 Samadhibhakti Sanskrit:2 | ch.54 short:E1:down | **WEAK** | 31/43 (72.1%) | 12 | — |
| 471. R3 Acaryabhakti Sanskrit:8 | ch.55 short:E1:down | **NOT CONFIRMED** | 4/47 (8.5%) | 11 | — |
| 472. R3 Acaryabhakti Sanskrit:8 | ch.55 merged:E1:down | **NOT CONFIRMED** | 7/47 (14.9%) | 10 | — |
| 473. R3 Acaryabhakti Sanskrit:6 | ch.57 short:E1:down | **NOT CONFIRMED** | 5/44 (11.4%) | 9 | — |
| 474. R3 Santibhakti Sanskrit:1 | ch.57 short:E2:down | **CONFIRMED** | 39/50 (78.0%) | 13 | — |
| 475. R3 Pancamahaguru Sanskrit:6 | ch.57 short:E2:down | **NOT CONFIRMED** | 4/60 (6.7%) | 9 | — |
| 476. R3 Acaryabhakti Sanskrit:6 | ch.57 merged:E1:down | **NOT CONFIRMED** | 5/44 (11.4%) | 9 | — |
| 477. R3 Santibhakti Sanskrit:1 | ch.57 merged:E2:down | **CONFIRMED** | 39/50 (78.0%) | 13 | — |
| 478. R3 Pancamahaguru Sanskrit:4 | ch.58 short:E1:down | **NOT CONFIRMED** | 7/56 (12.5%) | 10 | — |
| 479. R3 Samadhibhakti Sanskrit:10 | ch.58 short:E2:down | **WEAK** | 18/39 (46.2%) | 10 | — |
| 480. R3 Pancamahaguru Sanskrit:7 | ch.58 short:E2:down | **NOT CONFIRMED** | 5/40 (12.5%) | 8 | — |
| 481. R3 Pancamahaguru Sanskrit:4 | ch.58 merged:E1:down | **NOT CONFIRMED** | 6/56 (10.7%) | 11 | — |
| 482. R3 Samadhibhakti Sanskrit:10 | ch.58 merged:E2:down | **WEAK** | 14/39 (35.9%) | 10 | — |
| 483. R3 Pancamahaguru Sanskrit:7 | ch.58 merged:E2:down | **NOT CONFIRMED** | 5/40 (12.5%) | 9 | — |
| 484. R3 Samadhibhakti Sanskrit:1 | ch.59 short:E1:down | **WEAK** | 39/83 (47.0%) | 16 | — |
| 485. R3 Samadhibhakti Sanskrit:5 | ch.59 short:E1:down | **WEAK** | 24/41 (58.5%) | 10 | — |
| 486. R3 Samadhibhakti Sanskrit:12 | ch.59 short:E2:down | **WEAK** | 31/49 (63.3%) | 14 | — |
| 487. R3 Samadhibhakti Sanskrit:1 | ch.59 merged:E1:down | **WEAK** | 40/83 (48.2%) | 15 | — |
| 488. R3 Samadhibhakti Sanskrit:5 | ch.59 merged:E1:down | **WEAK** | 24/41 (58.5%) | 11 | — |
| 489. R3 Samadhibhakti Sanskrit:12 | ch.59 merged:E2:down | **WEAK** | 27/49 (55.1%) | 12 | — |
| 490. R3 Caityabhakti Sanskrit:2 | ch.49 short:E2:down | **WEAK** | 65/87 (74.7%) | 19 | — |
| 491. R3 Caityabhakti Sanskrit:2 | ch.49 merged:E2:down | **WEAK** | 61/87 (70.1%) | 20 | — |
| 492. R3 Caityabhakti Sanskrit:28 | ch.50 short:E2:down | **WEAK** | 28/56 (50.0%) | 12 | — |
| 493. R3 Caityabhakti Sanskrit:28 | ch.50 merged:E2:down | **WEAK** | 30/56 (53.6%) | 11 | — |
| 494. R3 Caityabhakti Sanskrit:3 | ch.51 short:E1:down | **CONFIRMED** | 65/86 (75.6%) | 21 | — |
| 495. R3 Caityabhakti Sanskrit:4 | ch.51 short:E2:down | **CONFIRMED** | 39/49 (79.6%) | 13 | — |
| 496. R3 Caityabhakti Sanskrit:5 | ch.51 short:E2:down | **WEAK** | 30/46 (65.2%) | 14 | — |
| 497. R3 Caityabhakti Sanskrit:3 | ch.51 merged:E1:down | **WEAK** | 63/86 (73.3%) | 22 | — |
| 498. R3 Caityabhakti Sanskrit:4 | ch.51 merged:E2:down | **CONFIRMED** | 39/49 (79.6%) | 14 | — |
| 499. R3 Caityabhakti Sanskrit:27 | ch.52 short:E2:down | **WEAK** | 36/55 (65.5%) | 15 | — |
| 500. R3 Caityabhakti Sanskrit:27 | ch.52 merged:E2:down | **WEAK** | 37/55 (67.3%) | 14 | — |
| 501. R3 Caityabhakti Sanskrit:30 | ch.55 short:E2:down | **WEAK** | 36/54 (66.7%) | 14 | — |
| 502. R3 Caityabhakti Sanskrit:30 | ch.55 merged:E2:down | **WEAK** | 30/54 (55.6%) | 15 | — |
| 503. R3 Caityabhakti Sanskrit:8 | ch.56 short:E1:down | **CONFIRMED** | 37/47 (78.7%) | 12 | — |
| 504. R3 Caityabhakti Sanskrit:8 | ch.56 merged:E1:down | **CONFIRMED** | 36/47 (76.6%) | 12 | — |
| 505. R3 Caityabhakti Sanskrit:10 | ch.58 short:E1:down | **WEAK** | 33/47 (70.2%) | 11 | — |
| 506. R3 Caityabhakti Sanskrit:21 | ch.58 short:E2:down | **CONFIRMED** | 31/40 (77.5%) | 12 | — |
| 507. R3 Caityabhakti Sanskrit:21 | ch.58 merged:E2:down | **CONFIRMED** | 31/40 (77.5%) | 10 | — |
| 508. R3 Caityabhakti Sanskrit:9 | ch.59 short:E1:down | **WEAK** | 28/49 (57.1%) | 11 | — |
| 509. R3 Caityabhakti Sanskrit:23 | ch.59 short:E2:down | **WEAK** | 43/59 (72.9%) | 15 | — |
| 510. R3 Caityabhakti Sanskrit:23 | ch.59 merged:E2:down | **WEAK** | 35/59 (59.3%) | 14 | — |
| 511. R3 Samadhibhakti Sanskrit:6 | ch.49 package:49-short_second_from_last:listed | **WEAK** | 34/51 (66.7%) | 13 | — |
| 512. R3 Caityabhakti Sanskrit:2 | ch.49 package:49-short_second_from_last:listed | **WEAK** | 65/87 (74.7%) | 19 | — |
| 513. R3 Caityabhakti Sanskrit:28 | ch.50 package:50-short_second_from_last:listed | **WEAK** | 28/56 (50.0%) | 12 | — |
| 514. R3 Santibhakti Sanskrit:16 | ch.50 package:50-short_last:listed | **NOT CONFIRMED** | 11/69 (15.9%) | 16 | — |
| 515. R3 Samadhibhakti Sanskrit:11 | ch.50 package:50-short_last:listed | **NOT CONFIRMED** | 7/45 (15.6%) | 11 | — |
| 516. R3 Acaryabhakti Sanskrit:5 | ch.50 package:50-short_last:listed | **NOT CONFIRMED** | 4/43 (9.3%) | 8 | — |
| 517. R3 Pancamahaguru Sanskrit:2 | ch.51 package:51-short_second_from_last:listed | **NOT CONFIRMED** | 7/59 (11.9%) | 11 | — |
| 518. R3 Caityabhakti Sanskrit:4 | ch.51 package:51-short_second_from_last:listed | **CONFIRMED** | 39/49 (79.6%) | 13 | — |
| 519. R3 Caityabhakti Sanskrit:5 | ch.51 package:51-short_second_from_last:listed | **WEAK** | 30/46 (65.2%) | 13 | — |
| 520. R3 Santibhakti Sanskrit:5 | ch.51 package:51-short_last:listed | **NOT CONFIRMED** | 12/52 (23.1%) | 15 | — |
| 521. R3 Caityabhakti Sanskrit:3 | ch.51 package:51-short_last:listed | **NOT CONFIRMED** | 14/86 (16.3%) | 19 | — |
| 522. R3 Caityabhakti Sanskrit:27 | ch.52 package:52-short_second_from_last:listed | **WEAK** | 36/55 (65.5%) | 14 | — |
| 523. R3 Samadhibhakti Sanskrit:7 | ch.52 package:52-short_last:listed | **NOT CONFIRMED** | 6/48 (12.5%) | 11 | — |
| 524. R3 Siddhabhakti Sanskrit:7 | ch.53 package:53-short_second_from_last:listed | **WEAK** | 63/111 (56.8%) | 23 | — |
| 525. R3 Santibhakti Sanskrit:11 | ch.53 package:53-short_last:listed | **NOT CONFIRMED** | 8/51 (15.7%) | 13 | — |
| 526. R3 Samadhibhakti Sanskrit:2 | ch.54 package:54-short_last:listed | **NOT CONFIRMED** | 8/43 (18.6%) | 13 | — |
| 527. R3 Caityabhakti Sanskrit:30 | ch.55 package:55-short_second_from_last:listed | **WEAK** | 36/54 (66.7%) | 12 | — |
| 528. R3 Acaryabhakti Sanskrit:8 | ch.55 package:55-short_last:listed | **NOT CONFIRMED** | 5/47 (10.6%) | 11 | — |
| 529. R3 Caityabhakti Sanskrit:8 | ch.56 package:56-short_last:listed | **NOT CONFIRMED** | 8/47 (17.0%) | 12 | — |
| 530. R3 Santibhakti Sanskrit:1 | ch.57 package:57-short_second_from_last:listed | **CONFIRMED** | 39/50 (78.0%) | 13 | — |
| 531. R3 Pancamahaguru Sanskrit:6 | ch.57 package:57-short_second_from_last:listed | **NOT CONFIRMED** | 4/60 (6.7%) | 9 | — |
| 532. R3 Acaryabhakti Sanskrit:6 | ch.57 package:57-short_last:listed | **NOT CONFIRMED** | 4/44 (9.1%) | 9 | — |
| 533. R3 Samadhibhakti Sanskrit:10 | ch.58 package:58-short_second_from_last:listed | **WEAK** | 18/39 (46.2%) | 11 | — |
| 534. R3 Pancamahaguru Sanskrit:7 | ch.58 package:58-short_second_from_last:listed | **NOT CONFIRMED** | 5/40 (12.5%) | 8 | — |
| 535. R3 Caityabhakti Sanskrit:21 | ch.58 package:58-short_second_from_last:listed | **CONFIRMED** | 31/40 (77.5%) | 10 | — |
| 536. R3 Pancamahaguru Sanskrit:4 | ch.58 package:58-short_last:listed | **NOT CONFIRMED** | 6/56 (10.7%) | 9 | — |
| 537. R3 Caityabhakti Sanskrit:10 | ch.58 package:58-short_last:listed | **NOT CONFIRMED** | 8/47 (17.0%) | 12 | — |
| 538. R3 Samadhibhakti Sanskrit:12 | ch.59 package:59-short_second_from_last:listed | **WEAK** | 31/49 (63.3%) | 12 | — |
| 539. R3 Caityabhakti Sanskrit:23 | ch.59 package:59-short_second_from_last:listed | **WEAK** | 43/59 (72.9%) | 15 | — |
| 540. R3 Samadhibhakti Sanskrit:1 | ch.59 package:59-short_last:listed | **NOT CONFIRMED** | 9/83 (10.8%) | 15 | — |
| 541. R3 Samadhibhakti Sanskrit:5 | ch.59 package:59-short_last:listed | **NOT CONFIRMED** | 6/41 (14.6%) | 11 | — |
| 542. R3 Caityabhakti Sanskrit:9 | ch.59 package:59-short_last:listed | **NOT CONFIRMED** | 6/49 (12.2%) | 11 | — |
| 543. R4 Jinasahasranama:69 | 30-short-E2-up | **WEAK** | 25/41 (61.0%) | 11 | — |
| 544. R4 Jinasahasranama:69 | 30-merged-E2-up | **WEAK** | 26/41 (63.4%) | 10 | — |
| 545. R4 Jinasahasranama:7 | 32-short-E1-down | **WEAK** | 21/40 (52.5%) | 10 | — |
| 546. R4 Jinasahasranama:31 | 32-short-E1-down | **NOT CONFIRMED** | 5/35 (14.3%) | 8 | — |
| 547. R4 Jinasahasranama:45 | 32-short-E1-down | **WEAK** | 26/38 (68.4%) | 10 | — |
| 548. R4 Jinasahasranama:7 | 32-merged-E1-down | **WEAK** | 22/40 (55.0%) | 11 | — |
| 549. R4 Jinasahasranama:31 | 32-merged-E1-down | **NOT CONFIRMED** | 5/35 (14.3%) | 8 | — |
| 550. R4 Jinasahasranama:45 | 32-merged-E1-down | **WEAK** | 27/38 (71.1%) | 10 | — |
| 551. R4 Jinasahasranama:1 | 34-long-E1-down | **CONFIRMED** | 37/47 (78.7%) | 14 | — |
| 552. R4 Jinasahasranama:7 | 34-short-E2-up | **WEAK** | 21/40 (52.5%) | 11 | — |
| 553. R4 Jinasahasranama:31 | 34-short-E2-up | **NOT CONFIRMED** | 5/35 (14.3%) | 8 | — |
| 554. R4 Jinasahasranama:45 | 34-short-E2-up | **WEAK** | 14/38 (36.8%) | 9 | — |
| 555. R4 Jinasahasranama:7 | 34-merged-E2-up | **WEAK** | 21/40 (52.5%) | 11 | — |
| 556. R4 Jinasahasranama:31 | 34-merged-E2-up | **NOT CONFIRMED** | 5/35 (14.3%) | 8 | — |
| 557. R4 Jinasahasranama:84 | 35-long-E1-down | **WEAK** | 25/41 (61.0%) | 10 | — |
| 558. R4 Jinasahasranama:31 | 35-short-E1-down | **NOT CONFIRMED** | 4/35 (11.4%) | 8 | — |
| 559. R4 Jinasahasranama:35 | 35-short-E1-down | **WEAK** | 24/42 (57.1%) | 11 | — |
| 560. R4 Jinasahasranama:36 | 35-short-E1-down | **WEAK** | 21/43 (48.8%) | 11 | — |
| 561. R4 Jinasahasranama:53 | 35-short-E1-down | **WEAK** | 14/35 (40.0%) | 12 | — |
| 562. R4 Jinasahasranama:54 | 35-short-E1-down | **WEAK** | 24/42 (57.1%) | 13 | — |
| 563. R4 Jinasahasranama:31 | 35-merged-E1-down | **NOT CONFIRMED** | 7/35 (20.0%) | 9 | — |
| 564. R4 Jinasahasranama:36 | 35-merged-E1-down | **WEAK** | 21/43 (48.8%) | 11 | — |
| 565. R4 Jinasahasranama:54 | 35-merged-E1-down | **WEAK** | 26/42 (61.9%) | 13 | — |
| 566. R4 Jinasahasranama:93 | 35-merged-E1-down | **WEAK** | 25/38 (65.8%) | 12 | — |
| 567. R4 Jinasahasranama:3 | 35-merged-E2-down | **WEAK** | 19/45 (42.2%) | 12 | — |
| 568. R4 Jinasahasranama:54 | 35-short-mod3-E1-down | **WEAK** | 19/42 (45.2%) | 13 | — |
| 569. R4 Mahabharata-mangala:0 | 36-long-E1-down | **WEAK** | 28/39 (71.8%) | 12 | — |
| 570. R4 Jinasahasranama:8 | 36-short-E1-down | **WEAK** | 25/41 (61.0%) | 10 | — |
| 571. R4 Jinasahasranama:21 | 36-short-E1-down | **NOT CONFIRMED** | 7/37 (18.9%) | 10 | — |
| 572. R4 Jinasahasranama:4 | 36-short-E2-down | **WEAK** | 27/42 (64.3%) | 12 | — |
| 573. R4 Jinasahasranama:10 | 36-short-E2-down | **WEAK** | 29/48 (60.4%) | 12 | — |
| 574. R4 Jinasahasranama:114 | 36-short-E2-down | **WEAK** | 22/41 (53.7%) | 11 | — |
| 575. R4 Jinasahasranama:8 | 36-merged-E1-down | **WEAK** | 25/41 (61.0%) | 10 | — |
| 576. R4 Jinasahasranama:21 | 36-merged-E1-down | **NOT CONFIRMED** | 6/37 (16.2%) | 11 | — |
| 577. R4 Jinasahasranama:4 | 36-merged-E2-down | **WEAK** | 27/42 (64.3%) | 12 | — |
| 578. R4 Jinasahasranama:10 | 36-merged-E2-down | **WEAK** | 28/48 (58.3%) | 11 | — |
| 579. R4 Jinasahasranama:114 | 36-merged-E2-down | **WEAK** | 22/41 (53.7%) | 11 | — |
| 580. R4 Jinasahasranama:66 | 37-long-E1-down | **WEAK** | 17/46 (37.0%) | 10 | — |
| 581. R4 Jinasahasranama:7 | 37-long-E2-down | **WEAK** | 22/40 (55.0%) | 11 | — |
| 582. R4 Jinasahasranama:103 | 37-short-E1-down | **WEAK** | 27/48 (56.2%) | 11 | — |
| 583. R4 Jinasahasranama:5 | 37-short-E2-down | **WEAK** | 23/47 (48.9%) | 13 | — |
| 584. R4 Jinasahasranama:12 | 37-short-E2-down | **WEAK** | 21/44 (47.7%) | 11 | — |
| 585. R4 Jinasahasranama:25 | 37-short-E2-down | **WEAK** | 9/40 (22.5%) | 8 | — |
| 586. R4 Jinasahasranama:103 | 37-merged-E1-down | **WEAK** | 28/48 (58.3%) | 11 | — |
| 587. R4 Jinasahasranama:5 | 37-merged-E2-down | **WEAK** | 25/47 (53.2%) | 12 | — |
| 588. R4 Jinasahasranama:12 | 37-merged-E2-down | **WEAK** | 21/44 (47.7%) | 12 | — |
| 589. R4 Jinasahasranama:25 | 37-merged-E2-down | **NOT CONFIRMED** | 4/40 (10.0%) | 8 | — |
| 590. R4 Jinasahasranama:12 | 37-short-mod3-E2-down | **WEAK** | 18/44 (40.9%) | 11 | — |
| 591. R4 Jinasahasranama:97 | 38-long-E1-down | **WEAK** | 27/41 (65.9%) | 13 | — |
| 592. R4 Jinasahasranama:85 | 38-short-E1-down | **WEAK** | 25/40 (62.5%) | 11 | — |
| 593. R4 Jinasahasranama:110 | 38-short-E1-down | **WEAK** | 24/42 (57.1%) | 10 | — |
| 594. R4 Jinasahasranama:16 | 38-short-E2-down | **WEAK** | 20/45 (44.4%) | 10 | — |
| 595. R4 Jinasahasranama:46 | 38-short-E2-down | **WEAK** | 25/47 (53.2%) | 11 | — |
| 596. R4 Jinasahasranama:85 | 38-merged-E1-down | **WEAK** | 26/40 (65.0%) | 11 | — |
| 597. R4 Jinasahasranama:110 | 38-merged-E1-down | **WEAK** | 24/42 (57.1%) | 10 | — |
| 598. R4 Jinasahasranama:16 | 38-merged-E2-down | **WEAK** | 21/45 (46.7%) | 10 | — |
| 599. R4 Jinasahasranama:46 | 38-merged-E2-down | **WEAK** | 26/47 (55.3%) | 11 | — |
| 600. R4 Jinasahasranama:86 | 39-short-E2-down | **WEAK** | 16/37 (43.2%) | 8 | — |
| 601. R4 Jinasahasranama:96 | 39-short-E2-down | **WEAK** | 19/41 (46.3%) | 9 | — |
| 602. R4 Jinasahasranama:98 | 39-short-E2-down | **WEAK** | 18/42 (42.9%) | 9 | — |
| 603. R4 Jinasahasranama:86 | 39-merged-E2-down | **WEAK** | 17/37 (45.9%) | 8 | — |
| 604. R4 Jinasahasranama:96 | 39-merged-E2-down | **WEAK** | 21/41 (51.2%) | 10 | — |
| 605. R4 Jinasahasranama:98 | 39-merged-E2-down | **WEAK** | 18/42 (42.9%) | 9 | — |
| 606. R4 Jinasahasranama:17 | 40-short-E1-down | **WEAK** | 29/51 (56.9%) | 13 | — |
| 607. R4 Jinasahasranama:60 | 40-short-E1-down | **WEAK** | 23/37 (62.2%) | 9 | — |
| 608. R4 Jinasahasranama:95 | 40-short-E1-down | **WEAK** | 28/41 (68.3%) | 9 | — |
| 609. R4 Jinasahasranama:121 | 40-short-E1-down | **WEAK** | 20/43 (46.5%) | 10 | — |
| 610. R4 Jinasahasranama:45 | 40-short-E2-down | **WEAK** | 22/38 (57.9%) | 9 | — |
| 611. R4 Jinasahasranama:57 | 40-short-E2-down | **WEAK** | 23/41 (56.1%) | 13 | — |
| 612. R4 Jinasahasranama:58 | 40-short-E2-down | **WEAK** | 18/36 (50.0%) | 12 | — |
| 613. R4 Jinasahasranama:59 | 40-short-E2-down | **WEAK** | 20/37 (54.1%) | 13 | — |
| 614. R4 Jinasahasranama:17 | 40-merged-E1-down | **WEAK** | 30/51 (58.8%) | 14 | — |
| 615. R4 Jinasahasranama:60 | 40-merged-E1-down | **WEAK** | 25/37 (67.6%) | 9 | — |
| 616. R4 Jinasahasranama:95 | 40-merged-E1-down | **WEAK** | 27/41 (65.9%) | 8 | — |
| 617. R4 Jinasahasranama:109 | 40-merged-E1-down | **WEAK** | 20/45 (44.4%) | 10 | — |
| 618. R4 Jinasahasranama:121 | 40-merged-E1-down | **WEAK** | 22/43 (51.2%) | 10 | — |
| 619. R4 Jinasahasranama:45 | 40-merged-E2-down | **WEAK** | 22/38 (57.9%) | 9 | — |
| 620. R4 Jinasahasranama:57 | 40-merged-E2-down | **WEAK** | 23/41 (56.1%) | 13 | — |
| 621. R4 Jinasahasranama:58 | 40-merged-E2-down | **WEAK** | 19/36 (52.8%) | 12 | — |
| 622. R4 Jinasahasranama:59 | 40-merged-E2-down | **WEAK** | 19/37 (51.4%) | 13 | — |
| 623. R4 Jinasahasranama:69 | 41-short-E2-down | **WEAK** | 17/41 (41.5%) | 9 | — |
| 624. R4 Jinasahasranama:69 | 41-merged-E2-down | **WEAK** | 16/41 (39.0%) | 9 | — |
| 625. R4 Jinasahasranama:82 | 42-short-E1-down | **WEAK** | 23/44 (52.3%) | 10 | — |
| 626. R4 Jinasahasranama:82 | 42-merged-E1-down | **WEAK** | 24/44 (54.5%) | 11 | — |
| 627. R4 Jinasahasranama:9 | 43-short-E1-down | **WEAK** | 30/51 (58.8%) | 12 | — |
| 628. R4 Jinasahasranama:117 | 43-short-E1-down | **CONFIRMED** | 43/52 (82.7%) | 14 | — |
| 629. R4 Jinasahasranama:132 | 43-short-E2-down | **WEAK** | 38/52 (73.1%) | 13 | — |
| 630. R4 Jinasahasranama:117 | 43-merged-E1-down | **CONFIRMED** | 43/52 (82.7%) | 14 | — |
| 631. R4 Jinasahasranama:87 | 44-short-E1-down | **CONFIRMED** | 39/45 (86.7%) | 12 | — |
| 632. R4 Jinasahasranama:124 | 44-short-E1-down | **CONFIRMED** | 41/50 (82.0%) | 14 | — |
| 633. R4 Jinasahasranama:131 | 44-short-E1-down | **NOT CONFIRMED** | 9/49 (18.4%) | 13 | — |
| 634. R4 Jinasahasranama:40 | 44-short-E2-down | **WEAK** | 17/42 (40.5%) | 9 | — |
| 635. R4 Jinasahasranama:49 | 44-short-E2-down | **WEAK** | 28/41 (68.3%) | 10 | — |
| 636. R4 Jinasahasranama:99 | 44-short-E2-down | **WEAK** | 30/42 (71.4%) | 13 | — |
| 637. R4 Jinasahasranama:125 | 44-short-E2-down | **WEAK** | 30/41 (73.2%) | 12 | — |
| 638. R4 Jinasahasranama:87 | 44-merged-E1-down | **CONFIRMED** | 39/45 (86.7%) | 13 | — |
| 639. R4 Jinasahasranama:124 | 44-merged-E1-down | **CONFIRMED** | 39/50 (78.0%) | 13 | — |
| 640. R4 Jinasahasranama:131 | 44-merged-E1-down | **NOT CONFIRMED** | 9/49 (18.4%) | 11 | — |
| 641. R4 Jinasahasranama:49 | 44-merged-E2-down | **WEAK** | 27/41 (65.9%) | 10 | — |
| 642. R4 Jinasahasranama:99 | 44-merged-E2-down | **WEAK** | 25/42 (59.5%) | 13 | — |
| 643. R4 Jinasahasranama:125 | 44-merged-E2-down | **WEAK** | 30/41 (73.2%) | 12 | — |
| 644. R4 Jinasahasranama:124 | 44-short-mod3-E1-down | **WEAK** | 29/50 (58.0%) | 13 | — |
| 645. R4 Jinasahasranama:49 | 44-short-mod3-E2-down | **WEAK** | 20/41 (48.8%) | 10 | — |
| 646. R4 Jinasahasranama:125 | 44-short-mod3-E2-down | **WEAK** | 22/41 (53.7%) | 11 | — |
| 647. R4 Jinasahasranama:39 | 45-short-E1-down | **CONFIRMED** | 36/43 (83.7%) | 11 | — |
| 648. R4 Jinasahasranama:89 | 45-short-E2-down | **WEAK** | 26/40 (65.0%) | 9 | — |
| 649. R4 Jinasahasranama:39 | 45-merged-E1-down | **CONFIRMED** | 36/43 (83.7%) | 11 | — |
| 650. R4 Jinasahasranama:89 | 45-merged-E2-down | **WEAK** | 16/40 (40.0%) | 10 | — |
| 651. R4 Jinasahasranama:19 | 46-short-E1-down | **CONFIRMED** | 33/40 (82.5%) | 11 | — |
| 652. R4 Jinasahasranama:100 | 46-short-E1-down | **CONFIRMED** | 36/43 (83.7%) | 11 | — |
| 653. R4 Jinasahasranama:108 | 46-short-E1-down | **WEAK** | 25/42 (59.5%) | 9 | — |
| 654. R4 Jinasahasranama:112 | 46-short-E1-down | **CONFIRMED** | 35/42 (83.3%) | 11 | — |
| 655. R4 Jinasahasranama:123 | 46-short-E1-down | **CONFIRMED** | 36/47 (76.6%) | 13 | — |
| 656. R4 Jinasahasranama:127 | 46-short-E1-down | **CONFIRMED** | 31/41 (75.6%) | 12 | — |
| 657. R4 Jinasahasranama:52 | 46-short-E2-down | **WEAK** | 40/56 (71.4%) | 16 | — |
| 658. R4 Jinasahasranama:115 | 46-short-E2-down | **WEAK** | 30/46 (65.2%) | 13 | — |
| 659. R4 Jinasahasranama:19 | 46-merged-E1-down | **CONFIRMED** | 33/40 (82.5%) | 11 | — |
| 660. R4 Jinasahasranama:100 | 46-merged-E1-down | **CONFIRMED** | 35/43 (81.4%) | 11 | — |
| 661. R4 Jinasahasranama:108 | 46-merged-E1-down | **WEAK** | 20/42 (47.6%) | 10 | — |
| 662. R4 Jinasahasranama:112 | 46-merged-E1-down | **CONFIRMED** | 35/42 (83.3%) | 13 | — |
| 663. R4 Jinasahasranama:123 | 46-merged-E1-down | **WEAK** | 33/47 (70.2%) | 14 | — |
| 664. R4 Jinasahasranama:127 | 46-merged-E1-down | **WEAK** | 26/41 (63.4%) | 12 | — |
| 665. R4 Jinasahasranama:52 | 46-merged-E2-down | **WEAK** | 39/56 (69.6%) | 14 | — |
| 666. R4 Jinasahasranama:115 | 46-merged-E2-down | **WEAK** | 30/46 (65.2%) | 10 | — |
| 667. R4 Jinasahasranama:19 | 46-short-mod3-E1-down | **WEAK** | 23/40 (57.5%) | 11 | — |
| 668. R4 Jinasahasranama:100 | 46-short-mod3-E1-down | **WEAK** | 25/43 (58.1%) | 11 | — |
| 669. R4 Jinasahasranama:108 | 46-short-mod3-E1-down | **WEAK** | 17/42 (40.5%) | 9 | — |
| 670. R4 Jinasahasranama:112 | 46-short-mod3-E1-down | **WEAK** | 25/42 (59.5%) | 11 | — |
| 671. R4 Jinasahasranama:52 | 46-short-mod3-E2-down | **WEAK** | 27/56 (48.2%) | 15 | — |
| 672. R4 Jinasahasranama:26 | 47-short-E1-down | **NOT CONFIRMED** | 9/38 (23.7%) | 10 | — |
| 673. R4 Jinasahasranama:33 | 47-short-E1-down | **NOT CONFIRMED** | 5/41 (12.2%) | 9 | — |
| 674. R4 Jinasahasranama:105 | 47-short-E1-down | **CONFIRMED** | 33/44 (75.0%) | 13 | — |
| 675. R4 Jinasahasranama:107 | 47-short-E1-down | **CONFIRMED** | 31/41 (75.6%) | 10 | — |
| 676. R4 Jinasahasranama:50 | 47-short-E2-down | **WEAK** | 27/53 (50.9%) | 12 | — |
| 677. R4 Jinasahasranama:92 | 47-short-E2-down | **CONFIRMED** | 41/50 (82.0%) | 13 | — |
| 678. R4 Jinasahasranama:94 | 47-short-E2-down | **WEAK** | 20/36 (55.6%) | 8 | — |
| 679. R4 Jinasahasranama:102 | 47-short-E2-down | **WEAK** | 26/41 (63.4%) | 10 | — |
| 680. R4 Jinasahasranama:26 | 47-merged-E1-down | **NOT CONFIRMED** | 7/38 (18.4%) | 9 | — |
| 681. R4 Jinasahasranama:33 | 47-merged-E1-down | **NOT CONFIRMED** | 5/41 (12.2%) | 10 | — |
| 682. R4 Jinasahasranama:105 | 47-merged-E1-down | **CONFIRMED** | 33/44 (75.0%) | 13 | — |
| 683. R4 Jinasahasranama:107 | 47-merged-E1-down | **CONFIRMED** | 31/41 (75.6%) | 10 | — |
| 684. R4 Jinasahasranama:50 | 47-merged-E2-down | **WEAK** | 27/53 (50.9%) | 12 | — |
| 685. R4 Jinasahasranama:92 | 47-merged-E2-down | **CONFIRMED** | 39/50 (78.0%) | 11 | — |
| 686. R4 Jinasahasranama:94 | 47-merged-E2-down | **WEAK** | 15/36 (41.7%) | 8 | — |
| 687. R4 Jinasahasranama:102 | 47-merged-E2-down | **WEAK** | 26/41 (63.4%) | 9 | — |
| 688. R4 Jinasahasranama:107 | 47-short-mod3-E1-down | **WEAK** | 23/41 (56.1%) | 10 | — |
| 689. R4 Jinasahasranama:92 | 47-short-mod3-E2-down | **WEAK** | 27/50 (54.0%) | 12 | — |
| 690. R4 Jinasahasranama:28 | 48-short-E2-down | **NOT CONFIRMED** | 4/37 (10.8%) | 9 | — |
| 691. R4 Jinasahasranama:65 | 48-short-E2-down | **WEAK** | 27/41 (65.9%) | 12 | — |
| 692. R4 Jinasahasranama:28 | 48-merged-E2-down | **NOT CONFIRMED** | 5/37 (13.5%) | 9 | — |
| 693. R4 Jinasahasranama:84 | 56-short-E1-down | **WEAK** | 22/41 (53.7%) | 9 | — |
| 694. R4 Jinasahasranama:84 | 56-short-mod3-E1-down | **WEAK** | 16/41 (39.0%) | 11 | — |
| 695. R4 Jinasahasranama:1 | package:34-5-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 696. R4 Jinasahasranama:84 | package:35-5-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 697. R4 Jinasahasranama:2 | package:36-4-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 698. R4 Jinasahasranama:55 | package:36-4-4:given | **NOT REPRODUCIBLE** | — | — | — |
| 699. R4 Jinasahasranama:56 | package:36-4-4:given | **NOT REPRODUCIBLE** | — | — | — |
| 700. R4 Mahabharata-mangala:0 | package:36-5-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 701. R4 Jinasahasranama:76 | package:37-4-4:given | **NOT REPRODUCIBLE** | — | — | — |
| 702. R4 Jinasahasranama:7 | package:37-5-2:given | **NOT REPRODUCIBLE** | — | — | — |
| 703. R4 Jinasahasranama:97 | package:38-5-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 704. R4 Jinasahasranama:15 | package:40-4-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 705. R4 Jinasahasranama:106 | package:42-probe-Mj-3:given | **NOT REPRODUCIBLE** | — | — | — |
| 706. R4 Jinasahasranama:120 | package:42-probe-Mj-2:given | **NOT REPRODUCIBLE** | — | — | — |
| 707. R4 Jinasahasranāma 80 | ch.44→45 outer-word join | **NOT REPRODUCIBLE** | — | — | — |
| 708. R5 Samayikapatha:23 | ch57:short:end1:plain:down→ch58:merged:end1:plain:down | **CONFIRMED** | 46/59 (78.0%) | 14 | — |
| 709. R5 Samayikapatha:23 | ch57:short:end1:plain:down→ch56:short:end2:plain:down | **WEAK** | 32/59 (54.2%) | 14 | — |
| 710. R6 Svayambhūstotra 123 | ch.19 B2_7 | **NOT REPRODUCIBLE** | — | — | — |
| 711. R6 Mahāsubhāṣitasaṃgraha MSS_0343-1 | ch.42 copyist group 3 first up | **NOT CONFIRMED** | 3/20 (15.0%) | 7 | — |
| 712. R6 Tiloyapaṇṇattī page:82:line:1851:chunk:1 | ch.44 copyist group 1 first down | **WEAK** | 31/45 (68.9%) | 13 | — |
| 713. R6 Tiloyapaṇṇattī page:83:line:1867:chunk:1 | ch.50 copyist group 1 first down | **WEAK** | 23/42 (54.8%) | 10 | — |
| 714. R6 Tiloyapaṇṇattī page:80:line:1810:chunk:1 | ch.52 copyist group 1 first down | **NOT CONFIRMED** | 5/90 (5.6%) | 12 | — |
| 715. R7 Kṛṣṇāmṛtamahārṇava 53 | ch.42 merged E1 down | **WEAK** | 20/40 (50.0%) | 10 | — |
| 716. R7 Vaikhānasa Mantrapraśna 5.1.125 | ch.34 short E1 down | **WEAK** | 22/85 (25.9%) | 16 | — |
| 717. R7 Jayadhavalā praśasti 6 | ch.31 B3_1 down | **NOT REPRODUCIBLE** | — | — | — |
| 718. R7 Jayadhavalā praśasti 8 | ch.31 B3_1 down | **NOT REPRODUCIBLE** | — | — | — |
| 719. R7 Uttarapurāṇa praśasti 5 | ch.30 B3_1 down | **NOT REPRODUCIBLE** | — | — | — |

## Rows without a reproducible score

| Row | Reason |
|---:|---|
| 19 | archived/package band has no numeric-grid extraction rule in reading guide |
| 20 | archived/package band has no numeric-grid extraction rule in reading guide |
| 34 | archived/package band has no numeric-grid extraction rule in reading guide |
| 35 | archived/package band has no numeric-grid extraction rule in reading guide |
| 36 | archived/package band has no numeric-grid extraction rule in reading guide |
| 37 | archived/package band has no numeric-grid extraction rule in reading guide |
| 247 | archived/package band has no numeric-grid extraction rule in reading guide |
| 248 | archived/package band has no numeric-grid extraction rule in reading guide |
| 249 | archived/package band has no numeric-grid extraction rule in reading guide |
| 276 | archived/package band has no numeric-grid extraction rule in reading guide |
| 313 | archived/package band has no numeric-grid extraction rule in reading guide |
| 314 | archived/package band has no numeric-grid extraction rule in reading guide |
| 315 | archived/package band has no numeric-grid extraction rule in reading guide |
| 316 | archived/package band has no numeric-grid extraction rule in reading guide |
| 347 | archived/package band has no numeric-grid extraction rule in reading guide |
| 348 | archived/package band has no numeric-grid extraction rule in reading guide |
| 349 | archived/package band has no numeric-grid extraction rule in reading guide |
| 366 | archived/package band has no numeric-grid extraction rule in reading guide |
| 367 | archived/package band has no numeric-grid extraction rule in reading guide |
| 392 | archived/package band has no numeric-grid extraction rule in reading guide |
| 393 | archived/package band has no numeric-grid extraction rule in reading guide |
| 394 | archived/package band has no numeric-grid extraction rule in reading guide |
| 414 | archived/package band has no numeric-grid extraction rule in reading guide |
| 415 | archived/package band has no numeric-grid extraction rule in reading guide |
| 416 | archived/package band has no numeric-grid extraction rule in reading guide |
| 417 | archived/package band has no numeric-grid extraction rule in reading guide |
| 425 | Gītā dhyana.5 absent from independent edition |
| 429 | archived/package band has no numeric-grid extraction rule in reading guide |
| 430 | archived/package band has no numeric-grid extraction rule in reading guide |
| 431 | archived/package band has no numeric-grid extraction rule in reading guide |
| 432 | archived/package band has no numeric-grid extraction rule in reading guide |
| 434 | Gītā dhyana.5 absent from independent edition |
| 695 | column locator cannot be reduced to a numeric-grid position |
| 696 | column locator cannot be reduced to a numeric-grid position |
| 697 | column locator cannot be reduced to a numeric-grid position |
| 698 | column locator cannot be reduced to a numeric-grid position |
| 699 | column locator cannot be reduced to a numeric-grid position |
| 700 | column locator cannot be reduced to a numeric-grid position |
| 701 | column locator cannot be reduced to a numeric-grid position |
| 702 | column locator cannot be reduced to a numeric-grid position |
| 703 | column locator cannot be reduced to a numeric-grid position |
| 704 | column locator cannot be reduced to a numeric-grid position |
| 705 | column locator cannot be reduced to a numeric-grid position |
| 706 | column locator cannot be reduced to a numeric-grid position |
| 707 | outer-word join is not a fixed numeric-grid column or a defined copyist band |
| 710 | B2_7 line-band position is not marked in numeric JSON; guide warns the band offsets are unreliable |
| 717 | B3_1 first inserted unit of line 3 is not recoverable from numeric ranks; the guide says band offsets vary by verse |
| 718 | B3_1 first inserted unit of line 3 is not recoverable from numeric ranks; the guide says band offsets vary by verse |
| 719 | B3_1 first inserted unit of line 3 is not recoverable from numeric ranks; the guide says band offsets vary by verse |

## Side-by-side evidence for every confirmed row

`—` is an alignment gap. These are full source-unit alignments; the grid units are uncorrected. Coordinates and source text are in RESULTS3.json.

### 9. R1 Gītā 2.50 — ch.15 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 32/41; best shuffle 10; decoys ≥ 0.

```text
Grid:      u·dh·dhi·yu·k·tō·ja·hā·tī·ha·vu·bhē·su·ru·ta·du·ṣ·ru·te·ta·s·mā·d·yō·ga·ya·yu·j·ya·s·va·yō·h·k·r·ma·su·v·śa·la·m
Published: bu·d·dhi·yu·k·to·ja·hā·tī·ha·u·bhe·su·kṛ·ta·du·ṣ·kṛ·te·ta·s·mā·d·yo·gā·ya·yu·j·ya·s·va·yo·gaḥ·ka·r·ma·su·kau·śa·la·m
```

### 10. R1 Gītā 3.30 — ch.15 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 35/44; best shuffle 11; decoys ≥ 0.

```text
Grid:      a·ḍi·sa·r·vā·ṇi·ka·r·pā·ṇi·m·n·ya·s·yā·n·yā·t·ma·ē·t·sā·ni·rā·śī·vu·ni·r·ma·mō·bhū·t·vā·yu·dh·ya·s·va·vi·ga·ta·j·va·ś
Published: ma·yi·sa·r·vā·ṇi·ka·r·mā·ṇi·saṃ·n·ya·s·yā·dh·yā·t·ma·ce·ta·sā·ni·rā·śī·r·ni·r·ma·mo·bhū·t·vā·yu·dh·ya·s·va·vi·ga·ta·j·va·raḥ
```

### 32. R1 Gītā 2.67 — ch.18 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 33/42; best shuffle 12; decoys ≥ 0.

```text
Grid:      i·n·d·ri·yā·m·hi·ca·ra·tā·ya·n·ma·nō·nu·vi·dhī·ya·tē·ta·—·da·s·ya·ha·ra·ti·p·ra·j·m·vā·yu·ra·nā·va·—·mi·vā·lu·bha·si
Published: i·n·d·ri·yā·ṇāṃ·hi·ca·ra·tāṃ·ya·n·ma·no·nu·vi·dhī·ya·te·ta·d·a·s·ya·ha·ra·ti·p·ra·j·ñāṃ·vā·yu·r·nā·va·m·i·vā·m·bha·si
```

### 43. R1 Gītā 3.21 — ch.19 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/44; best shuffle 13; decoys ≥ 0.

```text
Grid:      ya·d·ya·v·dā·ca·ra·t·ś·rē·ṣ·h·s·ta·t·ta·—·dē·vē·ta·rō·ja·ha·sa·ya·t·p·ra·mā·m·ku·ru·tē·lō·ka·s·ta·—·da·nu·va·r·ta·tē
Published: ya·d·ya·d·ā·ca·ra·ti·ś·re·ṣ·ṭha·s·ta·t·ta·d·e·ve·ta·ro·ja·naḥ·sa·ya·t·p·ra·mā·ṇaṃ·ku·ru·te·lo·ka·s·ta·d·a·nu·va·r·ta·te
```

### 48. R1 Gītā 18.6 — ch.19 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 36/46; best shuffle 13; decoys ≥ 0.

```text
Grid:      yē·tā·—·na·ya·pi·tu·ka·—·mā·ṇi·sa·ga·m·t·ya·k·t·vā·pha·lā·ni·ca·ka·r·ta·v·yā·nī·ti·mē·pā·r·tha·ni·ś·ci·m·ma·ta·—·mu·t·ta·ma·m
Published: e·tā·n·y·a·pi·tu·ka·r·mā·ṇi·sa·ṅ·gaṃ·t·ya·k·t·vā·pha·lā·ni·ca·ka·r·ta·v·yā·nī·ti·me·pā·r·tha·ni·ś·ci·taṃ·ma·ta·m·u·t·ta·ma·m
```

### 55. R1 Gītā 3.11 — ch.20 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 31/40; best shuffle 12; decoys ≥ 0.

```text
Grid:      de·vā·n·bhā·va·rā·tā·nē·na·tē·dē·vā·bhā·va·ya·n·tu·ha·pa·ra·s·pa·m·bhā·va·ya·n·h·ś·rē·h·pa·—·?·ma·vā·p·?·ya·tha
Published: de·vā·n·bhā·va·ya·tā·ne·na·te·de·vā·bhā·va·ya·n·tu·vaḥ·pa·ra·s·pa·raṃ·bhā·va·ya·n·taḥ·ś·re·yaḥ·pa·ra·m·a·vā·p·s·ya·tha
```

### 56. R1 Gītā 4.9 — ch.20 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/46; best shuffle 17; decoys ≥ 0.

```text
Grid:      ja·n·ma·ka·r·ma·ca·mē·di·v·l·m·va·m·yō·vē·t·ti·ta·—·t·va·ha·t·ya·k·t·vā·dē·m·pu·na·r·ja·n·ma·y·ti·mā·—·mē·ti·sō·r·ju·na
Published: ja·n·ma·ka·r·ma·ca·me·di·v·ya·m·e·vaṃ·yo·ve·t·ti·ta·t·t·va·taḥ·t·ya·k·t·vā·de·haṃ·pu·na·r·ja·n·ma·nai·ti·mā·m·e·ti·so·r·ju·na
```

### 57. R1 Gītā 1.21 — ch.20 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 31/40; best shuffle 11; decoys ≥ 0.

```text
Grid:      ru·ṣī·kē·m·ta·m·vā·k·ya·m·i·da·—·mā·ha·ma·hī·pa·tē·sē·na·gi·mō·ru·bha·yō·r·ma·dh·yē·ra·ra·s·thā·pa·ya·mē·c·yu·ta
Published: hṛ·ṣī·ke·śaṃ·ta·dā·vā·k·ya·m·i·da·m·ā·ha·ma·hī·pa·te·se·na·yo·r·u·bha·yo·r·ma·dh·ye·ra·thaṃ·s·thā·pa·ya·me·c·yu·ta
```

### 60. R1 Gītā 2.50 — ch.20 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 31/41; best shuffle 10; decoys ≥ 0.

```text
Grid:      u·d·dhi·yu·k·tō·ja·hā·tī·h·u·bhē·su·ru·ta·du·ṣ·ru·tē·ta·hi·mā·y·yō·gā·ya·yu·j·ya·s·va·ga·h·ru·r·ma·su·v·śa·la·m
Published: bu·d·dhi·yu·k·to·ja·hā·tī·ha·u·bhe·su·kṛ·ta·du·ṣ·kṛ·te·ta·s·mā·d·yo·gā·ya·yu·j·ya·s·va·yo·gaḥ·ka·r·ma·su·kau·śa·la·m
```

### 61. R1 Gītā 3.30 — ch.20 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/44; best shuffle 12; decoys ≥ 0.

```text
Grid:      a·i·sa·r·vā·ṇi·ka·l·mā·ṇi·n·n·ya·s·yā·dh·yā·t·ma·cē·ta·sā·ni·rā·śī·r·ni·r·ma·mō·bhū·t·vā·yu·dh·ya·—·va·vi·ga·d·j·va·ha
Published: ma·yi·sa·r·vā·ṇi·ka·r·mā·ṇi·saṃ·n·ya·s·yā·dh·yā·t·ma·ce·ta·sā·ni·rā·śī·r·ni·r·ma·mo·bhū·t·vā·yu·dh·ya·s·va·vi·ga·ta·j·va·raḥ
```

### 72. R1 Gītā 14.11 — ch.21 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/46; best shuffle 12; decoys ≥ 0.

```text
Grid:      sa·r·va·d·vā·rē·ṣu·dē·hē·s·mi·n·p·ra·kā·śa·u·pa·jā·ya·tē·j·ñā·m·ya·dā·ta·da·vi·d·yā·d·vi·ru·d·m·sa·—·t·va·—·mi·t·—·yu·ta
Published: sa·r·va·d·vā·re·ṣu·de·he·s·mi·n·p·ra·kā·śa·u·pa·jā·ya·te·j·ñā·naṃ·ya·dā·ta·dā·vi·d·yā·d·vi·vṛ·d·dhaṃ·sa·t·t·va·m·i·t·y·u·ta
```

### 73. R1 Gītā 14.25 — ch.21 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/42; best shuffle 12; decoys ≥ 0.

```text
Grid:      mā·nā·p·mā·?·yō·s·tu·l·ya·s·tu·l·yō·mi·t·rā·ri·pa·k·ṣa·h·sa·r·vā·ra·m·bh·pa·r·t·yā·gī·gu·ṇā·tī·s·sa·u·c·—·y
Published: mā·nā·va·mā·na·yo·s·tu·l·ya·s·tu·l·yo·mi·t·rā·ri·pa·k·ṣa·yoḥ·sa·r·vā·ra·m·bha·pa·ri·t·yā·gī·gu·ṇā·tī·taḥ·sa·u·c·ya·te
```

### 78. R1 Gītā 1.46 — ch.21 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 41/47; best shuffle 13; decoys ≥ 0.

```text
Grid:      y·di·mā·—·ma·p·ra·tī·kā·ra·m·a·śa·s·t·m·śa·s·t·ra·pā·ṇa·ha·dhā·r·ta·rā·ṣ·ṭ·rā·ra·ṇē·ha·n·yu·s·ta·n·mē·k·ṣē·ma·ta·m·bha·vē·t
Published: ya·di·mā·m·a·p·ra·tī·kā·ra·m·a·śa·s·t·raṃ·śa·s·t·ra·pā·ṇa·yaḥ·dhā·r·ta·rā·ṣ·ṭ·rā·ra·ṇe·ha·n·yu·s·ta·n·me·k·ṣe·ma·ta·raṃ·bha·ve·t
```

### 80. R1 Gītā 2.37 — ch.21 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/48; best shuffle 14; decoys ≥ 0.

```text
Grid:      ha·tō·bā·p·rā·p·—·ya·si·s·va·r·m·ji·ta·vā·vā·bhō·k·ṣ·y·sē·ma·hī·m·ta·s·mā·—·du·t·ti·ṣ·ka·v·n·tē·ya·yu·d·dhā·ya·ru·ta·ni·ś·ca·ya
Published: ha·to·vā·p·rā·p·s·ya·si·s·va·r·gaṃ·ji·t·vā·vā·bho·k·ṣ·ya·se·ma·hī·m·ta·s·mā·d·u·t·ti·ṣ·ṭha·kau·n·te·ya·yu·d·dhā·ya·kṛ·ta·ni·ś·ca·yaḥ
```

### 81. R1 Gītā 2.41 — ch.21 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 38/44; best shuffle 10; decoys ≥ 0.

```text
Grid:      v·ya·va·sā·yā·t·mi·kā·bu·d·dhi·—·rē·kē·va·ku·ru·na·n·da·na·ba·hu·śā·khā·h·—·ya·na·n·tā·ś·ca·bu·d·dha·yō·v·ya·va·sā·i·nā·m
Published: v·ya·va·sā·yā·t·mi·kā·bu·d·dhi·r·e·ke·ha·ku·ru·na·n·da·na·ba·hu·śā·khā·h·y·a·na·n·tā·ś·ca·bu·d·dha·yo·v·ya·va·sā·yi·nā·m
```

### 96. R1 Gītā 4.23 — ch.22 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/42; best shuffle 12; decoys ≥ 0.

```text
Grid:      ga·ta·sa·n·ga·s·ya·mu·k·ta·s·ya·j·ñā·nā·va·s·thi·ta·cē·ta·sā·ya·j·ñā·yā·ca·ra·ha·ka·r·ma·sa·ma·g·m·p·rā·vi·lī·ya·tē
Published: ga·ta·sa·ṅ·ga·s·ya·mu·k·ta·s·ya·j·ñā·nā·va·s·thi·ta·ce·ta·saḥ·ya·j·ñā·yā·ca·ra·taḥ·ka·r·ma·sa·ma·g·raṃ·p·ra·vi·lī·ya·te
```

### 97. R1 Gītā 9.34 — ch.22 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/44; best shuffle 13; decoys ≥ 0.

```text
Grid:      ma·n·ma·nā·bha·va·ma·d·bha·k·tō·ma·d·yā·jī·m·na·ma·s·ku·ru·—·mū·mē·vē·ṣ·ya·si·yu·k·t·—·va·va·mā·t·mā·m·ma·t·pa·rā·ya·ṇa
Published: ma·n·ma·nā·bha·va·ma·d·bha·k·to·ma·d·yā·jī·māṃ·na·ma·s·ku·ru·mā·m·e·vai·ṣ·ya·si·yu·k·t·vai·va·m·ā·t·mā·naṃ·ma·t·pa·rā·ya·ṇaḥ
```

### 99. R1 Gītā 2.14 — ch.22 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 35/43; best shuffle 11; decoys ≥ 0.

```text
Grid:      mā·t·rā·s·pa·r·śā·s·ka·v·n·tē·ya·śī·tō·ṣ·ṇa·su·kha·h·kha·h·ā·ga·mā·pā·i·nō·ni·t·yā·s·m·s·tī·ti·k·ṣa·s·na·bhā·ra·ta
Published: mā·t·rā·s·pa·r·śā·s·tu·kau·n·te·ya·śī·to·ṣ·ṇa·su·kha·duḥ·kha·dāḥ·ā·ga·mā·pā·yi·no·ni·t·yā·s·tāṃ·s·ti·ti·k·ṣa·s·va·bhā·ra·ta
```

### 100. R1 Gītā 7.3 — ch.22 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 35/44; best shuffle 12; decoys ≥ 0.

```text
Grid:      m·nu·ṣ·yā·m·sa·h·s·rē·ṣu·ka·ś·ci·d·ya·ta·ti·si·d·dha·yē·ya·ta·tā·—·ma·pi·si·d·dhā·m·ka·ś·ci·n·m·vē·t·ti·—·t·t·va·ta
Published: ma·nu·ṣ·yā·ṇāṃ·sa·ha·s·re·ṣu·ka·ś·ci·d·ya·ta·ti·si·d·dha·ye·ya·ta·tā·m·a·pi·si·d·dhā·nāṃ·ka·ś·ci·n·māṃ·ve·t·ti·ta·t·t·va·taḥ
```

### 110. R1 Gītā 13.8 — ch.23 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/42; best shuffle 12; decoys ≥ 0.

```text
Grid:      i·n·d·ri·yā·r·nē·ṣu·y·rā·g·ya·—·ma·na·m·kā·ra·ē·va·ca·ja·n·ma·ru·t·yu·ja·rā·v·yā·dhi·h·kha·ō·ṣā·nu·da·r·śa·na·m
Published: i·n·d·ri·yā·r·the·ṣu·vai·rā·g·ya·m·a·na·haṃ·kā·ra·e·va·ca·ja·n·ma·mṛ·t·yu·ja·rā·v·yā·dhi·duḥ·kha·do·ṣā·nu·da·r·śa·na·m
```

### 114. R1 Gītā 9.2 — ch.23 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 36/48; best shuffle 14; decoys ≥ 0.

```text
Grid:      ā·ja·vi·d·yā·rā·ja·gu·h·m·pa·vi·t·ra·—·mi·da·—·mu·t·ta·ma·m·p·ra·t·ya·k·ṣā·va·ga·m·dha·r·m·m·su·su·m·ka·r·tu·—·ma·v·?·ya·m
Published: rā·ja·vi·d·yā·rā·ja·gu·h·yaṃ·pa·vi·t·ra·m·i·da·m·u·t·ta·ma·m·p·ra·t·ya·k·ṣā·va·ga·maṃ·dha·r·m·yaṃ·su·su·khaṃ·ka·r·tu·m·a·v·ya·ya·m
```

### 115. R1 Gītā 3.18 — ch.23 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/42; best shuffle 13; decoys ≥ 0.

```text
Grid:      y·vē·ta·s·ya·ru·tē·nā·r·thō·nā·ru·tē·nē·ha·ka·ś·ca·na·na·cā·s·ya·sa·r·va·bhū·tē·ṣu·ka·ś·ci·—·da·r·tha·v·yā·pā·ś·ra·ya
Published: nai·va·ta·s·ya·kṛ·te·nā·r·tho·nā·kṛ·te·ne·ha·ka·ś·ca·na·na·cā·s·ya·sa·r·va·bhū·te·ṣu·ka·ś·ci·d·a·r·tha·v·ya·pā·ś·ra·yaḥ
```

### 116. R1 Gītā 3.21 — ch.23 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 33/44; best shuffle 13; decoys ≥ 0.

```text
Grid:      ya·d·ya·—·dā·ca·ra·ti·ś·rē·ṣ·ṭha·s·ta·t·ta·—·dē·vē·ta·ō·ja·ha·sa·ya·t·p·ra·mā·m·ku·śu·tē·dō·ka·s·ta·—·da·nu·va·r·ta·tē
Published: ya·d·ya·d·ā·ca·ra·ti·ś·re·ṣ·ṭha·s·ta·t·ta·d·e·ve·ta·ro·ja·naḥ·sa·ya·t·p·ra·mā·ṇaṃ·ku·ru·te·lo·ka·s·ta·d·a·nu·va·r·ta·te
```

### 128. R1 Gītā 11.1 — ch.24 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 35/44; best shuffle 13; decoys ≥ 0.

```text
Grid:      mi·da·nu·g·ra·hā·ya·pa·ra·m·gu·māḥ·ya·—·ma·dh·yā·t·ma·m·j·i·ta·m·ya·t·t·va·yō·k·ta·va·ca·s·tē·na·mō·hō·m·vi·ga·tō·ma·ma
Published: ma·da·nu·g·ra·hā·ya·pa·ra·maṃ·gu·h·ya·m·a·dh·yā·t·ma·saṃ·j·ñi·ta·m·ya·t·t·va·yo·k·taṃ·va·ca·s·te·na·mo·ho·yaṃ·vi·ga·to·ma·ma
```

### 129. R1 Gītā 11.28 — ch.24 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 47/56; best shuffle 14; decoys ≥ 0.

```text
Grid:      ra·thā·na·dī·n·ba·ha·vō·m·bu·vē·ha·sa·mu·d·ra·—·mē·vā·bhi·mu·khā·d·ra·va·n·ti·ta·thā·ta·vā·mī·na·ra·lō·ka·vī·rā·vi·śa·m·ti·va·k·t·rā·ṇ·—·ya·bhi·vi·j·va·la·m·ti
Published: ya·thā·na·dī·nāṃ·ba·ha·vo·m·bu·ve·gāḥ·sa·mu·d·ra·m·e·vā·bhi·mu·khā·d·ra·va·n·ti·ta·thā·ta·vā·mī·na·ra·lo·ka·vī·rā·vi·śa·n·ti·va·k·t·rā·ṇ·y·a·bhi·vi·j·va·la·n·ti
```

### 132. R1 Gītā 13.27 — ch.24 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/45; best shuffle 17; decoys ≥ 0.

```text
Grid:      ma·m·sa·r·vē·ṣu·bhū·tē·ṣu·ti·ṣ·ṭha·n·tu·pa·ra·mē·ś·va·ra·m·vi·na·ś·ya·t·s·—·va·vi·na·s·ya·n·ya·h·pa·ś·ya·ti·sa·pa·ś·ya·ti
Published: sa·maṃ·sa·r·ve·ṣu·bhū·te·ṣu·ti·ṣ·ṭha·n·taṃ·pa·ra·me·ś·va·ra·m·vi·na·ś·ya·t·s·v·a·vi·na·ś·ya·n·taṃ·yaḥ·pa·ś·ya·ti·sa·pa·ś·ya·ti
```

### 134. R1 Gītā 5.10 — ch.24 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 35/46; best shuffle 14; decoys ≥ 0.

```text
Grid:      b·ra·m·?·ṇ·—·yā·dā·ya·k·r·mā·ṇi·sa·ga·m·t·ya·k·t·vā·ka·rō·ti·ha·li·p·ya·tē·na·sa·pā·pē·na·pa·d·ma·pa·t·ra·—·mi·vā·m·bha·sā
Published: b·ra·h·ma·ṇ·y·ā·dhā·ya·ka·r·mā·ṇi·sa·ṅ·gaṃ·t·ya·k·t·vā·ka·ro·ti·yaḥ·li·p·ya·te·na·sa·pā·pe·na·pa·d·ma·pa·t·ra·m·i·vā·m·bha·sā
```

### 139. R1 Gītā 3.11 — ch.24 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/40; best shuffle 12; decoys ≥ 0.

```text
Grid:      dē·vā·n·bhā·va·ya·tā·nē·na·tē·dē·vā·bhā·va·ya·n·tu·ha·pa·ra·s·pa·m·bhā·va·ya·n·h·ś·rē·h·pa·ra·—·ma·vā·p·s·ya·tha
Published: de·vā·n·bhā·va·ya·tā·ne·na·te·de·vā·bhā·va·ya·n·tu·vaḥ·pa·ra·s·pa·raṃ·bhā·va·ya·n·taḥ·ś·re·yaḥ·pa·ra·m·a·vā·p·s·ya·tha
```

### 140. R1 Gītā 4.9 — ch.24 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/46; best shuffle 13; decoys ≥ 0.

```text
Grid:      ja·n·ma·ka·r·ma·ca·mē·di·v·ya·m·va·m·yō·vē·t·ti·ta·—·t·va·ha·t·ya·k·t·h·dē·m·pu·na·r·ja·n·ma·y·ti·mā·—·mē·ti·sō·r·ju·na
Published: ja·n·ma·ka·r·ma·ca·me·di·v·ya·m·e·vaṃ·yo·ve·t·ti·ta·t·t·va·taḥ·t·ya·k·t·vā·de·haṃ·pu·na·r·ja·n·ma·nai·ti·mā·m·e·ti·so·r·ju·na
```

### 163. R1 Gītā 11.55 — ch.25 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/44; best shuffle 13; decoys ≥ 0.

```text
Grid:      a·t·ka·r·ma·ru·n·ma·t·pa·ra·mō·ma·d·bha·k·taḥ·sa·yaṃ·gha·va·r·ji·gaḥ·ni·r·ra·s·sa·r·va·bhū·tē·ṣu·s·sa·mā·—·mē·ti·pā·ṇ·ḍa·va
Published: ma·t·ka·r·ma·kṛ·n·ma·t·pa·ra·mo·ma·d·bha·k·taḥ·sa·ṅ·ga·va·r·ji·taḥ·ni·r·vai·raḥ·sa·r·va·bhū·te·ṣu·yaḥ·sa·mā·m·e·ti·pā·ṇ·ḍa·va
```

### 164. R1 Gītā 17.20 — ch.25 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 32/41; best shuffle 10; decoys ≥ 0.

```text
Grid:      dhā·ta·v·ya·—·mi·ti·ya·d·dā·yaṃ·dī·ya·tē·nu·pa·kā·ri·ṇē·dē·śē·kā·lē·ca·pā·t·rē·ca·ta·d·dā·m·sā·—·t·vi·saṃ·s·—·—·m
Published: dā·ta·v·ya·m·i·ti·ya·d·dā·naṃ·dī·ya·te·nu·pa·kā·ri·ṇe·de·śe·kā·le·ca·pā·t·re·ca·ta·d·dā·naṃ·sā·t·t·vi·kaṃ·s·mṛ·ta·m
```

### 165. R1 Gītā 18.65 — ch.25 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/42; best shuffle 12; decoys ≥ 0.

```text
Grid:      diṃ·n·ma·nā·bhā·va·ma·d·bha·k·tō·ma·d·yā·jī·taṃ·na·ma·s·ku·ru·mā·—·mē·vē·ṣ·yā·si·sa·t·n·tē·p·ra·ti·jā·nē·p·ri·yō·si·mē
Published: ma·n·ma·nā·bha·va·ma·d·bha·k·to·ma·d·yā·jī·māṃ·na·ma·s·ku·ru·mā·m·e·vai·ṣ·ya·si·sa·t·yaṃ·te·p·ra·ti·jā·ne·p·ri·yo·si·me
```

### 170. R1 Gītā 14.25 — ch.25 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 39/42; best shuffle 11; decoys ≥ 0.

```text
Grid:      mā·nā·pa·mā·na·yō·s·tu·l·ya·s·tu·l·yō·mi·t·rā·ri·pa·k·ṣa·a·sa·r·vā·ra·m·bha·pa·ri·t·yā·gī·gu·ṇā·tī·s·sa·u·c·ya·tē
Published: mā·nā·va·mā·na·yo·s·tu·l·ya·s·tu·l·yo·mi·t·rā·ri·pa·k·ṣa·yoḥ·sa·r·vā·ra·m·bha·pa·ri·t·yā·gī·gu·ṇā·tī·taḥ·sa·u·c·ya·te
```

### 186. R1 Gītā 14.18 — ch.26 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 41/47; best shuffle 13; decoys ≥ 0.

```text
Grid:      rū·r·dh·vaṃ·ga·c·cha·n·ti·sa·t·t·va·s·thā·ma·dh·yē·ti·ṣ·ṭha·n·ti·rā·ja·mḥ·ja·gha·n·ya·gu·ṇa·ru·t·ti·s·thā·a·dhō·g·c·cha·n·ti·tā·ma·sā
Published: ū·r·dh·vaṃ·ga·c·cha·n·ti·sa·t·t·va·s·thā·ma·dh·ye·ti·ṣ·ṭha·n·ti·rā·ja·sāḥ·ja·gha·n·ya·gu·ṇa·vṛ·t·ta·s·thā·a·dho·ga·c·cha·n·ti·tā·ma·sāḥ
```

### 191. R1 Gītā 2.50 — ch.26 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 32/41; best shuffle 10; decoys ≥ 0.

```text
Grid:      v·ru·dhi·yu·k·tō·ja·hā·tī·ha·su·bhē·su·śu·ta·du·ṣ·ru·tē·ta·s·mā·d·d·gā·ya·yu·j·ya·s·va·yō·paḥ·ka·r·ma·su·v·śa·la·rṃ
Published: bu·d·dhi·yu·k·to·ja·hā·tī·ha·u·bhe·su·kṛ·ta·du·ṣ·kṛ·te·ta·s·mā·d·yo·gā·ya·yu·j·ya·s·va·yo·gaḥ·ka·r·ma·su·kau·śa·la·m
```

### 208. R1 Gītā 12.12 — ch.27 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 40/52; best shuffle 12; decoys ≥ 0.

```text
Grid:      ś·rē·yō·hi·j·ñā·na·—·ma·bh·yā·sā·j·j·mā·nā·—·dh·na·gaṃṃ·vi·—·śē·ya·tē·dh·yā·nā·t·ka·r·ma·pha·la·t·yā·ga·?·t·yā·gā·c·chā·n·ti·—·ra·na·n·ta·ra·āṃ
Published: ś·re·yo·hi·j·ñā·na·m·a·bh·yā·sā·j·j·ñā·nā·d·dh·yā·naṃ·vi·śi·ṣ·ya·te·dh·yā·nā·t·ka·r·ma·pha·la·t·yā·ga·s·t·yā·gā·c·chā·n·ti·r·a·na·n·ta·ra·m
```

### 211. R1 Gītā 17.7 — ch.27 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 33/43; best shuffle 11; decoys ≥ 0.

```text
Grid:      ā·hā·ra·s·t·—·va·pi·sa·r·va·s·ya·t·ri·vi·dhō·bha·va·ti·p·ri·vaḥ·ya·j·ña·—·ta·pa·s·ta·thā·dā·pṃ·tē·yaṃ·bhē·da·ma·mṃ·ś·ru·ṇu
Published: ā·hā·ra·s·t·v·a·pi·sa·r·va·s·ya·t·ri·vi·dho·bha·va·ti·p·ri·yaḥ·ya·j·ña·s·ta·pa·s·ta·thā·dā·naṃ·te·ṣāṃ·bhe·da·m·i·maṃ·śṛ·ṇu
```

### 212. R1 Gītā 2.45 — ch.27 mixed:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 44/49; best shuffle 13; decoys ≥ 0.

```text
Grid:      t·y·gu·ṇ·ya·vi·ṣa·yā·vē·dā·ni·s·t·y·gu·ṇ·yō·bha·vā·r·ju·na·ni·r·d·n·d·ō·ni·t·ya·sa·—·t·va·s·thō·ni·r·yō·ga·k·ṣē·ma·ā·t·ma·vā·n
Published: t·rai·gu·ṇ·ya·vi·ṣa·yā·ve·dā·ni·s·t·rai·gu·ṇ·yo·bha·vā·r·ju·na·ni·r·d·vaṃ·d·vo·ni·t·ya·sa·t·t·va·s·tho·ni·r·yo·ga·k·ṣe·ma·ā·t·ma·vā·n
```

### 214. R1 Gītā 11.28 — ch.27 mixed:E2:up


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 45/56; best shuffle 14; decoys ≥ 0.

```text
Grid:      ra·thā·na·dī·suṃ·ba·ha·vō·m·bu·vē·ha·sa·mu·d·ra·—·mē·vā·bhi·mu·khā·d·ra·va·n·ti·ta·thā·mo·vā·mī·na·ra·lō·ka·vī·rā·vi·śa·m·ti·va·k·t·rā·ṇ·—·ya·bhi·j·j·va·la·gaṃ·ti
Published: ya·thā·na·dī·nāṃ·ba·ha·vo·m·bu·ve·gāḥ·sa·mu·d·ra·m·e·vā·bhi·mu·khā·d·ra·va·n·ti·ta·thā·ta·vā·mī·na·ra·lo·ka·vī·rā·vi·śa·n·ti·va·k·t·rā·ṇ·y·a·bhi·vi·j·va·la·n·ti
```

### 233. R1 Gītā 13.10 — ch.28 long:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 30/40; best shuffle 12; decoys ≥ 0.

```text
Grid:      m·ṣi·cā·na·n·ya·ō·ge·na·bha·k·ti·—·ra·v·ya·bhi·cā·ri·ṇi·vi·vi·k·ta·dē·śa·sē·vi·t·va·—·ma·ra·ti·r·ju·na·ṭaṃ·sa·di
Published: ma·yi·cā·na·n·ya·yo·ge·na·bha·k·ti·r·a·v·ya·bhi·cā·ri·ṇī·vi·vi·k·ta·de·śa·se·vi·t·va·m·a·ra·ti·r·ja·na·saṃ·sa·di
```

### 357. R1 Gītā 12.4 — ch.32 long:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 37/44; best shuffle 13; decoys ≥ 0.

```text
Grid:      n·ni·ya·raṃ·yē·n·d·ri·ya·g·rā·daṃ·sa·r·va·t·ra·sa·ma·bu·d·dha·yḥ·tē·p·rā·p·nu·va·n·ti·mā·—·mē·va·sa·r·va·bhū·ta·hi·tē·ra·tā
Published: saṃ·ni·ya·m·ye·n·d·ri·ya·g·rā·maṃ·sa·r·va·t·ra·sa·ma·bu·d·dha·yaḥ·te·p·rā·p·nu·va·n·ti·mā·m·e·va·sa·r·va·bhū·ta·hi·te·ra·tāḥ
```

### 421. R1 Gītā 11.12 — ch.35 long:E1:down


Source: [https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm).
Identity 34/43; best shuffle 13; decoys ≥ 0.

```text
Grid:      i·vi·ū·r·ya·sa·ha·s·ra·s·ya·bha·vē·d·yu·ga·pa·—·du·t·thi·tā·ya·di·s·sa·ṛ·śī·sā·s·ya·d·bhā·s·s·ta·s·ya·ma·hā·t·ma·na
Published: di·vi·sū·r·ya·sa·ha·s·ra·s·ya·bha·ve·d·yu·ga·pa·d·u·t·thi·tā·ya·di·bhāḥ·sa·dṛ·śī·sā·s·yā·d·bhā·sa·s·ta·s·ya·ma·hā·t·ma·naḥ
```

### 449. R2 Nirvāṇa-bhakti 5 — ch.33 long S1 down (loose)


Source: [https://encyclopediaofjainism.com/निर्वाण_भक्ति/](https://encyclopediaofjainism.com/निर्वाण_भक्ति/).
Identity 32/42; best shuffle 11; decoys ≥ N/A.

```text
Grid:      t·ṃ·sā·—·pa·j·ju·ṇ·sa·ṃ·bhu·ku·mā·rō·dha·hē·va·a·ṇi·ru·d·dhō·bā·ha·t·ta·ra·kō·ḍī·ō·u·j·ṃ·tē·sa·t·ta·sa·ya·siṃ·d·dhā
Published: ṇe·mi·sā·mī·pa·j·ju·ṇ·ṇo·saṃ·bu·ku·mā·ro·ta·he·va·a·ṇi·ru·d·dho·bā·ha·t·ta·ra·ko·ḍī·o·u·j·jaṃ·te·sa·t·ta·sa·yā·si·d·dhā
```

### 451. R2 Nirvāṇa-bhakti 2 — ch.34 long S1 down (loose)


Source: [https://encyclopediaofjainism.com/निर्वाण_भक्ति/](https://encyclopediaofjainism.com/निर्वाण_भक्ति/).
Identity 31/40; best shuffle 10; decoys ≥ N/A.

```text
Grid:      i·la·k·kha·ṇa·jā·sā·dā·a·ma·rā·su·ra·n·di·dā·dhu·da·ki·lē·sā·sa·m·mē·dē·gi·ri·si·ha·rē·ṇi·v·vā·ṇa·ga·yā·ṇa·mū·tē·si
Published: vī·saṃ·tu·ji·ṇa·viṃ·ra·dā·a·ma·rā·su·ra·vaṃ·di·dā·dhu·da·ki·le·sā·sa·m·me·de·gi·ri·si·ha·re·ṇi·v·vā·ṇa·ga·yā·ṇa·mo·te·siṃ
```

### 452. R2 Nirvāṇa-bhakti 18 — ch.35 long S1 down (loose)


Source: [https://encyclopediaofjainism.com/निर्वाण_भक्ति/](https://encyclopediaofjainism.com/निर्वाण_भक्ति/).
Identity 31/40; best shuffle 10; decoys ≥ N/A.

```text
Grid:      e·sa·ha·ra·rā·ya·s·—·su·pa·ṃ·ca·sa·yā·ka·ṃ·ga·dē·sa·m·hi·kō·ḍi·si·ṃ·hī·kō·ḍi·mu·ṇī·ṇi·v·vā·ṇa·ga·yā·ṇa·mō·tē·si
Published: ja·sa·ha·ra·rā·ya·s·sa·su·ā·paṃ·ca·sa·yā·ka·liṃ·ga·de·sa·m·mi·ko·ḍi·si·lā·e·ko·ḍi·mu·ṇī·ṇi·v·vā·ṇa·ga·yā·ṇa·mo·te·siṃ
```

### 458. R3 Samadhibhakti Sanskrit:11 — ch.50 short:E1:down


Source: [https://encyclopediaofjainism.com/समाधि_भक्ति/](https://encyclopediaofjainism.com/समाधि_भक्ति/).
Identity 35/45; best shuffle 11; decoys ≥ N/A.

```text
Grid:      a·r·ha·mi·t·ya·k·ṣa·ra·b·ra·dḥṃ·ha·vā·ca·naṃ·pa·ra·mē·va·ra·kaḥ·si·d·dha·ca·k·ra·s·ya·sa·d·bī·raṃ·sa·r·ta·aḥ·p·ra·ṇi·da·dh·ma·ē
Published: a·r·ha·mi·t·ya·k·ṣa·ra·b·ra·h·ma·vā·ca·kaṃ·pa·ra·me·ṣ·ṭhi·naḥ·si·d·dha·ca·k·ra·s·ya·sa·d·bī·jaṃ·sa·r·va·taḥ·p·ra·ṇi·da·dh·ma·he
```

### 460. R3 Samadhibhakti Sanskrit:11 — ch.50 merged:E1:down


Source: [https://encyclopediaofjainism.com/समाधि_भक्ति/](https://encyclopediaofjainism.com/समाधि_भक्ति/).
Identity 36/45; best shuffle 11; decoys ≥ N/A.

```text
Grid:      a·r·ha·mi·t·ya·k·ṣa·ra·b·ra·dḥṃ·ha·vā·ca·va·pa·ra·mē·va·ra·kaḥ·si·d·dha·ca·k·ra·s·ya·sa·d·bī·raṃ·sa·r·va·aḥ·p·ra·ṇi·da·dh·ma·ē
Published: a·r·ha·mi·t·ya·k·ṣa·ra·b·ra·h·ma·vā·ca·kaṃ·pa·ra·me·ṣ·ṭhi·naḥ·si·d·dha·ca·k·ra·s·ya·sa·d·bī·jaṃ·sa·r·va·taḥ·p·ra·ṇi·da·dh·ma·he
```

### 467. R3 Santibhakti Sanskrit:11 — ch.53 short:E1:down


Source: [https://encyclopediaofjainism.com/शांतिभक्ति-6/](https://encyclopediaofjainism.com/शांतिभक्ति-6/).
Identity 42/51; best shuffle 13; decoys ≥ N/A.

```text
Grid:      i·v·ya·ta·ru·su·?·pu·ṣ·pa·su·ṛ·ṣ·ṭi·r·du·tāṃ·du·bhi·rā·sa·na·yō·ja·na·ghō·au·pā·ta·pa·vā·—·ṇa·cā·ma·ra·yu·g·mō·ya·s·ya·vi·bhā·ti·ca·haṃ·ḍa·la·tē·ja
Published: di·v·ya·ta·ru·su·ra·pu·ṣ·pa·su·vṛ·ṣ·ṭi·r·du·n·du·bhi·rā·sa·na·yo·ja·na·gho·ṣau·ā·ta·pa·vā·ra·ṇa·cā·ma·ra·yu·g·me·ya·s·ya·vi·bhā·ti·ca·maṃ·ḍa·la·te·ja
```

### 474. R3 Santibhakti Sanskrit:1 — ch.57 short:E2:down


Source: [https://encyclopediaofjainism.com/शांतिभक्ति-6/](https://encyclopediaofjainism.com/शांतिभक्ति-6/).
Identity 39/50; best shuffle 13; decoys ≥ N/A.

```text
Grid:      a·t·ya·kaṃ·ta·s·phu·ra·du·g·ra·ra·t·mi·ni·ka·ra·v·yā·kī·r·ṇa·bhū·ma·dēṃ·ḍa·lō·ra·ai·ṣ·ma·kā·pe·ya·i·baṃ·du·pā·da·vi·li·la·c·chā·yā·nu·bhē·ga·ra·vi
Published: a·t·ya·n·ta·s·phu·ra·du·g·ra·ra·ś·mi·ni·ka·ra·v·yā·kī·r·ṇa·bhū·ma·ṇ·ḍa·lo·g·rai·ṣ·ma·kā·ra·ya·tī·n·du·pā·da·sa·li·la·c·chā·yā·nu·rā·gaṃ·ra·vi
```

### 477. R3 Santibhakti Sanskrit:1 — ch.57 merged:E2:down


Source: [https://encyclopediaofjainism.com/शांतिभक्ति-6/](https://encyclopediaofjainism.com/शांतिभक्ति-6/).
Identity 39/50; best shuffle 13; decoys ≥ N/A.

```text
Grid:      a·t·ya·kaṃ·ta·s·phu·ra·du·g·ra·ra·t·mi·ni·ka·ra·v·yā·kī·r·ṇa·bhū·ma·dēṃ·ḍa·lō·ra·ai·ṣ·ma·kā·pe·ya·i·baṃ·du·pā·da·vi·li·la·c·chā·yā·nu·bhē·ga·ra·vi
Published: a·t·ya·n·ta·s·phu·ra·du·g·ra·ra·ś·mi·ni·ka·ra·v·yā·kī·r·ṇa·bhū·ma·ṇ·ḍa·lo·g·rai·ṣ·ma·kā·ra·ya·tī·n·du·pā·da·sa·li·la·c·chā·yā·nu·rā·gaṃ·ra·vi
```

### 494. R3 Caityabhakti Sanskrit:3 — ch.51 short:E1:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 65/86; best shuffle 21; decoys ≥ N/A.

```text
Grid:      ?·da·nu·ja·ya·tā·j·ai·nī·vi·i·sḥ·dh·ra·bhṃ·ga·ta·jāṃ·gi·ṇī·p·ra·bha·va·vi·ga·ma·d·ra·v·ya·d·ra·v·ya·s·va·bhā·va·vi·bā·vi·nī·ni·ru·pa·ma·su·kha·s·yē·yaṃ·d·vā·vaṃ·vi·gha·ṭ·ya·ni·ra·r·ga·naṃ·vi·ga·—·ra·ja·sa·tṃ·k·vēṃ·dē·yā·n·ni·ra·t·ya·ya·ma·—·—·—·—
Published: ta·da·nu·ja·ya·tā·j·jai·nī·vi·t·ti·p·ra·bhaṃ·ga·ta·raṃ·gi·ṇī·p·ra·bha·va·vi·ga·ma·dh·rau·v·ya·d·ra·v·ya·s·va·bhā·va·vi·bhā·vi·nī·ni·ru·pa·ma·su·kha·s·ye·daṃ·d·vā·raṃ·vi·gha·ṭ·ya·ni·ra·r·ga·laṃ·vi·ga·ta·ra·ja·saṃ·mo·k·ṣaṃ·de·yā·n·ni·ra·t·ya·ya·ma·v·ya·ya·m
```

### 495. R3 Caityabhakti Sanskrit:4 — ch.51 short:E2:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 39/49; best shuffle 13; decoys ≥ N/A.

```text
Grid:      ka·r·ha·t·si·d·dhā·cā·r·yō·pā·dh·yā·yē·bh·ya·s·ta·thā·ca·sā·dhu·bh·vaḥ·sa·r·ḷ·ja·ga·d·miṃ·d·yē·bh·yō·ṣi·mō·s·—·sa·r·va·—·sā·sa·r·d·bha·ya
Published: a·r·ha·t·si·d·dhā·cā·r·yo·pā·dh·yā·ye·bh·ya·s·ta·thā·ca·sā·dhu·bh·ya·sa·r·va·ja·ga·d·vaṃ·d·ye·bh·yo·na·mo·s·tu·sa·r·va·t·ra·sa·r·ve·bh·ya
```

### 498. R3 Caityabhakti Sanskrit:4 — ch.51 merged:E2:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 39/49; best shuffle 14; decoys ≥ N/A.

```text
Grid:      ka·r·ha·t·si·d·dhā·cā·r·yō·pā·dh·yā·yē·bh·ya·s·ta·thā·ca·sā·dhu·bh·vaḥ·sa·r·ḷ·ja·ga·d·miṃ·d·yē·bh·yō·ṣi·mō·s·—·sa·r·va·—·sā·sa·r·d·bha·ya
Published: a·r·ha·t·si·d·dhā·cā·r·yo·pā·dh·yā·ye·bh·ya·s·ta·thā·ca·sā·dhu·bh·ya·sa·r·va·ja·ga·d·vaṃ·d·ye·bh·yo·na·mo·s·tu·sa·r·va·t·ra·sa·r·ve·bh·ya
```

### 503. R3 Caityabhakti Sanskrit:8 — ch.56 short:E1:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 37/47; best shuffle 12; decoys ≥ N/A.

```text
Grid:      bha·va·na·vi·mā·na·j·yō·ti·r·v·laṃṃ·ta·ra·na·ra·lō·ka·vi·ś·va·ai·t·yā·ni·t·ri·ja·ga·da·bhi·va·pṃ·di·tā·—·nā·tṃ·t·rē·dhā·mu·nī·naṃ·d·rā·nā
Published: bha·va·na·vi·mā·na·j·yo·ti·r·v·yaṃ·ta·ra·na·ra·lo·ka·vi·ś·va·cai·t·yā·ni·t·ri·ja·ga·da·bhi·va·n·di·tā·nāṃ·vaṃ·de·t·re·dhā·ji·ne·n·d·rā·ṇāṃ
```

### 504. R3 Caityabhakti Sanskrit:8 — ch.56 merged:E1:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 36/47; best shuffle 12; decoys ≥ N/A.

```text
Grid:      bha·va·na·vi·mā·na·j·yō·ti·r·v·laṃṃ·ta·ra·na·ra·lō·ka·vi·ś·va·ai·t·yā·ni·t·ri·ja·ga·da·bhi·va·pṃ·di·tā·—·nā·tṃ·t·rē·dhā·—·—·—·śi·rā·ra
Published: bha·va·na·vi·mā·na·j·yo·ti·r·v·yaṃ·ta·ra·na·ra·lo·ka·vi·ś·va·cai·t·yā·ni·t·ri·ja·ga·da·bhi·va·n·di·tā·nāṃ·vaṃ·de·t·re·dhā·ji·ne·n·d·rā·ṇāṃ
```

### 506. R3 Caityabhakti Sanskrit:21 — ch.58 short:E2:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 31/40; best shuffle 12; decoys ≥ N/A.

```text
Grid:      va·dṃ·dē·su·ra·?·rī·ṭā·g·ra·ma·ṇi·c·chā·yā·ri·ṣē·ca·na·l·ha·k·ra·ṇi·rē·va·sē·c·tē·ta·da·r·duḥ·si·d·dhi·la·b·dha·yē
Published: va·n·de·su·ra·ti·rī·ṭā·g·ra·ma·ṇi·c·chā·yā·bhi·ṣe·ca·na·m·yā·k·ra·me·ṇai·va·se·vaṃ·te·ta·da·r·cā·si·d·dhi·la·b·dha·ye
```

### 507. R3 Caityabhakti Sanskrit:21 — ch.58 merged:E2:down


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 31/40; best shuffle 10; decoys ≥ N/A.

```text
Grid:      va·dṃ·dē·su·ra·?·rī·ṭā·g·ra·ma·ṇi·c·chā·yā·ri·ṣē·ca·na·l·ha·k·ra·ṇi·rē·va·sē·c·tē·ta·da·r·duḥ·si·d·dhi·la·b·dha·yē
Published: va·n·de·su·ra·ti·rī·ṭā·g·ra·ma·ṇi·c·chā·yā·bhi·ṣe·ca·na·m·yā·k·ra·me·ṇai·va·se·vaṃ·te·ta·da·r·cā·si·d·dhi·la·b·dha·ye
```

### 518. R3 Caityabhakti Sanskrit:4 — ch.51 package:51-short_second_from_last:listed


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 39/49; best shuffle 13; decoys ≥ N/A.

```text
Grid:      ka·r·ha·t·si·d·dhā·cā·r·yō·pā·dh·yā·yē·bh·ya·s·ta·thā·ca·sā·dhu·bh·vaḥ·sa·r·ḷ·ja·ga·d·miṃ·d·yē·bh·yō·ṣi·mō·s·—·sa·r·va·—·sā·sa·r·d·bha·ya
Published: a·r·ha·t·si·d·dhā·cā·r·yo·pā·dh·yā·ye·bh·ya·s·ta·thā·ca·sā·dhu·bh·ya·sa·r·va·ja·ga·d·vaṃ·d·ye·bh·yo·na·mo·s·tu·sa·r·va·t·ra·sa·r·ve·bh·ya
```

### 530. R3 Santibhakti Sanskrit:1 — ch.57 package:57-short_second_from_last:listed


Source: [https://encyclopediaofjainism.com/शांतिभक्ति-6/](https://encyclopediaofjainism.com/शांतिभक्ति-6/).
Identity 39/50; best shuffle 13; decoys ≥ N/A.

```text
Grid:      a·t·ya·kaṃ·ta·s·phu·ra·du·g·ra·ra·t·mi·ni·ka·ra·v·yā·kī·r·ṇa·bhū·ma·dēṃ·ḍa·lō·ra·ai·ṣ·ma·kā·pe·ya·i·baṃ·du·pā·da·vi·li·la·c·chā·yā·nu·bhē·ga·ra·vi
Published: a·t·ya·n·ta·s·phu·ra·du·g·ra·ra·ś·mi·ni·ka·ra·v·yā·kī·r·ṇa·bhū·ma·ṇ·ḍa·lo·g·rai·ṣ·ma·kā·ra·ya·tī·n·du·pā·da·sa·li·la·c·chā·yā·nu·rā·gaṃ·ra·vi
```

### 535. R3 Caityabhakti Sanskrit:21 — ch.58 package:58-short_second_from_last:listed


Source: [https://encyclopediaofjainism.com/चैत्यभक्ति-2/](https://encyclopediaofjainism.com/चैत्यभक्ति-2/).
Identity 31/40; best shuffle 10; decoys ≥ N/A.

```text
Grid:      va·dṃ·dē·su·ra·?·rī·ṭā·g·ra·ma·ṇi·c·chā·yā·ri·ṣē·ca·na·l·ha·k·ra·ṇi·rē·va·sē·c·tē·ta·da·r·duḥ·si·d·dhi·la·b·dha·yē
Published: va·n·de·su·ra·ti·rī·ṭā·g·ra·ma·ṇi·c·chā·yā·bhi·ṣe·ca·na·m·yā·k·ra·me·ṇai·va·se·vaṃ·te·ta·da·r·cā·si·d·dhi·la·b·dha·ye
```

### 551. R4 Jinasahasranama:1 — 34-long-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 37/47; best shuffle 14; decoys ≥ N/A.

```text
Grid:      dhiḥ·sa·si·d·dhā·ṣ·ṭa·sa·ha·s·rē·d·dha·la·k·ṣa·maṃ·t·ṇāṃ·gi·rā·tēṃ·pa·ti·na·nā·m·nā·ma·ṣ·ṭa·sa·ha·s·rē·ṇa·tō·ṣ·ṭu·mō·bhū·ṣ·ṭa·si·d·dha·ē
Published: p·ra·si·d·dhā·ṣ·ṭa·sa·ha·s·ra·d·ve·la·k·ṣa·ṇaṃ·t·vāṃ·gi·rā·m·pa·ti·m·nā·m·nā·ma·ṣ·ṭa·sa·ha·s·re·ṇa·to·ṣ·ṭu·mo·bhī·ṣ·ṭa·si·d·dha·ye
```

### 628. R4 Jinasahasranama:117 — 43-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 43/52; best shuffle 14; decoys ≥ N/A.

```text
Grid:      a·na·riṃ·ta·śa·k·ti·ra·c·chē·d·ya·s·t·ri·?·rā·ri·s·t·ri·lō·ca·ghaḥ·t·ri·ṇē·t·ra·s·t·—·ra·laṃṃ·ba·ka·s·t·r·ya·k·sḥ·kē·va·la·j·ñā·na·vī·k·ṣa·ṇa
Published: a·na·n·ta·śa·k·ti·ra·c·che·d·ya·s·t·ri·pu·rā·ri·s·t·ri·lo·ca·naḥ·t·ri·ne·t·ra·s·t·r·ya·m·ba·ka·s·t·r·ya·k·ṣaḥ·ke·va·la·j·ñā·na·vī·k·ṣa·ṇaḥ
```

### 630. R4 Jinasahasranama:117 — 43-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 43/52; best shuffle 14; decoys ≥ N/A.

```text
Grid:      a·na·riṃ·ta·śa·k·ti·ra·c·chē·d·ya·s·t·ri·?·rā·ri·s·t·ri·lō·ca·ghaḥ·t·ri·ṇē·t·ra·s·t·—·ra·laṃṃ·ba·ka·s·t·r·ya·k·sḥ·kē·va·la·j·ñā·na·vī·k·ṣa·ṇa
Published: a·na·n·ta·śa·k·ti·ra·c·che·d·ya·s·t·ri·pu·rā·ri·s·t·ri·lo·ca·naḥ·t·ri·ne·t·ra·s·t·r·ya·m·ba·ka·s·t·r·ya·k·ṣaḥ·ke·va·la·j·ñā·na·vī·k·ṣa·ṇaḥ
```

### 631. R4 Jinasahasranama:87 — 44-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 39/45; best shuffle 12; decoys ≥ N/A.

```text
Grid:      su·s·thi·vaḥ·s·vā·s·th·ya·bhā·k·s·va·s·thō·nī·ra·ja·s·kō·ni·ru·d·va·ruḥ·a·lē·pō·ni·ṣ·ka·la·rṃ·kā·t·mā·?·ta·rā·gō·ga·ta·s·p·nṛ
Published: su·s·thi·taḥ·s·vā·s·th·ya·bhā·k·s·va·s·tho·nī·ra·ja·s·ko·ni·ru·d·va·vaḥ·a·le·po·ni·ṣ·ka·la·ṅ·kā·t·mā·vī·ta·rā·go·ga·ta·s·pṛ·haḥ
```

### 632. R4 Jinasahasranama:124 — 44-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 41/50; best shuffle 14; decoys ≥ N/A.

```text
Grid:      t·jēṃ·pa·ṇaṃṃ·ca·b·ra·yāṃ·ha·ta·t·t·vā·t·mā·pa·tṃ·ca·ka·l·yā·ṇa·nā·ya·bḥ·ṣa·ḍ·bhē·da·bhā·va·ta·t·t·va·j·ña·s·t·pāṃ·sa·p·ta·na·ya·sa·raṃ·g·ra·ha
Published: t·vaṃ·pa·ñ·ca·b·ra·h·ma·ta·t·t·vā·t·mā·pa·ñ·ca·ka·l·yā·ṇa·nā·ya·kaḥ·ṣa·ḍ·bhe·da·bhā·va·ta·t·t·va·j·ña·s·t·vaṃ·sa·p·ta·na·ya·sa·ṅ·g·ra·haḥ
```

### 638. R4 Jinasahasranama:87 — 44-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 39/45; best shuffle 13; decoys ≥ N/A.

```text
Grid:      su·s·thi·vaḥ·s·vā·s·th·ya·bhā·k·s·va·s·thō·nī·ra·ja·s·kō·ni·ru·d·va·ruḥ·a·lē·pō·ni·ṣ·ka·la·rṃ·kā·t·mā·?·ta·rā·gō·ga·ta·s·p·nṛ
Published: su·s·thi·taḥ·s·vā·s·th·ya·bhā·k·s·va·s·tho·nī·ra·ja·s·ko·ni·ru·d·va·vaḥ·a·le·po·ni·ṣ·ka·la·ṅ·kā·t·mā·vī·ta·rā·go·ga·ta·s·pṛ·haḥ
```

### 639. R4 Jinasahasranama:124 — 44-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 39/50; best shuffle 13; decoys ≥ N/A.

```text
Grid:      ṭ·ṣ·rā·ṇaṃṃ·ca·b·ra·yāṃ·ha·ta·t·t·vā·t·mā·pa·tṃ·ca·ka·l·yā·ṇa·nā·ya·bḥ·ṣa·ḍ·bhē·da·bhā·va·ta·t·t·va·j·ña·s·t·pāṃ·sa·p·ta·na·ya·sa·raṃ·g·ra·ra
Published: t·vaṃ·pa·ñ·ca·b·ra·h·ma·ta·t·t·vā·t·mā·pa·ñ·ca·ka·l·yā·ṇa·nā·ya·kaḥ·ṣa·ḍ·bhe·da·bhā·va·ta·t·t·va·j·ña·s·t·vaṃ·sa·p·ta·na·ya·sa·ṅ·g·ra·haḥ
```

### 647. R4 Jinasahasranama:39 — 45-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 36/43; best shuffle 11; decoys ≥ N/A.

```text
Grid:      su·ga·ṇ·kḥ·pu·ṇ·ya·dhī·r·gu·ṇ·yu·pu·ṇ·ya·ṛ·t·pu·ṇ·ya·śā·sa·duṃḥ·dha·r·mā·rā·mō·gu·ṇa·g·rā·māḥ·pu·ṇ·yā·pu·ṇ·ya·ni·rō·dha·ka
Published: a·ga·ṇ·yaḥ·pu·ṇ·ya·dhī·r·gu·ṇ·yaḥ·pu·ṇ·ya·kṛ·t·pu·ṇ·ya·śā·sa·naḥ·dha·r·mā·rā·mo·gu·ṇa·g·rā·maḥ·pu·ṇ·yā·pu·ṇ·ya·ni·ro·dha·kaḥ
```

### 649. R4 Jinasahasranama:39 — 45-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 36/43; best shuffle 11; decoys ≥ N/A.

```text
Grid:      su·ga·ṇ·kḥ·pu·ṇ·ya·dhī·r·gu·ṇ·yu·pu·ṇ·ya·ṛ·t·pu·ṇ·ya·śā·sa·duṃḥ·dha·r·mā·rā·mō·gu·ṇa·g·rā·māḥ·pu·ṇ·yā·pu·ṇ·ya·ni·rō·dha·ka
Published: a·ga·ṇ·yaḥ·pu·ṇ·ya·dhī·r·gu·ṇ·yaḥ·pu·ṇ·ya·kṛ·t·pu·ṇ·ya·śā·sa·naḥ·dha·r·mā·rā·mo·gu·ṇa·g·rā·maḥ·pu·ṇ·yā·pu·ṇ·ya·ni·ro·dha·kaḥ
```

### 651. R4 Jinasahasranama:19 — 46-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 33/40; best shuffle 11; decoys ≥ N/A.

```text
Grid:      i·ra·ṇ·ya·nā·bhi·r·bhū·tā·t·mā·bhū·ta·ṛ·d·bhū·ta·bhā·va·ghiḥ·p·ra·bha·vō·vi·bha·ō·bhā·s·va·n·bha·vō·bhā·vō·bha·vā·rṃ·ta·ka
Published: hi·ra·ṇ·ya·nā·bhi·r·bhū·tā·t·mā·bhū·ta·bhṛ·d·bhū·ta·bhā·va·naḥ·p·ra·bha·vo·vi·bha·vo·bhā·s·vā·n·bha·vo·bhā·vo·bha·vā·n·ta·kaḥ
```

### 652. R4 Jinasahasranama:100 — 46-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 36/43; best shuffle 11; decoys ≥ N/A.

```text
Grid:      ta·pa·nī·ya·ni·bha·s·tu·vaṃ·gō·bā·lā·r·kā·bhō·na·la·p·ra·bhaḥ·sa·tṃ·dh·yā·bh·ra·bha·bh·ru·hē·mā·bhā·s·a·p·ta·cā·mī·ka·ra·j·cha·vi
Published: ta·pa·nī·ya·ni·bha·s·tu·ṅ·go·bā·lā·r·kā·bho·na·la·p·ra·bhaḥ·sa·n·dh·yā·bh·ra·ba·bh·ru·he·mā·bha·s·ta·p·ta·cā·mī·ka·ra·c·cha·viḥ
```

### 654. R4 Jinasahasranama:112 — 46-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 35/42; best shuffle 11; decoys ≥ N/A.

```text
Grid:      ṛ·g·va·k·—·va·ca·sā·mī·śō·mā·ra·ji·d·vi·ś·va·bhā·va·vi·t·su·ta·nu·s·ta·nu·—·ni·r·mu·k·yaḥ·su·ga·tō·ha·ta·du·r·na·ya
Published: p·ra·va·k·tā·va·ca·sā·mī·śo·mā·ra·ji·d·vi·ś·va·bhā·va·vi·t·su·ta·nu·s·ta·nu·r·ni·r·mu·k·taḥ·su·ga·to·ha·ta·du·r·ṇa·yaḥ
```

### 655. R4 Jinasahasranama:123 — 46-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 36/47; best shuffle 13; decoys ≥ N/A.

```text
Grid:      t·va·mē·gṃ·ja·ga·pṃ·j·yō·ti·s·t·rāṃ·d·vi·rū·pō·pa·ṣō·ga·bhā·k·t·tṃ·t·ri·rū·rai·ka·mu·k·t·ya·ga·liḥḥ·s·ō·t·thā·na·pāṃ·ta·ca·tu·ṣ·ṭa·ya
Published: t·va·me·kaṃ·ja·ga·tāṃ·j·yo·ti·s·t·vaṃ·d·vi·rū·po·pa·yo·ga·bhā·k·t·vaṃ·t·ri·rū·pai·ka·mu·k·t·ya·ṅ·gaḥ·s·vo·t·thā·na·n·ta·ca·tu·ṣ·ṭa·yaḥ
```

### 656. R4 Jinasahasranama:127 — 46-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 31/41; best shuffle 12; decoys ≥ N/A.

```text
Grid:      i·jṃ·s·tō·t·ra·ma·m·jṛ·t·ya·pū·tō·bha·va·ti·bhā·k·ti·riḥ·ya·sa·pā·tōṃ·pa·ṭha·t·ē·na·sa·s·yā·t·ka·l·yā·ṇa·bhā·ja·na·ṣōṃ
Published: i·daṃ·s·to·t·ra·ma·nuḥ·mṛ·t·ya·pū·to·bha·va·ti·bhā·k·ti·kaḥ·yaḥ·saṃ·pā·ṭhaṃ·pa·ṭha·t·ye·naṃ·sa·s·yā·t·ka·l·yā·ṇa·bhā·ja·na·m
```

### 659. R4 Jinasahasranama:19 — 46-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 33/40; best shuffle 11; decoys ≥ N/A.

```text
Grid:      i·ra·ṇ·ya·nā·bhi·r·bhū·tā·t·mā·bhū·ta·ṛ·d·bhū·ta·bhā·va·ghiḥ·p·ra·bha·vō·vi·bha·ō·bhā·s·va·n·bha·vō·bhā·vō·bha·vā·rṃ·ta·ka
Published: hi·ra·ṇ·ya·nā·bhi·r·bhū·tā·t·mā·bhū·ta·bhṛ·d·bhū·ta·bhā·va·naḥ·p·ra·bha·vo·vi·bha·vo·bhā·s·vā·n·bha·vo·bhā·vo·bha·vā·n·ta·kaḥ
```

### 660. R4 Jinasahasranama:100 — 46-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 35/43; best shuffle 11; decoys ≥ N/A.

```text
Grid:      ta·pa·nī·ya·ni·bha·s·tu·vaṃ·gō·bā·lā·r·kā·bhō·na·la·p·ra·bhaḥ·sa·tṃ·dh·yā·bh·ra·bha·bh·ru·hē·mā·bhā·s·a·p·ta·cā·mī·ka·ra·ra·ta·t
Published: ta·pa·nī·ya·ni·bha·s·tu·ṅ·go·bā·lā·r·kā·bho·na·la·p·ra·bhaḥ·sa·n·dh·yā·bh·ra·ba·bh·ru·he·mā·bha·s·ta·p·ta·cā·mī·ka·ra·c·cha·viḥ
```

### 662. R4 Jinasahasranama:112 — 46-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 35/42; best shuffle 13; decoys ≥ N/A.

```text
Grid:      ṛ·g·va·k·—·va·ca·sā·mī·śō·mā·ra·ji·d·vi·ś·va·bhā·va·vi·t·su·ta·nu·s·ta·nu·—·ni·r·mu·k·yaḥ·su·ga·tō·ha·ta·du·r·na·ya
Published: p·ra·va·k·tā·va·ca·sā·mī·śo·mā·ra·ji·d·vi·ś·va·bhā·va·vi·t·su·ta·nu·s·ta·nu·r·ni·r·mu·k·taḥ·su·ga·to·ha·ta·du·r·ṇa·yaḥ
```

### 674. R4 Jinasahasranama:105 — 47-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 33/44; best shuffle 13; decoys ≥ N/A.

```text
Grid:      j·ñē·yo·ni·dhi·ra·dhi·ṣ·ṭhā·na·ma·p·ra·ti·ṣ·lōḥ·p·ra·ti·ṣ·ṭhi·ṇiḥ·su·s·thi·rauḥ·s·thā·va·yōḥ·s·thā·maḥ·p·ra·thī·ya·n·p·ra·thi·ta·rḥ·p
Published: ś·re·yo·ni·dhi·ra·dhi·ṣ·ṭhā·na·ma·p·ra·ti·ṣ·ṭhaḥ·p·ra·ti·ṣ·ṭhi·taḥ·su·s·thi·raḥ·s·thā·va·raḥ·s·thā·ṇuḥ·p·ra·thī·yā·n·p·ra·thi·taḥ·pṛ·thuḥ
```

### 675. R4 Jinasahasranama:107 — 47-short-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 31/41; best shuffle 10; decoys ≥ N/A.

```text
Grid:      j·yō·rā·śi·ra·na·ta·au·jā·j·ñ·nā·dhi·daṃḥ·śī·la·sā·ga·ṇaṃḥ·tē·jō·ma·yō·mi·ta·j·yō·ti·r·j·yō·ti·mū·r·—·ti·s·ta·mō·pa·ha
Published: te·jo·rā·śi·ra·na·n·tau·jā·j·ñā·nā·n·dhiḥ·śī·la·sā·ga·raḥ·te·jo·ma·yo·mi·ta·j·yo·ti·r·j·yo·ti·mū·r·t·ti·s·ta·mo·pa·haḥ
```

### 677. R4 Jinasahasranama:92 — 47-short-E2-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 41/50; best shuffle 13; decoys ≥ N/A.

```text
Grid:      hā·va·ja·ga·d·va·l·la·bhō·bh·ya·r·c·ya·s·t·ri·ja·ga·vi·ma·dṃ·ga·lō·da·vīṃḥ·t·r·ja·ga·t·pa·ti·pū·j·yā·daṃ·gh·ri·s·t·ri·śa·kā·g·ra·śi·khā·ma·ta
Published: t·ri·ja·ga·d·va·l·la·bho·bh·ya·r·c·ya·s·t·ri·ja·ga·n·ma·ṅ·ga·lo·da·yaḥ·t·ri·ja·ga·t·pa·ti·pū·j·yā·ṅ·gh·ri·s·t·ri·lo·kā·g·ra·śi·khā·ma·ṇiḥ
```

### 682. R4 Jinasahasranama:105 — 47-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 33/44; best shuffle 13; decoys ≥ N/A.

```text
Grid:      thi·ñē·yo·ni·dhi·ra·dhi·ṣ·ṭhā·na·ma·p·ra·ti·ṣ·lōḥ·p·ra·ti·ṣ·ṭhi·ṇiḥ·su·s·thi·rauḥ·s·thā·va·yōḥ·s·thā·maḥ·p·ra·thī·ya·n·p·ra·thi·ta·rḥ·p
Published: ś·re·yo·ni·dhi·ra·dhi·ṣ·ṭhā·na·ma·p·ra·ti·ṣ·ṭhaḥ·p·ra·ti·ṣ·ṭhi·taḥ·su·s·thi·raḥ·s·thā·va·raḥ·s·thā·ṇuḥ·p·ra·thī·yā·n·p·ra·thi·taḥ·pṛ·thuḥ
```

### 683. R4 Jinasahasranama:107 — 47-merged-E1-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 31/41; best shuffle 10; decoys ≥ N/A.

```text
Grid:      j·yō·rā·śi·ra·na·ta·au·jā·j·ñ·nā·dhi·daṃḥ·śī·la·sā·ga·ṇaṃḥ·tē·jō·ma·yō·mi·ta·j·yō·ti·r·j·yō·ti·mū·r·—·ti·s·ta·mō·pa·ha
Published: te·jo·rā·śi·ra·na·n·tau·jā·j·ñā·nā·n·dhiḥ·śī·la·sā·ga·raḥ·te·jo·ma·yo·mi·ta·j·yo·ti·r·j·yo·ti·mū·r·t·ti·s·ta·mo·pa·haḥ
```

### 685. R4 Jinasahasranama:92 — 47-merged-E2-down


Source: [https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).
Identity 39/50; best shuffle 11; decoys ≥ N/A.

```text
Grid:      va·la·ya·da·d·va·l·la·bhō·bh·ya·r·c·ya·s·t·ri·ja·ga·vi·ma·dṃ·ga·lō·da·vīṃḥ·t·r·ja·ga·t·pa·ti·pū·j·yā·daṃ·gh·ri·s·t·ri·śa·kā·g·ra·śi·khā·ma·ta
Published: t·ri·ja·ga·d·va·l·la·bho·bh·ya·r·c·ya·s·t·ri·ja·ga·n·ma·ṅ·ga·lo·da·yaḥ·t·ri·ja·ga·t·pa·ti·pū·j·yā·ṅ·gh·ri·s·t·ri·lo·kā·g·ra·śi·khā·ma·ṇiḥ
```

### 708. R5 Samayikapatha:23 — ch57:short:end1:plain:down→ch58:merged:end1:plain:down


Source: [https://jain1.com/jain-samayik-path-sanskrit-hindi/](https://jain1.com/jain-samayik-path-sanskrit-hindi/).
Identity 46/59; best shuffle 14; decoys ≥ N/A.

```text
Grid:      sa·kaṃ·s·—·rō·bha·d·ra·—·mā·dhi·ā·dha·paṃ·na·lō·ka·pū·jā·na·ca·sa·vaṃ·gha·mē·la·na·gaṃ·ya·ta·s·ta·thō·dh·—·t·ma·ra·tō·bha·vā·ni·paṃ·vi·mu·c·—·sa·r·vā·ma·pi·bā·h·ya·vā·sa·nā·vēṃ
Published: na·saṃ·s·ta·ro·bha·d·ra·sa·mā·dhi·sā·dha·naṃ·na·lo·ka·pū·jā·na·ca·sa·ṅ·gha·me·la·na·m·ya·ta·s·ta·to·dh·yā·t·ma·ra·to·bha·vā·ni·śaṃ·vi·mu·c·ya·sa·r·vā·ma·pi·bā·h·ya·vā·sa·nā·m
```

## Reproduction

Run `rtk c++ -O3 -std=c++17 -shared -fPIC reports/independent_audit/align2.cpp -o reports/independent_audit/align2.so`, then `rtk python3 reports/independent_audit/run_audit3.py` and `rtk python3 reports/independent_audit/make_report3.py`. The runner is one process with no parallel workers and rewrites its progress file during the run. The saved source files are used so a rerun does not depend on live website availability.
