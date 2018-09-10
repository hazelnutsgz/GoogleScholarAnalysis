year = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
result_20 = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 9, 13]
result_50 = [1.0, 2.0, 2.0, 3.0, 4.0, 4.0, 5.0, 6.0, 6.0, 7.0, 8.0, 8.0, 9.0, 10.0, 11.0, 11.0, 12.0, 13.0, 13.0, 14.0, 15.0, 16.0, 17.0, 25.0]
result_80 = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 20, 20, 22, 23, 24, 25, 27, 29, 42]
figure;

plot(year, result_20, 'r', year, result_50, 'b', year, result_80, 'k');
title('Evolution of h-index', 'FontSize', 16);
xlabel('Year', 'FontSize', 16);
ylabel('h-index', 'FontSize', 16);
legend('20th', '50th', '80th', 4);

load gs_h_idx.txt


up_bound = max(gs_h_idx)/5;

cdf_h_idx =store_re(gs_h_idx);
pdf_h_idx =store_re_pdf(gs_h_idx);


%figure;
%plot(0:up_bound/1000:up_bound-up_bound/1000, cdf_h_idx)
figure;
plot(0:up_bound, cdf_h_idx(1:up_bound+1));hold on;
title('CDF', 'FontSize', 16);
xlabel('H-index', 'FontSize', 16);

figure;
plot(0:up_bound, pdf_h_idx(1:up_bound+1));hold on;
title('PDF', 'FontSize', 16);
xlabel('H-index', 'FontSize', 16);


fit_lambda = 0.5;
fit_value = [];
for i=0:999
    %fit_value = [fit_value geo_dist(fit_p, 
        %exp_dist(up_bound/1000*i, fit_lambda)]
end

%plot(0:up_bound/1000:up_bound-up_bound/1000, fit_lambda);hold on;

%fitdist(gs_h_idx, 'Gamma')