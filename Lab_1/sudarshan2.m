% checking the energy plot and  periodicity 
% try doing the sine wave with different variable 


t = -5:0.001:5;
x = exp(-abs(t)); 

E = trapz(t,x.^2);
fprintf('Energy = %.4f\n' , E);

x2 = sin(2*pi*2*t);
T = 10;
p = (1/T) * trapz(t,x2.^2);
fprintf('Power = %.4f\n' , p);

f = 2 ;
Ts = 1/f;
 
figure('Name', 'Energy Signal');
plot(t, x, 'LineWidth', 1.5);

figure('Name', 'Power Signal');
plot(t, x2, 'r', 'LineWidth', 1.5);