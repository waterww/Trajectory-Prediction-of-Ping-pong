# Trajoctory-Prediction-of-Ping-pong
## Image Processing
Turn RGB image to gray image, set the white area as white and other area as black, then extract the edges. The target ping-pong ball is white.
## Extract Ball Center
Because ping-pong ball is moving at high speed and the RGB camera used in the project has maximum fps 30Hz, it is not enogh to catch clear round shape in image.
The average of maximum and minimum coordinate values is taken as ball center.
## Trajectory Prediction
Take the trajectory that ping-pong bounces from the ground to sky and falls as parabola, use bouncing ball model to predict the height of ball at a fixed place.
## Experiment
In 8 rounds of experiments, the minimum prediction error is 0.2cm, the maximum prediction error is 24.2cm, the average error is 14.9cm. Actually the prediction
 result is not good enough.
## Result Analysis
1. In the model, we consider the recovery coefficient *k* and the acceleration a in the Z-direction as a constant, and find the acceleration *a* by fitting the previous jump cycle. Analyzing several sets of recorded side-view data and fitting the acceleration *a* for two adjacent cycles with a second-order polynomial, we found that the value of *a* varied considerably from cycle to cycle in the same set of data, and was not stable at a constant value as assumed. The recovery coefficients were manually adjusted by the parameters based on the recorded data, and also did not stabilize around a constant value.
Acceleration analysis
2. In the pinball model, we ignore many external forces, such as air resistance, air buoyancy, and the Magnus force caused by the rotation of the ping pong ball. The change in acceleration in the Z-direction is so large that the air buoyancy has a large effect on the motion of the ping pong ball.
3. We assume that the initial velocity of the table tennis ball in the Y-direction is zero, but in fact the table tennis ball has displacement in the Y-direction, so the depth value of the table tennis ball in the side camera keeps changing, which leads to errors in the coordinates of the derived spatial coordinate system, and thus the prediction of the catch point.
4. The table tennis table is about 1.2m long, and the frame rate of the camera is 30fps. The ping pong ball can only be recorded for about 10 frames, i.e. 10 sampling points, when it completely jumps over the table. And one cycle can record 3-5 frames, so the sample points used for fitting are too few, which leads to the initial velocity and acceleration that are not accurate.
