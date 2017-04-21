# LFA_01
Trabalho 01 de LFA-2017/1

Instruções Gerais Para o Trabalho:

1. Esta atividade vale 20 pontos e poderá ser resolvida em grupo com no máximo 2 integrantes.
2. Caso você ache que falta algum detalhe nas especificações, você deverá fazer as suposições que julgar
necessárias e escrevê-las no seu relatório. Pode acontecer também que a descrição dessa atividade
contenha dados e/ou especificações supérfluas para sua solução. Utilize sua capacidade de julga-
mento para separar o supérfluo do necessário.
3. Para desenvolver esta atividade utilize preferencialmente as linguagens Python ou Java. Se quiser
utilizar outra linguagem deverá justificar a sua escolha no seu relatório.
4. Como produtos da atividade serão gerados dois artefatos: códigos fontes da implementação e docu-
mentação da atividade.
5. Cada arquivo-fonte deve ter um cabeçalho constando as seguintes informações: nome(s) do(s) aluno(s),
matrícula(s) e data.
6. O arquivo contendo a documentação da atividade (relatório) deve ser devidamente identificado com
o(s) nome(s) e matrícula do(s) autor(es) do trabalho. O arquivo contendo o relatório deve, obrigato-
riamente, estar no formado PDF.
7. Devem ser entregues os arquivos contendo os códigos-fontes e o arquivo contendo a documentação
da atividade (relatório). Compacte todos os artefatos gerados num único arquivo no formato ZIP.
8. O prazo final para entrega desta atividade é até 23:59:00 do dia 22/05/2017.
9. O envio é de total responsabilidade do aluno. Não serão aceitos trabalhos enviados fora do prazo
estabelecido.
10. Trabalhos plagiados serão desconsiderados, sendo atribuída nota 0 (zero) a todos os envolvidos.
11 Introdução
O Primeiro Trabalho Prático (TP) aborda o desenvolvimento (projeto e implementação) dos algoritmos
apresentados em sala de aula para manipulação de Autômatos Finitos Determinísticos (AFDs) sem pilha.
A primeira parte desse TP considera a implementação de uma classe para representar os AFDs seguindo
a especificação apresentada a seguir. As partes seguintes consideram a implementação dos métodos que
manipulam os objetos da classe.
A especificação dos requisitos que é apresentada aqui não é formal, em vez disso será apresentado somente
o ponto de vista de um possível usuário da classe, mostrando aquilo que ele esperaria encontrar numa im-
plementação. Serão apresentados exemplos de código mostrando a espectativa de um usuário que deseja
utilizar a classe e, com esses exemplos em vista, tente projetar a sua classe de modo a facilitar seu uso pelo
usuário. Todavia, esteja ciente de que em computação não vale a máxima “o usuário tem sempre razão”.
Você tem liberdade para alterar alguma coisa que pareça menos adequada nos exemplos, mas esteja pre-
parado para justificar as suas escolhas e convenver o usuário de que a sua implementação foi projetada e é
mais fácil de usar.
Os códigos que exemplificam o uso da classe não estão escritos em nenhuma linguagem de programação
particular, então faça as adaptações necessárias.
2 A classe AFD
Um Autômato Finito Determinístico (AFD) é definido como uma tupla (E , Σ, δ, i , F ) com os elementos:
E – conjunto finito de estados.
Σ – alfabeto, formado por um conjunto finito de símbolos.
δ – função de transição, tipada como δ : (E × Σ) → E .
i – estado inicial, tal que i ∈ E .
F – conjunto de estados finais, com F ⊆ E .


Para simplificação do modelo, considere que cada estado do AFD é representado por um inteiro positivo e
o alfabeto pertence ao conjunto de caracteres imprimíveis da tabela ASCii.
3 Os requisitos através de exemplos de uso
1. O usuário deseja aproveitar a ferramenta JFLAP para fazer a entrada dos dados. Desse modo, ele poderá
criar um AFD utlizando o JFLAP, salvá-lo no formato .jff, e então carregá-lo num objeto da classe AFD. Essa
tarefa não será difícil tendo em vista que um arquivo .jff nada mais é do que um arquivo texto em XML.

AFD m;
...
m. load ( "entrada.jff" ) ;

2. O usuário também deseja aproveitar a ferramenta JFLAP para fazer a saída dos dados. Desse modo, ele
poderá salvar uma representação do AFD no objeto para um arquivo .jff, depois carregar esse arquivo no
JFLAP para visualizar graficamente o AFD.

AFD m;
...
m. s a l v e ( "saida.jff" ) ;

3. O usuário deseja poder identificar estados equivalentes, além de obter uma versão mínima do AFD.

AFD m, mm;
L i s t eqv ;
...
eqv = m. equivalents ( ) ;
mm = m.minimum( ) ;

4. O usuário deseja poder comparar dois AFDs para saber se são ou não equivalentes.

AFD m1, m2;
...
i f (AFD. equivalents (m1, m2) )
p r i n t ( "sim" ) ;
el se
p r i n t ( "não" ) ;

5. O usuário deseja poder realizar operações de complementação, união, intersessão e diferença.

AFD m1, m2, m3, m4, m5, m6;
...
m3 = m1. complement ( ) ;
m4 = m1. union (m2) ;
m5 = m1. i n t e r s e c t i o n (m2) ;
m6 = m1. d i f f e r e n c e (m2) ;

6. O usuário deseja poder consultar o AFD, testar a pertença de uma palavra na linguagem, testar movi-
mentos.

AFD m;
int estado ;
...
i f (m. accept ( "aaabbbaa" ) )
p r i n t ( "aceita" ) ;
el se
p r i n t ( "não aceita" ) ;
...
estado = m. i n i t i a l ( ) ;
estado = m. move( estado , "aaab" ) ;
i f ( estado in m. f i n a l s ( ) )
p r i n t ( "aceita" ) ;
el se
p r i n t ( "não aceita" ) ;

7. O usuário deseja poder alterar o AFD.

AFD m;
...
m. addState ( id =10 , i n i t i a l = f a l s e , f i n a l =true ) ;
m. addTransition ( source =1 , t a r g e t =2 , consume= "b" ) ;
m. d e l e t e S t a t e ( 3 ) ;
m. de l e te Tr an si ti o n ( source =1 , t a r g e t =4 , consume= "a" ) ;

4 Critérios de Correção
Serão adotados os seguintes critérios de correção para o trabalho:
1. correção: somente serão corrigidos códigos portáveis e sem de erros de compilação;
2. precisão: execução correta numa bateria de testes práticos; (70%)
3. modularização: projeto da classe; (30%)
4. qualidade do código fonte: legibilidade, indentação, uso adequado de comentários; (requisito)
5. documentação: relatório, conforme instruções apresentadas a seguir. (requisito)


Alguns critérios não receberão pontuação específica, mas funcionarão como “requisitos” que poderão afe-
tar a pontuação se não forem atendidos adequadamente, portanto leve-os em conta durante o desenvolvi-
mento do trabalho.
3Haverá uma apresentação oral e individual do trabalho. Todos os integrantes do grupo devem participar
dessa apresentação.
Na ausência de plágio, as notas dos trabalhos corretos serão computadas individualmente da seguinte
forma: nota = nota_apresentacao ∗ nota_trabalho, ou seja, a nota final é ponderada pela nota da apre-
sentação.

4.1 Documentação
Esta seção descreve o formato e o conteúdo do relatório que deve ser gerado como produto final do traba-
lho. Seja sucinto: em geral é possível escrever um bom relatório entre 2 e 4 páginas.
O relatório documentando seu sistema deve conter as seguintes informações:
1. introdução: descrever o problema resolvido e apresentar uma visão geral do sistema implementado;
2. implementação: descrever as decisões de projeto e implementação do programa. Essa parte da do-
cumentação deve mostrar como as estruturas de dados planejadas e implementadas. Sugestao: mos-
tre uma figura ilustrativa, os tipos definidos, detalhes de implementação e especificação que porven-
tura estavam omissos no enunciado, etc.
3. validação: descrição dos testes que o grupo fez para validar o trabalho, se seguiu alguma metodologia
etc.
4. conclusão: avaliação do grupo sobre o trabalho considerando a experiência adquirida, a contribuição
para o aprendizado da disciplina, as principais dificuldades encontradas ao implementá-lo e como
tais dificuldades foram superadas;