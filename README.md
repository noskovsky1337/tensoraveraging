# tensoraveraging
I passed the theoretical minimum of Landau in mathematics-1, and the third problem from it is about averaging a tensor object, often of course they can be solved through mathematical statistics "head-on", but most often the problem is reduced to averaging a certain tensor object due to the vector nature of the problem and the isotropy and invariance of the object itself. For example, using the reasoning that the only invariant rank 2 tensor is only \delta_ab, you can get the answer up to a constant, and then find the constant itself through the trace of the matrices.
This project considers two options for solving this problem using mathematical statistics, which is analytically cumbersome compared to tensor averaging (the second method).
It should be noted that if the expression were not root mean square, but average, i.e., without the square, the volume would be zero because the probabilities would simply “collapse.”

The condition of the problem itself: Select four random points A, B, C, D on a unit sphere in three dimensions (uniformly distributed across the area and independent of each other). Let \V_ABCD be the volume of the tetrahedron with vertices
at these points. Find the average value.
 (<((\V_abcd)^2)>)^(1/2)
