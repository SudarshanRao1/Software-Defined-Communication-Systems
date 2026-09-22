t = -5:0.01:5;
x = exp(-t).*(t>=0);

x_flip = fliplr(x);

x_even = 0.5*(x + x_flip);
x_odd  = 0.5*(x - x_flip);

subplot(3,1,1);
plot(t,x);
title('orgignal wave');

subplot(3,1,2);
plot(t,x_even);
title('even component');

subplot(3,1,3);
plot(t,x_odd);
title('odd componenet');

