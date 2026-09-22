t = 0:0.1:2;
x = sin(2*pi*2*t);

c = 1.5;
x_amptitude = x+c;

a = 0.5;
x_ampscale = a*x;

subplot(3,1,1);
plot(t,x);
title('orgignal wave');

subplot(3,1,2);
plot(t,x_amptitude);
title('Amptitude Shiftes(-1.5)');

subplot(3,1,3);
plot(t,x_ampscale);
title('Aptitude Scaled(x0.5)'); 