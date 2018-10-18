#ifndef MY_ALLOC_H
#define MY_ALLOC_H

int** matriz_alloc(int Linhas,int Colunas){ //Recebe a quantidade de Linhas e Colunas como Parâmetro

	int i,j; //Variáveis Auxiliares

	int **m = (int**)malloc(Linhas * sizeof(int*)); //Aloca um Vetor de Ponteiros

	for (i = 0; i < Linhas; i++){ //Percorre as linhas do Vetor de Ponteiros
		m[i] = (int*) malloc(Colunas * sizeof(int)); //Aloca um Vetor de Inteiros para cada posição do Vetor de Ponteiros.
		for (j = 0; j < Colunas; j++){ //Percorre o Vetor de Inteiros atual.
			m[i][j] = 0; //Inicializa com 0.
		}
	}
	return m; //Retorna o Ponteiro para a Matriz Alocada
}

#endif
