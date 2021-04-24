%%%Script para alfa, master

clc; clear; close all; clear all;

% Defaults for this blog post
width = 3;     % Width in inches
height = 3;    % Height in inches
alw = 0.75;    % AxesLineWidth
fsz = 13;      % Fontsize >11.5 <15
lw = 1.5;      % LineWidth
msz = 8;       % MarkerSize
%% %%%%% 1)Load %%%%%%%%%%%%%%%%%%%%%%%%%%

Data = load('6_amplitude_60s_800mV_Bias_gain_gate_standar_histo.txt'); %data
Counts = Data(:,2);
ADC_channels = Data(:,1);

%% %%%%% 2)Load %%%%%%%%%%%%%%%%%%%%%%%%%%

 figure
 bar(ADC_channels, Counts)
 title('Spectra for amplitude 6 of the Led Driver')
 xlabel('ADC channels'); ylabel('Counts')
 grid on

%% %%%%% 3)Calcs %%%%%%%%%%%%%%%%%%%%%%%%%%

%I have to fit all the peaks. The easiest version is to count the peaks by
%hand, and find the indexes, and the fit it, in a similar fashion as what
%I did usually in the bachelor and masters degree

%16 peaks, so this will be hard bro. The idea to choose numbers is two
%above and below after and before the counts starts increasing
%drastically/decreasing

%Initialization of the storing
Sigma = [];         
Delta_sigma = [];
N = [];

%###Peak 1 (around 0)

x_data = ADC_channels(122:130);   
y_data = Counts(122:130);
n = 1;                                      %number of peak


%f(x)=1/(sqrt(2pi)*sigma)*exp(-1/2* ((x-<x>)^2/sigma)
%<x> = mean value and sigma the standar deviation

%The gauss1 fit is a1*exp(-((x-b1)/c1)^2)

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95);  %confidence intervals = coefficients with 95% 
    %confidence bounds this are the coefficientes returned when print 
    %in command windows ajuste1

%Print of the command windows
% ajuste1 = 
%      General model Gauss1:
%      ajuste1(x) =  a1*exp(-((x-b1)/c1)^2)
%      Coefficients (with 95% confidence bounds):
%        a1 =       86.36  (75.63, 97.08)
%        b1 =      0.9616  (-1.323, 3.246)
%        c1 =       22.57  (19.22, 25.93)


delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); %Error of sigma 1.
    %Note that the error is simply the mean value of the extremal bound.
    %1/sqrt(2) to scalate it to convert it into sigma, since the error is
    %of c

%FWHM_Am=2*sqrt(2*log(2))*sigma1 %MeV
%delta_FWHM_Am=delta_sigma1*2*sqrt(2*log(2))

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))
%It is awesome, so moving on to the controversial peaks!!

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];

%###Peak 2 ##################

x_data = ADC_channels(158:168); 
y_data = Counts(158:168); 
n = 2;

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95);  

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))
%It is awesome, so F, this works, and python dont :((

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];

%###Peak 3 ##############

x_data = ADC_channels(192:207); 
y_data = Counts(192:207);
n = 3;

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95);  

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))
%It is awesome, so F, this works, and python dont :((

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%###Peak 4 ###################
n = 4;
x_data = ADC_channels(225:243); 
y_data = Counts(225:243); 


ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];

%###Peak 5 ###############
n = 5;
x_data = ADC_channels(263:282); 
y_data = Counts(263:282); 


ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%###Peak 6 ################
n = 6;
x_data = ADC_channels(299:319); 
y_data = Counts(299:319); 

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%###Peak 7##############
n = 7;
x_data = ADC_channels(335:356); 
y_data = Counts(335:356); 

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%###Peak 8#############
n = 8;
x_data = ADC_channels(371:388); 
y_data = Counts(371:388); 

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%###Peak 9#############
n = 9;
x_data = ADC_channels(407:423); 
y_data = Counts(407:423); 

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%###Peak 10#############
n = 10;
x_data = ADC_channels(444:458); 
y_data = Counts(444:458); 

ajuste = fit(x_data,y_data,'gauss1');
a = ajuste.a1;
mu = ajuste.b1;
sigma = ajuste.c1/sqrt(2);
ci = confint(ajuste,0.95); 

delta_sigma=abs(ci(1,3)-ci(2,3))/2*1/sqrt(2); 

%Plot of the fit
Gauss = @(x) ajuste.a1*exp(-((x-ajuste.b1)/ajuste.c1).^2);
range = linspace(min(x_data),max(x_data));   %to do the plot of the fit
figure; grid on;
plot(x_data, y_data,'ro-')
hold on
plot(range,Gauss(range))
xlabel('ADC channels')
ylabel('Counts')
legend('data','fit')
title(sprintf('peak %d',n))

%Storing of the values
Sigma = [Sigma, sigma];
Delta_sigma = [Delta_sigma, delta_sigma];
N = [N, n];


%%%From here, it is hard to see where it is a peak, so will stop now!


%% 3) Plot%%%%%%%%%%%%%%%%%%%
% 
% figure; grid on;
% errorbar(N, Sigma, Delta_sigma,'b*-')
% xlabel('Number of peaks')
% ylabel('\sigma')
% title('Standard deviation vs number of peaks')
% 
% %plot of the variance, sigma^2
% Delta_sigma2 = Delta_sigma*sqrt(2).*Sigma
% figure; grid on;
% errorbar(N, Sigma.^2, Delta_sigma2, 'b*-')
% xlabel('Number of peaks')
% ylabel('\sigma^2')
% title('Variance vs number of peaks')

%The plot is perfect, very similar to the one in the Caen book, so now its
%time to fit it!!!!

%%% 3.1) Linear fit to the data

%y = mx+n

[m, n, r, delta_m, delta_n] = Regresion(N,Sigma);

%%% 3.2) Plot=linear fit

figure; 
errorbar(N, Sigma, Delta_sigma,'r*-','LineWidth', 1.5);
hold on
plot(linspace(min(N),max(N)),m*linspace(min(N),max(N))+n,'LineWidth', 1.5);
xlabel('Peak number')
ylabel('\sigma')
title('Standard deviation vs peak number')
lgd = legend('Data', 'linear fit');
lgd.Location = 'NorthWest';
set(gca,'XLim',[0 max(N)+1]);
set(gca, 'FontSize', fsz, 'LineWidth', alw); %<- Set
%Include fit equation + correlation coefficient
grid on
txt = ['y = ' num2str(m) 'x +' num2str(n) '; r = ' num2str(r)];
text(4,15, txt)     %(2,50) are the x,y position
saveas(gcf, 'sigma_vs_peak_number.png')
%y = mx+n

[m2, n2, r2, delta_m2, delta_n2] = Regresion(N,Sigma.^2);

%%% 3.2) Plot=linear fit

figure; 
errorbar(N, Sigma.^2, Delta_sigma2,'r*-','LineWidth', 1.5);
hold on
plot(linspace(min(N),max(N)),m2*linspace(min(N),max(N))+n2,'LineWidth', 1.5);
xlabel('Peak number')
ylabel('\sigma^2')
title('Variance vs peak number')
lgd = legend('Data', 'linear fit');
lgd.Location = 'NorthWest';
set(gca,'XLim',[0 max(N)+1]);
%set(gca,'YLim',[0 3000]);
set(gca, 'FontSize', fsz, 'LineWidth', alw); %<- Set
%Include fit equation + correlation coefficient
grid on
txt = ['y = ' num2str(m2) 'x +' num2str(n2) '; r = ' num2str(r2)];
text(4,300, txt)     %(2,50) are the x,y position
saveas(gcf, 'sigma2_vs_peak_number.png')


%% 4) Discussion%%%%%%555

%Is weird, CAENs book says sigma goes like sqrt(N), and I found thatit goes
%as N, so my sigma2 is cuadratic, since hes is lineal. However, his graph
%axes are weird, so wil try to mimic them:

figure; 
errorbar(N, Sigma.^2, Delta_sigma2,'r*-','LineWidth', 1.5);
hold on
plot(linspace(min(N),max(N)),m2*linspace(min(N),max(N))+n2,'LineWidth', 1.5);
xlabel('Peak number')
ylabel('\sigma^2')
title('Variance vs peak number')
lgd = legend('Data', 'linear fit');
lgd.Location = 'NorthWest';
set(gca,'XLim',[0 max(N)+1]);
set(gca,'YLim',[0 7000]);
set(gca, 'FontSize', fsz, 'LineWidth', alw); %<- Set
%Include fit equation + correlation coefficient
grid on;
txt = ['y = ' num2str(m2) 'x +' num2str(n2) '; r = ' num2str(r2)];
text(4,300, txt)     %(2,50) are the x,y position
saveas(gcf, 'sigma2_vs_peak_number_CAEN_style.png')

%Not ithas the same scale,  and, as expected, the deviation from the
%linearity are diminished, so now is looks way more linear. So, is CAEN
%(which uses data from MAHAMATSU) fooling us??????????