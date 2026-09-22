% regarding the plotting the different kinds of graphs

t = 0:0.001:1;
f = 5;
A = 2;
phi = pi/4;

sine_wave = A*sin(2*pi*f*t + phi);
square_wave = A*square(2*pi*f*t);
sawtooth_wave = A*sawtooth(2*pi*f*t);
triangle_wave = A*sawtooth(2*pi*f*t , 0.5);

subplot(4,1,1);
plot(t,sine_wave);
title('Sine wave');

subplot(4,1,2);
plot(t,square_wave);
title('Square wave');

subplot(4,1,3);
plot(t,sawtooth_wave);
title('Sawtooth wave');

subplot(4,1,4);
plot(t,triangle_wave);
title('Triangle_wave');