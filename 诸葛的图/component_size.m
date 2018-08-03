A = [35690080, 1614, 407, 301, 301, 269, 136, 117, 116, 106];
bar(A, 0.6);
ylabel('Size','FontSize',16);
set(gca,'xticklabel',{'1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'}, 'FontSize',16);
set(gca,'yscale','log');
axis([0.5 10.5 0 100000000]);
saveas(gcf, 'component_size.eps');
saveas(gcf, 'component_size.png');
