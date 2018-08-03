M = load('./data/path_length.txt');
A = M(:,1);
B = M(:,2);

plot(A,B,'-*', 'LineWidth',2);
xlabel('Path length', 'FontSize',16),ylabel('Number','FontSize',16);
saveas(gcf, 'path_length.eps');
saveas(gcf, 'path_length.png');