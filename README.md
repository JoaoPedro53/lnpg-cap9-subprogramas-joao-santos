<h2>João Pedro Santos Vieira</h2>
<p>LNPG-BSI-2026.1</p>

<h3>Tarefa 1 — Modularização em Java</h3>
<p>Implementar um sistema de controle acadêmico com Java em subprogramas.</p>

<p>Versão <b>monolítica:</b></p>
<li>Coesão -> Código de baixa coesão, tudo misturado em um único método</li>
<li>Legibilidade -> Tem uma boa legibilidade.</li>
<li>Reutilização -> Não existem métodos definidos. Não se pode usar a mesma lógica em outros casos, causando repetição de código.</li>
<li>Facilidade de Manutenção -> Péssima manutenção devida a baixa coesão.</li>
<li>Clareza do fluxo -> Por ser só um método, pode aparentar ter um fluxo mais simples, pórem em casos de bugs fica difícil. O fluxo fica complicado.</li>
<li>tamanho dos métodos -> Só tem um único método, onde toda lógica está.</li>
<br>

<p>Versão <b>modularizada:</b></p>
<li>Coesão -> Código de alta coesão, cada método tendo sua própia responsabilidade.</li>
<li>Legibilidade -> Ao entender o que cada método é responsável, fica com uma ótima legibilidade.</li>
<li>Reutilização -> Em grande parte reutilizável, cada método pode ser usado novamente ao decorrer do código.</li>
<li>Facilidade de Manutenção -> Ótima manutenção, dévido ao seu fraco acoplamento.</li>
<li>Clareza do fluxo -> Fluxo claro devido aos seus métodos.</li>
<li>tamanho dos métodos -> Na versão monolítica tudo estava no método main, agora ele foi quebrado em vários outros. Com isso, cada método tendo tamanhos aceitáveis.</li>

<h3>Tarefa 2 — Modularização em Python</h3>
<p>Implementar um sistema de vendas em Python em subprogramas</p>

<p>Versão <b>monolítica:</b></p>
<li>No código monolítico, tudo fica em um único bloco, deixando o código maior, mais confuso e difícil de manter. Ou seja, qualquer alteração pode ficar mais trabalhosa, porque tudo está misturado no mesmo lugar </li>
<br>

<p>Versão <b>modularizada:</b></p>
<li>No código modularizado, as tarefas foram separadas em funções, deixando o código mais organizado e fácil de entender. Também facilita reutilizar partes do programa sem precisar copiar código.</li>
<br>

<li>As partes repetitivas eram a leitura dos produtos, os cálculos e a impressão do cupom, tudo ficando junto no mesmo bloco de código.</li>
<li>Com funções, essas partes ficaram reutilizáveis, porque agora podemos chamar a mesma função várias vezes sem reescrever código.</li>
<li>A modularização deixou o código mais organizado e fácil de entender, já que cada função faz apenas uma tarefa específica.</li>
<br>

<h3>Tarefa 3 — Passagem de Parâmetros por Valor em Java</h3>
<p>Programa Java contendo passagem por valor de tipos primitivos.</p>

<li>O valor original não mudou, porque foi passado um cópia do valor para o método e não a variável original.</li>
<li>“Passagem por valor” significa que o método recebe uma cópia do valor da variável, e não a variável original.</li>
<li>O valor da varíavel 'x' do método 'main' foi copiado para a varíavel local 'x' do método 'alterarNumero'.</li>
<br>

<h3>Tarefa 4 — Objetos e Referência em Java</h3>
<p>Classe Java para entender o comportamento de objetos em chamadas de métodos.</p>

<li>Não. Java não tem passagem por referência verdadeira.</li>
<li>É copiada uma cópia da referência do objeto, um “endereço” para o objeto.</li>
<li>Porque tanto o método quanto o main apontam para o mesmo objeto na memória, então qualquer mudança no objeto afeta os dois.</li>
