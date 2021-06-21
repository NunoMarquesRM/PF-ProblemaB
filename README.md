# PF-ProblemaB
 
# Entrada
A entrada começa pela especificação de uma imagem no formato ppm sem comentários. A linha final contém o inteiro p, potência de 2, que indica o tamanho do thumbnail por calcular.

# Saída
Uma linha com o valor inteiro que indica a profundidade da folha mais alta da árvore calculada.
Uma linha que indica o número de folhas totais da árvore. Uma matriz p por p que contém o thumbnail calculado. Esta matriz está organizada em p linhas de p inteiros.

# Limites
Os valores de n e p são potências de dois. E garantido que 0 < p ≤ n ≤ 1024.

# Exemplo de Entrada
P1  
8 8  
0 0 0 0 1 0 1 0  
0 0 0 0 0 0 0 1  
0 0 0 0 0 0 1 1  
0 0 0 0 0 1 1 1  
0 0 0 0 1 1 1 1  
0 0 0 0 1 1 1 1  
0 0 0 1 1 1 1 1  
0 0 1 1 1 1 1 1  
4  

# Exemplo de Saída
1  
22  
0 0 0 1  
0 0 0 1  
0 0 1 1  
0 1 1 1  