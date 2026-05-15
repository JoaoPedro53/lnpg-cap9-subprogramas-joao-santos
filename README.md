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
