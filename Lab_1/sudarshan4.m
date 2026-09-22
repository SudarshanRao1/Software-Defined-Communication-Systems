t = -5:0.01:5;
x = exp(-t.^2);

t0 = 2;
x_shifted = exp(-(t-t0).^2);

a = 2;
x_scaled = exp(-(a*t).^2);

subplot(3,1,1);
plot(t,x);
title('orgignal wave');

subplot(3,1,2);
plot(t,x_shifted);
title('line shift delay = 2');

subplot(3,1,3);
plot(t,x_scaled);
title('line scale delay = 2');