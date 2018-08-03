M = load('./data/active_de.txt');
N = load('./data/normal_de.txt');
A = M(:,1);
B = M(:,2)*100;
C = N(:,1);
D = N(:,2)*100;
plot(A,B,'-',C,D,'--', 'LineWidth',2);

xlabel('Node Degree', 'FontSize',16),ylabel('Percentage(%)','FontSize',16);
h = legend('Active','Others');
set(h,'Fontsize',16);
saveas(gcf, 'active_degree.eps');
saveas(gcf, 'active_degree.png');